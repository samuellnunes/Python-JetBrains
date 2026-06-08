characters = input()
vowels = ["a", "e", "i", "o", "u"]

for char in characters:

    if char.isalpha() and char in vowels:
        print("vowel")
    elif char.isalpha():
        print("consonant")
    else:
        break