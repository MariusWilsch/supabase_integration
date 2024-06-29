from pydantic import BaseModel, UUID4, EmailStr
from typing import Dict
from datetime import datetime


# class User(BaseModel):
#     """
#     Represents a custom user table in the database.

#     Member variables:
#         id (str): Unique identifier based on auth.users table.
#         created_at (datetime): Timestamp of user creation.
#         name (str): User's name (required).
#         email (EmailStr): User's email address (required).
#         user_id (str | None): Unique identifier for the user.
#         login (str | None): User's login name.
#         phone_number (str | None): User's phone number.
#         social_media (str | None): User's type of social media.
#         social_media_name (str | None): User's social media name.
#         communication_channel (str | None): Preferred communication channel.
#         communication_channel_name (str | None): # ???
#         last_contacted (datetime | None): Timestamp of last contact.

#     Class Methods:
#         from_dict: Creates a User instance from a supabase response.
#     """

#     id: str
#     created_at: datetime = None
#     name: str
#     user_id: str = None
#     login: str = None
#     phone_number: str = None
#     email: EmailStr
#     social_media: str = None
#     social_media_name: str = None
#     communication_channel: str = None
#     communication_channel_name: str = None
#     last_contacted: datetime = None

#     @classmethod
#     def from_dict(cls, data: Dict):
#         return cls(**data)

from pydantic import BaseModel, EmailStr
from typing import Dict, Optional
from datetime import datetime


class User(BaseModel):
    id: str
    created_at: Optional[datetime] = None
    name: str
    user_id: Optional[str] = None
    login: Optional[str] = None
    phone_number: Optional[str] = None
    email: Optional[str] = None
    social_media: Optional[str] = None
    social_media_name: Optional[str] = None
    communication_channel: Optional[str] = None
    communication_channel_name: Optional[str] = None
    last_contacted: Optional[datetime] = None
