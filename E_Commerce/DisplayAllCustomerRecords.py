from DbConnection import getDBConnection
from Customer import Customer

def displayAllCustomerRecords():
    con = getDBConnection()
    cursor = con.cursor()

    query = "SELECT cid, cname, caddress, cmob FROM Customer"
    cursor.execute(query)
    
    customers = cursor.fetchall()
    
    if not customers:
        print("\n !!! No customer records found !!!.")
        return

    print("\n\t\tAll Customer Records\n")
    for row in customers:
        cid, cname, caddress, cmob = row
        customer = Customer(cid, cname, caddress, cmob)
        customer.getCustomer()
