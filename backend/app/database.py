from typing import Dict, List, Optional
from datetime import datetime
from .models import ReservationResponse, AnnouncementResponse, ReservationStatus
import threading

class InMemoryDatabase:
    def __init__(self):
        self.reservations: Dict[int, dict] = {}
        self.announcements: Dict[int, dict] = {}
        self.reservation_counter = 1
        self.announcement_counter = 1
        self.lock = threading.Lock()
        
        self._add_sample_data()
    
    def _add_sample_data(self):
        sample_announcements = [
            {
                "title": "新メニューのご案内",
                "content": "季節限定の桜ラテと抹茶チーズケーキを追加いたしました。ぜひお試しください。"
            },
            {
                "title": "営業時間変更のお知らせ",
                "content": "4月より営業時間を平日9:00-20:00、土日祝9:00-21:00に変更いたします。"
            },
            {
                "title": "Wi-Fi環境改善のお知らせ",
                "content": "店内のWi-Fi環境を改善いたしました。より快適にお過ごしいただけます。"
            }
        ]
        
        for announcement in sample_announcements:
            now = datetime.now()
            self.announcements[self.announcement_counter] = {
                "id": self.announcement_counter,
                "title": announcement["title"],
                "content": announcement["content"],
                "created_at": now,
                "updated_at": now
            }
            self.announcement_counter += 1

    def create_reservation(self, reservation_data: dict) -> ReservationResponse:
        with self.lock:
            reservation_id = self.reservation_counter
            now = datetime.now()
            
            reservation = {
                "id": reservation_id,
                "name": reservation_data["name"],
                "phone": reservation_data["phone"],
                "email": reservation_data["email"],
                "party_size": reservation_data["party_size"],
                "reservation_date": reservation_data["reservation_date"],
                "status": ReservationStatus.PENDING,
                "notes": reservation_data.get("notes"),
                "created_at": now
            }
            
            self.reservations[reservation_id] = reservation
            self.reservation_counter += 1
            
            return ReservationResponse(**reservation)
    
    def get_reservation(self, reservation_id: int) -> Optional[ReservationResponse]:
        reservation = self.reservations.get(reservation_id)
        if reservation:
            return ReservationResponse(**reservation)
        return None
    
    def get_all_reservations(self) -> List[ReservationResponse]:
        return [ReservationResponse(**reservation) for reservation in self.reservations.values()]
    
    def update_reservation(self, reservation_id: int, update_data: dict) -> Optional[ReservationResponse]:
        with self.lock:
            if reservation_id not in self.reservations:
                return None
            
            reservation = self.reservations[reservation_id]
            for key, value in update_data.items():
                if value is not None:
                    reservation[key] = value
            
            return ReservationResponse(**reservation)
    
    def delete_reservation(self, reservation_id: int) -> bool:
        with self.lock:
            if reservation_id in self.reservations:
                del self.reservations[reservation_id]
                return True
            return False

    def create_announcement(self, announcement_data: dict) -> AnnouncementResponse:
        with self.lock:
            announcement_id = self.announcement_counter
            now = datetime.now()
            
            announcement = {
                "id": announcement_id,
                "title": announcement_data["title"],
                "content": announcement_data["content"],
                "created_at": now,
                "updated_at": now
            }
            
            self.announcements[announcement_id] = announcement
            self.announcement_counter += 1
            
            return AnnouncementResponse(**announcement)
    
    def get_announcement(self, announcement_id: int) -> Optional[AnnouncementResponse]:
        announcement = self.announcements.get(announcement_id)
        if announcement:
            return AnnouncementResponse(**announcement)
        return None
    
    def get_all_announcements(self) -> List[AnnouncementResponse]:
        announcements = list(self.announcements.values())
        announcements.sort(key=lambda x: x["created_at"], reverse=True)
        return [AnnouncementResponse(**announcement) for announcement in announcements]
    
    def update_announcement(self, announcement_id: int, update_data: dict) -> Optional[AnnouncementResponse]:
        with self.lock:
            if announcement_id not in self.announcements:
                return None
            
            announcement = self.announcements[announcement_id]
            for key, value in update_data.items():
                if value is not None:
                    announcement[key] = value
            announcement["updated_at"] = datetime.now()
            
            return AnnouncementResponse(**announcement)
    
    def delete_announcement(self, announcement_id: int) -> bool:
        with self.lock:
            if announcement_id in self.announcements:
                del self.announcements[announcement_id]
                return True
            return False

db = InMemoryDatabase()
