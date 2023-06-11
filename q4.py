# Take the file path as input
file_path = input("Enter the file path: ")

# Read the matrix from the file
matrix = []
file = open(file_path, 'r')
for line in file:
    row = list(map(int,line.split()))
    matrix.append(row)

# Get the dimensions of the original matrix
rows = len(matrix)
cols = len(matrix[0])

# Transpose the matrix
transposed_matrix = [[matrix[j][i] for j in range(rows)] for i in range(cols)]

# Printing  the original matrix
print("Original Matrix:")
for row in matrix:
    print(row)

# Printing  the transposed matrix
print("\nTransposed Matrix:")
for row in transposed_matrix:
    print(row)

