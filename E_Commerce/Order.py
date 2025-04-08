from DbConnection import getDBConnection
from Customer import Customer
from Product import Product

class Order(Customer, Product):
    def __init__(self, oid, odate, cid, cname, caddress, cmob, pid, pname, pdesc, price, qty, total_amt):
        Customer.__init__(self, cid, cname, caddress, cmob)  
        Product.__init__(self, pid, pname, pdesc, price)
        
        self.oid = oid
        self.odate = odate
        self.qty = qty
        self.total_amt = total_amt
    
    def displayOrder(self):
        print("\n\t Product Details\n")
        print("Product ID: ", self.pid)
        print("Product Name: ", self.pname)
        print("Product Description: ", self.pdesc)
        print("Price per Unit: ", self.price)
        print("Quantity: ", self.qty)
        print("Total Amount: ", self.total_amt)
        print("\n")

        print("\n\t\tOrder Details\n")
        print("Order ID: ", self.oid)
        print("Order Date: ", self.odate)
        print("-" * 50)

        
