# Question:
# Your code should add up the odd numbers in the list, but only up to the first 5 odd numbers together.
#If there are more than 5 odd numbers, you should stop at the fifth.
#If there are fewer than 5 odd numbers, add all of the odd numbers.

num_list = [422, 136, 524, 85, 96, 719, 85, 92, 10, 17, 312, 542,
             87, 23, 86, 191, 116, 35, 173, 45, 149, 59, 84, 69, 113, 166]

odd_count = 0
odd_sum = 0
len_num_list = len(num_list)
i = 0

while odd_count < 5 and i < len_num_list:
    if num_list[i] % 2 == 1:
        odd_count += 1
        odd_sum += num_list[i]
    i += 1

print(f"Sum of the {odd_count} odd numbers is: {odd_sum}")

"""
We would write a while loop to write this code for the following reasons:

1. We don't need a break statement that a for loop will require. Without a break statement,
   a for loop will iterate through the whole list, which is not efficient.
2. We don't want to iterate over the entire list, but only over the required number
   of elements in the list that meets our condition.
3. It is easier to understand because you explicitly control the exit conditions for the loop.
"""