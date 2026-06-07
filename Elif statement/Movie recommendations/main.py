age = int(input())

if age <= 14:
    print("Toy Story 4")
elif age > 14 and age <= 18:
    print("The Matrix")
elif age > 18 and age <= 25:
    print("John Wick")
elif age > 25 and age <= 35:
    print("Constantine")
else:
    print("Speed")