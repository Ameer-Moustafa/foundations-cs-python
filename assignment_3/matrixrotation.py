matrix1 = [[1,2,3], 
           [4,5,6]]

matrix2 = [[1,4], 
           [2,5], 
           [3,6]]

matrix3 = []

for row in range(len(matrix1)):
    for col in range(len(matrix1[row])):
        matrix3.append(matrix1[row][col])

print(matrix3)

for row in range(len(matrix2)):
    print(matrix2[row])