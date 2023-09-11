import time, numpy 

print("First Program\n")

n = int(input("Enter the number of elements in the vector: "))
u = []

for i in range(n):
    element = float(input(f"Enter element {i+1}: "))
    u.append(element)

print("Vector list U:", u)

print()
print()



time.sleep(1)
print("Second Program\n")

v = []

for i in range(n):
    element_v = float(input(f"Enter element {i+1} of vector v: "))
    v.append(element_v)

print("Entered vector v:", v)

print()
print()

time.sleep(1)
print("Third Program\n")

a = float(input("Enter value for a: "))
b = float(input("Enter value for b: "))

result = [a * u[i] + b * v[i] for i in range(n)]

print()
print(f"Vector {a}u + {b}v:", result)


print()
print()

time.sleep(1)
print("Fourth Program\n")

result = sum(u[i] * v[i] for i in range(n))

print("Dot product of u and v:", result)

