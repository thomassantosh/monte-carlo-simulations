"""Simulate the chances of getting 5 heads in a row"""
import random
from collections import Counter

def simulation_run(number_of_trials_per_sim=None):
    """A single simulation run"""
    count_of_heads = []
    for _ in range(number_of_trials_per_sim):
        a_value = 0
        for _ in range(5):
            b_value = random.randint(0,1)
            #print(f'value of b_value: {b_value}')
            a_value = a_value + b_value
        count_of_heads.append(a_value)
    tally = Counter(count_of_heads)
    prob = tally[5]/ number_of_trials_per_sim
    #print(tally)
    #print(f'Probability of 5 heads in a row is {tally[5]/1000}')
    return prob

def average(passed_list=None):
    """Calculate the average"""
    return sum(passed_list) / len(passed_list)

def main():
    """Main operational flow"""
    number_of_trials_per_sim=int(input("Enter the number of trials per simulation (integer): "))
    number_of_sims=int(input("Enter the number of simulations (integer): "))

    prob_list = []
    for _ in range(number_of_sims):
        p_val = simulation_run(number_of_trials_per_sim)
        prob_list.append(p_val)

    print(prob_list)
    print(f' Average probability is {average(prob_list)}')

if __name__ == "__main__":
    main()
