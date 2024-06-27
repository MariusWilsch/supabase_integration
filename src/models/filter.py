from pydantic import BaseModel, UUID4
from typing import List, Optional, Dict
from datetime import datetime


class Filter(BaseModel):
    """Represents a filter for property search.

    Member variables:
        TBD

    Class Methods:
        from_dict: Creates a Filter instance from a supabase response.

    """

    id: Optional[str]
    user_id: str
    thread_id: str
    created_at: Optional[datetime] = None
    name: Optional[str] = None
    budget_from: Optional[int] = None
    budget_to: Optional[int] = None
    commercial_type: Optional[str] = None
    property_type: Optional[str] = None
    size_from: Optional[int] = None
    size_to: Optional[int] = None
    bedrooms_from: Optional[int] = None
    bedrooms_to: Optional[int] = None
    bathrooms_from: Optional[int] = None
    bathrooms_to: Optional[int] = None
    floor_from: Optional[int] = None
    floor_to: Optional[int] = None
    total_floors: Optional[int] = None
    balcony_size_from: Optional[int] = None
    balcony_size_to: Optional[int] = None
    furnishing: Optional[str] = None
    parking: Optional[bool] = None
    year_of_completion_from: Optional[int] = None
    year_of_completion_to: Optional[int] = None
    location: Optional[str] = None
    amenities: Optional[List[str]] = None
    other_wishes: Optional[List[str]] = None
