string = "red yellow fox bite orange goose beeeeeeeeeeep"
vowels = 'aeiou'

qtdVowels = 0

for letter in string:
    for vowel in vowels:
        if letter == vowel:
            qtdVowels += 1

print(qtdVowels)