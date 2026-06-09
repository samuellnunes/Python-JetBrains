import math

sideA = int(input())
sideB = int(input())
sideC = int(input())

perimeter = (sideA + sideB + sideC) / 2
heronFormula = math.sqrt(perimeter * (perimeter - sideA) *
                         (perimeter - sideB) * (perimeter - sideC))

print(heronFormula)