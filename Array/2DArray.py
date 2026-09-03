# A 2D array is an array that contains rows and columns, like a table.
# Accessing elements:- matrix[row][column]

# Traversing a 2D array
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for row in matrix:
  
    # Traversing each element
    # in the current row
    for x in row:
        print(x, end=" ")
    print()