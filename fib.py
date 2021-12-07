
s1 = "abcd efgh"
length = len(s1)
slice1 = s1[length::-1]
words = slice1.split()
words = list(reversed(words))
print(' '.join(words))

strSample, strSample2 = 'a1bcd', 'hgf!e'


listSample, listSample2 = list(strSample), list(strSample2)

i = 0
j = len(listSample) - 1

while i < j:
    if not listSample[i].isalpha():
        i += 1
    elif not listSample[j].isalpha():
        j -= 1
    else:
        listSample[i], listSample[j] = listSample[j], listSample[i]
        i += 1
        j -= 1
strOut = ''.join(listSample)
strOut2 = ''.join(listSample2)
print(strOut, strOut2)





