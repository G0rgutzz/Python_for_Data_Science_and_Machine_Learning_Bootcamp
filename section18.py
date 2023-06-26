import numpy as np
np.set_printoptions(precision=4)

my_list = [1, 2, 3]
a = np.array(my_list)
print(a)
my_mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
b = np.array(my_mat)
print(b)
c = np.arange(0, 10, 2)
print(c)
zero = np.zeros(3)
zero1 = np.zeros((5, 5))
print(zero)
print(zero1)
one = np.ones(4)
one1 = np.ones((4, 4))
print(one)
print(one1)
d = np.linspace(0, 5, 101)  # start, stop, number
print(d)
e = np.eye(4)
print(e)
f = np.random.rand(5)  # array of a given size with random numbers
print(f)
g = np.random.rand(5, 4)
print(g)
h = np.random.randn(2, 5)
print(h)
i = np.random.randint(1, 100, 10)
print(i)
arr = np.arange(25)
print(arr)
ranarr = np.random.randint(0, 50, 10)
print(ranarr)
j = arr.reshape(5, 5)
print(j)
maxv = ranarr.max()  # max value
minv = ranarr.min()  # min value
maxl = ranarr.argmax()  # position of max value
minl = ranarr.argmin()  # position of min value
print(maxv, minv, maxl, minl)
k = j.shape  # shape of an array
print(k)
l1 = j.dtype
print(l1)
