"""
This module contains all preference models to interact with user
no matter is it comes from an API REST interface or CLI interface.


All preference options may be exposed to user in order to change
the default behavior of the application.
"""

from datetime import datetime, timedelta
from dateutil.parser import parse

from typing import Union, List, Tuple
from typing_extensions import Annotated

from syncmodels.model import Enum, IntEnum
from syncmodels.model import BaseModel, field_validator, Field
from syncmodels.mapper import *

# from models.generic.price import PriceSpecification
# from models.generic.schedules import OpeningHoursSpecificationSpec


# ---------------------------------------------------------
# Enum Definitions
# ---------------------------------------------------------
class ExampleEnum(str, Enum):
    """Example of an Enum representing something ..."""

    # a reference to the specification
    # https://github.com/smart-data-models/dataModel.TourismDestinations/blob/master/TouristProfile/schema.json
    SINGLE = "Single"
    COUPLE = "Couple"
    FAMILY = "Family"
    FRIENDS = "Friends"


class NumberedExampleEnum(IntEnum):
    """Example of an Enum representing a numeric sorted something ..."""

    NONE: Annotated[int, "lowest"] = 0
    VERY_LOW = 1
    LOW = 2
    MEDIUM = 3
    HIGH = 4
    VERY_HIGHT: Annotated[int, "highest"] = 5


# ---------------------------------------------------------
# App Config Preferences Models
# ---------------------------------------------------------
class MyAppExamplePreferences(BaseModel):
    """Example of all preferences that may be exposed to user."""

    name: str = Field(
        default="no_name",
        description="A name for this user app preference",
        examples=[
            "A travel to Roma",
            "Second Visit to Budapest",
        ],
    )

    alternatives: int = Field(
        default=1,
        description="number of max alternatives to compute for the same preferences",
        ge=1,
    )
    temperature: float = 0.5
