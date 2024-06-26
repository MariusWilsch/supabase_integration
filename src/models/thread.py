from pydantic import BaseModel, UUID4
from typing import Optional, Dict
from datetime import datetime


class Thread(BaseModel):
    """Represents a conversation thread in the chat app.

    Member variables:
        id (UUID4): Unique identifier which references the user id in the custom user table.
        created_at (datetime): Timestamp of thread creation.
        name Optional[str]: #???
        user_id (UUID4): #! Proably the same as id. Should we just remove it?
        status (Optional[str]): #???
        meeting_booked (Optional[bool]): If the user has booked a meeting.
        meeting_date (Optional[datetime]): Date of the meeting.
        user_feedback (Optional[str]): #???
        conversation (Optional[str]): Conversation between the user and the chatbot.
        costs (Optional[float]): Costs of the entire conversation.
        time_spent_in_conve (Optional[float]): #???

    Class Methods:
        from_dict: Creates a Thread instance from a supabase response.

    Returns:
        Thread: A Thread instance.
    """

    id: UUID4
    created_at: datetime
    name: Optional[str]
    user_id: Optional[UUID4]
    status: Optional[str]
    meeting_booked: Optional[bool]
    meeting_date: Optional[datetime]
    user_feedback: Optional[str]
    conversation: Optional[str]
    costs: Optional[float]
    time_spent_in_conversation: Optional[float]

    @classmethod
    def from_dict(cls, data: Dict):
        return cls(**data)
