def solve_linear_equation(a, b, c):
    if a == 0:
        if b == c:
            return "Nekonečně mnoho řešení."
        else:
            return "Žádné řešení."
    else:
        return (c - b) / a

# Příklad použití
a = 1
b = 5
c = 10

x = solve_linear_equation(a, b, c)
print(f"Řešení rovnice {a}x + {b} = {c} je x = {x}")
