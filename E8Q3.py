# Question 3
# WAP for numpy array properties and functions.   Answer:Python
import numpy as np
arr = np.array([[10, 20, 30], [40, 50, 60]])

# array properties
print(arr)
print("number of dimension:", arr.ndim)
print("shape:", arr.shape)
print("size:", arr.size)
print("Datatype:", arr.dtype)
print("Item size:", arr.itemsize)

# functions
print("maximum:", np.max(arr))
print("minimum:", np.min(arr))
print("mean:", np.mean(arr))
print("square:", np.sqrt(arr))
