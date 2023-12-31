# -*- coding: utf-8 -*-
"""Myers.Kaydian-Pythoncode-ITT103-F2023.PY

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Q7g8czv0oHn5DJF8dEapHdIIr14QzAPc
"""

# Constants
FIRST_CLASS_ROWS = 3
FIRST_CLASS_COLUMNS = 9
BUSINESS_CLASS_ROWS = 4
BUSINESS_CLASS_COLUMNS = 9
ECONOMY_CLASS_ROWS = 8
ECONOMY_CLASS_COLUMNS = 7

# Initialize two-dimensional arrays to represent seat availability
first_class_seats = [['E'] * FIRST_CLASS_COLUMNS for _ in range(FIRST_CLASS_ROWS)]
business_class_seats = [['E'] * BUSINESS_CLASS_COLUMNS for _ in range(BUSINESS_CLASS_ROWS)]
economy_class_seats = [['E'] * ECONOMY_CLASS_COLUMNS for _ in range(ECONOMY_CLASS_ROWS)]

# Dictionary to map user choices to seat classes
class_mapping = {'F': 'First Class', 'B': 'Business Class', 'E': 'Economy Class'}

def display_menu():
    print("UCC Signature Express Limited")
    print("<For Comfort And Safety Choose SIgnature And Express Limited>")
    print("Reservation Options:")
    print("  First Class (F/f)")
    print("  Business Class (B/b)")
    print("  Economy Class (E/e)")
    print("  Quit or Cancel (Q/q)")
    print("Please select an option:")

def reserve_seat(seat_class):
    # Prompt the user for a row number
    row_number = int(input("Enter the row number (positive integer): "))

    # Prompt the user for a seat preference (window/aisle)
    column_number = int(input("Enter the column number (positive integer): "))

    if row_number <= 0 or column_number <= 0:
        print("Number must be positive or greater than zero!")
        return

    # Display the message while processing the user's request
    print(f"Reserving seat: row {row_number:02d} column {column_number:02d}")

    # Select the appropriate seat array based on the class
    if seat_class == 'F':
        seat_array = first_class_seats
    elif seat_class == 'B':
        seat_array = business_class_seats
    elif seat_class == 'E':
        seat_array = economy_class_seats
    else:
        print("Invalid choice!")
        return

    # Check if the seat is available
    if seat_array[row_number - 1][column_number - 1] == 'E':
        # Reserve the seat
        seat_array[row_number - 1][column_number - 1] = 'X'
        print("Seat reserved successfully!")
    else:
        print("Seat already reserved!")

def print_seat_info(seat_class):
    total_seats = 0
    reserved_seats = 0

    # Select the appropriate seat array based on the class
    if seat_class == 'F':
        seat_array = first_class_seats
    elif seat_class == 'B':
        seat_array = business_class_seats
    elif seat_class == 'E':
        seat_array = economy_class_seats
    else:
        print("Invalid choice!")
        return

    # Calculate total and reserved seats
    for row in seat_array:
        total_seats += len(row)
        reserved_seats += row.count('X')

    # Print seat information
    print(f"\nReservation Type: {class_mapping[seat_class]}")
    print(f"Total number of seats: {total_seats}")
    print(f"Total number of seats reserved: {reserved_seats}")

# Main program loop
while True:
    display_menu()

    user_choice = input().upper()

    if user_choice == 'Q':
        print_seat_info('F')
        print_seat_info('B')
        print_seat_info('E')
        print("\nThank you for reserving a seat with us!")
        break
    elif user_choice in ['F', 'B', 'E']:
        reserve_seat(user_choice)
    else:
        print("Invalid choice! Please try again.")

from google.colab import drive
drive.mount('/content/drive')