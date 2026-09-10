import json
import datetime
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
            all_id = [int(id[1:]) for id in self.rooms]
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
                
                    



