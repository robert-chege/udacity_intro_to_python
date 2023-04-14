limit = 40

# write your while loop here
num = 0
while (num + 1) ** 2 < limit:
    num += 1
    
nearest_square = num ** 2

print(nearest_square)
# NOTE
# ** while** loops are ideal when the iterations need to continue until a condition is met.
# for loops are ideal when the number of iterations is known or finite.
# When you have an iterable collection (list, string, set, tuple, dictionary)
# for name in names:
#When you want to iterate through a loop for a definite number of times, using range()
#for i in range(5):
