age = int(input("Please enter your age: "))

# age payment limits
free_up_to_age = 4
child_up_to_age = 18
senior_from_age = 65

# fixed prices
concession_ticket = 1.25
adult_ticket = 2.50

# Conditional statement evaluating amount to be paid
if age <= free_up_to_age:
    ticket_price = 0
elif age <= child_up_to_age:
    ticket_price = concession_ticket
elif age >= senior_from_age:
    ticket_price = concession_ticket
else:
    ticket_price = adult_ticket

print(f"Ticket price for age {age} is {ticket_price}. \nPay via mpesa!")