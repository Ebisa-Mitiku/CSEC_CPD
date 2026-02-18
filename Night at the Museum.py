n=input()
s="abcdefghijklmnopqrstuvwxyz"
d=0
c="a"
for i in range(len(n)):
    t=s.index(n[i])
    y=s.index(c)
    difr=abs(t-y)
    difr2=26-difr
    d=d+min(difr,difr2)
    c=n[i]        
print(d)
