
def sumofAP(A, N, D):
    total = (A * (2 * A + (N - 1) * D)) / 2
    return total
A = int(input("Enter First Number of an A.P Series: : "))
N = int(input("Enter the Total Numbers in this A.P Series: : "))
D = int(input("Enter the Common Difference : "))
total = sumofAP(A, N, D)
print("\nThe Sum of Arithmetic Progression  = " , total)
