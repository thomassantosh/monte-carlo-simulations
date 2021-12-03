"""Simulation of rolling two dice, and the probability
of getting a 7 on rolling the dice. Since there are six possible
outcomes, i.e. (1,6), (2,5), (3,4), (4,3), (5,2), and (6,1), there
is a probability of 6 outcomes out of a total of 6 * 6 = 36 outcomes.
As we run more simulations (>10k times), it approximates closer to this
probability.
"""
import random

def simulation_cycle(number_of_runs=None):
    """A single simulation run"""
    outcomes = [1,2,3,4,5,6]
    trigger_value = 0

    for _ in range(number_of_runs):
        first_dice = random.sample(outcomes,1)[0]
        second_dice = random.sample(outcomes,1)[0]
        if first_dice + second_dice == 7:
            trigger_value += 1

    result = trigger_value / number_of_runs
    return result

def average(passed_list=None):
    """Calculate the average"""
    return sum(passed_list) / len(passed_list)

def main():
    """Main operational flow"""
    number_of_runs=int(input("Enter the number of runs per simulation cycle (integer): "))
    number_of_sims=int(input("Enter the number of cycles (integer): "))
    estimated_outcome = 6/36

    prob_list = []
    for _ in range(number_of_sims):
        p_val = simulation_cycle(number_of_runs)
        prob_list.append(p_val)

    print(prob_list)
    average_prob = average(prob_list)
    delta_to_estimate = estimated_outcome - average_prob
    print(f"""
    Avg. probability across {number_of_sims} simulations, with {number_of_runs} runs per simulation 
    is {average_prob:.3f}, which is {delta_to_estimate:.3f} off the ESTIMATE of {estimated_outcome:.3f}
    """)

if __name__ == "__main__":
    main()
