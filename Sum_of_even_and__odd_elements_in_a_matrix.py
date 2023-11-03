r,c=map(int,input().split())
e=0
o=0
matrix1 = []
for i in range(r):
    d=list(map(int,input().split()))
    matrix1.append(d)
    

for i in range(r):
    for j in range(c):
        if matrix1[i][j]%2==0:e+=matrix1[i][j]
        else:o+=matrix1[i][j]
print(e,o)            
            
