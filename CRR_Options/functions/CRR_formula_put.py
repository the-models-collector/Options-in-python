def CRR_formula_put(S0, K, T, u, d, r):
    """
    CRR_formula_put(S0, K, T, u, d, r) = initial price of a call option using CRR formula

    CRR formula = S_0*phi(A;T,q')- (K/R^T)*phi(A;T,q)

    where: 
    phi(_;_,_) is a binomial distribution function
    A = minimum number of upmoves for the option to be in the money
    q_dash = q*(U/D)
    q = risk neutral probability
    S0 = initial asset price
    K = strike pirce
    T = expiary time
    u = up
    d = down
    r = fixed interest rate

    """

    # import modules
    import numpy as np
    from scipy.stats import binom

    # check input paramters
    if S0 <= 0.0 or u <= -1 or (d <= -1 or d >= u) or r <= -1:
        print("Invalid input arguments")
        print("Terminating program")
        return(1)

    # check for arbitrage
    if not(d < r < u):
        print("Model contains arbitrage")
        print("Terminating program")
        return(1)

    # import modules
    import math
    import numpy as np
    from scipy.stats import binom

    # crr variables
    U = 1 + u
    D = 1 + d
    R = 1 + r

    # calculating terms: q, q_dash, A
    q = (R - D) / (U - D)
    q_dash = ((R - D) / (U - D)) * (U / R)
    A = math.ceil((np.log(K / (S0 * D**T)) / np.log(U / D)))

    # price of call option
    price = (K / (R**T)) * binom.cdf(A - 1, T, q) - \
        S0 * binom.cdf(A - 1, T, q_dash)

    return(price)


# input values
S0 = 10
K = 10
u = 1
d = -0.5
r = 0.5
T = 4

answer = round(CRR_formula_put(S0, K, T, u, d, r), 2)
print(answer)  # 0.17
