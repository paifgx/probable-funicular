import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy import linalg

# array = np.array([1, 2, 3, 4, 5])
# array_2 = array * 2
# print(array_2)

# matrix_1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# matrix_2 = np.array([[9, 8, 7], [6, 5, 4], [3, 2, 1]])
# result = np.dot(matrix_1, matrix_2)
# print(result)

# matrix = np.array([[1, 2], [3, 4]])
# # det = linalg.det(matrix)
# # print(det)

# eigenvalues, eigenvectors = linalg.eig(matrix)
# print(f"Eigenvalues: {eigenvalues}")
# print(f"Eigenvectors: {eigenvectors}")

# x = np.linspace(0, 10, 100)
# y = np.sin(x)

# plt.plot(x, y)
# plt.xlabel("x")
# plt.ylabel("sin(x)")
# plt.title("Sinuskurve")
# plt.show()

# series_data = pd.Series([10, 20, 30], index=["a", "b", "c"])
# print(series_data)

# frame_data = { "Name": ["Alice", "Bob", "Charlie"], "Age": [24, 25, 26] }
# df = pd.DataFrame(frame_data)
# print(df)

# df = pd.read_csv("./tips.csv")
# print(df.head())

# total_bill = df["total_bill"]
# tip = df["tip"]
# b, a = np.polyfit(total_bill, tip, deg=1)

# plt.plot(total_bill, a + b * total_bill, color="red")
# plt.scatter(total_bill, tip)
# plt.xlabel("Total Bill")
# plt.ylabel("Tip")
# plt.title("Total Bill vs. Tip")
# plt.show()