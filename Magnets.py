n=int(input())
lst=[]
count=1
for i in range(n):
    l=list(input())
    lst.append(l)
for i in range(len(lst)-1):
    if(lst[i][1]==lst[i+1][0]):
       count=count+1

print(count)
