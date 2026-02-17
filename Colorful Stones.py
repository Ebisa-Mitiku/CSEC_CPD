s=list(input())
r=list(input())
pos=1
for i in range(len(r)):
    if r[i]==s[0]:
        pos=pos+1
        del s[0]
print(pos)
