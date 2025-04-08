from DbConnection import getDBConnection
from Order import Order

def displayAllOrder():
    con = getDBConnection()
    cursor = con.cursor()

    query = """
    SELECT o.oid, o.odate, o.cid, c.cname, c.caddress, c.cmob, o.pid, p.pname, p.pdesc, o.price, o.qty, o.total_amt
    FROM Orders o
    JOIN Customer c 
    ON o.cid = c.cid
    JOIN Product p 
    ON o.pid = p.pid
    """
    
    cursor.execute(query)
    orders = cursor.fetchall()
    
    if not orders:
        print("\nNo orders found.")
        return

    print("\n\t\tAll Orders\n")
    for row in orders:
        order = Order(*row) 
        order.displayOrder()
