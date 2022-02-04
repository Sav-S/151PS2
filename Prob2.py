########################################
# Name: Savanna Starks
# Collaborators:
# Estimated time spent (hr):2
########################################

def approximate_pi(n_terms):
    """ Approximates the value of pi using Leibniz's series.

    Inputs:
        n_terms (int): The number of desired terms
    Outputs:
        float: The approximate value of pi
    """
    # Add your code below!
    count = 0
    o = 3.0 #starting odd number
    s = 1.0 #the estimation
    if n_terms - 1 > 0:
        for i in range(n_terms):
            s = s-(((1/o) * (-1)) ** count)
            o += 2
            count = count + 1
    return 4 * s



if __name__ == '__main__':
    # You can alter the below value to test your function with a variety
    # of numeric inputs!
    test_num_terms = 2
    print("Pi is approximately ", approximate_pi(test_num_terms), " using ", test_num_terms, " terms.")
