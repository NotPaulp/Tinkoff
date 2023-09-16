s=int(input())
n=int(input())
scopy=s
while n>=s:
    n-=s
    s-=1
    if s==0:
        s=scopy
print(n)