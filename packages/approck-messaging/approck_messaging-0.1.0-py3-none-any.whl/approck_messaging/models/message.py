import enum
from typing import Optional, List

from pydantic import BaseModel, HttpUrl


class MessageType(str, enum.Enum):
    GENERIC = "generic"
    VIDEO_NOTE = "video_note"


class MessageButton(BaseModel):
    label: str
    url: HttpUrl


class Message(BaseModel):
    type: MessageType

    # Generic
    caption: Optional[str] = None
    media: Optional[List[HttpUrl]] = None
    buttons: Optional[List[MessageButton]] = None

    # Video Note
    video_note: Optional[HttpUrl] = None


class TransportMessageRecipient(BaseModel):
    telegram_id: int


class TransportMessage(Message):
    recipient: TransportMessageRecipient
