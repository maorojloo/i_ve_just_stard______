#calculating factorial with recerciv function
n=int(input("num:"))
def fr(n):
    if n<=1:
        return 1
    else:
        return n*fr(n-1)
print(fr(n))