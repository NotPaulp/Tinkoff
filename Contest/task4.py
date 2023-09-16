import math
n,c,d=map(int,input().split())
a=(list(map(int,input().split())))
negatives=0
for x in a:
    if x<0:
        negatives+=1
while c>0:
    if negatives%2==0:
        last_pos=0
        pos_min=float('inf')
        for i in range(0,len(a)):
            if pos_min>=a[i]:
                pos_min=a[i]
                last_pos=i
        if math.ceil(pos_min/d)<=c:
            a[last_pos]-=math.ceil(pos_min/d)*d
            c-=math.ceil(pos_min/d)
            if c>0 and a[last_pos]>=0:
                a[last_pos]-=d
                c-=1
            negatives+=1
        else:
            a[last_pos]-=c*d
            c=0
    else:
        min_pos=0
        abs_min=float('inf')
        for i in range(len(a)):
            if math.fabs(a[i])<abs_min:
                abs_min=math.fabs(a[i])
                min_pos=i
        if a[min_pos]<0:
            a[min_pos]-=d
            c-=1
        else:
            a[min_pos]+=d
            c-=1
print(*a)
