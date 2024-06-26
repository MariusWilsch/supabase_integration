from pydantic import BaseModel, UUID4
from typing import List, Optional, Dict
from datetime import datetime


class Filter(BaseModel):
    """Represents a filter for property search.

    Member variables:
        id (UUID4): Unique identifier that references the user id in the custom user table.
        created_at (datetime): Timestamp of filter creation.
        user_id (UUID4): #! Proably the same as id. Should we just remove it?
        thread_id Optional[UUID4]: References the thread id in the custom thread table.
        budget_from (Optional[int]): Minimum budget for the property.
        budget_to (Optional[int]): Maximum budget for the property.
        commercial_type (Optional[str]): Commercial type of the property.
        property_type (Optional[str]): Property type of the property.
        size_from (Optional[int]): Minimum size of the property.
        size_to (Optional[int]): Maximum size of the property.
        bedrooms_from (Optional[int]): Minimum number of bedrooms for the property.
        bedrooms_to (Optional[int]): Maximum number of bedrooms for the property.
        bathrooms_from (Optional[int]): Minimum number of bathrooms for the property.
        bathrooms_to (Optional[int]): Maximum number of bathrooms for the property.
        floor_from (Optional[int]): Minimum floor for the property.
        floor_to (Optional[int]): Maximum floor for the property.
        total_floors (Optional[int]): Total number of floors for the property.
        balcony_size_from (Optional[int]): Minimum balcony size for the property.
        balcony_size_to (Optional[int]): Maximum balcony size for the property.
        furnishing (Optional[str]): Furnishing of the property.
        parking (Optional[bool]): Whether the property has parking.
        year_of_completion_from (Optional[int]): Minimum year of completion for the property.
        year_of_completion_to (Optional[int]): Maximum year of completion for the property.
        location (Optional[str]): Location of the property.
        amenities (Optional[List[str]]): List of amenities for the property.
        other_wishes (Optional[List[str]]): List of other wishes for the property.

    Class Methods:
        from_dict: Creates a Filter instance from a supabase response.

    """

    id: UUID4
    created_at: datetime
    name: Optional[str]
    user_id: Optional[UUID4]
    thread_id: Optional[UUID4]
    budget_from: Optional[int]
    budget_to: Optional[int]
    commercial_type: Optional[str]
    property_type: Optional[str]
    size_from: Optional[int]
    size_to: Optional[int]
    bedrooms_from: Optional[int]
    bedrooms_to: Optional[int]
    bathrooms_from: Optional[int]
    bathrooms_to: Optional[int]
    floor_from: Optional[int]
    floor_to: Optional[int]
    total_floors: Optional[int]
    balcony_size_from: Optional[int]
    balcony_size_to: Optional[int]
    furnishing: Optional[str]
    parking: Optional[bool]
    year_of_completion_from: Optional[int]
    year_of_completion_to: Optional[int]
    location: Optional[str]
    amenities: Optional[List[str]]
    other_wishes: Optional[List[str]]

    @classmethod
    def from_dict(cls, data: Dict):
        return cls(**data)
