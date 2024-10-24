# Bayesian Inference

## Resources

"rasmusab" YouTube 3-part video series - uses the Swedish Fish Company example o illustrate use of Binomial model:

[https://youtu.be/3OJEae7Qb_o?si=1y_0JCztA1GV0R1W]

"Brandon Rohrer" YouTube - uses example of weighing his dog "Reign":

[https://youtu.be/5NMxiOGL39M?si=AyE4OJNZUnTtqWrz]

[https://www.quantstart.com/articles/Bayesian-Statistics-A-Beginners-Guide/]


## Foundational Concepts

There are several distinguishing features of Bayesian Inference compared to classical statistical analysis.  Here are a few features:

- **Prior, Generative Model + Parameter(s), Data**:
  In the Baysian approach to statistics, one follows a recipe that composes of a 3 main things: the prior, the generative model with associated parameter(s) and the data itself.  
  
  The prior, $P(\theta)$, provides a mechanism to incorporate our initial beliefs about how the value of the parameter is distributed. 

  A generative model and its associated parameter(s) must be selected before an analysis can commence. An example of a model is the Binomial distribution with its parameter $p$ which determines the probability of a positive result (e.g. a head in a coin flip).  As such, a Bayesian analysis will involve determining the likely distribution of $p$ given the observed data $D$ i.e. $P(\theta = p|D)$.

  In most real-life problems, the data, $D$, is collected and available from the outset.  However, once a Bayesian analysis is completed, it can inform the practitioner what further data might be needed to get a more certain result e.g. how to get a better estimate of the true value of $\theta$.

- **Calculates the likely distribution of the model parameter(s), $P(\theta|D)$:**
  In a classical statistical analysis, one might compute the mean, $\mu$, standard deviation, $\sigma$, and the confidence intervals from the data $D$.  This yields just a *single* value for the $\mu$, $\sigma$ etc. from $D$.  In contrast, a Baysian analysis yields the probablistic distribution of the generative model's parameters $\theta$ i.e. $P(\theta|D)$, which in the case of a Normal distribution are $\theta = \{\mu, \sigma\}$.  This will be drawn out in the example(s) below.

## Bayes Theorem for Inference

Bayes Theorem for inference is conventionally written as follows:

$$P(\theta | D) = \frac{P(D | \theta ) P(\theta)}{P(D)}$$

where $\theta$ are the parameters of a probability distribution and $D$ is the data we have.  In the language of Bayes Theorem, each of the terms in the above formula have the names:

$$ {\tt Posterior} = \frac{ {\tt Likelihood} \times {\tt Prior} }{ {\tt Margin} } $$


## Inferring the Parameters of a Probability Distribution


### An example of weighing Nessie the Dog

$$ f(x) = \frac{1}{\sqrt{2 \pi \sigma^2}} \exp \left( -\frac{(x-\mu)^2}{2\sigma ^2} \right) $$

$$ \theta = \{ \mu, \sigma \} $$

$$ P(D | \theta) = P(w_1 = 14.0 | \{ \mu = 16.0, \sigma=2.0 \}) \\ \times P(w_1 = 15.5 | \{ \mu = 16.0, \sigma=2.0 \}) \\ \times P(w_1 = 17.9 | \{ \mu = 16.0, \sigma=2.0 \}) $$

