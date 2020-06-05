bicycles = []
next_word = 1
print("Welcome to adding text to list")
while next_word == 1:
    new_word=input("To break adding type 'Stop'!, new word in list will be - ")
    if new_word == 'Stop':
        next_word = 0
        print(bicycles)
    else:
        bicycles.append(new_word)
        print(bicycles)
