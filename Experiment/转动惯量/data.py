import math
import csv

# # Define the formula (2 * math.pi * (k_n * t_m - k_m * t_n)) / (t_n**2 * t_m - t_m**2 * t_n) as a function, rounding the result to 4 decimal places
def calculate_beta(k_m, k_n, t_m, t_n):
    return round((2 * math.pi * (k_n * t_m - k_m * t_n)) / (t_n**2 * t_m - t_m**2 * t_n), 4)

# # Given values for k_m, k_n, t_m, t_n in the 9 sets
values1 = [
########################1
(1, 2, 1.1913, 2.4178),
(2, 3, 2.4178, 3.6824),
(3, 4, 3.6824, 4.9902),
(4, 5, 4.9902, 6.3434),
(5, 6, 6.3434, 7.7468),
(6, 7, 7.7468, 9.2043),
(7, 8, 9.2043, 10.7220),
(8, 9, 10.7220, 12.3081),
(9, 10, 12.3081, 13.9729)
]

values2 = [
    #########################2
(1, 2, 0.8765, 1.5700),
(2, 3, 1.5700, 2.1622),
(3, 4, 2.1622, 2.6889),
(4, 5, 2.6889, 3.1674),
(5, 6, 3.1674, 3.6096),
(6, 7, 3.6096, 4.0223),
(7, 8, 4.0223, 4.4111),
(8, 9, 4.4111, 4.7823),
(9, 10,4.7823, 5.1530)
]

values3 = [
    #########################3
(1, 2, 1.8176, 3.7022),
(2, 3, 3.7022, 5.6560),
(3, 4, 5.6560, 7.6944),
(4, 5, 7.6944, 9.8214),
(5, 6, 9.8214, 12.0532),
(6, 7, 12.0532, 14.3983),
(7, 8, 14.3983, 16.8786),
(8, 9, 16.8786, 19.5142),
(9, 10,19.5142, 22.3463)
]

values4 = [
    #########################4
(1, 2, 1.2744, 2.2623),
(2, 3, 2.2623, 3.0992),
(3, 4, 3.0992, 3.8395),
(4, 5, 3.8395, 4.5098),
(5, 6, 4.5098, 5.1279),
(6, 7, 5.1279, 5.7039),
(7, 8, 5.7039, 6.2463),
(8, 9, 6.2463, 6.7624),
(9, 10,6.7624, 7.2773)
]

values5 = [
    #########################5
(1, 2, 1.7846, 3.6409),
(2, 3, 3.6409, 5.5845),
(3, 4, 5.5845, 7.6166),
(4, 5, 7.6166, 9.7590),
(5, 6, 9.7590, 12.0205),
(6, 7, 12.0205, 14.4343),
(7, 8, 14.4343, 17.0191),
(8, 9, 17.0191, 19.8308),
(9, 10,19.8308, 22.9035)
]

values6 = [
    #########################6
(1, 2, 1.5880, 2.6479),
(2, 3, 2.6479, 3.5036),
(3, 4, 3.5036, 4.2410),
(4, 5, 4.2410, 4.9006),
(5, 6, 4.9006, 5.5021),
(6, 7, 5.5021, 6.0596),
(7, 8, 6.0596, 6.5808),
(8, 9, 6.5808, 7.0727),
(9, 10,7.0727, 7.5412)
]

# # Calculate beta for each set of values
beta_values1 = [calculate_beta(k_m, k_n, t_m, t_n) for k_m, k_n, t_m, t_n in values1]
beta_values2 = [calculate_beta(k_m, k_n, t_m, t_n) for k_m, k_n, t_m, t_n in values2]
beta_values3 = [calculate_beta(k_m, k_n, t_m, t_n) for k_m, k_n, t_m, t_n in values3]
beta_values4 = [calculate_beta(k_m, k_n, t_m, t_n) for k_m, k_n, t_m, t_n in values4]
beta_values5 = [calculate_beta(k_m, k_n, t_m, t_n) for k_m, k_n, t_m, t_n in values5]
beta_values6 = [calculate_beta(k_m, k_n, t_m, t_n) for k_m, k_n, t_m, t_n in values6]

# # Print out the list of beta values for each set into a csv file at folder Experiment, each row corresponds to a set of values
with open('Experiment/转动惯量/beta_values.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows([beta_values1])
    writer.writerows([beta_values2])
    writer.writerows([beta_values3])
    writer.writerows([beta_values4])
    writer.writerows([beta_values5])
    writer.writerows([beta_values6])




def calculate_J_values(m_val, R_val, g_val, beta_1_val, beta_2_val, beta_3_val, beta_4_val):
    # Calculate J1
    J_1_val = R_val * m_val * (g_val - R_val * beta_2_val) / (beta_2_val - beta_1_val)
    # Calculate J2
    J_2_val = R_val * m_val * (g_val - R_val * beta_4_val) / (beta_4_val - beta_3_val)
    # Calculate J3
    J_3_val = J_2_val - J_1_val
    
    return J_1_val, J_2_val, J_3_val

# Example calculation with assumed default values
print(calculate_J_values(m_val=0.0396, R_val=0.020, g_val=9.7940, beta_1_val = sum(beta_values1)/len(beta_values1), beta_2_val = sum(beta_values2)/len(beta_values2), beta_3_val = sum(beta_values3)/len(beta_values3), beta_4_val = sum(beta_values4)/len(beta_values4)))

def calculate_J_values2(m_val, R_val, g_val, beta_1_val, beta_2_val, beta_5_val, beta_6_val):
    # Calculate J1
    J_1_val = R_val * m_val * (g_val - R_val * beta_2_val) / (beta_2_val - beta_1_val)
    # Calculate J2
    J_2_val = R_val * m_val * (g_val - R_val * beta_6_val) / (beta_6_val - beta_5_val)
    # Calculate J3
    J_3_val = J_2_val - J_1_val
    
    return J_1_val, J_2_val, J_3_val

print(calculate_J_values2(m_val=0.0396, R_val=0.020, g_val=9.7940, beta_1_val = sum(beta_values1)/len(beta_values1), beta_2_val = sum(beta_values2)/len(beta_values2), beta_5_val = sum(beta_values5)/len(beta_values5), beta_6_val = sum(beta_values6)/len(beta_values6)))
# Define the function to calculate J and the relative error E based on given or default values for R_outer and R_inner.

def calculate_J_and_error(J_3_val, m_val, R_outer_val=0.2388633 / 2, R_inner_val=0.2100167 / 2):
    # Calculate J
    J_val = (m_val / 2) * (R_outer_val**2 + R_inner_val**2)
    
    # Calculate the relative error E
    E_val = ((J_3_val - J_val) / J_val) * 100
    
    return J_val, E_val

# Using the previously calculated J_3 value (assuming it's the correct one from the earlier calculation)
J_3_value_from_previous_calculation = 0.005715011450111824

# Example calculation with default values for R_outer and R_innerf
print(calculate_J_and_error(J_3_value_from_previous_calculation, m_val=0.4215))