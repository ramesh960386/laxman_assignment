import numpy as np

m_list = [[4, 3], [-5, 9]]
A = np.array(m_list)
inv_A = np.linalg.inv(A)
print(inv_A)


B = np.array([20, 26])
X = np.linalg.inv(A).dot(B)
print(X)