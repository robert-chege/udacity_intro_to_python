# Write a for loop that iterates over a list of strings, tokens, and counts how many of them are XML tags.
tokens = ['<greeting>', 'Hello World!', '</greeting>']
count = 0

for token in tokens:
    if token[0] == '<' and token[-1] == '>':
        count += 1

print(count)