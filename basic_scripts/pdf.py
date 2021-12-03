"""Probability Density function"""
import sys
import random
import matplotlib.pyplot as plt
import numpy as np


def data_generation(
        lower_range=None,
        higher_range=None,
        number_of_variables=None,
        generation_type=None
        ):
    """Data generation method"""
    if generation_type == 'linear':
        x_value = np.linspace(lower_range,higher_range,number_of_variables)
    elif generation_type == 'random':
        x_value = random.choices(range(lower_range,higher_range), k=number_of_variables)
    return x_value

def normal_dist(x_value, mean, std_dev):
    """Manually compute normal distribution"""
    prob_density = (np.pi*std_dev) * np.exp(-0.5*((x_value-mean)/std_dev)**2)
    return prob_density

def plotting_view(x_value, pdf, title):
    """Plotting code"""
    plt.plot(x_value,pdf , color = 'red')
    plt.xlabel('Data points')
    plt.ylabel('Probability Density')
    plt.title(title)
    plt.show()

def main():
    """Main operational flow"""
    lower_range = int( input("Enter the lower range (integer): ") )
    higher_range = int( input("Enter the higher range (integer): ") )
    number_of_variables = int(input("Enter the number of values (integer): "))
    generation_type = sys.argv[1]
    title = 'PDF (' + str(generation_type) + ')'

    x_value = data_generation(lower_range, higher_range, number_of_variables, generation_type)
    mean = np.mean(x_value)
    std_dev = np.std(x_value)
    pdf = normal_dist(x_value, mean, std_dev)
    plotting_view(x_value, pdf, title)


if __name__ == "__main__":
    main()
