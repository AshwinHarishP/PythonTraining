TICKET_PRICE = 100
noOfTickets = int(input("Enter Total Number of Tickets: "))
totalCost = 0

for i in range(noOfTickets):
    cost = TICKET_PRICE
    print(" ")
    
    print("Passanger" , i+1,  "Details")
    name = input("Enter name of passanger: ")
    gender = input("Enter Gender: (M/F) ").upper()
    age = int(input("Enter age: "))
    handicapped = input("Handicapped: (Y/N) ").upper()

    if gender == "F" and age >= 50:
        cost = (TICKET_PRICE * 50)/100

    elif gender == "M" and age >= 65:
       cost = (TICKET_PRICE * 50)/100
    
    elif age > 70:
        cost = (TICKET_PRICE * 10)/100
    
    elif handicapped == "Y" or age <= 5:
        cost = 0
    
    totalCost += cost

    print(" ")
    print("--------Details of Passanger" , i+1, "--------")
    print("Name of the Passanger: " + name)
    print("Age of the Passanger: " , age)
    print("Gender of the Passanger: " + gender)
    print("TicketPrice of passanger", i+1, ":" , cost)
    print(" ")

totalCost += (totalCost * 18 /100)
print("Total Ticket Cost: ", totalCost, "Rs")