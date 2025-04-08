from DbConnection import getDBConnection

class Product:
    
    def __init__(self, pid, pname, pdesc, price):
        self.pid = pid
        self.pname = pname
        self.pdesc = pdesc
        self.price = price

    def getProduct(self):
        print("Product ID: ", self.pid)
        print("Product Name: ", self.pname)
        print("Product Description: ", self.pdesc)
        print("Product Price: ", self.price)

    def getPrice(self):
        con = getDBConnection()
        if con:
            try:
                cursor = con.cursor()
                query = "SELECT price FROM Product WHERE pid = ?"
                cursor.execute(query, (self.pid,))
                result = cursor.fetchone()
                return result[0] 
            except Exception as Error:
                print("Error fetching price:", Error)

    def getProductID(self, pid):
        con = getDBConnection()
        if con:
            try:
                cursor = con.cursor()
                check_query = "SELECT COUNT(*) FROM Product WHERE pid = ?"
                cursor.execute(check_query, (pid,))
                result = cursor.fetchone()
                return result[0] if result else 0
            
            except Exception as Error:
                print("Error Occoured", Error)