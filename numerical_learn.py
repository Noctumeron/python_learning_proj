START_POINT = input("We need you to define one static number. Type it - ")
print("So, we start from ", START_POINT, " what we do next?")
something_1 = input("Type math symbol ")
if something_1 == '+':
    next_number_1 = input("And number? ")
    print(int(START_POINT) + int(next_number_1))
else:
    print("I mean + sign")
