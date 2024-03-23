"""
An Example of Model classes for a `beacon` fictitious demo service.
"""

from datetime import datetime, timedelta
import random
import uuid
from dateutil.parser import parse

from typing import Union, List, Tuple
from typing_extensions import Annotated

from syncmodels.model import BaseModel, field_validator, Field
from syncmodels.mapper import *

# from models.generic.price import PriceSpecification
# from models.generic.schedules import OpeningHoursSpecificationSpec

# TODO: extend model corpus classes, a.k.a: the pydantic based thesaurus foundations classes
# TODO: this classes may be included in the main thesaurus when project is stable
# TODO: and others projects can benefit from them, making the thesaurus bigger and more powerful


# ---------------------------------------------------------
# Foundations Model classes
# (maybe from global model repository)
# ---------------------------------------------------------
class GeoJSON(BaseModel):
    """GeoJSON Specification"""

    type: str = "Point"
    coordinates: List[List[float]] | List[float] = [
        -0.4927112533945035,
        38.42381440278734,
    ]


# ---------------------------------------------------------
# Another group of Model classes with default comples values
# to be easily represented in FastAPI for instance
# ---------------------------------------------------------


class Location(BaseModel):
    """A GeoJSON Location with additional information"""

    address: str | None = None
    geojson: GeoJSON | None = None


DEFAULT_LOCATION = Location(
    address="Plaça de Baix, 1, 03202 Elx, Alicante",
    geojson=GeoJSON(
        coordinates=[
            [
                -0.6989062426179778,
                38.26566276366765,
            ]
        ]
    ),
)


# ---------------------------------------------------------
# Beacon relate Model classes
# ---------------------------------------------------------
class BeaconTrace(BaseModel):
    """A Beacon Trace model"""

    id: str = Field(
        description="gpdt",
        examples=[
            "11111-222222-333333-44444",
            "11111-222222-333333-55555",
            "11111-222222-333333-66666",
        ],
    )
    date: datetime
    location: GeoJSON | None = None


def random_trace(n=10):
    result = []
    n = random.randint(1, n + 1)
    start = datetime.now() - timedelta(seconds=120)
    for i in range(n):
        uid = uuid.uuid1().hex
        item = BeaconTrace(
            id=uid,
            date=start,
        )
        start = start + timedelta(seconds=2)
        result.append(item)
    return result


class BeaconDataSet(BaseModel):
    """A Beacon data set models.
    This data set contains Gpdt trace information and the datetime associated to the publishing attempt.

    """

    publish_date: datetime | None = Field(
        description="date of dataset publishing attempt",
        examples=[datetime.now()],
    )
    traces: List[BeaconTrace] = Field(
        description="List of traces",
        examples=[random_trace()],
    )


# ---------------------------------------------------------
# Some examples of other demo Model classes
# TODO: delete / replace (just for educational purposes)
# ---------------------------------------------------------
class BeaconsPreferences(BaseModel):
    name: str = Field(
        default="no_name",
        description="A name for this user travel preferences",
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


# ---------------------------------------------------------
# Main Model Class
# This represents the state of the whole application
# ---------------------------------------------------------
class BeaconAppRepresentation(BaseModel):
    """Example of an possible Beacon App Internal representation."""

    id: str
    name: str
    # summary: Optional[str] = ""
    # image_url: Optional[str] = ""
    # location: Location | dict | None = None
    # tags: Optional[List[str]] = []
    # time_table: Optional[OpeningHoursSpecification] | None = None
