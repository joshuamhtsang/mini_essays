import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

def run_binom_demo_1():
    n = 1000
    k = np.arange(0, n)
    p = 0.01

    P = stats.binom.pmf(k, n, p)

    plt.plot(k, P, '-bD')
    plt.xlabel(r"$k$")
    plt.ylabel(r"$P(k, n=%i)$" % n)
    plt.title(r"Binomial distribution, P(k,n,p) for n=%i and p=%f" % (n, p))
    plt.show()


def run_transcendence_demo_1():
    # Model a certain number of hours of hunting

    p = 0.0044 # Trigger chance 0.44% per turn
    n = 1800 # 1800 turns in 1 hour
    hours = 1000 # Number of hours of hunting

    outcomes = np.zeros((hours, n))
    for i in range(hours):
        print("Simulating hour = ", i)
        for j in range(n):
            outcome = stats.bernoulli.rvs(p, size=1)
            outcomes[i][j] = outcome[0]

    plt.matshow(outcomes)
    plt.show()

    # Compute number of triggers per hour and store in array

    num_triggers = np.zeros(hours)
    for i in range(hours):
        num_triggers[i] = np.sum(outcomes[i, :])
        print(num_triggers)
    
    num_bins = 20
    hist, bin_edges = np.histogram(num_triggers, bins=np.arange(0, num_bins))
    print("hist = ", hist)
    print("bin_edges = ", bin_edges)

    plt.bar(np.arange(0, num_bins-1), hist, width=0.3)
    plt.show()

    # Compute Poisson distribution for mu number of triggers in an hour given p = 0.0044 [https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.poisson.html]

    mu = 1800*p
    k = np.arange(0, n)
    f = stats.poisson.pmf(k, mu)

    print("mu = ", mu, " activations per hour")

    # Plot the modelled data and the theoretical Poisson distribution for mu number of activations per hour
    plt.bar(np.arange(0, num_bins-1), hist/hours, width=0.3)
    plt.plot(k, f, '-rD')
    plt.show()





