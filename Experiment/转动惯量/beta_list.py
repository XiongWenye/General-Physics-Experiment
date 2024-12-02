import math
import csv

# Read the data from the file beta_values.csv. This file contains 6 sets of beta values: beta1, beta2, beta3, beta4, beta5, beta6
# Separate the data into a list of lists
with open('Experiment/转动惯量/beta_values.csv', 'r') as file:
    reader = csv.reader(file)
    beta_values = [list(map(float, row)) for row in reader]

#calculate the mean, sum_squared_diff, std_dev, mean_std_dev, delta_A, delta_B, uncertainty_U of each set of beta values
#Output the results for each set of beta into a same csv file at folder Experiment/转动惯量
for i, beta_value in enumerate(beta_values):
    mean = sum(beta_value) / len(beta_value)
    sum_squared_diff = sum((x - mean) ** 2 for x in beta_value)
    std_dev = math.sqrt(sum_squared_diff / (len(beta_value) - 1))
    mean_std_dev = std_dev / math.sqrt(len(beta_value))
    delta_A = 2.57 * mean_std_dev
    delta_B = 0.95 * 0.01
    uncertainty_U = math.sqrt(delta_A ** 2 + delta_B ** 2)

    with open('Experiment/转动惯量/beta_values_analysis.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([f"Beta {i+1}: {beta_value}"])
        writer.writerow([f"Mean: {mean}"])
        writer.writerow([f"Standard deviation of the 6 measurements: {std_dev}"])
        writer.writerow([f"Standard deviation of the mean: {mean_std_dev}"])
        writer.writerow([f"ΔA = {delta_A}, ΔB = {delta_B}"])
        writer.writerow([f"Uncertainty U = {uncertainty_U}"])
        writer.writerow([f"Beta {i+1} = {mean} ± {uncertainty_U}"])