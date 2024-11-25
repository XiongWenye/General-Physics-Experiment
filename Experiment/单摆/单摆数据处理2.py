import numpy as np
import matplotlib.pyplot as plt

Four_T = [5.709, 5.722, 5.735, 5.744, 5.753, 5.765]

T = [t / 2 for t in Four_T]

theta = [5, 8, 11, 14, 17, 20]

sin_half_theta_squared = [(np.sin(np.radians(t / 2)) ** 2) for t in theta]

fig, ax = plt.subplots()

table_data = [
    ["", "1", "2", "3", "4", "5", "6"],
    ["4T", 5.709, 5.722, 5.735, 5.744, 5.753, 5.765],
    ["sin^2(θ/2)", f"{sin_half_theta_squared[0]:.4f}", f"{sin_half_theta_squared[1]:.4f}", f"{sin_half_theta_squared[2]:.4f}", f"{sin_half_theta_squared[3]:.4f}", f"{sin_half_theta_squared[4]:.4f}", f"{sin_half_theta_squared[5]:.4f}"],
]

ax.axis('tight')
ax.axis('off')
table = ax.table(cellText=table_data, cellLoc='center', loc='center')
table.auto_set_font_size(False)
table.set_fontsize(14)

table.scale(1, 1.5)

plt.figure()
plt.scatter(sin_half_theta_squared, T, c='black', s=60, label='Data Points (Highlighted)')

coefficients = np.polyfit(sin_half_theta_squared, T, 1)
polynomial = np.poly1d(coefficients)
plt.plot(sin_half_theta_squared, polynomial(sin_half_theta_squared), linestyle='--', label=f'Fit Line: {coefficients[0]:.4f}sin^2(θ/2) + {coefficients[1]:.4f}')
plt.xlabel("sin^2(θ/2)")
plt.ylabel("2T")
plt.legend()
plt.title(f'Linear Fit: 2T = {coefficients[0]:.4f}sin^2(θ/2) + {coefficients[1]:.4f}')
plt.grid(True)

L = 0.51
T_0 = coefficients[1] / 2

g = 4 * np.pi ** 2 * L / (T_0 ** 2)
print(f"g = {g:.4f}")

plt.show()