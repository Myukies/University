import numpy as np

v = np.array([-1,4])
u = np.array([2,7])

v_norm = np.sqrt(v**2)
uONv = (np.dot(u, v)/v_norm**2)*v

print("Projection of vector V on vector U is: ", uONv)
