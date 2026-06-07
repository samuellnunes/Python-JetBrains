ticket = input()

half1 = sum(int(digit) for digit in ticket[:3])
half2 = sum(int(digit) for digit in ticket[3:])

if half1 == half2:
    print("Lucky")
else:
    print("Ordinary")