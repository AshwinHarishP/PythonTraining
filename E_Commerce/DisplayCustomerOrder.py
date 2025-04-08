from DbConnection import getDBConnection
from Customer import Customer
from Order import Order
def displayCustomerOrder():
    con = getDBConnection()
    cursor = con.cursor()

    print("\n Displaying the Customer Order Details")
    cid = int(input("\nEnter Customer id: "))
    query = """
    SELECT c.cid, c.cname, c.caddress, c.cmob, o.oid, o.odate, o.cid, 
           o.pid, p.pname, p.pdesc, o.price, o.qty, o.total_amt
    FROM Orders o
    JOIN Customer c ON o.cid = c.cid
    JOIN Product p ON o.pid = p.pid
    WHERE c.cid = ?
    """

    cursor.execute(query, (cid,))
    orders = cursor.fetchall() 

    if not orders:
        print(f"\nNo customer order found with Customer ID: {cid}")
        return
    
    specificCustomer = Customer(orders[0][0], orders[0][1], orders[0][2], orders[0][3])
    specificCustomer.getCustomer()

    

    for order in orders:
        specificOrder = Order(
            order[4], order[5],  
            specificCustomer.cid, specificCustomer.cname, specificCustomer.caddress, specificCustomer.cmob, 
            order[6], order[7], order[8],  
            order[9], order[10], order[11]  
        )
        specificOrder.displayOrder()  
