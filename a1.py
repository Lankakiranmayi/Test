import re
fname=input("enter file name:")
hand=open(fname)
numlist=list()
count=0
for line in hand:
    line=line.rstrip()
    stuff=re.findall('[0-9]+',line)
    if len(stuff)==0:
        continue
    for i in range(len(stuff)):
        num=int(stuff[i])
        numlist.append(num)
print(len(numlist))
print(sum(numlist))
