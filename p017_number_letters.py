# this solution works. However, would have been better using a dictionary
# https://www.programiz.com/python-programming/dictionary


def ones(o):
    if o == 0:
        return 0
    if o == 1:
        return 3 #one
    if o == 2:
        return 3 #two
    if o == 3:
        return 5 #three
    if o == 4:
        return 4 #four
    if o == 5:
        return 4 #five
    if o == 6:
        return 3 #six
    if o == 7:
        return 5 #seven
    if o == 8:
        return 5 #eight
    if o == 9:
        return 4 #nine

def tens(t):
    if t == 0:
        return 0
    if t == 1:
        return 4 #teen
    if t == 2:
        return 6 #twenty
    if t == 3:
        return 6 #thirty
    if t == 4:
        return 5 #forty
    if t == 5:
        return 5 #fifty
    if t == 6:
        return 5 #sixty
    if t == 7:
        return 7 #seventy
    if t == 8:
        return 6 #eighty
    if t == 9:
        return 6 #ninety

def hundreds(h):
    if h == 0:
        return 0
    if h == 1:
        return 13 #one hundred and
    if h == 2:
        return 13 #two hundred and
    if h == 3:
        return 15 #three hundred and
    if h == 4:
        return 14 #four hundred and
    if h == 5:
        return 14 #five hundred and
    if h == 6:
        return 13 #six hundred and
    if h == 7:
        return 15 #seven hundred and
    if h == 8:
        return 15 #eight hundred and
    if h == 9:
        return 14 #nine hundred and

def count_letters(n):
    ret = 0
    L_n = list(map(int, str(n).zfill(4)))
    #print(L_n)
    if n == 1000:
        return 11
    ret += hundreds(L_n[1])
    if L_n[2] + L_n[3] == 0:
        ret -= 3
        return ret
    elif L_n[2] == 1:
        if L_n[3] == 0:
            ret += 3
            return ret
        elif L_n[3] == 1:
            ret += 6
            return ret
        elif L_n[3] == 2:
            ret += 6
            return ret
        elif L_n[3] == 3:
            ret += 8
            return ret
        elif L_n[3] == 5:
            ret += 7
            return ret
        elif L_n[3] == 8:
            ret += 8
            return ret
    ret += tens(L_n[2])
    ret += ones(L_n[3])
    return ret



    print(i)


i = 1
count = 0
while i <= 1000:
    #print(count_letters(i))
    count += count_letters(i)
    i += 1
print("final count=",count)

