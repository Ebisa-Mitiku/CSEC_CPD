a,b=map(int,input().split())
l=list(map(int,input().split()))
count=0
for i in range(len(l)):
    if(l[i]>b):
        count=count+2
    else:
        count=count+1
print(count)
