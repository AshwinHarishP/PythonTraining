from DbConnection import getDBConnection
from Product import Product

import random
from datetime import datetime

def orderProduct():
    con = getDBConnection()
    cursor = con.cursor()
    print("\t\t\nOrder Product")
    
    oid = random.randint(1000, 9999) 
    odate = str(datetime.today().strftime('%Y-%m-%d'))

    cid  =int(input("Enter Customer id: "))
    pid = int(input("Enter product id: "))
    product = Product(pid, None, None, None)

    isProductExist = product.getProductID(pid)

    if isProductExist == 0:
        print("!!! Product is not there in the inventory !!!")
    
    else:
        qty = int(input("Enter Product Quantity: "))
        price = product.getPrice()
        total_Amt = price * qty
        print("\nTotal Price: ", total_Amt)
        orderChoice = input("Are you sure to place this order?(Y/N)").upper()

        if orderChoice == "Y":
            orderQuerry = "INSERT INTO Orders(oid, odate, cid, pid, qty, price, total_Amt) VALUES(?, ?, ?, ?, ?, ?, ?)"
            cursor.execute(orderQuerry, (oid, odate, cid, pid, qty, price, total_Amt))
            con.commit()
            print("\nOrder Placed Sucessfully")

        else:
            orderQuerry = "INSERT INTO Cart(oid, odate, cid, pid, qty, price, total_Amt) VALUES(?, ?, ?, ?, ?, ?, ?)"
            cursor.execute(orderQuerry, (oid, odate, cid, pid, qty, price, total_Amt))
            con.commit()
            print("Item added in the cart")
