# Hotel Management System

A Python hotel management system built using Object-Oriented Programming and JSON data storage. It allows users to manage rooms, customers, bookings, check-in/check-out, cancellations, and hotel information.

## Features

- Add and manage hotel rooms
- Assign room types and prices
- View all rooms
- Search rooms by room number, type, or status
- Add customers
- Validate customer information
- Create room bookings
- Set check-in and check-out dates
- Check customers in and out
- Generate bills based on room price and stay duration
- View customer information
- Cancel bookings
- View all bookings
- Search bookings by status
- Save room, customer, and booking data to JSON files
- Load saved data automatically

## Concepts Used

- Object-Oriented Programming (OOP)
- Classes and objects
- Constructors (`__init__`)
- Instance attributes
- Instance methods
- `self`
- `__str__()`
- Lists
- Dictionaries
- List comprehensions
- Functions
- JSON module
- `json.dump()`
- `json.load()`
- File handling
- `with open()`
- `datetime` module
- `date.today()`
- `timedelta()`
- `datetime.strptime()`
- `try` and `except`
- `for` and `while` loops
- `if`, `elif`, and `else`
- `match` statement
- `break` and `continue`
- Type conversion
- String methods
- Basic input validation
- Data persistence using JSON
- Basic date calculations

>This project was built while learning Python fundamentals and may be improved as I gain more experience.

## How to Run

Make sure Python is installed.

The program uses three JSON files to store data:

- `rooms_data.json` — stores room information
- `customers_data.json` — stores customer information
- `bookings_data.json` — stores booking information

These files are automatically created when the corresponding data is saved. They do not need to exist before the first run.

Then run:

```bash
python 18_hotel_management.py

