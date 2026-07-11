def print_identity_matrix(n):
    """
    Prints an identity matrix of size n x n.
    :param n: Size of the identity matrix
    """
    
    if n <= 0:
        print("Please enter a positive integer for the size of the matrix.")
        return

    for i in range(n):
        for j in range(n):
            if i == j:
                print(1, end=" ")
            else:
                print(0, end=" ")
        print()


try:
    size = int(input("Enter the size of the identity matrix: "))
    print_identity_matrix(size)

except ValueError:
    print("Invalid input! Please enter a valid integer.")