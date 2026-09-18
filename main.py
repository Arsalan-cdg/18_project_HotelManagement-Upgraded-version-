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
    def __str__(self):
        output = f'''
        Customer ID : {self.customer_id}
        Name : {self.name}
        Age : {self.age}
        Phone No : {"X"*6+self.phone_no[6:]}
        '''
        return textwrap.dedent(output).strip()
class Bookings:
    def __init__(self, booking_id, customer_id, room_id, check_in_date, check_out_date, booking_status):
        self.booking_id = booking_id
        self.customer_id = customer_id
        self.room_id = room_id
        self.check_in_date = check_in_date
        self.check_out_date = check_out_date
        self.booking_status = booking_status
    def __str__(self):
        output = f'''
        Booking ID : {self.booking_id}
        Customer ID : {self.customer_id}
        Room ID : {self.room_id}
        Check In Date : {self.check_in_date}
        Check Out Date : {self.check_out_date}
        Booking Status : {self.booking_status} 
        '''
        return textwrap.dedent(output).strip()
class HotelManagement:
    def __init__(self):
        self.rooms = []
        self.customers = []
        self.bookings = []
        self.LoadRoomsData()
        self.LoadCustomersData()
        self.LoadBookingsData()
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
    def AddRoom(self):
        room_id = self.GenerateRoomID()
        room_no = self.InputRoomNo() 
        room_type = self.InputRoomType()
        price = self.RoomPrice(room_type)
        room_status = "AVAILABLE"
        room = Rooms(room_id,room_no,room_type,price,room_status)
        self.rooms.append(room)
        self.SaveRoomsData()
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
        self.SaveCustomersData()
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
        phone_no = self.InputPhoneNo()
        id = [obj.customer_id for obj in self.customers if obj.name == name and obj.phone_no == phone_no]
        if not id:
            print("Please Add Customer first")
        else:
            return id[0]
    def CheckRoomID(self):
        while True:
            room_no = input("Enter Room No Which You want to Book : ")
            if self.CheckInput(room_no):
                if len(room_no) <= 5:
                    obj = [obj for obj in self.rooms if obj.room_no == room_no]
                    if not obj:
                        print("Room Not Found")
                    else:
                        obj = obj[0]
                        if obj.status == "OCCUPIED":
                            print("Room Is Currrently Occupied")
                        else:
                            obj.status = "OCCUPIED"
                            self.SaveRoomsData()
                            break
                else:
                    print("Invalid Room No")
        return obj.room_id

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
            booking_status = "BOOKED"
            booking = Bookings(booking_id,customer_id,room_id,check_in_date,check_out_date,booking_status)
            self.bookings.append(booking)
            self.SaveBookingsData()
    def CheckInAndOut(self):
        booking_id = input("Enter Booking ID : ")
        if booking_id.isalnum():
            obj = [obj for obj in self.bookings if obj.booking_id == booking_id]
            if not obj:
                print("Invalid Booking ID")
            else:
                obj = obj[0]
                if date.today() == obj.check_in_date:
                    obj.booking_status = "CHECK IN"
                    print("You Check In")
                    self.SaveBookingsData()
                elif date.today() == obj.check_out_date:
                    obj.booking_status = "COMPLETED"
                    print("You Check Out")
                    print(self.GenerateBill(obj))
                    room_id = obj.room_id
                    for obj in self.rooms:
                        if obj.room_id == room_id:
                            obj.status = "AVAILABLE"
                    self.SaveBookingsData()
                    self.SaveRoomsData()
                else:
                    print("Please Check Your Check IN and Out Dates")
        else:
            print("Invalid Booking ID")
    def ViewCustomerInfo(self):
        if self.CheckRooms():
            if self.customers:
                name = self.InputName() 
                phone_no = self.InputPhoneNo()             
                customer_obj = [obj for obj in self.customers if obj.name == name and obj.phone_no == phone_no]
                if not customer_obj:
                    print("Please Add Customer First")
                else:
                    customer_obj = customer_obj[0]
                    customer_id = customer_obj.customer_id
                    if self.bookings:
                        booking_obj = [obj for obj in self.bookings if obj.customer_id == customer_id]
                        if not booking_obj:
                            print(customer_obj)
                            print("You Have Not Book Any Room Yet!")
                        else:
                            print(booking_obj[0])
                    else:
                        print("You Have Not Book Any Room Yet!")
            else:
                print("Please Add Customer First")
    def CancelBooking(self):
        if not self.bookings:
            print("There Are No Bookings")
        else:
            booking_id = input("Enter Your Booking ID : ")
            if booking_id.isalnum():
                booking_obj = [obj for obj in self.bookings if obj.booking_id == booking_id]
                if not booking_obj:
                    print("You Have Not Book any Room")
                else:
                    booking_obj = booking_obj[0]
                    if booking_obj.booking_status == "BOOKED":
                        choice = input("Do You Want to Cancel Your Booking(Y/N) : ").upper()
                        if choice == "Y":
                            booking_obj.booking_status = "CANCELLED"
                            room_id = booking_obj.room_id
                            room_obj = [obj for obj in self.rooms if obj.room_id == room_id]
                            room_obj = room_obj[0]
                            room_obj.status = "AVAILABLE"
                            print("Your Booking is Successfully Cancelled")
                            self.SaveBookingsData()
                            self.SaveRoomsData()
                        elif choice == "N":
                            print("OK,Your Booking is Still Active")
                        else:
                            print("Invalid Choice")
                    else:
                        print("You Can't Cancel Your Booking")
            else:
                print("Invalid Booking ID")
    def GenerateBill(self,booking_obj):
        room_id = booking_obj.room_id
        customer_id = booking_obj.customer_id
        room_obj = [obj for obj in self.rooms if obj.room_id == room_id]
        room_obj = room_obj[0]
        customer_obj = [obj for obj in self.customers if obj.customer_id == customer_id]
        customer_obj = customer_obj[0]
        check_in_date = booking_obj.check_in_date
        check_out_date = booking_obj.check_out_date
        stay = int((str(check_out_date - check_in_date).split(" "))[0])
        room_price = room_obj.price
        bill = stay*room_price
        output = f'''
        Your Bill ------------------------------------
        Name : {customer_obj.name}
        Customer ID : {customer_obj.customer_id}
        Booking ID : {booking_obj.booking_id}
        Room ID : {room_obj.room_id}
        Room Type : {room_obj.room_type}
        Room Price/Night : {room_price} Rs
        Check In Date : {check_in_date}
        Check Out Date : {check_out_date}
        You Stay Here : {stay} Days
        ----------------------------------------------
        Total Bill : {bill} Rs
        '''
        return textwrap.dedent(output).strip()
    def SaveRoomsData(self):
        rooms_data = {}
        for obj in self.rooms:
            rooms_data[obj.room_id] = {"Room No":obj.room_no,"Room Type":obj.room_type,"Status":obj.status,"Price":obj.price}
        with open("rooms_data.json","w") as f:
            json.dump(rooms_data,f,indent=4)
    def SaveCustomersData(self):
        customers_data = {}
        for obj in self.customers:
            customers_data[obj.customer_id] = {"Name":obj.name,"Age":obj.age,"Phone No":obj.phone_no}
        with open("customers_data","w") as f:
            json.dump(customers_data,f,indent=4)
    def SaveBookingsData(self):
        bookings_data = {}
        for obj in self.bookings:
            bookings_data[obj.booking_id] = {"Customer ID":obj.customer_id,"Room ID":obj.room_id,"Check In Date":obj.check_in_date,"Check Out Date":obj.check_out_date,"Booking Status":obj.booking_status}
        with open("bookings_data","w") as f:
            json.dump(bookings_data,f,indent=4)
    def LoadRoomsData(self):
        try:
            with open("rooms_data") as f:
                rooms_data = json.load(f)
            for id,info in rooms_data.items():
                room = Rooms(id,info["Room No"],info["Room Type"],info["Price"],info["Status"])
                self.rooms.append(room)
        except FileNotFoundError,json.JSONDecodeError:
            return
    def LoadCustomersData(self):
        try:
            with open("customers_data") as f:
                customers_data = json.load(f)
            for id,info in customers_data.items():
                customer = Customers(id,info["Name"],info["Age"],info["Phone No"])
                self.customers.append(customer)
        except FileNotFoundError,json.JSONDecodeError:
            return
    def LoadBookingsData(self):
        try:
            with open("bookings_data") as f:
                bookings_data = json.load(f)
            for id,info in bookings_data.items():
                check_in_date = info["Check In Date"]
                check_in_date = date.strptime(check_in_date,"%Y-%m-%d")
                check_out_date = info["Check Out Date"]
                check_out_date = date.strptime(check_out_date,"%Y-%m-%d")
                booking = Bookings(id,info["Customer ID"],info["Room ID"],check_in_date,check_out_date,info["Booking Status"])
                self.bookings.append(booking)
        except FileNotFoundError,json.JSONDecodeError:
            return
hotel_management = HotelManagement()
def menu():
    print('''
    1.Add Rooms
    2.View Rooms
    3.Search Rooms
    4.Add Customer
    5.Create Booking
    6.Check IN or OUT
    7.Customer Info
    8.Cancel Booking
    9.Exit
    ''')
def InputChoice():
    while True:
        try:
            choice = int(input("Enter Your Choice : "))
            break
        except ValueError:
            print("Only Numbers Allowed")
    return choice
while True:
    menu()
    InputChoice()
    if choice == 1:
        hotel_management.AddRoom()
    elif choice == 2:
        hotel_management.ViewRooms()
    elif choice == 3:
        hotel_management.SearchRooms()
    elif choice == 4:
        hotel_management.AddCustomer()
    elif choice == 5:
        hotel_management.Booking()
    elif choice == 6:
        hotel_management.CheckInAndOut()
    elif choice == 7:
        hotel_management.ViewCustomerInfo()
    elif choice == 8:
        hotel_management.CancelBooking()
    elif choice == 9:
        print("Exited")
        break
    else:
        print("Invalid Choice")


