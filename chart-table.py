scorelist = [['mmd',10,20,11,12,14,15,16,17,18],
             ['meshed',14,15,16,17,18,14,15,16,17,18],
             ['efi',1,2,3,4,5,14,15,16,17,18]]
def space(typee,leng):
    
    if typee == str:
        sp=7
        a=''
        end=(sp-leng)
        for mmd in range(0,int(end)):
            a+=" "
        a+="|"
        return a                
    else:
        sp=3
        a=''
        end=(sp-leng)
        for mmd in range(0,int(end)):
            a+=" "
        a+="|"
        return a  
for person in scorelist:
    for pinfo in person:
        if type(pinfo)==str:
            print(pinfo, end=space(type(pinfo),len(pinfo)))
        else:          
            print(pinfo, end=space(type(pinfo),len( str(pinfo))))
    print()
   # print('===============')







