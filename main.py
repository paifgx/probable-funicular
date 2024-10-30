import numpy as np

array_1 = np.arange(1, 11)
# print(array_1)

array_2 = np.arange(1, 10).reshape(3, 3)
# print(array_2)

# 3D array mit 2x3x4, zufällige Ganzzahlen zwischen 1 und 100
array_3 = np.random.randint(1, 101, (2, 3, 4))
# print(array_3)

array_a = np.arange(1, 6)
array_b = array_a * 10
# print(array_b)

array_c = np.array([1, 2, 3])
array_d = np.array([4, 5, 6])

array_sum = array_c + array_d
array_mult = array_c * array_d
# print(array_mult)

matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

array_e = np.array([10, 20, 30])
result = matrix * array_e

# print(sum(matrix, array_e))

a = [[1,2,3,4,5]]
b = [[10],
     [20],
     [30],
     [40],     
     [50]]

# print(np.dot(a, b))

ones_array = np.ones((4,4))
framed_array = np.pad(ones_array, pad_width=1, mode='constant', constant_values=0)
# print(framed_array)

array_l = np.random.uniform(-10, 10, 10)
# print(array_l)
array_l[array_l > 0] *= 2
# print(array_l)