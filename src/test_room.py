# add src to the sys.path
import sys
sys.path.append('src')
import unittest
from room import Room
from time_slot import TimeSlot

class TestRoom(unittest.TestCase):
    def setUp(self):
        # Set up any necessary objects or variables for the tests
        self.room = Room("Meeting Room 1", 10)
        self.availability = [TimeSlot("09:00", "10:00"), TimeSlot("11:00", "12:00"), TimeSlot("14:00", "15:00")]

    def test_book_available_slot(self):
        # Test booking an available time slot
        time_slot = TimeSlot("09:00", "10:00")
        self.room.book(time_slot)
        self.assertNotIn(time_slot, self.room.availability)

    def test_book_partial_overlap(self):
        # Test booking a time slot that partially overlaps with an existing availability slot
        time_slot = TimeSlot("09:00", "09:30")
        self.room.book(time_slot)
        expected_availability = [TimeSlot("09:30", "10:00"), TimeSlot("11:00", "12:00"), TimeSlot("14:00", "15:00")]
        self.assertEqual(self.room.availability, expected_availability)

    def test_book_no_overlap(self):
        # Test booking a time slot that has no overlap with any existing availability slot
        time_slot = TimeSlot("21:30", "22:00")
        self.room.book(time_slot)
        expected_availability = [TimeSlot("09:00", "10:00"), TimeSlot("11:00", "12:00"), TimeSlot("14:00", "15:00")]
        self.assertEqual(self.room.availability, expected_availability)

if __name__ == '__main__':
    unittest.main()