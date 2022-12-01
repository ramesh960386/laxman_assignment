import numpy as np
import numpy.linalg

matrix = np.matrix([[1,2],[3,4]])
print(matrix)

eigen_values = numpy.linalg.eigvals(matrix)
print(eigen_values)