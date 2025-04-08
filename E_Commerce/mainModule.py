from AddCustomer import addCustomer
from AddProduct import addProduct
from DisplayAllCustomerRecords import displayAllCustomerRecords
from DisplayAllOrder import displayAllOrder
from DisplaySpecificOrder import displaySpecificOrder
from OrderProduct import orderProduct
from DbConnection import getDBConnection
from DisplayCustomerOrder import displayCustomerOrder



con = getDBConnection()

if con:
    try:
        cursor = con.cursor()

    except:
        print("Error in Connection")


print("\n\t\tWelcome to E-Commerce Application")
print("\n\t\t Menu")
print("\n 1. Add Customer")
print("\n 2. Add Product")
print("\n 3. Order Product")
print("\n 4. Display All Orders")
print("\n 5. Display Specific Order")
print("\n 6. Display All Customer Records")
print("\n 7. Display Specific Customer Orders")
print("\n 8. Exit")

while True:
    choice = int(input("\n Enter your choice: "))
    if choice == 1:
        addCustomer()

    elif choice == 2:
        addProduct()

    elif choice == 3:
        orderProduct()

    elif choice == 4:
        displayAllOrder()

    elif choice == 5:
        displaySpecificOrder()

    elif choice == 6:
        displayAllCustomerRecords()
        
    elif choice == 7:
        displayCustomerOrder()

    elif choice == 8:
        print("Exiting from menu...\n")
        break

    else:
        print("!!! Invalid Choice !!!")

    