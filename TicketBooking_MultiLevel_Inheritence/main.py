from Booking import Booking
from Flight import Flight
from Customer import Customer
import random

def displayDetails(customerObj):
    print("\n--------------------------------------------------")
    print("\nCustomer Details:")
    Customer.display_customer_details()
    
    print("\nFlight Details:")
    Flight.display_flight_details()
    customerObj.display_ticket_price()


def addDetails():
    bid = random.random()
    gst = 0.18  
    total_price = None  
    deduction = None

    print("\n Enter Customer Details\n")

    cid = int(input("Enter Customer id: "))
    cname = input("Enter Customer name: ")
    address = input("Enter Customer address: ")
    phone_no = int(input("Enter Customer phone number: "))
    age = int(input("Enter Customer age: "))


    print("\n\n Enter Flight Details\n")

    fid = int(input("Enter Flight ID: "))
    fname = input("Enter Flight Name: ")
    source = input("Enter Boarding Point: ")
    destination = input("Enter Your Destination: ")

    

    no_of_tickets = int(input("Enter Number of Tickets: "))
    customerObj = Booking(bid, gst, None, None, cid, cname, address, phone_no, fid, fname, source, destination, age)
    customerObj.ticket_booking(no_of_tickets, age)
    customerObj.add_Customer(customerObj)

    flightObj = Flight(fid, fname, source, destination, 1000, age)
    flightObj.add_flight(flightObj)
    return customerObj

customerObj = addDetails()
displayDetails(customerObj)