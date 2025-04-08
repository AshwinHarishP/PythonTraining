import pyodbc

def getDBConnection():
    driver_name = "SQL Server"
    server = "LAPTOP-2Q84MA0J\SQLEXPRESS"
    databse = "Ecommerce"
    username = ""
    password = ""
    
    connectionString = f"Driver={driver_name}; Server={server}; Database={databse}; UID={username}; PWD={password};"

    try:
        con = pyodbc.connect(connectionString) 
        return con
    

    except Exception as Error:
        print("Error in the database connection", Error)
        return None