def CRR_formula_Binput(S0, K, T, u, d, r):
    """
    CRR_formula_Binput(S0, K, T, u, d, r) = initial price of a binary put option using CRR formula

    CRR formula = (1/(1+r)^T)phi(A;T,q)

    where:
    phi(_;_,_) is a binomial distribution function
    A = minimum number of upmoves for the option to be in the money
    q = risk neutral probability
    S0 = initial asset price
    K = strike pirce
    T = expiry time
    u = up factor
    d = down factor
    r = fixed interest rate

    """

    # check input paramters
    if S0 <= 0.0 or d <= -1 or d >= u or r <= -1:
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
    A = math.floor((np.log(K / (S0 * D**T)) / np.log(U / D)))

    # price of a binary put option
    price = (1 / (R**T)) * binom.cdf(A, T, q)

    return(price)


# input values
S0 = 10
K = 10
u = 1
d = -0.5
r = 0.5
T = 4

answer = round(CRR_formula_Binput(S0, K, T, u, d, r), 2)
print(answer)  # 0.08
