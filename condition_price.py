# Allow user to enter their number of points
points = int(input("What is your number of points: "))

# establish the default prize value to None
prize = None

# use the points value to assign prizes to the correct prize names
if points <= 50:
    prize = "Wooden Rabbit"
elif 151 <= points <= 180:
    prize = "Wafer-thin Mint"
elif points > 180:
    prize = "Penguin"

# use the truth value of prize to assign result to the correct prize
if prize:
    result = f"Congratulations! You won a {prize}!"
else:
    result = "Oops! No prize for you this time!"

print(result)