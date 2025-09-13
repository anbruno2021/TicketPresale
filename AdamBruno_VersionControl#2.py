# cinema ticket pre-sale
# lets people buy up to 4 tickets, stops when all 10 sold; also counts how many buyers

# total tickets 
MAX_TICKETS = 10

# function for one person buying tickets
def buy_tickets(remaining_tickets):
    
    # tell them how many left
    print(f"\nthere is {remaining_tickets} tickets left")
    
    # ask how many they want
    desired_tickets = int(input("how many tickets would you like to purchase today? (1-4)? "))

    # check if they ask for too many or too few
    if desired_tickets < 1 or desired_tickets > 4:
        print("only can purchase 1-4 tickets, try again")
        return 0  # no tickets sold

    # check if enough tickets left
    if desired_tickets > remaining_tickets:
        print(f"sorry, only {remaining_tickets} left")
        return 0 

    # return how many sold
    return desired_tickets

# main function for ticket selling
def ticket_presale():
    remaining_tickets = MAX_TICKETS
    total_buyers = 0

    # loop till all sold
    while remaining_tickets > 0:
        tickets_sold = buy_tickets(remaining_tickets)
        
        # only update if some sold
        if tickets_sold > 0:
            remaining_tickets -= tickets_sold
            total_buyers += 1
            print(f"there is {remaining_tickets} tickets left")

    # total amount of buyers displayed
    print(f"\nall tickets gone. total buyers: {total_buyers}")

# start the program
ticket_presale()

# wait for user before closing
input("\npress enter to leave :)")
