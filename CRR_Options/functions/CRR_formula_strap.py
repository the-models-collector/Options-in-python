def CRR_formula_strap(S0, K, T, u, d, r):
    """
    
    CRR_formula_strap(S0, K, T, u, d, r) = initial price of a strap option using CRR formula

    CRR formula = 2 * pi_c + pi_p

    where: 
    pi_c = price of a call option 
    pi_p = price of a put option 
    q = risk neutral probability
    S0 = initial asset price
    K = strike pirce
    T = expiry time
    u = up
    d = down
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
    q_dash = ((R - D) / (U - D)) * (U / R)
    A = math.floor((np.log(K / (S0 * D**T)) / np.log(U / D)))

    # price of put and call of call option
    pi_p = (K / (R**T)) * binom.cdf(A, T, q) - \
        S0 * binom.cdf(A, T, q_dash)
    pi_c = S0 * (1 - binom.cdf(A, T, q_dash)) - (K /
                                                 (R**T)) * (1 - binom.cdf(A, T, q))

    return(pi_p + 2 * pi_c)


# input values
S0 = 10
K = 10
u = 1
d = -0.5
r = 0.5
T = 4

answer = round(CRR_formula_strap(S0, K, T, u, d, r), 2)
print(answer)  # 16.56
