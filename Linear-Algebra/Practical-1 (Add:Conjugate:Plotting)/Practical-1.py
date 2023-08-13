import matplotlib.pyplot as plt

#Question-Aim
z = 3 + 2j
conjugate_z = z.conjugate()
print(conjugate_z)  
print()
print()

#Question - 1 
result = (1 + 3j) + (10 + 20j)
print("Addition of two complex numbers: ",result)
print()
print()

#Question - 2
x = 1 + 3j
result = (x - 1) ** 2
print("(x-1)**2 is ",result)
print()
print()

#Question - 3
result = 1 + 2j * 3
print("Result for 1+2j*3 is ",result)
print()
print()

#Question - 4
result = 4 * (3j) ** 2
print("Result for 4*(3j)**2 is ",result)
print()
print()

#Question - 5
x = 1 + 3j
a = x.real
b = x.imag
print("Real part:", a)
print("Imaginary part:", b)
print()
print()

#Question - 6
x = 1 + 3j
conjugate_x = x.conjugate()
print("Conjugate of x:", conjugate_x)
print()
print()

#Question - 7
S = [3 + 3j, 4 + 3j, 2 + 1j, 2.5 + 1j, 3 + 1j, 3.25 + 1j]
real_parts = [x.real for x in S]
imaginary_parts = [x.imag for x in S]
plt.scatter(real_parts, imaginary_parts, color='blue', label='S')
plt.xlabel('Real Part')
plt.ylabel('Imaginary Part')
plt.title('Plot of S')
plt.grid()
plt.legend()
plt.show()




