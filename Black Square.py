l=list(map(str,input().split()))
s=list(input())
x=0
for i in range(len(s)):
    if(s[i]=="1"):
        s[i]=l[0]
    elif(s[i]=="2"):
        s[i]=l[1]
    elif(s[i]=="3"):
        s[i]=l[2]
    else:
        s[i]=l[3]
for i in range(len(s)):
    x=x+int(s[i])     
print(x)
