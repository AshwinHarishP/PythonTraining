from DbConnection import getDBConnection

# studentID = int(input("Enter Student ID: "))
# studentName = input("Enter Student Name: ")
# studentAddress = input("Enter Student Address: ")
# studentDOB = input("Enter Student DOB: ")
con = getDBConnection()

if con:
    try:
        cursor = con.cursor()
        #                                  One way commands
        # cursor.execute("INSERT INTO Students VALUES (14, 'Raj', 'Banglore', '2003-07-12')") --> Insert
        # cursor.execute("UPDATE Students SET name = 'Eren' WHERE id = 4") --> Update
        # query = "UPDATE Students SET name=?, address = ?, dob = ? WHERE Id = ?" --> Update by user input
        # query = "DELETE FROM Students WHERE Id=?;" --> Soft Delete by user input
        # cursor.execute(query,(studentID))
        # cursor.commit()

        #                                  Two way commands

        #                                       1. fetchall()
        
        # query = "SELECT * FROM Students;"
        # cursor.execute(query)                       # It will excute the query in cursor and from the cursor we will display the records
        # res = cursor.fetchall()
        
        # for i in res:
        #     print(i)
        # print("Record Affected Successfully")


        #                                       2. fetchone()

        query = "SELECT * FROM Students WHERE id = 2;"
        cursor.execute(query)                       # It will excute the query in cursor and from the cursor we will display the records
        res = cursor.fetchone()
        
        for i in res:
            print(i)
        print("Record Affected Successfully")
    

    except Exception as Error:
        print("Error: ", Error)

    finally:
        cursor.close()
        con.close()
        print("Resource Closed Sucessfully")


