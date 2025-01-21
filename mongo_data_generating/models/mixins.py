from datetime import datetime

from bson import ObjectId
from pydantic import Field

from mongo_data_generating.models import fake


class CreatedTimestampMixin:
    # created_by: ObjectId = Field()
    created_by: ObjectId = Field(default_factory=ObjectId)  # For tests
    created_at: datetime | None = Field(default_factory=lambda: fake.date_time_this_year())
