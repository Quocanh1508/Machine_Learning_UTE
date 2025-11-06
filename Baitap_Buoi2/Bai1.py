import numpy as np
vector_1chieu = np.arange(1, 17)
print("Ma tran 1 chiều gốc ( Shape :", vector_1chieu.shape, ")")
print(vector_1chieu)
matrix_4x4 = vector_1chieu.reshape(4, 4)
print(" Ma tran 4x4 sau khi reshape ( Shape :",matrix_4x4,")")
print(matrix_4x4)

matrix_phu = matrix_4x4[2:,2:]
print("Ma trận được trích xuất là :")
print(matrix_phu)
