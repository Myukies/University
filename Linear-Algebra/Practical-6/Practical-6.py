import matplotlib as plt, numpy as np

x = int(input("\nEnter the real part: "))
y = int(input("\nEnter the imaginary part: "))
complex = complex(x,y)

print("\nThe complex number you've entered is: ", complex)
print("\nReal part: ", complex.real, "\nImaginary part: ", complex.imag)

rotated_complex = complex * 1j

print("\nThe rotated complex numbers are: ")
print("\nThe rotated complex number for 90 is: ", rotated_complex)

rotated_complex = complex * -1

print("\nThe rotated complex number for 180 is: ", rotated_complex)

rotated_complex = complex * (-1j)

print("\nThe rotated complex number for 270 is: ", rotated_complex)







