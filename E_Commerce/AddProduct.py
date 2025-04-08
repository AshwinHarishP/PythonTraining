from DbConnection import getDBConnection

def addProduct():
    con = getDBConnection()
    print("\t\t\nEnter Product Details")
    pname = input("Enter Poduct Name: ")
    pdesc = input("Enter Product Descriptoin: ")
    price = float(input("Enter Your Product Price: "))

    if con:
        try:
            cursor = con.cursor()
            query = "INSERT INTO Product(pname, pdesc, price) VALUES(?, ?, ?)"
            cursor.execute(query, (pname, pdesc, price))
            con.commit()

            print("\nProduct Added")
    
        except Exception as Error:
            print("Error:", Error)
    
    else:
        print("No Connection Created")
    