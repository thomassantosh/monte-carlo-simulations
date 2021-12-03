"""
Simulation of a five task project. Hard-coded to this specific example.
Task A is first. Task B, C and D all follow Task A and
can be performed concurrently after Task A. Once Task B, C and D are done,
Task E can be done.
Each task has a similar time to complete, with a similar standard deviation.
With any task, you have to guesstimate the most improbable time to complete.
Ignored flexibility for Parkinson's law.
"""

import random
import numpy as np
from scipy.stats import beta

def random_float():
    """Return a random float between 0 and 1"""
    for _ in range(0,1):
        rand_number = random.random()
    return rand_number

def beta_values(random_number=None, a_val=None, b_val=None, min_val=None, max_val=None):
    """Get beta inverse"""
    ppf = beta.ppf(random_number, a=a_val, b=b_val)
    ppf = ppf * (max_val-min_val) + min_val
    return ppf

def task_estimates(iterations=None):
    """Discrete task iteration converted to array"""
    task_iteration_list = []
    for _ in range(iterations):
        r_float = random_float()
        min_val, max_val, a_val, b_val = 24, 90, 2, 4
        beta_value = beta_values(
                random_number=r_float,
                a_val=a_val,
                b_val=b_val,
                min_val=min_val,
                max_val=max_val
                )
        task_iteration_list.append(beta_value)
    return np.array(task_iteration_list, dtype=float)

def combine_arrays(*args):
    """Combines all arrays"""
    complete_array = np.column_stack((args))
    #print(f' Combined array:\n {complete_array}')
    return complete_array

def aggregate_arrays(passed_array=None):
    """Takes an array, and sums it along the vertical axis"""
    summed_array = passed_array.sum(1)
    #print(f' Summed array:\n {summed_array}')
    return summed_array

def max_arrays(passed_array=None):
    """Takes an array, and gets the max by row"""
    max_array = np.max(passed_array, axis=1)
    #print(f' Max array:\n {max_array}')
    return max_array

def main():
    """Main operational flow"""
    number_of_iterations = int ( input("Enter number of iterations (integer): ") )
    percentile_certainty = int ( input("Enter percentile certainty (decimal): ") )

    # Task_a triggered
    task_a = task_estimates(iterations=number_of_iterations)

    # Next three tasks are concurrent, and depend on task_a
    task_b = task_estimates(iterations=number_of_iterations)
    task_c = task_estimates(iterations=number_of_iterations)
    task_d = task_estimates(iterations=number_of_iterations)
    sub_combination = combine_arrays(task_b, task_c, task_d)
    concurrent_tasks = max_arrays(sub_combination)

    # Task E can only be triggered after task_b, task_c and task_d are done
    task_e = task_estimates(iterations=number_of_iterations)

    # Combine them all and sum result
    final_total_array = combine_arrays(task_a, concurrent_tasks, task_e)
    summed_array = aggregate_arrays(final_total_array)
    final_result = round (np.percentile(summed_array, percentile_certainty, axis=0),0)
    print(f' Final percentile result: {final_result}')
    print(f"""
        With {percentile_certainty}% reliability,
        I can achieve the project 
        in {final_result:.0f} hours.
        """)

if __name__ == "__main__":
    main()
