i = open("help.txt", 'r').read().split()
o = open("helped.txt", 'w')

for word in range(len(i)):
    a = i[word].find('1') + i[word].find('2') + i[word].find('3') + i[word].find('4') + i[word].find('5') + i[word].find('6') + i[word].find('7') + i[word].find('8') + i[word].find('9') + i[word].find('0')
    if a > -10:
        try:
            i[word] = f"{int(i[word])-1}"
        except ValueError:
            pass



o.write("".join(i))