# Method 1
book_title =  ['great', 'expectations','the', 'adventures', 'of', 'sherlock','holmes','the','great','gasby','hamlet','adventures','of','huckleberry','fin']

word_counter = {}
# **Step 2.** Iterate through each element in the list. If an element is already included in the dictionary, add 1 to its value. If not, add the element to the dictionary and set its value to 1.

for word in book_title:
    if word not in word_counter:
        word_counter[word] = 1
    else:
        word_counter[word] += 1
    
    #####  What's happening here?
    # - The `for` loop iterates through each element in the list. For the first iteration, `word` takes the value 'great'.
    # - Next, the if statement checks if `word` is in the `word_counter` dictionary.
    # - Since it doesn't yet, the statement  `word_counter[word] = 1` adds *great* as a key to the dictionary with a value of 1.
    # - Then, it leaves the if else statement and moves on to the next iteration of the for loop. `word` now takes the value *expectations* and repeats the process.
    # - When the if condition is not met, it is because that`word` already exists in the `word_counter` dictionary, and the statement `word_counter[word] = word_counter[word] + 1` increases the count of that word by 1.
    # - Once the `for` loop finishes iterating through the list, the `for` loop is complete. 
    
    #We can see the output by printing out the dictionary. Printing `word_counter` results in the following output.

print(word_counter)

# Method 2: Using the get method
for word in book_title:
    word_counter[word] = word_counter.get(word, 0) + 1

print(word_counter)

#ITERATING THROUGH DICTIONARIES
cast = {
           "Jerry Seinfeld": "Jerry Seinfeld",
           "Julia Louis-Dreyfus": "Elaine Benes",
           "Jason Alexander": "George Costanza",
           "Michael Richards": "Cosmo Kramer"
       }

# normal loop gives only keys
for key in cast:
    print(key)

# Usinf function items gives key value
for key, value in cast.items():
    print(f"Actor: {key}    Role: {value}")
