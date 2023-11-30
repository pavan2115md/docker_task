def print_triangle(rows):
    for i in range(1, rows + 1):
        print(" " * (rows - i) + "*" * (2 * i - 1))

# Set the number of rows for the triangle (adjust as needed)
num_rows = 10

# Call the function to print the triangle
print_triangle(num_rows)
       
