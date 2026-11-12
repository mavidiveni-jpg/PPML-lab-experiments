# Question 2WAP for date types structures in numpy.
#   Answer:Python
import numpy as np
a = np.array([1, 2, 3], dtype=int)
b = np.array([1.5, 2.5, 3.5, 4.5], dtype=float)
c = np.array([True, False, True], dtype=bool)
d = np.array(["A", "B", "C"], dtype=str)

print("Datatype:", a.dtype)
print("Datatype:", b.dtype)
print("Datatype:", c.dtype)
print("Datatype:", d.dtype)

# Different array structures
one_d = np.array([1, 2, 3])
two_d = np.array([[1, 2], [3, 4]])
three_d = np.array([[[1, 2, 3], [3, 4]]])

print("1-D array \n", one_d)
print("2-D array \n", two_d)
print("3-D array \n", three_d)