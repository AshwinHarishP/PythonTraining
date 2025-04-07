from Customer import Customer
class Booking(Customer):
    FinalPrice = 0
    def __init__(self, bid, gst, total_price, deduction, cid, cname, address, phone_no, fid, fname, source, destination, age):
        super().__init__(cid, cname, address, phone_no, fid, fname, source, destination, age)
        self.bid = bid
        self.gst = gst
        self.total_price = total_price
        self.deduction = deduction

    def ticket_booking(self, no_of_tickets, age):
        basePrice = 5000 * no_of_tickets

        if age < 2:
            concession = 100  
        elif age > 60:
            concession = 40  
        else:
            concession = 0  

        if no_of_tickets >= 5:
            concession += 10  

        
        concession = min(concession, 100)  

        discounted_price = basePrice * (1 - (concession / 100))

        
        gst = self.gst if hasattr(self, "gst") else 0.18

        self.total_price = discounted_price * (1 + gst)
        Booking.FinalPrice = self.total_price 
        

    def Registeration(self):
        totCustomer = int(input("Enter Total Number of Customers: "))
        for i in range(totCustomer):
            print("\n Enter Customer", i+1, " Details\n")
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

            self.ticket_booking(totCustomer, age)

    def display_ticket_price(self):
        print("Total Ticket Price After GST:", self.total_price)


