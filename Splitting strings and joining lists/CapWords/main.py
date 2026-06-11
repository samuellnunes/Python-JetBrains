words = input().split("_")
wordRedfined = []

for word in words:
    wordRedfined.append(word.lower().capitalize())

print("".join(wordRedfined))