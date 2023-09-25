import numpy as np

u = np.array([-10, 20])
v = np.array([3, 7])

v_norm = np.sqrt(v**2)
uONv = (np.dot(u, v)/v_norm**2)*v

print("Projection of vector U on vector V is: ", uONv)
