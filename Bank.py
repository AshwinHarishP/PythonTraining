class Bank:
    __BankName = "SBI"
    __RateOfInterest = 0.04

    def __init__(self, cid: int, cname: str, amount: float, year: float):
        self.cid = cid
        self.cname = cname
        self.amount = amount
        self.year = year

    def customerDetails(self) -> None:
        print("\n\t\tCustomer", self.cid, " Detail")
        print("Customer ID: ", self.cid)
        print("Customer Name: ", self.cname)
        print("Initial Amount: ", self.amount)
        print("Duration: ", self.year)

    def calculateAmt(self) -> float:
        return self.amount + self.amount * self.year * Bank.__RateOfInterest


if __name__ == __main__:
    customerCount = int(input("Enter total Customers: "))
    customers = []
    for i in range(customerCount):
        
        print("\n\t\t Enter Details for Customer ", i+1)
        customerID = int(input("Enter Customer ID: "))
        customerName = input("Enter Customer Name: ")
        amount = float(input("Enter Amount: "))
        year = float(input("Enter Duration in years: "))

        customer = Bank(customerID, customerName, amount, year)
        customers.append(customer)

    for customer in customers:
        customer.customerDetails()
        print("Final Amount: ", customer.calculateAmt())  




        