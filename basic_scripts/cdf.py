"""Probability function"""
from scipy.stats import norm

# Finding the probability of a discrete value
def prob_norm_single_value(discrete_value=None, mean=None,stdev=None):
    """Probability function for a discrete value"""
    x_value = norm(loc = mean, scale= stdev).cdf(discrete_value)
    return x_value

# Finding the probability between two ranges
def prob_norm_between_values(lower_val=None, upper_val=None, mean=None,stdev=None):
    """Probability between two values"""
    l_value = norm(loc = mean, scale= stdev).cdf(lower_val)
    u_value = norm(loc = mean, scale= stdev).cdf(upper_val)
    delta = u_value - l_value
    return delta

# Finding the probability above a discrete value
def prob_norm_above_value(discrete_value=None, mean=None,stdev=None):
    """Probability above a discrete value"""
    x_value = norm(loc = mean, scale= stdev).cdf(discrete_value)
    delta = 1 - x_value
    return delta

def main():
    """Main logic flow"""
    func_type = input ('Enter the function type (single/range/above): ')
    lower_val = float ( input("Enter the single or lower range (value): ") )
    if func_type == 'range':
        upper_val = float ( input("Enter the upper range (value): ") )
    mean = float ( input("Enter the mean (value): ") )
    stdev = float ( input("Enter the standard deviation (value): ") )
    if func_type == 'range':
        return_value = prob_norm_between_values(
                lower_val=lower_val,
                upper_val=upper_val,
                mean=mean,
                stdev=stdev
                )
        print(f'Probability between {lower_val} and {upper_val} is: {return_value}')
    elif func_type == 'above':
        return_value = prob_norm_above_value(
                discrete_value=lower_val,
                mean=mean,
                stdev=stdev
                )
        print(f'Probability above {lower_val} is: {return_value}')
    else:
        return_value = prob_norm_single_value(
                discrete_value=lower_val,
                mean=mean,
                stdev=stdev
                )
        print(f'Probability of {lower_val} is: {return_value}')


if __name__ == "__main__":
    main()
