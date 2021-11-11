def txt_reverser_v1 (txt) :
    r =''
    for i in txt:
        r= i+r

    return r
def txt_reverser_v2 (txt) :
    r =[]
    for i in txt :
        r=r+[i]
        print(i)
    print(r)
    b = r.reverse()
    print(b)
    return b





print(txt_reverser_v1(txt)(input('txt:')))
