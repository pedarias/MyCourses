def partition(weight,n,l):
    count=0
    value=[[0 for i in range(n+1)]for j in range(weight+1)]  #or import numpy and create a 2d array by doing (value=numpy.zeros((weight+1,n+1)))
    for i in range(1,weight+1):
        for j in range(1,n+1):
            value[i][j]=value[i][j-1]
            if l[j-1]<=i:
                temp=value[i-l[j-1]][j-1]+l[j-1]
                if temp>value[i][j]:
                    value[i][j]=temp
            if value[i][j]==weight:
                count+=1
    if count<3:
        return 0
    else:
        return 1
n=int(input())
l=list(map(int,input().split(' ',n)))
total=sum(l)
if total%3 !=0:
    print("0")
elif n<3:
    print("0")
else:
    print(partition(total//3,n,l))