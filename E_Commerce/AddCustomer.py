from DbConnection import getDBConnection
def addCustomer():
    con = getDBConnection()
    print("\t\t\nEnter Customer Details")
    cname = input("Enter Your Name: ")
    caddress = input("Enter Your Address: ")
    cmob = input("Enter Your Mobile Number: ")

    if con:
        try:
            cursor = con.cursor()
            query = "INSERT INTO Customer(cname, caddress, cmob) VALUES(?, ?, ?)"
            cursor.execute(query, (cname, caddress, cmob))
            con.commit()

            print("\nCustomer Added")
    
        except Exception as Error:
            print("Error:", Error)
    else:
        print("No Connection Created")
    

    