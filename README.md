# Room Booking Challenge

Welcome to the Room Booking Challenge! Your task is to implement the `book` method in the `Room` class in the `room.py` file. The method is responsible for booking a time slot for a room and updating the room's availability accordingly.

## Problem Statement

The `book` method takes a `TimeSlot` object as an argument. This object has `start_time` and `end_time` properties, both in the format 'HH:MM'. The method should remove the booked time slot from the room's availability.

Here are the cases you need to handle:

1. **The booked time slot exactly matches an availability slot:** In this case, you should remove the availability slot. For example, if a room is available from '09:00' to '10:00' and it is booked from '09:00' to '10:00', then the availability slot from '09:00' to '10:00' should be removed.

2. **The booked time slot is at the start of an availability slot:** In this case, you should update the start time of the availability slot. For example, if a room is available from '09:00' to '10:00' and it is booked from '09:00' to '09:30', then the availability slot should be updated to '09:30' to '10:00'.

3. **The booked time slot is at the end of an availability slot:** In this case, you should update the end time of the availability slot. For example, if a room is available from '09:00' to '10:00' and it is booked from '09:30' to '10:00', then the availability slot should be updated to '09:00' to '09:30'.

4. **The booked time slot is in the middle of an availability slot:** In this case, you should split the availability slot into two. For example, if a room is available from '09:00' to '10:00' and it is booked from '09:30' to '09:45', then the availability slots should be '09:00' to '09:30' and '09:45' to '10:00'.

## Instructions

1. Clone the repository and open the `room.py` file.
2. Implement the `book` method according to the problem statement. Use comments to explain your code.
3. Run the tests in `test_room.py` to check your solution.
4. If all tests pass, take a screenshot of the test results and submit it in the chat.
