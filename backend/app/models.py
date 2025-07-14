from pydantic import BaseModel, EmailStr
from typing import Optional, List
from datetime import datetime
from enum import Enum

class ReservationStatus(str, Enum):
    PENDING = "pending"
    CONFIRMED = "confirmed"
    CANCELLED = "cancelled"

class ReservationCreate(BaseModel):
    name: str
    phone: str
    email: EmailStr
    party_size: int
    reservation_date: datetime
    notes: Optional[str] = None

class ReservationResponse(BaseModel):
    id: int
    name: str
    phone: str
    email: str
    party_size: int
    reservation_date: datetime
    status: ReservationStatus
    notes: Optional[str] = None
    created_at: datetime

class ReservationUpdate(BaseModel):
    status: Optional[ReservationStatus] = None
    notes: Optional[str] = None

class AnnouncementCreate(BaseModel):
    title: str
    content: str

class AnnouncementResponse(BaseModel):
    id: int
    title: str
    content: str
    created_at: datetime
    updated_at: datetime

class AnnouncementUpdate(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None

class AdminLogin(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str
