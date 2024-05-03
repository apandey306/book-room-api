from room import Room
from time_slot import TimeSlot
import random

class Booking:
    def __init__(self):
        # Generate a random id to the booking
        self.id = random.randint(1000, 9999)

        self.rooms = []
        self.time_slots = []
        self.bookings = {}

        # Add dummy data to the lists
        self.rooms.append(Room("Room 1", 10))
        self.rooms.append(Room("Room 2", 8))
        self.rooms.append(Room("Room 3", 12))

        self.time_slots.append(TimeSlot("09:00", "10:00"))
        self.time_slots.append(TimeSlot("10:00", "11:00"))
        self.time_slots.append(TimeSlot("11:00", "12:00"))

    def add_room(self, room_name, capacity):
        room = Room(room_name, capacity)
        self.rooms.append(room)

    def add_time_slot(self, start_time, end_time):
        time_slot = TimeSlot(start_time, end_time)
        self.time_slots.append(time_slot)

    def check_availability(self, room_name, start_time, end_time):
        room = self.get_room_by_name(room_name)
        time_slot = self.get_time_slot(start_time, end_time)

        if room and time_slot:
            return room.is_available(time_slot)
        else:
            return False

    def book_room(self, room_name, start_time, end_time):
        room = self.get_room_by_name(room_name)
        time_slot = self.get_time_slot(start_time, end_time)
        # generate a booking ID
        booking_id = random.randint(1000, 9999)

        if room and time_slot:
            if room.is_available(time_slot):
                room.book(time_slot)
                self.bookings[booking_id] = (room_name, start_time, end_time)
                return booking_id
            else:
                return ""
        else:
            return ""

    def cancel_booking(self, booking_id):
        if booking_id in self.bookings:
            room_name, start_time, end_time = self.bookings[booking_id]
            room = self.get_room_by_name(room_name)
            time_slot = self.get_time_slot(start_time, end_time)

            if room and time_slot:
                room.add_availability(time_slot)
                del self.bookings[booking_id]
                return True

        return False

    def get_booked_rooms(self, start_time, end_time):
        booked_rooms = []
        time_slot = self.get_time_slot(start_time, end_time)

        if time_slot:
            for room in self.rooms:
                if room.is_booked(time_slot):
                    booked_rooms.append(room.name)

        return booked_rooms

    def get_room_by_name(self, room_name):
        for room in self.rooms:
            if room.name == room_name:
                return room

        return None

    def get_time_slot(self, start_time, end_time):
        return TimeSlot(start_time, end_time)