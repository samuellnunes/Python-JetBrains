sumNum = 0
quantiyNum = 0

while True:

    number = int(input())

    if number == 55:
        break
    else:
        sumNum += number
        quantiyNum += 1

print(quantiyNum)
print(sumNum)
print(round(sumNum / quantiyNum))