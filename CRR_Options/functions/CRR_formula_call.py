def CRR_formula_call(S0, K, T, u, d, r):
    """
    CRR_formula_call(S0, K, T, u, d, r) = initial price of a call option using CRR formula

    CRR formula = S_0*varphi(A;T,q_dash) - (K/R^T)*varphi(A;T,q)

    where: 
    varphi(_;_,_) is a complementary binomial distribution function
    A = minimum number of upmoves for the option to be in the money
    q_dash = q*(U/D)
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
    A = math.floor((np.log(K / (S0 * D**T)) / np.log(U / D))) + 1

    """ ----------- begin comment -----------
    # calculating A in the following way is incorrect.
    # A = math.ceil((np.log(K / (S0 * D**T)) / np.log(U / D)))
    # to be quite fair, it will work most of the time.
    # except when (np.log(K / (S0 * D**T)) / np.log(U / D)) is an integer
    # example, if (np.log(K / (S0 * D**T)) / np.log(U / D)) = 1 then A = math.ceil(1) = 1
    # however, the true correct value of A = 2
    # the problem is because the function math.ceil(x) yields the smallest integer value greater or equal to x
        ----------- end comment -----------"""

    # price of call option
    price = S0 * (1 - binom.cdf(A - 1, T, q_dash)) - (K /
                                                      (R**T)) * (1 - binom.cdf(A - 1, T, q))

    return(price)


# input values
S0 = 10
K = 10
u = 1
d = -0.5
r = 0.5
T = 4

answer = round(CRR_formula_call(S0, K, T, u, d, r), 2)
print(answer)  # 8.19
