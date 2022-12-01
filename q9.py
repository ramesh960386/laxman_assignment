import numpy as np
	
# 1D array
arr = [1, 2, 3, 4, 5]

print("arr : ", arr)
print("var of arr : ", np.var(arr))
print("\nvar of arr : ", np.var(arr, dtype = np.float32))
print("\nvar of arr : ", np.var(arr, dtype = np.float64))
