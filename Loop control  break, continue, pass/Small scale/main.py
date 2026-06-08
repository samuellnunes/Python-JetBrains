min_number = 10000000

while True:

    number = input()

    if number == ".":
        break

    number = float(number)
    if number < min_number:
        min_number = number

print(min_number)