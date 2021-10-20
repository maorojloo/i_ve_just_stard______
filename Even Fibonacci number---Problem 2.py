privious_num = 1
current_num = 2
sum = 2
while 1==1 :
    x=current_num
    current_num=current_num+privious_num
    privious_num=x
    if current_num+privious_num <= 4000000:
        print(current_num+privious_num)
    else:
        break
    if current_num+privious_num%2 == 0:
        sum+=current_num+privious_num
print(sum)
