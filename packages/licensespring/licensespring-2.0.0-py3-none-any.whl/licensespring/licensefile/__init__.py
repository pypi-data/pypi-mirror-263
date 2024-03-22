from datetime import datetime, timezone

from requests.exceptions import RequestException

from licensespring.api.error import ClientError
from licensespring.licensefile.error import (
    ClockTamperedException,
    ConfigurationMismatch,
    ConsumptionError,
    ErrorType,
    LicenseSpringTypeError,
    LicenseStateException,
    TimeoutExpiredException,
    VMIsNotAllowedException,
)


class License:
    """
    Represents and manages license operations including activation, deactivation,
    and consumption tracking for a software product.

    Methods:
        __init__(self, product, api_client, licensefile_handler): Initializes the license object with a product, API client, and licensefile handler.
        is_floating_expired(self): Checks if a floating license has expired. Placeholder method that currently always returns False.
        is_validity_period_expired(self): Determines whether the license's validity period has expired, based on the enabled state and validity period.
        check_license_status(self): Verifies the current status of the license, raising exceptions if the license is not enabled, not active, or expired.
        check(self, include_expired_features=False, req_overages=-1): Performs an online check to sync license data with the backend
        deactivate(self, delete_license=False): Deactivates the license and optionally deletes the local license file.
        local_check(self): Performs a local check of the license against product code, hardware ID, and VM restrictions.
        add_local_consumption(self, consumptions=1): Adds local consumption records for consumption-based licenses,
        sync_consumption(self, req_overages=-1): Syncs local consumption data with the server, adjusting for overages if specified.
        is_grace_period(self, e: Exception): Determines if the current license state is within a grace period


    Attributes:
        product (str): The software product this license is associated with.
        api_client: An instance responsible for communicating with the licensing API.
        licensefile_handler: Handles local license file operations such as reading and writing.
    """

    def __init__(self, product, api_client, licensefile_handler) -> None:
        self.product = product
        self.api_client = api_client
        self.licensefile_handler = licensefile_handler

    def is_floating_expired(self) -> bool:
        return False

    def is_validity_period_expired(self) -> bool:
        """
        Determines whether the license's validity period has expired.

        Returns:
            bool: True if the validity period has expired or the license is disabled, False otherwise.
        """

        if self.licensefile_handler._cache.is_expired:
            return True

        if isinstance(self.licensefile_handler._cache.validity_period, datetime):
            if (
                self.licensefile_handler._cache.validity_with_grace_period()
                < datetime.now(timezone.utc).replace(tzinfo=None)
            ):
                self.licensefile_handler._cache.is_expired = True

                return True

        return False

    def check_license_status(self) -> None:
        """
        Verifies the current status of the license, including its enablement, activation, and expiration.

        Raises:
            LicenseStateException: If the license is not enabled, not active, or expired.
        """

        if not self.licensefile_handler._cache.license_enabled:
            raise LicenseStateException(
                ErrorType.LICENSE_NOT_ENABLED, "The license disabled"
            )

        if not self.licensefile_handler._cache.license_active:
            raise LicenseStateException(
                ErrorType.LICENSE_NOT_ACTIVE, "The license is not active."
            )

        if self.is_validity_period_expired():
            raise LicenseStateException(
                ErrorType.LICENSE_EXPIRED, "The license is expired."
            )

    def check(self, include_expired_features=False) -> dict | None:
        """
        Performs an online license check, syncing the license data with the backend.
        This includes syncing consumptions for consumption-based licenses.

        Args:
            include_expired_features (bool, optional): If True, includes expired license features in the check.
                Defaults to False.
            req_overages (int, optional): Specifies the behavior for consumption overages.
                Use -1 to ignore, 0 to disable overages, and a positive value to enable overages
                up to the specified value. Defaults to -1.

        Returns:
            dict: The response from the license check operation.

        Raises:
            Exceptions: Various exceptions can be raised depending on the API client's implementation and the response from the licensing server.
        """

        try:
            response = self.api_client.check_license(
                product=self.licensefile_handler._cache.product,
                hardware_id=None,
                license_key=self.licensefile_handler._cache.license_key,
                username=self.licensefile_handler._cache.username,
                include_expired_features=include_expired_features,
            )

            self.licensefile_handler.update_cache("check_license", response)

            if self.licensefile_handler._cache.license_type == "consumption":
                self.sync_consumption(req_overages=-1)

            self.licensefile_handler._cache.reset_grace_period_start_date()

            return response

        except ClientError as e:
            self.licensefile_handler._cache.update_from_error_code(e.code)

        except RequestException:
            if (
                self.licensefile_handler._cache.is_floating == False
                or self.licensefile_handler._cache.is_active_floating_cloud()
            ) and self.is_grace_period():
                return None

            raise RequestException("Grace period not allowed/passed")

        finally:
            self.licensefile_handler.save_licensefile()
            self.check_license_status()

    def deactivate(self, delete_license=False) -> None:
        """
        Deactivates the license and optionally deletes the local license file.

        Args:
            delete_license (bool, optional): If True, deletes the local license file upon deactivation.
                Defaults to False.
        """

        if not self.licensefile_handler._cache.license_active:
            if delete_license:
                self.licensefile_handler.delete_licensefile()
            return None

        self.api_client.deactivate_license(
            product=self.licensefile_handler._cache.product,
            hardware_id=None,
            license_key=self.licensefile_handler._cache.license_key,
            username=self.licensefile_handler._cache.username,
            password=self.licensefile_handler._cache.password,
        )

        if delete_license:
            self.licensefile_handler.delete_licensefile()
            return None

        if self.licensefile_handler._cache.times_activated > 0:
            self.licensefile_handler._cache.times_activated -= 1

        else:
            self.licensefile_handler._cache.times_activated = 0

        self.licensefile_handler._cache.license_active = False
        self.licensefile_handler.save_licensefile()

    def local_check(self) -> None:
        """
        Performs a local check of the license, ensuring product code, hardware ID, VM (virtual machine), and other conditions are met.

        Raises:
            Various exceptions for different failure conditions.
        """
        try:
            if self.licensefile_handler._cache.product != self.product:
                raise ConfigurationMismatch(
                    ErrorType.PRODUCT_MISMATCH,
                    "License product code does not correspond to configuration product code",
                )

            if (
                self.licensefile_handler._cache.hardware_id
                != self.api_client.hardware_id_provider.get_id()
            ):
                raise ConfigurationMismatch(
                    ErrorType.HARDWARE_ID_MISMATCH,
                    "License hardware id does not correspond to configuration hardware id",
                )

            self.check_license_status()

            if (
                self.api_client.hardware_id_provider.get_is_vm()
                != self.licensefile_handler._cache.prevent_vm
            ):
                raise VMIsNotAllowedException(
                    ErrorType.VM_NOT_ALLOWED, "Virtual machine not allowed."
                )

            if self.is_floating_expired():
                raise TimeoutExpiredException(
                    ErrorType.FLOATING_TIMEOUT, "Floating license timeout has expired."
                )

            if self.licensefile_handler._cache.last_usage > datetime.now(
                timezone.utc
            ).replace(tzinfo=None):
                raise ClockTamperedException(
                    ErrorType.CLOCK_TAMPERED, "Detected cheating with local date time."
                )

        except LicenseStateException as e:
            self.licensefile_handler._cache.update_from_error_code(e.error_type.name)

            raise e

    def change_password(self, password: str, new_password: str) -> str:
        """
        Changes the password for user-based license.
        This method first checks the current license status to ensure it is active and not expired.
        It then attempts to change the password with the licensing server.

        Params:
            password (str): Old password of license user
            new_password (str): New password of license user

        Returns:
            str: password was changed.
        """

        self.check_license_status()

        response = self.api_client.change_password(
            self.licensefile_handler._cache.username,
            password=password,
            new_password=new_password,
        )

        self.licensefile_handler._cache.password = new_password

        return response

    def add_local_consumption(self, consumptions=1) -> dict:
        """
        Adds local consumptions for consumption-based licenses.

        Args:
            consumptions (int): The number of consumptions to add locally.

        Returns:
            dict: The updated license cache reflecting the new consumption count.

        Raises:
            LicenseTypeError: If the license is not of type 'consumption'.
            ConsumptionError: If adding the consumptions would exceed the allowed maximum.
        """

        if self.licensefile_handler._cache.license_type != "consumption":
            raise LicenseSpringTypeError(
                ErrorType.WRONG_LICENSE_TYPE,
                f" WRONG License Type: {self.licensefile_handler._cache.license_type}",
            )

        elif self.licensefile_handler._cache.allow_unlimited_consumptions:
            self.licensefile_handler._cache.local_consumption += consumptions

        elif (
            self.licensefile_handler._cache.max_consumptions
            + self.licensefile_handler._cache.max_overages
            < self.licensefile_handler._cache.local_consumption
            + consumptions
            + self.licensefile_handler._cache.total_consumptions
        ):
            raise ConsumptionError(
                ErrorType.NOT_ENOUGH_LICENSE_CONSUMPTIONS,
                "Not enough conusmptions left!",
            )

        else:
            self.licensefile_handler._cache.local_consumption += consumptions

            return self.licensefile_handler.cache

    def sync_consumption(self, req_overages=-1) -> bool:
        """
        Syncs the local consumption data with the server for consumption-based licenses.

        Args:
            req_overages (int, optional): Specifies the behavior for requesting consumption overages.
                Defaults to -1, which means no overage request is made. A value of 0 disables overages,
                and a positive value requests permission for overages up to the specified value.

        Returns:
            bool: True if the consumption data was successfully synchronized; False otherwise.

        Side Effects:
            Resets local consumption count after successful synchronization.
        """

        if not hasattr(self.licensefile_handler._cache, "local_consumption"):
            return False

        if self.licensefile_handler._cache.local_consumption == 0 and req_overages < 0:
            return False

        try:
            if req_overages == 0:
                max_overages = req_overages
                allow_overages = False

            elif req_overages > 0:
                max_overages = req_overages
                allow_overages = True

            else:
                max_overages = None
                allow_overages = None

            response = self.api_client.add_consumption(
                product=self.licensefile_handler._cache.product,
                license_key=self.licensefile_handler._cache.license_key,
                username=self.licensefile_handler._cache.username,
                password=self.licensefile_handler._cache.password,
                consumptions=self.licensefile_handler._cache.local_consumption,
                max_overages=max_overages,
                allow_overages=allow_overages,
            )

        except ClientError as e:
            raise e

        except RequestException as e:
            if self.is_grace_period():
                self.licensefile_handler.save_licensefile()
                self.check_license_status()

                return False

            raise RequestException("Grace period not allowed/passed")

        else:
            self.licensefile_handler._cache.local_consumption = 0

            self.licensefile_handler.update_cache("consumptions", response)

            self.licensefile_handler._cache.reset_grace_period_start_date()
            self.licensefile_handler.save_licensefile()

            return True

    def is_grace_period(self) -> bool:
        """
        Determines if the license is currently within its grace period following a specific exception.
        The grace period logic is activated only if the license cache has a 'grace_period' attribute set,
        and the passed exception is of type 'RequestException', typically indicating a communication
        error with the licensing server.

        Args:
            e (Exception): The exception that triggered the grace period check. Expected to be
                        a 'RequestException' for the grace period logic to proceed.

        Returns:
            bool: True if the license is within its grace period, False otherwise.

        Side Effects:
            - If the license is within its grace period and a 'RequestException' occurs, this method
            updates the grace period start date in the license cache to the current time.
        """

        if not hasattr(self.licensefile_handler._cache, "grace_period_conf"):
            return False

        elif self.licensefile_handler._cache.grace_period_conf > 0:
            self.licensefile_handler._cache.update_grace_period_start_date()

            return (
                datetime.now(timezone.utc).replace(tzinfo=None)
                < self.licensefile_handler._cache.grace_period_end_date()
            )

        return False
