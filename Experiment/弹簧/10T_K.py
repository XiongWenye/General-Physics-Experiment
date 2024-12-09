import math
data = [0.8209, 0.8195, 0.8196, 0.8197, 0.8196, 0.8190, 0.8195, 0.8199, 0.8200, 0.8195]
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

K = 4 * (math.pi ** 2) * (21.758 + (13.524/3)) / (mean  ** 2) /1000
print(f"5.弹簧常数K = {K}")