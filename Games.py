n=int(input())
l=[]
temp=[]
count=0
for i in range(n):
    h,g=map(int,input().split())
    l.append([h,g])
for i in range(len(l)):
    temp.append(l[i])
    for j in range(len(l)):
        if(temp[0][0]==l[j][0]):
            continue
        elif(temp[0][0]==l[j][1]):
            count=count+1
    del temp[0]

print(count)
