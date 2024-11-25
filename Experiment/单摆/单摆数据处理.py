import matplotlib.pyplot as plt
import numpy as np

# 数据
T = [2.383, 2.537, 2.691, 2.839, 2.975]
L = [35.010, 40.010, 45.010, 50.010, 55.010]
T_squared = [(t / 2) ** 2 for t in T]

# 绘制表格
fig, ax = plt.subplots()
table_data = [
    ["", "1", "2", "3", "4", "5"],
    ["2T", 2.383, 2.537, 2.691, 2.839, 2.975],
    ["T^2", f"{T_squared[0]:.4f}", f"{T_squared[1]:.4f}", f"{T_squared[2]:.4f}", f"{T_squared[3]:.4f}", f"{T_squared[4]:.4f}"],
    ["L", 35.010, 40.010, 45.010, 50.010, 55.010],
]
ax.axis('tight')
ax.axis('off')
table = ax.table(cellText=table_data, cellLoc='center', loc='center')
table.auto_set_font_size(False)
table.set_fontsize(14)
table.scale(1, 1.5)

# 绘制T^2和L的图像
plt.figure()
plt.scatter(L, T_squared, c='black', s=60, label='Data Points (Highlighted)')
coefficients = np.polyfit(L, T_squared, 1)
polynomial = np.poly1d(coefficients)
plt.plot(L, polynomial(L), linestyle='--', label=f'Fit Line: {coefficients[0]:.4f}L + {coefficients[1]:.4f}')
plt.xlabel("L")
plt.ylabel("T^2")
plt.legend()
plt.title(f'Linear Fit: T^2 = {coefficients[0]:.4f}L + {coefficients[1]:.4f}')
plt.grid(True)

g = 4 * np.pi ** 2 / (0.04)
print(f"g = {g:.4f}")

plt.show()