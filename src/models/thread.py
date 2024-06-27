from pydantic import BaseModel, UUID4
from typing import Optional, Dict
from datetime import datetime


class Thread(BaseModel):
    """Represents a conversation thread in the chat app.

    Member variables:
        TBD

    Class Methods:
        from_dict: Creates a Thread instance from a supabase response.

    Returns:
        Thread: A Thread instance.
    """

    id: Optional[str]
    user_id: str
    created_at: Optional[datetime] = None
    name: Optional[str] = None
    status: Optional[str] = None
    meeting_booked: Optional[bool] = None
    meeting_date: Optional[datetime] = None
    user_feedback: Optional[str] = None
    conversation: Optional[dict] = None
    costs: Optional[float] = None
    time_spent_in_conversation: Optional[float] = None

    @classmethod
    def from_dict(cls, data: Dict):
        return cls(**data)
