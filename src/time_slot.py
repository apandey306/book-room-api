class TimeSlot:
    def __init__(self, start_time, end_time):
        self.start_time = start_time
        self.end_time = end_time
        self.is_available = True

    def book(self):
        if self.is_available:
            self.is_available = False
            return True
        else:
            return False

    def cancel_booking(self):
        if not self.is_available:
            self.is_available = True
            return True
        else:
            return False

    def __eq__(self, other):
        return self.start_time == other.start_time and self.end_time == other.end_time

    def __str__(self):
        return f'{self.start_time} - {self.end_time}'