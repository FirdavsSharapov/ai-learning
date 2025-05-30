# Day 4: NumPy Basics
# Focus: Arrays, Operations, and Stats

import numpy as np

arr = np.array([1,2,3,4,5,6,7,8,9,10])
print(arr)
print(type(arr))

print(arr + 5)
print(arr ** 2)
print(arr * 3)

d_arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(d_arr.shape)
print(d_arr.size)
print(d_arr.dtype)
print(d_arr.T)

print(d_arr.mean())
print(d_arr.max())
print(d_arr.min())
print(d_arr.std())

f_arr = np.random.randint(10, 101, size=(4, 4))
print("\n4x4 Random Array:")
print(f_arr)

row_sums = f_arr.sum(axis=1)
max_row_index = np.argmax(row_sums)
print("\nRow with the highest sum:")
print(f_arr[max_row_index])
