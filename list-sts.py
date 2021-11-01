scorelist = [['mmd',10,11,12],['meshed',14,15,16,17,18],['efi',1,2,3,4,5]]
stdn = 'kirkharrr6565'
classsum=0
for person in scorelist:  
    scorsum=0
    for i in range(1,len(person)): 
        if stdn != person[0]:
            print('student name is',person[0])  
            stdn= person[0]        
        print(person[i])
        scorsum+=person[i]        
    print('av=',scorsum/(len(person)-1))
    classsum+=(scorsum/(len(person)-1))
print('calssav=',classsum/len(scorelist))
