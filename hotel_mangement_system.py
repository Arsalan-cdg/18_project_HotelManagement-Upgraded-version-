class Rooms:
    def __init__(self, room_id, room_no, room_type, price, status):
        self.room_id = room_id
        self.room_no = room_no
        self.room_type = room_type
        self.price = price
        self.status = status
class Customers:
    def __init__(self, customer_id, name, age, phone_no):
        self.customer_id = customer_id
        self.name = name
        self.age = age
        self.phone_no = phone_no
class Bookings:
    def __init__(self, booking_id, customer_id, room_id, check_in_date, check_out_date, booking_status):
        self.booking_id = booking_id
        self.customer_id = customer_id
        self.room_id = room_id
        self.check_in_date = check_in_date
        self.check_out_date = check_out_date
        self.booking_status = booking_status
class HotelManagement:
    def __init__(self):
        self.rooms = []
        self.customers = []
        self.bookings = []