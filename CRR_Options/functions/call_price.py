def call_price(S0, K, T, u, d, r):
    """
    call_price(S0, K, T, u, d, r) = initial price of a call option using put-call parity

    S0 = initial asset price
    K = strike pirce
    T = expiry time
    u = up
    d = down
    r = fixed interest rate
    """

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

    import crr_put

    # put price rounded to 2 decimal places
    put_price = round(crr_put.put_price(S0, K, T, u, d, r),2)

    return S0 - K/((1+r)**T) + put_price

# input values
S0 = 10
K = 10
u = 1
d = -0.5
r = 0.5
T = 4

# answer = round(call_price(S0, K, T, u, d, r),2)
# print(answer) # 8.19
