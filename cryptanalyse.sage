from sage.modules.free_module_integer import IntegerLattice

def knapsack_mh_sage(e, S, C):
    n = len(e)
    
    # Create the lattice matrix
    lattice_matrix = Matrix(ZZ, n + 1, n + 1)
    
    for i in range(n):
        lattice_matrix[i, i] = 1
        lattice_matrix[i, n] = e[i] * C
    
    lattice_matrix[n, n] = -S * C
    
    # Apply LLL reduction
    lattice = IntegerLattice(lattice_matrix)
    short_vector = lattice.shortest_vector()
    
    # Check the conditions for a solution
    if short_vector[-1] == 0 and all(abs(short_vector[i]) <= 1 for i in range(n)) and sum(short_vector[i] * e[i] for i in range(n)) == S:
        return tuple(short_vector[:-1])
    else:
        return None

# Example parameters
e = [205, 119, 281, 56, 112, 171]   #clé publique
S = 825 #message
C = 10

e2 = [22, 16, 71, 54, 56]    
message = "10101"
S2 = 149 
c2 = 10


# Apply the knapsack algorithm using SageMath
solution = knapsack_mh_sage(e, S, C)

# Display the result
if solution:
    print("Solution found:", solution)
else:
    print("No solution found.")