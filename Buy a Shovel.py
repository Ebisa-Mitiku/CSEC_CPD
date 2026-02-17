k,r=map(int,input().split())
i=1
while(k%10!=0 or (k-r)%10!=0 ):
    total=k*i
    if(total%10==0 or (total-r)%10==0):
        break
    else:
        i=i+1
print(i)   
