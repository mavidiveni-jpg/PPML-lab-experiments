# Question 4
# WAP for statistical operation & broadcasting.  
#  Answer:Python
import numpy as np
arr = np.array([10, 20, 30, 40, 50])

# statistical operations
print("array:", arr)
print("mean:", np.mean(arr))
print("median:", np.median(arr))
print("standard deviation:", np.std(arr))
print("variance:", np.var(arr))
print("maximum:", np.max(arr))
print("minimum:", np.min(arr))

# Broadcasting
a = np.array([1, 2, 3, 4])
b = 10
print("original array:", a)
print("After adding 10:", a + b)
print("After multiplying 10:", a * b)