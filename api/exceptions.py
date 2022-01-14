from django.conf import settings
from django.utils.translation import gettext as _
from rest_framework.exceptions import ValidationError


class TotalAvgAreaException(ValidationError):
    default_detail = _(
        f"Average area of all added boxes should not exceed {settings.A1}"
    )


class TotalAvgUserVolException(ValidationError):
    default_detail = _(
        f"Average volume of all boxes added by the current user shall not exceed {settings.V1}"
    )


class TotalWeekBoxException(ValidationError):
    default_detail = _(f"Total Boxes added in a week cannot be more than {settings.L1}")


class TotalWeekUserBoxException(ValidationError):
    default_detail = _(
        f"Total Boxes added in a week by a user cannot be more than {settings.L2}"
    )
