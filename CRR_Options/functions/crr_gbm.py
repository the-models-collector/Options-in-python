# n_th crr approximation of a geometric brownian motion

# -------
import numpy
import random
# -------

# ------- geometric brownian motion

# time parameters
t = 0  # start time
T = 10  # end time
n1 = 1000  # number of time steps between t and T

# model parameters
S0 = 10  # initial stock price
r = 0.15  # interest rate
sigma = 0.1  # volatility

# model initialisation
w = 0  # initial position of brownian motion
bm = [w]  # brownian motion vector
gm_bm = [S0]  #  stock prices vector

for i in numpy.linspace(0, T, n1 + 1):
    if i == 0:
        continue

    w = w + ((T / n1) ** 0.5) * numpy.random.standard_normal()
    bm.append(w)
    gm_bm.append(S0 * numpy.exp((r - 0.5 * sigma**0.5) * i + sigma * w))

# -------

# ------- n_th crr model

# time parameters
n0 = 10  # number of time steps in n_th crr between t and T
delta_t = T / n0  # change in time

# random walk paramters
step_size = delta_t**0.5  # step size in n_th crr model
rw = 0  # initial position of random walk
rw_vector = [rw]  # random walk vector

# modle initialisation
n_crr = [S0]  # stock prices vector

for i in numpy.linspace(0, T, n0 + 1):
    if i == 0:
        continue

    z = random.choice([step_size, -step_size])
    rw = rw + z
    s_crr = S0 * numpy.exp((r - 0.5 * sigma**0.5) * i +
                           sigma * rw)
    rw_vector.append(rw)
    n_crr.append(s_crr)

# -------

# ------- plots

import matplotlib.pyplot as plt
plt.plot(list(numpy.linspace(0, T, n1 + 1)),
         gm_bm,  color="blue", linewidth=0.8)

plt.plot(list(numpy.linspace(0, T, n0 + 1)),
         n_crr, color="green", linewidth=0.8, marker=".")
plt.axvline(x=0, linewidth=0.8, color="black", linestyle='dashed')
plt.axhline(y=10, linewidth=0.8, color="black", linestyle='dashed')
plt.xlabel("time")
plt.ylabel("stock price")
plt.savefig("crr_gbm")
plt.show()

# -------

# ------- end
