import random
people=[]
count=0
random.seed()
for i in range (0,50):
    people+=[100]
#--------------------------------- 
zeiro=[]
while 1==1:
    count+=1
    for x in range(0,50):
        if x not in zeiro:
            people[x]= people[x]-1
            reciver=random.randrange(0,50)
            print('from',x,'to',reciver,x,'is',people[x],'now')
            people[reciver]=people[reciver]+1
            
        for i in range(0,50):
            if people[i]==0:
                if i not in zeiro:
                    zeiro=zeiro+[i]
                    print(i,'is empityyyyyyyyyyy')
                    
    print('empity list is ###########################',zeiro)                
    if len(zeiro) == 49:
        print('done')
        print('done')
        print('done')
        print('round c=',count)
        break
        
        
