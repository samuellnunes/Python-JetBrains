digits = ["zero", "one", "two", "three", "four", "five", "six",
          "seven", "eight", "nine"]

phoneNumber = list(input())

for i in range(0, len(phoneNumber)):

    if int(phoneNumber[i]) == 0:
        print(digits[0])
    elif int(phoneNumber[i]) == 1:
        print(digits[1])
    elif int(phoneNumber[i]) == 2:
        print(digits[2])
    elif int(phoneNumber[i]) == 3:
        print(digits[3])
    elif int(phoneNumber[i]) == 4:
        print(digits[4])
    elif int(phoneNumber[i]) == 5:
        print(digits[5])
    elif int(phoneNumber[i]) == 6:
        print(digits[6])
    elif int(phoneNumber[i]) == 7:
        print(digits[7])
    elif int(phoneNumber[i]) == 8:
        print(digits[8])
    elif int(phoneNumber[i]) == 9:
        print(digits[9])