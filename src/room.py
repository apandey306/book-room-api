from time_slot import TimeSlot

class Room:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.availability = []
        # Add dummy data for availability
        self.availability.append(TimeSlot(start_time='09:00', end_time='10:00'))
        self.availability.append(TimeSlot(start_time='11:00', end_time='12:00'))
        self.availability.append(TimeSlot(start_time='14:00', end_time='15:00'))

    def add_availability(self, time_slot):
        self.availability.append(time_slot)

    def book(self, time_slot):
        # To be implemented
        pass

    def is_available(self, time_slot):
        # Check if the time_slot lies within the availability slots
        # First convert the start and end time strings in HH:MM format to minutes
        start_time = int(time_slot.start_time.split(':')[0]) * 60 + int(time_slot.start_time.split(':')[1])
        end_time = int(time_slot.end_time.split(':')[0]) * 60 + int(time_slot.end_time.split(':')[1])
        for slot in self.availability:
            slot_start_time = int(slot.start_time.split(':')[0]) * 60 + int(slot.start_time.split(':')[1])
            slot_end_time = int(slot.end_time.split(':')[0]) * 60 + int(slot.end_time.split(':')[1])
            if start_time >= slot_start_time and end_time <= slot_end_time:
                return True

        return False
        
    def is_booked(self, time_slot):
        for slot in self.availability:
            if slot.start_time == time_slot.start_time and slot.end_time == time_slot.end_time:
                return False
        return True

    def get_available_slots(self):
        return self.availability