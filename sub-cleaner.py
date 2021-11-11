import re
f= open("C:\\Users\maoro\Desktop\The.Walking.Dead.S06E03.HDTV (2).srt", "r")
result=[]
for x in f:
    replaced = re.sub('^\d.*\d$', '', x)
    result+=replaced
result2=[]
for x in result:
    replaced = re.sub('^\d$', '', x)
    result2+=replaced
result3=''
for x in  result2:
    result3+=x  
f.close()      
f= open("C:\\Users\maoro\Desktop\The.Walking.Dead.S06E03.HDTV (2).srt", "w")
print(result3)
f.write(str(result3)) 
