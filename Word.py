s=input()
cap=0
low=0
for i in s:
    if i.isupper():
        cap=cap+1
    else:
        low=low+1
if(cap>low):
    print(s.upper())
elif(cap<low):
    print(s.lower())
else:
    print(s.lower())
