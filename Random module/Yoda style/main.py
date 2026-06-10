import random

sentence = input()

words = sentence.split()

random.seed(43)
random.shuffle(words)

print(' '.join(words))
