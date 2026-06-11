words = input().split()
wordEndWithS = []

for word in words:
    if word.endswith("s"):
        wordEndWithS.append(word)

print("_".join(wordEndWithS))