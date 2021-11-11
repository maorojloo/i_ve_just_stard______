scorelist = [['mmd',10,20,11,12],['meshed',14,15,16,17,18],['efi',1,2,3,4,5]]
stdn = 'kirkharrr6565'
classsum=0
elemnts = []
mark = []
for person in scorelist:  
    scorsum=0
    for i in range(1,len(person)): 
        if stdn != person[0]:
           # print('student name is',person[0])  
            elemnts+=[person[0]]
            stdn= person[0]        
       # print(person[i])
        scorsum+=person[i]        
   # print('av=',scorsum/(len(person)-1))
    mark+=[scorsum/(len(person)-1)]
    classsum+=(scorsum/(len(person)-1))
#print('calssav=',classsum/len(scorelist))
elemnts+=['calssav']
mark+=[classsum/len(scorelist)]
import matplotlib.pyplot as plt
   

plt.bar(elemnts, mark)
plt.title('class marks bar chart')
plt.xlabel('std name')
plt.ylabel('name')
plt.show()