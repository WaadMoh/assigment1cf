from enum import Enum

class Gender(Enum):
    Male = "Male"
    Female = "Female"
class Currency(Enum):
    AED = "AED"
    USD = "USD"

class Customer:
    def __init__(self, firstName, lastName,gender,dateOfBirth,emiratesID,phoneNumber):
        self.__firstName=firstName
        self.__lastName=lastName
        self.__gender=gender
        self.__dateOfBirth=dateOfBirth
        self.__emiratesID=emiratesID
        self.__phoneNumber=phoneNumber


    def get_firstName(self):
        return self.__firstName

    def set_firstName(self,firstName):
        self.__firstName = firstName

    def get_lastName(self):
        return self.__lastName

    def set_lastName(self, lastName):
        self.__lastName=lastName

    def get_gender(self):
        return self.__gender

    def set_gender(self, gender):
        self.__gender=gender

    def get_dateOfBirth(self):
        return self.__dateOfBirth

    def set_dateOfBirth(self, dateOfBirth):
        self.__dateOfBirth=dateOfBirth

    def get_emiratesID(self):
        return self.__emiratesID

    def set_emiratesID(self, emiratesID):
        self.__emiratesID=emiratesID

    def get_phoneNumber(self):
        return self.__phoneNumber

    def set_phoneNumber(self, phoneNumber):
        self.__phoneNumber=phoneNumber

    def searchRooms(self):
        pass

    def viewReservation(self):
        pass

    def register(self):
        pass

    def login(self):
        pass

class Reservation:
    def __init__(self, reservationID, checkInDate, checkOutDate, status, amount):
        self.__reservationID =reservationID
        self.__checkInDate = checkInDate
        self.__checkOutDate = checkOutDate
        self.__status = status
        self.__amount = amount


    def get_reservationID(self):
        return self.__reservationID
    def set_reservationID(self,reservationID):
        self.__reservationID=reservationID

    def get_checkInDate(self):
        return self.__checkInDate
    def set_checkInDate(self,checkInDate):
        self.__checkInDate = checkInDate

    def get_checkOutDatee(self):
        return self.__checkOutDate
    def set_checkOutDate(self,checkOutDate):
        self.__checkOutDate = checkOutDate

    def get_status(self):
        return self.__status
    def set_status(self, status):
        self.__status = status

    def get_amount(self):
        return self.__amount
    def set_amount(self, amount):
        self.__amount = amount

    def confirmReservation(self):
        pass
    def updateReservation(self):
        pass
    def cancelReservation(self):
        pass

class Room:
    def __init__(self,roomNum,roomFloor, roomType,roomPrice,availability):
        self.__roomNum = roomNum
        self.__roomFloor = roomFloor
        self.__roomType = roomType
        self.__roomPrice = roomPrice
        self.__availability = availability


    def get_roomNum(self):
        return self.__roomNum
    def set_roomNum(self,roomNum):
        self.__roomNum = roomNum

    def get_roomFloor(self):
        return self.__roomFloor
    def set_roomFloor(self,roomFloor):
        self.__roomFloor = roomFloor

    def get_roomType(self):
        return self.__roomType
    def set_roomType(self,roomType):
        self.__roomType = roomType

    def get_roomPrice(self):
        return self.__roomPrice
    def set_roomPrice(self,roomPrice):
        self.__roomPrice = roomPrice

    def get_availability(self):
        return self.__availability
    def set_availability(self,availability):
        self.__availability = availability

    def checkAvailability(self):
        return self.__availability
    def updateAvailability(self):
        pass

class Payment:
    def __init__(self, amount,paymentMethod, paymentStatus, currency, cardNum):
        self.__amount=amount
        self.__paymentMethod=paymentMethod
        self.__paymentStatus=paymentStatus
        self.__currency=currency
        self.__cardNum=cardNum


    def get_amount(self):
        return self.__amount
    def set_amount(self,amount):
        self.__amount=amount

    def get_paymentMethod(self):
        return self.__paymentMethod
    def set_paymentMethod(self,paymentMethod ):
        self.__paymentMethod=paymentMethod

    def get_paymentStatus(self):
        return self.__paymentStatus
    def set_paymentStatus(self,paymentStatus ):
        self.__paymentStatus=paymentStatus

    def get_currency(self):
        return self.__currency
    def set_currency(self,currency ):
        self.__currency=currency

    def get_cardNum(self):
        return self.__cardNum
    def set_cardNum(self,cardNum ):
        self.__cardNum=cardNum

    def processPayment(self):
        pass
    def refundPayment(self):
        pass
    def confirmPayment(self):
        pass


customer= Customer("Waad","Alhefeiti", Gender.Female,"26/10/2004",768490,50889380389)
print(f"First Name: {customer.get_firstName()}")
print(f"Last Name: {customer.get_lastName()}")
print(f"Gender: {customer.get_gender().value}")
print(f"Date of Birth: {customer.get_dateOfBirth()}")
print(f"Emirates ID: {customer.get_emiratesID()}")
print(f"Phone Number: {customer.get_phoneNumber()}")


reservation=Reservation("8789h", "26/11/2024","2/12/2024","available",500)
print(f"Reservation ID: {reservation.get_reservationID()}")
print(f"Check In Date: {reservation.get_checkInDate()}")
print(f"Check Out Date: {reservation.get_checkOutDatee()}")
print(f"Status: {reservation.get_status()}")
print(f"Amount: {reservation.get_amount()}")


room=Room(562,5,"standard room",500,"available")
print(f"Room Number: {room.get_roomNum()}")
print(f"Room Floor: {room.get_roomFloor()}")
print(f"Room Type: {room.get_roomType()}")
print(f"Room Price: {room.get_roomPrice()}")
print(f"Availability: {room.get_availability()}")

payment=Payment(570,"card","paid",Currency.AED,73879909)
print(f"Amount: {payment.get_amount()}")
print(f"Payment Method: {payment.get_paymentMethod()}")
print(f"Payment Status: {payment.get_paymentStatus()}")
print(f"Currency: {payment.get_currency().value}")
print(f"Card Number: {payment.get_cardNum()}")