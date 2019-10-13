def call_price(S0, K, T, u, d, r):
    """
    put_price(S0, K, T, u, d, r) = price of a put option in CRR method

    S0 = initial asset price
    K = strike pirce
    T = expiary time
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

    # calculating terminal asset prices
    ST = []
    for i in range(0, T + 1):
        ST.append(S0 * ((u + 1)**(T - i)) * ((d + 1)**i))

    # calculating terminal payoff of put option
    price = []
    for i in ST:
        price.append(max((i - K), 0))

    # calculating risk neutral probabilities
    q = (r - d) / (u - d)

    # backward induction
    for i in range(T - 1, -1, -1):
        for j in range(0, len(price) - 1):
            price[j] = ((q * price[j]) + (1 - q) * price[j + 1]) / (1 + r)
        price.pop()

    return(price)


# input values
S0 = 10
K = 10
u = 1
d = -0.5
r = 0.5
T = 4

call_price(S0, K, T, u, d, r)
answer = round(call_price(S0, K, T, u, d, r)[0], 2)
print(answer)


