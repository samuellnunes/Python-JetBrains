def activity(day):
    if day == 6:
        return "Leisure!"
    elif day == 0 or day == 1 or day == 2 or day == 3 or day == 4:
        return "Study!"
    else:
        return "Rest!"


day = int(input())
print(activity(day))