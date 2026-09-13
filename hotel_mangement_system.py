import json
from datetime import date,timedelta
import textwrap
class Rooms:
    def __init__(self, room_id, room_no, room_type, price, status):
        self.room_id = room_id
        self.room_no = room_no
        self.room_type = room_type
        self.price = price
        self.status = status
    def __str__(self):
        output = f'''
        Room No : {self.room_no}
        Room Type : {self.room_type}
        Room Price : {self.price}
        Room Status : {self.status}
        '''
        return textwrap.dedent(output).strip()
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
        # load
    def GenerateRoomID(self): 
        if not self.rooms:
            return "R101"
        else:
            all_id = [int(obj.room_id[1:]) for obj in self.rooms]
            return "R" + str(max(all_id) + 1)
    def CheckRooms(self):
        if not self.rooms:
            print("No Rooms Data Available")
        else:
            return True
    def CheckInput(self,input):
        if not input.isdigit():
            print("Only Numbers Allowed")
        else:
            return True
    def InputRoomNo(self):
        while True:
            room_no = input("Enter Room No : ")
            if len(room_no) > 5 and not room_no.isdigit():
                # Assuming room no can't be 5 digits
                print("Invalid Room No")
            else:
                if not self.rooms:
                    break
                else:
                    for obj in self.rooms:
                        if obj.room_no == room_no:
                            print("Dublicate Room No")
                            break
                    else:
                        break
        return room_no
    def InputRoomType(self):
        while True:
            room_type = input("Enter Room Type (Single/Double/Deluxe/Suite) : ").upper()
            room_types = ["SINGLE","DOUBLE","DELUXE","SUITE"]
            if not room_type in room_types:
                print("Invalid Room Type")
            else:
                break
        return room_type
    def RoomPrice(self,room_type):
        prices = {
            "SINGLE":1500,
            "DOUBLE":2500,
            "DELUXE":3500,
            "SUITE":5000
            }
        price = prices[room_type]
        return price
    def InputRoomStatus(self):
        while True:
            status = input("Enter Room Status : ").upper()
            if status == "AVAILABLE" or status == "OCCUPIED":
                break
            else:
                print("Invalid Status")
        return status
    def AddRoom(self):
        room_id = self.GenerateRoomID()
        room_no = self.InputRoomNo() 
        room_type = self.InputRoomType()
        price = self.RoomPrice(room_type)
        room_status = self.InputRoomStatus()
        room = Rooms(room_id,room_no,room_type,price,room_status)
        self.rooms.append(room)
        #save
    def ViewRooms(self):
        if self.CheckRooms():
            for obj in self.rooms:
                print(obj)
    def SearchRooms(self):
        if self.CheckRooms():
            while True:
                choice = input("Search By, \n1.Room No \n2.Type \n3.Status \n---> ")
                if self.CheckInput(choice):
                    match choice:
                        case "1":
                            while True:
                                room_no = input("Enter Room No : ")
                                if self.CheckInput(room_no):
                                    for obj in self.rooms:
                                        if obj.room_no == room_no:
                                            print(obj)
                                            break
                                    else:
                                        print("Room Not Found")
                                    break
                                else:
                                    print("Invalid Room No")
                        case "2":
                            type = self.InputRoomType()
                            for obj in self.rooms():
                                if obj.room_type == type:
                                    print(obj)
                        case "3":
                            while True:
                                status = input("Enter Room Status : ").upper()
                                if status == "AVAILABLE" or status == "OCCUPIED":
                                    for obj in self.rooms:
                                        if obj.status == status:
                                            print(obj)
                                    break                                    
                                else:
                                    print("Invalid Status")
                        case _:
                            print("Invalid Choice")
                    break
    def GenerateCustomerID(self):
        if not self.customers:
            return "C10001"
        else:
            all_id = [int(obj.customer_id[2:]) for obj in self.customers]
            return "C" + str(max(all_id) + 1)
    def InputName(self):
        while True:
            name = input("Enter Your Name : ").upper()
            if name.isalpha():
                break
            else:
                print("Only Alphabets Allowed")
        return name
    def InputAge(self):
        while True:
            age = input("Enter Your Age : ")
            if self.CheckInput(age):
                age = int(age)
                if 0 <= age <= 100:
                    break
                else:
                    print("Invalid Age")
        return str(age)
    def InputPhoneNo(self):
        while True:
            phone = input("Enter your Phone No : ")
            if self.CheckInput(phone):
                if len(phone) == 10 and phone[0] != "0":
                    break
                else:
                    print("Invalid Phone No")
        return phone
    def AddCustomer(self):
        customer_id = self.GenerateCustomerID()
        name = self.InputName()
        age = self.InputAge()
        phone_no = self.InputPhoneNo()
        customer = Customers(customer_id,name,age,phone_no)
        self.customers.append(customer)
        #save
    def GenerateBookingID(self):
        if not self.bookings:
            return "B10001"
        else:
            all_id = [int(obj.booking_id[2:]) for obj in self.bookings]
            return "B" + str(max(all_id) + 1)
    def CheckCustomers(self):
        if not self.customers:
            print("No Customer Data Available")
        else:
            return True
    def CheckCustomerID(self):
        name = self.InputName()
        id = []
        for obj in self.customers:
            if obj.name == name:
                id.append(obj.customer_id)
        if len(id) == 0:
            print("Please Add Customer first")
        elif len(id) == 1:
            return id[0]
        else:
            phone = self.InputPhoneNo()
            for obj in self.customers:
                if obj.phone_no == phone:
                    return obj.customer_id
    def CheckRoomID(self):
        while True:
            room_no = input("Enter Room No Which You want to Book : ")
            if self.CheckInput(room_no):
                if len(room_no) <= 5:
                    objects = [obj for obj in self.rooms if obj.room_no == room_no]
                    if not objects:
                        print("Room Not Found")
                    else:
                        if objects[0].status == "OCCUPIED":
                            print("Room Is Currrently Occupied")
                        else:
                            break
                else:
                    print("Invalid Room No") 
        return objects[0].room_id
    def BookingDate(self):
        while True:
            check_in_date = input("Enter Date in Which You Want to Book Room (YYYY-MM-DD): ")
            try:
                current_year = date.today().year
                if current_year >= int(check_in_date[:4]) <= current_year + 1:
                    check_in_date = date.strptime(check_in_date,"%Y-%m-%d")
                    if check_in_date < date.today():
                        print("Invalid Date")
                    else:
                        break
                else:
                    print("Invalid Year")
            except ValueError:
                print("Invalid Date")
        return check_in_date
    def CalculateDate(self,date):
        while True:
            stay = input("How Many Days You Will Stay Here ? ")
            if self.CheckInput(stay):
                if len(stay) > 100:
                    print("You Can't Stay Such Days")
                else: 
                    stay = int(stay)
                    new_date = date + timedelta(days=stay)
                    break
        return new_date
    def Booking(self):
        if self.CheckCustomers() and self.CheckRooms():
            booking_id = self.GenerateBookingID()
            Customers_id = self.CheckCustomerID()
            room_id = self.CheckRoomID()
            check_in_date = self.BookingDate()
            check_out_date = self.CalculateDate(check_in_date)
            booking_status = "Check In" if check_in_date == date.today() else "Booked"
            booking = Bookings(booking_id,customer_id,room_id,check_in_date,check_out_date,booking_status)
            self.bookings.append(booking)
            #save


                
                    



