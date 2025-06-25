def logic_circuit_bitwise(A, B, C):
    # Inputs must be either 0 or 1
    Q = (A & B) | ((B | C) & (B & C))
    return Q

# Print the truth table
print("A B C | Q")
for A in [0, 1]:
    for B in [0, 1]:
        for C in [0, 1]:
            Q = logic_circuit_bitwise(A, B, C)
            print(f"{A} {B} {C} | {Q}")
