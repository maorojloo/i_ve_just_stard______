sum = 0
for x in range(1, 1000):
    if x%3 == 0 and x%5 != 0 :
        print(x,'mazrab 3')
        sum +=x
    if x%5 == 0 and x%3 != 0 :
        print(x,'mazrab 5')
        sum +=x
    if x%15 == 0  :
        print(x,'mazrab 5 va 3')
        sum +=x
print(sum)
