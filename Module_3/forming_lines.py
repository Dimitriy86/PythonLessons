for i in range(8):
    s = f"int: {i:d}; hex: {i:#x}; oct: {i:#o}; bin: {i:#b}"
    print(s)

# -------------------------------------------------------------------

price = 19.99
quantity = 3
total = f" Total: {price * quantity:.2f}"
print(total)

# -------------------------------------------------------------------

width = 5
for num in range(12):
    print(f"{num:^10} {num**2:^10} {num**3:^10}")

# -------------------------------------------------------------------

name = "Alice"
formatted = f"{name:>10}"
print(formatted)

# -------------------------------------------------------------------

completion = 0.756
formatted = f"{completion:.1%}"
print(formatted)

# -------------------------------------------------------------------

progress = 0.5
formatted = f"{progress:.0%}"
print(formatted)

# -------------------------------------------------------------------