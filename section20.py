import numpy as np

arr = np.arange(0, 11)
print(arr)
arr[0:5] = 100
print(arr)
arr1 = np.arange(0, 11)
slice_off_array = arr1[0:6]  # it's a view of an array, not a copy, if I change this variable, original array will change as well
arr1_copy = arr1.copy()  # now I can change values in the slice of arr1 without affecting it
arr_2d = np.array([[5, 10, 15], [20, 25, 30], [35, 40, 45]])
print(arr_2d)
print(arr_2d[2, 0])  # better than many brackets
print(arr_2d[:2, 1:])  # everything from rows 0 and 1 and everything from column 1 and highier
arr2 = np.arange(1, 11)
bool_arr = arr2 > 5
print(arr2[bool_arr])
print(arr2[arr2 < 3])
arr3 = np.arange(50).reshape(5, 10)
print(arr3)
print(arr3[1:3, 3:5])
a = np.zeros(10)
print(a)
b = np.ones(10)
print(b)
c = np.ones(10)*5
print(c)
d = np.linspace(10, 50, 41)
print(d)
e = np.linspace(10, 50, 21)
print(e)
f = np.arange(9).reshape(3, 3)
print(f)
g = np.eye(3)
print(g)
h = np.random.randn(25)
print(h)
i = np.linspace(0.01, 1, 100).reshape(10, -1)
print(i)
j = np.linspace(0, 1, 20)
print(j)
mat = np.arange(1, 26).reshape(5, 5)
print(mat[2:, 1:])
print(mat[mat == 20])
print(mat[:3, 1:2])
print(mat[4, :])
print(mat[3:, :])
print(np.sum(mat))
print(np.std(mat))
print(mat.sum(axis=0))

