import math
#data = [5.709, 5.709, 5.704, 5.712, 5.710]
#data = [5.724, 5.721, 5.724, 5.720, 5.723]
#data = [5.733, 5.734, 5.734, 5.736, 5.737]
#data = [5.744, 5.743, 5.741, 5.745, 5.747]
#data = [5.757, 5.754, 5.752, 5.752, 5.751]
#data = [5.767, 5.764, 5.767, 5.763, 5.766]

#data = [2.381, 2.383, 2.384, 2.385, 2.383]
#data = [2.537, 2.537, 2.537, 2.538, 2.537]
#data = [2.691, 2.692, 2.691, 2.690, 2.691]
#data = [2.839, 2.839, 2.838, 2.839, 2.839]
#data = [2.975, 2.975, 2.975, 2.974, 2.975]

#data = [15.65, 15.55, 16.25, 16.09, 16.43, 16.30, 16.24, 16.34]
#data = [14.64, 15.46, 15.13, 15.20, 15.22, 15.61]
#data = [12.25, 12.10, 12.60, 12.39, 12.22, 12.17]

#data = [6.0577, 6.0577, 6.0577, 6.0600, 6.0566, 6.0577]
#data = [5.98, 6.09, 6.11, 6.10, 5.98, 6.23]

#data = [35.06, 35.04, 35.04, 35.04, 35.04]
#data = [33.02, 33.00, 33.02, 33.00, 33.02]

#data = [47.6, 47.6, 47.6, 45.7, 46.6, 47.0]

#data = [239.86, 239.84, 239.88, 239.88, 239.86, 239.86]

#data = [210.02, 210.00, 210.02, 210.02, 210.02, 210.02]

#data  = [164.9, 164.8, 164.9, 164.9, 164.9, 164.9]

#data = [21.70, 21.78, 21.78, 21.77, 21.76]

data = [13.50, 13.48, 13.54, 13.54, 13.56]

mean = sum(data) / len(data)

# 计算测量值的标准偏差
sum_squared_diff = sum((x - mean) ** 2 for x in data)
std_dev = math.sqrt(sum_squared_diff / (len(data) - 1))

# 计算平均值的标准偏差
mean_std_dev = std_dev / math.sqrt(len(data))

delta_A = 2.57 * mean_std_dev

delta_B = 0.95 * 0.01 

uncertainty_U = math.sqrt(delta_A ** 2 + delta_B ** 2)
#uncertainty_U=1.05*std_dev


print(f"1.平均值为: {mean}")
print(f"2.六个测量值的标准偏差为: {std_dev}")
print(f"3.平均值的标准偏差为: {mean_std_dev}")
print(f"4.ΔA = {delta_A}")
print(f"4.ΔB = {delta_B}")
print(f"4.不确定度U = {uncertainty_U}")