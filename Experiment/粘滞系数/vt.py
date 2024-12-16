import math

#data = [1.053, 1.050, 1.049, 1.049, 1.050]

#data = [18.42, 18.32, 18.19, 18.22, 18.21]
#data = [15.84, 15.77, 15.85, 15.63, 15.62]
#data = [14.03, 14.13, 14.05, 13.88, 13.73]
#data = [12.54, 12.22, 12.14, 12.04, 12.06]
#data = [10.81, 10.68, 10.95, 10.43, 10.51]
data = [9.81, 9.72, 9.58, 9.43, 9.48]

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

v = 0.1 / mean
print(f"v = {v}") 