n=int(input())
l=list(map(int,input().split()))
x=0
y=0
for i in range((n//2)):
    if(l[len(l)-1]>=l[0]):
        x=x+l[len(l)-1]
        del l[len(l)-1]
    else:
        x=x+l[0]
        del l[0]
    if(l[len(l)-1]>=l[0]):
        y=y+l[len(l)-1]
        del l[len(l)-1]
    else:
        y=y+l[0]
        del l[0]
if l:
    x=x+l[0]
d=[str(x),str(y)]
s=" ".join(d)
print(s)
