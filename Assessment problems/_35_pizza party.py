a,y=map(int,input().split())
ans=0
while True:
 if a%y==0:
    ans=y
 break
else:
 y+=1
s=0
while ans>0:
 n=ans%10
 s+=n
 ans=ans//10
print(s)