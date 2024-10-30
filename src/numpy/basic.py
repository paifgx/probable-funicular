import numpy as np
import matplotlib.pyplot as plt

# arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
# matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# result = arr + matrix
# print(result)

# print(f"Sum of all elements in the matrix: {np.sum(arr)}")
# print(f"Mean of all elements in the matrix: {np.mean(arr)}")
# print(f"Standard deviation of all elements in the matrix: {np.std(arr)}")
# print(f"Variance of all elements in the matrix: {np.var(arr)}")
# print(f"Minimum value in the matrix: {np.min(arr)}")
# print(f"Maximum value in the matrix: {np.max(arr)}")

# print(arr[arr > 7])

# arr = np.array([1, 2, 3], dtype=np.int8)
# print(arr, arr.dtype)

# arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
# matrix = np.array([[1, 2, 3], [4, 5, 6]])

# zeros = np.zeros(5)
# print(zeros)

# zero_matrix = np.zeros((3, 3))
# print(zero_matrix)

# ones = np.ones(5)
# print(ones)

# one_matrix = np.ones((3, 3))
# print(one_matrix)

# filled_array = np.full(5, 7)
# print(filled_array)

# sequence = np.arange(0, 10, 2)
# print(sequence)

# linspace_array = np.linspace(0, 1, 6)
# print(linspace_array)

# random_array = np.random.rand(5)
# print(random_array)

# random_matrix = np.random.rand(3, 3)
# print(random_matrix)

# matrix = np.array([
#     [11, 12, 13, 14, 15],
#     [21, 22, 23, 24, 25],
#     [31, 32, 33, 34, 35],
#     [41, 42, 43, 44, 45],
#     [51, 52, 53, 54, 55]
# ])

# print(matrix[:, -1:])


# X = np.array(
#     [[[3, 1, 2],
#       [4, 2, 2]],
#      [[-1, 0, 1],
#       [1, -1, -2]],
#      [[3, 2, 2],
#       [4, 4, 3]],
#      [[2, 2, 1],
#       [3, 1, 3]]])

# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')

# # Plot each point in the 3D array
# for i in range(X.shape[0]):
#     for j in range(X.shape[1]):
#         for k in range(X.shape[2]):
#             ax.scatter(i, j, k, c='b', marker='o')
#             ax.text(i, j, k, f'{X[i, j, k]}', color='red')

# ax.set_xlabel('Dimension 0')
# ax.set_ylabel('Dimension 1')
# ax.set_zlabel('Dimension 2')

# plt.show()
# # print(X.shape)

# print("Dimension 0 with size ", X.shape[0])
# for i in range(X.shape[0]):
#     print(f"\nAusgabe von X[{i:1},:,:]:")
#     print(X[i,:,:])
    
# print("\nDimension 1 with size ", X.shape[1])
# for i in range(X.shape[1]):
#     print(f"\nAusgabe von X[:,{i:1},:]:")
#     print(X[:,i,:])
    
# print("\nDimension 2 with size ", X.shape[2])
# for i in range(X.shape[2]):
#     print(f"\nAusgabe von X[:,:,{i:1}]:")
#     print(X[:,:,i])

# ax = plt.figure().add_subplot(projection='3d')

# identity_matrix = np.eye(3)
# print(identity_matrix)

diag_matrix = np.diag([1, 2, 3, 4, 5])
print(diag_matrix)