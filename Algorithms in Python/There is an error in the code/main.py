def aver(sent):

    for sym in [',', '!', '?', ';', '.', '"', "'"]:
        sent = sent.replace(sym, '')

    words = sent.split()

    total = 0
    qt_letters = 0
    for word in words:

        total += 1

        if len(word) != 0:
            qt_letters += len(word)



    return qt_letters / total

sentence = input()
print(aver(sentence))