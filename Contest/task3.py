n=int(input())
a=list(map(int,input().split()))
m=int(input())
dpmin=[0]*n
dpmax=[0]*n
for i in range(1,n):
    if a[i]<=a[i-1]:
        dpmin[i]=dpmin[i-1]
    else:
        dpmin[i]=i
dpmax[n-1]=n-1
for i in range(n-2,-1,-1):
    if a[i]<=a[i+1]:
        dpmax[i]=dpmax[i+1]
    else:
        dpmax[i]=i
for _ in range(m):
    x,y=map(int, input().split())
    y-=1
    x-=1
    if dpmax[x] >= dpmin[y]:
        print("Yes")
    else:
        print("No")
