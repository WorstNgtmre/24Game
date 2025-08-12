# 24 Game Solver
# This script solves the 24 Game by finding combinations of four numbers that can be combined to 24 using basic arithmetic operations.

OPERATIONS = ["+", "-", "*", "/"]
OBJECTIVE = 24

# Simple operation maker
def calculate(n: float, m: float, operation: str) -> float:
    if operation in OPERATIONS:
        if operation == "+":
            return n + m
        elif operation == "-":
            return n - m
        elif operation == "*":
            return  n * m
        else:
            return n / m if m != 0 else None
    else:
        print("Please provide a valid operation symbol")
        return None

# Calculates all the posible operation with 2 numbers
def calculate_comb_2(n: tuple, m: tuple):
    n_val, n_expr = n
    m_val, m_expr = m
    results = []
    for operation in OPERATIONS:
        results.append((calculate(n_val, m_val, operation),f"({n_expr} {operation} {m_expr})"))
    return results

def calc_n_number(numbers: list):
    if len(numbers) == 1:
        val, expr = numbers[0]
        if abs(val - OBJECTIVE) < 1e-6:  # Using a small epsilon for floating point comparison
            print(f"Found solution: {expr} = {OBJECTIVE}")
            return True
        return False    
    
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if i != j:
                n_val, n_expr = numbers[i]
                m_val, m_expr = numbers[j]

                for res_val, res_expr in calculate_comb_2((n_val,n_expr), (m_val,m_expr)):
                    if res_expr is not None and res_expr is not None:
                        new_nums = [numbers[k] for k in range(len(numbers)) if k != i and k != j]
                        new_nums.append((res_val, res_expr))
                        if calc_n_number(new_nums):
                            return True
    return False

# Main loop
while True:
    numbers = input("Provide four numbers separated by spaces or e(x)it: ").split(" ")
    if numbers[0] == "x":
        break
    elif len(numbers) != 4:
        print("Please enter exactly four numbers.")
        continue
    while not numbers[0].isdigit() or not numbers[1].isdigit() or not numbers[2].isdigit() or not numbers[3].isdigit():
        numbers = input("Provide four numbers separated by spaces: ").split(" ")
    
    tuples = []
    for num in numbers:
        r = (float(num),str(num))
        tuples.append(r)
    
    solution_found = calc_n_number(tuples)
    if not solution_found:
        print("No solution found for the provided numbers.")
            