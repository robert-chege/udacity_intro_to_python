num = 10
name = "Robert"
print(f"My name is {name} {num}.")


n = 3

if n % 2 != 0:
    result = "Weird"
elif (n % 2 == 0) and (n >= 2 and n <= 5 ):
    result = "Not Weird"
elif (n % 2 == 0) and (n >= 6 and n <= 20):
    result = "Weird"
elif n % 2 == 0 and n > 20:
    result = "Not Weird"
    
print(result)
