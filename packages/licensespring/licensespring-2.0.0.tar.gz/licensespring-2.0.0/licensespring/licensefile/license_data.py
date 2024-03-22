import json
from datetime import datetime, timedelta, timezone

import licensespring
from licensespring.licensefile.error import ErrorType, TimeoutExpiredException


class LicenseData:

    """
    A class for handling License file fields, providing functionalities for managing license data.

    Attributes:
        grace_period_conf (int): Defines how many hours can license be in offline mode.
        product (str): Identifier for the software product associated with this license.
        hardware_id (str): Unique hardware ID of the device using the license, used for license binding.
        version (str): Version of the Python SDK, fetched from licensespring.version.
        license_key (str, optional): The key used for license activation. Default is None.
        floating_period (int, optional): Defines the period for a floating license. Default is None.
        last_check (datetime, optional): Timestamp of the last license check. Default is None.
        last_usage (datetime, optional): Timestamp of the last usage of the license. Default is None.

    Methods:
        features_setup(): Sets up local consumption count for consumption-based features.
        local_consumption_setup(): Initializes local consumption count for licenses of type 'consumption'.
        to_json(): Serializes the license data to a JSON string.
        from_json_to_attr(licensefile_dict): Deserializes JSON string or dictionary to license data attributes.
    """

    datetime_attributes = [
        "last_check",
        "last_usage",
        "floating_period",
        "maintenance_period",
        "start_date",
        "validity_period",
        "borrowed_until",
        "grace_period_start_date",
    ]

    def __init__(self, product, hardwareID, grace_period_conf):
        self.grace_period_conf = grace_period_conf
        self.product = product
        self.hardware_id = hardwareID
        self.version = licensespring.version

        self.license_key = None
        self.floating_period = None

        self.last_check = None
        self.last_usage = None

    def features_setup(self):
        """
        Iterates over product features to initialize local consumption for consumption-based features.
        This method requires product_features to be defined and populated with relevant feature data.
        """

        for i, feature in enumerate(self.product_features):
            if (
                feature["feature_type"] == "consumption"
                and feature.get("local_consumption") is None
            ):
                self.product_features[i]["local_consumption"] = 0

    def local_consumption_setup(self):
        """
        Initializes the local consumption attribute for licenses of type 'consumption' if it's not already set.
        This method assumes the existence of a license_type attribute to check against 'consumption'.
        """

        if (
            not hasattr(self, "local_consumption")
            and self.license_type == "consumption"
        ):
            self.local_consumption = 0

    def grace_period_setup(self):
        if not hasattr(self, "grace_period_start_date"):
            self.grace_period_start_date = datetime(year=2099, month=1, day=1)

    def to_json(self) -> json:
        """
        Serializes the license data attributes to a JSON string, converting datetime objects to ISO format.

        Returns:
            str: The serialized JSON string of the license data.
        """

        data = {}
        for key, value in self.__dict__.items():
            if isinstance(value, datetime):
                data[key] = value.isoformat()
            else:
                data[key] = value
        return json.dumps(data)

    def from_json_to_attr(self, licensefile_dict):
        """
        Deserializes a JSON string or dictionary to update the license data attributes, converting ISO format strings back to datetime objects for specific fields.

        Args:
            licensefile_dict (dict): The dictionary containing license data to be deserialized.
        """

        for key, value in licensefile_dict.items():
            if key in LicenseData.datetime_attributes and value != None:
                setattr(self, key, datetime.fromisoformat(value).replace(tzinfo=None))

            else:
                setattr(self, key, value)

    def validity_with_grace_period(self) -> datetime | None:
        if hasattr(self, "grace_period") and self.validity_period != None:
            if self.grace_period > 0:
                return self.validity_period + timedelta(hours=self.grace_period)

        return self.validity_period

    def is_grace_period_started(self) -> datetime:
        return self.grace_period_start_date != datetime(year=2099, month=1, day=1)

    def grace_period_end_date(self) -> datetime:
        return self.grace_period_start_date + timedelta(hours=self.grace_period_conf)

    def update_grace_period_start_date(self):
        if not self.is_grace_period_started():
            self.grace_period_start_date = datetime.now(timezone.utc).replace(
                tzinfo=None
            )

    def reset_grace_period_start_date(self):
        if self.is_grace_period_started():
            self.grace_period_start_date = datetime(year=2099, month=1, day=1)

    def update_from_error_code(self, error_code):
        if error_code.upper() == "LICENSE_NOT_ACTIVE":
            self.license_active = False

        elif error_code.upper() == "LICENSE_NOT_ENABLED":
            self.license_enabled = False

        elif error_code.upper() == "LICENSE_EXPIRED":
            self.is_expired = True

    def is_active_floating_cloud(self):
        if self.is_floating_cloud:
            if timedelta(
                minutes=self.floating_timeout
            ) + self.last_check > datetime.now(timezone.utc).replace(tzinfo=None):
                return True

        return False
