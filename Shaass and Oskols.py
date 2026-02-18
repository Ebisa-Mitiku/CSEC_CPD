n=int(input())
l=list(map(int,input().split()))
m=int(input())
d=[]
if(m==0):
    for i in range(len(l)):
        print(l[i])
elif(len(l)==1):
    print(0)

else:
    for i in range(m):
        x,y=map(int,input().split())
        d.append([x-1,y])
    for i in range(m):
        if(d[i][0]==0):
            l[1]=l[1]+(l[0]-(d[i][1]))
            l[0]=0
        elif(d[i][0]==len(l)-1):
            l[len(l)-2]=l[len(l)-2]+(d[i][1]-1)
            l[len(l)-1]=0
        else:
            l[d[i][0]-1]=l[d[i][0]-1]+((d[i][1])-1)
            l[d[i][0]+1]=l[d[i][0]+1]+((l[d[i][0]])-d[i][1])
            l[d[i][0]]=0
    for i in range(len(l)):
        print(l[i]) 
