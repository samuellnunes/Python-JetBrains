duration = int(input())
costFood = duration * int(input())
flight = 2 * int(input())
costHotel = (duration - 1) * int(input())
totalCost = costHotel + flight + costFood
print(totalCost)