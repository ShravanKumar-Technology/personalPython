message = 'it was bright cold day in april.'

count = {}

for character in message.upper():
    count.setdefault(character,0)
    count[character] = count[character] + 1
     
print(count)
