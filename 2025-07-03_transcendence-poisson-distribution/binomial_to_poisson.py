import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

def run_binom_demo_1():
    n = 1000
    k = np.arange(0, n)
    p = 0.01
    
    print(k)

    P = stats.binom.pmf(k, n, p)

    plt.plot(k, P, '-bD')
    plt.xlabel(r"$k$")
    plt.ylabel(r"$P(k, n=%i)$" % n)
    plt.title(r"Binomial distribution, P(k,n,p) for n=%i and p=%f" % (n, p))
    plt.show()


def run_transcendence_demo_1():
    # Model

    p = 0.0044 # Trigger chance 0.44% per turn
    n = 1800 # 1800 turns in 1 hour
    hours = 14

    outcomes = np.zeros((hours, n))
    for i in range(hours):
        for j in range(n):
            outcome = stats.bernoulli.rvs(p, size=1)
            print(outcome[0])
            outcomes[i][j] = outcome[0]

    plt.matshow(outcomes)
    plt.show()





