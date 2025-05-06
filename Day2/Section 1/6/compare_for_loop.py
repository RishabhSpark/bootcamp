# Generator expression
gen_exp = (x**2 for x in range(10) if x % 2 == 0)

# List comprehension
list_comp = [x**2 for x in range(10) if x % 2 == 0]

print("Generator output:")
for val in gen_exp:
    print(val)

print("\nList comprehension output:")
print(list_comp)