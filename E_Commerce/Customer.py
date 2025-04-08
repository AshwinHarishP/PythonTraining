class Customer:
    def __init__(self, cid, cname, caddress, cmob):
        self.cid = cid
        self.cname = cname
        self.caddress = caddress
        self.cmob = cmob

    def getCustomer(self):
        print("\nCustomer Details:")
        print("Customer ID: ", self.cid)
        print("Customer Name: ", self.cname)
        print("Customer Address: ", self.caddress)
        print("Customer Mobile: ", self.cmob)
        print("-" * 50)
