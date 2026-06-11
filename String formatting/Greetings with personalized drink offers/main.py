def create_greeting(friend_name, favorite_drink):
    return f"""Hello {friend_name.capitalize()}, I hope you are having a wonderful day! Would you like a glass of {favorite_drink.capitalize()}?"""


name_input = input()
drink_input = input()

print(create_greeting(name_input, drink_input))