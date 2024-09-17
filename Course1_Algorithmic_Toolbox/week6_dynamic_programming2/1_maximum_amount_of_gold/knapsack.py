m,n=input().split(' ',2)
m=int(m)
n=int(n)
l=list(map(int,input().split(' ',n)))   
l.insert(0,0)
k=[[0 for i in range(m+1)]for j in range(n+1)] #creating a 2d array
for i in range(n+1):
    for j in range(m+1):
        if i==0 or j==0:
            k[i][j]=0
        elif l[i]<=j:
            k[i][j]=max(l[i]+k[i-1][j-l[i]],k[i-1][j])
        else:
            k[i][j]=k[i-1][j]
print(k[n][m])