matrix1 = [
            [0,1,3,5,7,9],
            [2,4,6,8,0,10],
            [1,2,3,4,5,6]
            ]
print(matrix1)
for row in matrix1:
    for i in row:
        print(i,end=' ')
    print()
print("*"*30)
#or
for i in range(len(matrix1)):
    for j in range(len(matrix1[i])):
        print(matrix1[i][j],end=" ")
    print()
