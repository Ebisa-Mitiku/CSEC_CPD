l=[]
for i in range(5):
    s=list(map(int,input().split()))
    l.append(s)
for i in range(5):
    for j in range(5):
        if(l[i][j]==1):
            x=i
            y=j
d=abs(x-2)+abs(y-2)
print(d)
