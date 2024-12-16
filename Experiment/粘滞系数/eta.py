rho = 7.8e3  
rho_0 = 0.95e3  
g = 9.79  
d = 0.0010502
v_0 = 0.01041 
D = 0.02  

eta = ((rho - rho_0) * g * d**2) / (18 * v_0 * (1 + 2.4 * d / D))

eta_1 = eta - (3 / 16) * v_0 * d * rho_0

print(f"eta 的值: {eta} Pa⋅s")
print(f"eta_1 的值: {eta_1} Pa⋅s")