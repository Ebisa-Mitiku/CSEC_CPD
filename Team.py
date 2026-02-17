n=int(input())
lst=[]
for i in range(n):
    l=list(map(int,input().split()))
    lst.append(l)
d=0
for i in range(len(lst)):
    count=0
    for j in range(3):
        if lst[i][j]==1:
            count=count+1
    if(count>=2):
        d=d+1
print(d)
