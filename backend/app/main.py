from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.middleware.cors import CORSMiddleware
from datetime import timedelta
from typing import List

from .models import (
    ReservationCreate, ReservationResponse, ReservationUpdate,
    AnnouncementCreate, AnnouncementResponse, AnnouncementUpdate,
    AdminLogin, Token
)
from .database import db
from .auth import authenticate_admin, create_access_token, verify_token, ACCESS_TOKEN_EXPIRE_MINUTES

app = FastAPI(title="Apaiser Cafe API", version="1.0.0")

# Disable CORS. Do not remove this for full-stack development.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

@app.get("/healthz")
async def healthz():
    return {"status": "ok"}

@app.get("/api/announcements", response_model=List[AnnouncementResponse])
async def get_announcements():
    """Get all announcements (public endpoint)"""
    return db.get_all_announcements()

@app.get("/api/announcements/{announcement_id}", response_model=AnnouncementResponse)
async def get_announcement(announcement_id: int):
    """Get a specific announcement (public endpoint)"""
    announcement = db.get_announcement(announcement_id)
    if not announcement:
        raise HTTPException(status_code=404, detail="Announcement not found")
    return announcement

@app.post("/api/reservations", response_model=ReservationResponse)
async def create_reservation(reservation: ReservationCreate):
    """Create a new reservation (public endpoint)"""
    try:
        return db.create_reservation(reservation.dict())
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/api/admin/login", response_model=Token)
async def admin_login(login_data: AdminLogin):
    """Admin login endpoint"""
    if not authenticate_admin(login_data.username, login_data.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": login_data.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

@app.get("/api/admin/reservations", response_model=List[ReservationResponse])
async def get_all_reservations(current_user: str = Depends(verify_token)):
    """Get all reservations (admin only)"""
    return db.get_all_reservations()

@app.get("/api/admin/reservations/{reservation_id}", response_model=ReservationResponse)
async def get_reservation(reservation_id: int, current_user: str = Depends(verify_token)):
    """Get a specific reservation (admin only)"""
    reservation = db.get_reservation(reservation_id)
    if not reservation:
        raise HTTPException(status_code=404, detail="Reservation not found")
    return reservation

@app.put("/api/admin/reservations/{reservation_id}", response_model=ReservationResponse)
async def update_reservation(
    reservation_id: int, 
    reservation_update: ReservationUpdate,
    current_user: str = Depends(verify_token)
):
    """Update a reservation (admin only)"""
    updated_reservation = db.update_reservation(reservation_id, reservation_update.dict(exclude_unset=True))
    if not updated_reservation:
        raise HTTPException(status_code=404, detail="Reservation not found")
    return updated_reservation

@app.delete("/api/admin/reservations/{reservation_id}")
async def delete_reservation(reservation_id: int, current_user: str = Depends(verify_token)):
    """Delete a reservation (admin only)"""
    if not db.delete_reservation(reservation_id):
        raise HTTPException(status_code=404, detail="Reservation not found")
    return {"message": "Reservation deleted successfully"}

@app.post("/api/admin/announcements", response_model=AnnouncementResponse)
async def create_announcement(
    announcement: AnnouncementCreate,
    current_user: str = Depends(verify_token)
):
    """Create a new announcement (admin only)"""
    return db.create_announcement(announcement.dict())

@app.put("/api/admin/announcements/{announcement_id}", response_model=AnnouncementResponse)
async def update_announcement(
    announcement_id: int,
    announcement_update: AnnouncementUpdate,
    current_user: str = Depends(verify_token)
):
    """Update an announcement (admin only)"""
    updated_announcement = db.update_announcement(announcement_id, announcement_update.dict(exclude_unset=True))
    if not updated_announcement:
        raise HTTPException(status_code=404, detail="Announcement not found")
    return updated_announcement

@app.delete("/api/admin/announcements/{announcement_id}")
async def delete_announcement(announcement_id: int, current_user: str = Depends(verify_token)):
    """Delete an announcement (admin only)"""
    if not db.delete_announcement(announcement_id):
        raise HTTPException(status_code=404, detail="Announcement not found")
    return {"message": "Announcement deleted successfully"}
