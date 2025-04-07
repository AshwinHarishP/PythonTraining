from Flight import Flight
class Customer(Flight):
    customers = []
    def __init__(self, cid, cname, address, phone_no, fid, fname, source, destination, age):
        super().__init__(fid, fname, source, destination, 5000, age)
        self.cid = cid
        self.cname = cname
        self.address = address
        self.phone_no = phone_no

    def add_Customer(self, customerObj):
        Customer.customers.append(customerObj)
        return "Customer Added"

    def display_customer_details():

        if len(Customer.customers) == 0:
            print("No customers available.")
        else:
            for customer in Customer.customers:
                print(f"Customer ID: {customer.cid}")
                print(f"Customer Name: {customer.cname}")
                print(f"Customer Address: {customer.address}")
                print(f"Customer Phone No: {customer.phone_no}")
                print(f"Customer Age: {customer.age}")
                print("-" * 50)
