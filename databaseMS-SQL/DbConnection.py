import pyodbc

def getDBConnection():

    driver_name = "SQL Server"
    server = "LAPTOP-2Q84MA0J\SQLEXPRESS"
    databse = "college"
    username = ""
    password = ""


    #Creating connection String
    connectionString = f"Driver={driver_name}; Server={server}; Database={databse}; UID={username}; PWD={password};"

    #connectionString = f"Driver={driver_name}; Server={server}; Database={databse}; Trusted_Connection=yes;" --> This is for windows authentication mode. It will automatically go for windows authentication mode

    #Creating Connection Object
    try:
        con = pyodbc.connect(connectionString) #connection object
        return con
    

    except Exception as Error:
        print("Error in the database connection", Error)
        return None