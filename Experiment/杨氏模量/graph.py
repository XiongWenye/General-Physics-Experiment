##最小二乘法拟合图像
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import leastsq


# 数据点
X = np.array([1.01, 2.01, 3.0, 4.01, 5.0, 6.01, 7.0, 8.02, 9.0, 10.01])
Y = np.array([0.465, 0.93, 1.395, 1.845, 2.275, 2.74, 3.2, 3.67, 4.05, 4.555])

coefficients = np.polyfit(X, Y, 1)
slope = coefficients[0]
intercept = coefficients[1]

# 拟合直线
Y_fit = slope * X + intercept

# 绘图
plt.scatter(X, Y, label='Data Points')
plt.plot(X, Y_fit, color='red', label=f'Fitted Line: y={slope:.2f}x+{intercept:.2f}')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Least Squares Fit')
plt.legend()
plt.show()

# 输出斜率
print(f'Slope: {slope}')