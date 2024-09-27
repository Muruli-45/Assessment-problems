x,n,y,m=map(int,input().split())
if x>n:
 x,y=y,x
 n,m=m,n
ans=y-x
pos=0
for pos in range(n):
 if (ans%n+pos*m)%n==0:
    break
if pos!=n:
 print(y+pos*m)