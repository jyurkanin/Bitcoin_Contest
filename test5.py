def test(l):
    word = 1
    bigno = 1
    for item in l:
       word = ""
       for c in item:
          word = word + str(ord(c))
       bigno = bigno * int(word)
    return bigno
