matrix1 = []
matrix2 = []
matrix3 = []

num_rows = eval(input("Enter number of rows: "))
num_col = eval(input("Enter number of cols: "))

for row in range(num_rows):
    matrix1.append([])
    matrix2.append([])
    matrix3.append([])
    for col in range(num_col):
        element = eval(input(f"Enter element {col} in row {row} in the FIRST matrix: "))
        matrix1[row].append(element)
        element2 = eval(input(f"Enter element {col} in row {row} in the \033[0;31m SECOND matrix: "))
        matrix2[row].append(element2)
        matrix3[row].append(matrix1[row][col] + matrix2[row][col])