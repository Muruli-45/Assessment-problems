n=int(input())
l=list(map(int,input().split()))
res=[]
f=False
pro=0
for i in range(0,len(l)-1):
 temp=0
 for j in range(i+1,len(l)):
    if l[i]+l[j]==18:
        temp=l[i]*l[j]
 if temp>pro:
    pro=temp
 res=sorted([l[i],l[j]],reverse=True)
print(res)