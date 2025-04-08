from DbConnection import getDBConnection
from Order import Order

def displaySpecificOrder():
    con = getDBConnection()
    cursor = con.cursor()

    oid = int(input("Enter Order ID to display: "))

    query = """
    SELECT o.oid, o.odate, o.cid, c.cname, c.caddress, c.cmob, 
           o.pid, p.pname, p.pdesc, o.price, o.qty, o.total_amt
    FROM Orders o
    JOIN Customer c ON o.cid = c.cid
    JOIN Product p ON o.pid = p.pid
    WHERE o.oid = ?
    """
    
    cursor.execute(query, (oid,))
    order = cursor.fetchone()
    
    if not order:
        print(f"\nNo order found with Order ID: {oid}")
        return

    print("\n\t\tOrder Details\n")
    specific_order = Order(*order) 
    specific_order.displayOrder()
