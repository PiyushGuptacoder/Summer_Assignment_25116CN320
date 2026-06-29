def ticket():
    print("Welcome to the Ticket Booking System!")
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    if age < 10:
        print("You did not required a ticket.")
    else:
        no_of_tickets = int(input("Enter no of tickets: "))
        seat=input("Enter seat choice(lower/mid/standard/premium): ")
        while True:
            if seat=="lower":
                price=100*no_of_tickets
                break
            elif seat=="mid":
                price=200*no_of_tickets
                break
            elif seat=="standard":
                price=300*no_of_tickets
                break
            elif seat=="premium":
                price=500*no_of_tickets
                break
            else:
                print("please select seat")
        print(f"Total price of ticket is: {price} \nThank you for booking the ticket, {name}!")

ticket()