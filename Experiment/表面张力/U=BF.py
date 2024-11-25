import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.stats import linregress
import math

# 数据准备
m = np.array([0.500, 1.000, 1.500, 2.000, 2.500, 3.000, 3.500])  # 质量m，单位10^{-3}kg
U = np.array([14.6, 29.9, 45.1, 59.1, 75.4, 88.3, 106.5])  # 电压U，单位10^{-3}V

# 计算f = mg
g = 9.794  # 重力加速度，单位N/kg
f = m * g  # f的值

# 制作数据表
data_table = pd.DataFrame({'m (10^{-3}kg)': m, 'U (10^{-3}V)': U})

# 拟合
slope, intercept, r_value, p_value, std_err = linregress(f, U)
line = slope * f + intercept

# 第一张图：表格
plt.figure(figsize=(8, 2))
plt.axis('tight')
plt.axis('off')
plt.table(cellText=data_table.values, colLabels=data_table.columns, loc='center')
plt.title("Ground Truth Data Points")

# 第二张图：U-f拟合曲线
plt.figure()
plt.plot(f, U, 'o', label='data point')
plt.plot(f, line, 'r', label=f'U = {slope:.2f}f + {intercept:.2f}')
plt.xlabel(' f (N)')
plt.ylabel(' U (10^{-3}V)')
plt.title('U-f ')
plt.legend()
plt.grid(True)
plt.show()

# 返回拟合直线的斜率
print(slope)