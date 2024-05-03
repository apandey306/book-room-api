from booking import Booking
from room import Room
from time_slot import TimeSlot

def main():
    # Initialize the booking system
    booking = Booking()

    # Display available options to the user
    print("Welcome to the Meeting Room Booking System!")
    print("1. Book a meeting room")
    print("2. View availability slots for a room")
    print("3. Exit")

    while True:
        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            # Get user input for booking details
            room_name = input("Enter the room name: ")
            start_time = input("Enter the start time (HH:MM): ")
            end_time = input("Enter the end time (HH:MM): ")
            no_of_people = int(input("Enter the number of people: "))

            # Check room availability and book if available
            if booking.check_availability(room_name, start_time, end_time):
                booking_id = booking.book_room(room_name, start_time, end_time)
                print("Room booked successfully!")
                print("Booking ID:", booking_id)
            else:
                print("Room is not available for the specified time slot.")

        elif choice == "2":
            # Check the availability slots for a given room
            room_name = input("Enter the room name: ")
            room = booking.get_room_by_name(room_name)
            available_slots = room.get_available_slots()
            print("Available slots for", room_name + ":")
            for slot in available_slots:
                print(slot.start_time, "-", slot.end_time)
        elif choice == "3":
            print("Thank you for using the Meeting Room Booking System!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()