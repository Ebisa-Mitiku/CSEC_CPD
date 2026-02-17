n=int(input())
l=list(map(int,input().split()))
crime=0
hired=0
un=0
for i in range(len(l)):
    if(l[i]>0):
        hired=hired+l[i]
    else:
        if(hired>0):
            hired=hired-1
        else:
            un=un+1
print(un)
