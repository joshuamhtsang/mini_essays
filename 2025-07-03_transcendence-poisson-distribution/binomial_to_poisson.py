import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

def run_binom_demo_1():
    n = 1800
    k = np.arange(0, n)
    p = 0.0044

    P = stats.binom.pmf(k, n, p)

    plt.plot(k, P, '-bD')
    plt.xlabel(r"$k$ (num activations)")
    plt.ylabel(r"$P(k, n=%i)$" % n)
    plt.title(r"Binomial distribution, P(k,n,p) for n=%i and p=%f" % (n, p))
    plt.show()


def run_transcendence_demo_1():
    # Model a certain number of hours of hunting

    p = 0.0044 # Trigger chance 0.44% per turn
    n = 1800 # 1800 turns in 1 hour
    hours = 2000 # Number of hours of hunting

    outcomes = np.zeros((hours, n))
    bernoulli_rolls = stats.bernoulli.rvs(p, size=n*hours)

    for i in range(hours):
        for j in range(n):
            outcome = bernoulli_rolls[i*n+j]
            outcomes[i][j] = outcome

    plt.matshow(outcomes)
    plt.xlabel(r"Turn")
    plt.ylabel(r"Hour")
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
    plt.xlabel(r"$\mu$, Procs per hour")
    plt.ylabel(r"Count")
    plt.title(r"Histogram for 'procs per hour' from the experiments")
    plt.show()

    # Compute Poisson distribution for mu number of triggers in an hour given p = 0.0044 [https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.poisson.html]

    mu = 1800*p
    k = np.arange(0, n)
    f = stats.poisson.pmf(k, mu)

    print("mu = ", mu, " activations per hour")

    # Plot the modelled data and the theoretical Poisson distribution for mu number of activations per hour
    plt.bar(np.arange(0, num_bins-1), hist/hours, width=0.3)
    plt.plot(k, f, '-rD')
    plt.xlabel(r"k")
    plt.ylabel(r"f(k)")
    plt.title(r"Comparison of simulated hunting and Poisson distribution for $\mu$ = 7.92")
    plt.show()





