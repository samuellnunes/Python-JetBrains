import math

value = int(input())

logisticFunction = (math.pow(math.e, value) /
                    (math.pow(math.e, value) + 1))

print(round(logisticFunction, 2))