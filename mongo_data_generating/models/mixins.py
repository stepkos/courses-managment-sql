from datetime import datetime

from bson import ObjectId
from pydantic import Field

from mongo_data_generating.models import fake


class TimestampMixin:
    created_by: ObjectId = Field(default_factory=ObjectId)
    created_at: datetime | None = Field(
        default_factory=lambda: fake.date_time_this_year()
    )
