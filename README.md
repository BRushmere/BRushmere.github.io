# Project Python & Finance

This is my very **work-in-progress** Github page to upload python files applicable to analysing financial markets and stocks.

![Name](IMG-20191130-WA00012.jpeg)

```
{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "\n",
    "def Bernoulli(p):\n",
    "    \n",
    "        if p<np.random.rand():\n",
    "            return 1\n",
    "        else:\n",
    "            return 0\n",
    "  \n",
    "print(Bernoulli(0.4))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
```

## Technical Analysis
**Trend**

  - Moving averages
  - MACD
  
**Momentum**

  - RSI
  
**Volatility**

  - [Bollinger Band](https://github.com/BRushmere/Finance-Models/blob/master/Bollinger_band.ipynb)

**Volume**
  
## Statistics

**Discrete distributions**

- [Bernoulli trial](https://github.com/BRushmere/BRushmere.github.io/blob/master/Bernoulli_trial.ipynb)
- [Binomial](https://github.com/BRushmere/BRushmere.github.io/blob/master/Binomial.py)
- Poisson
- Hyper Geometric

**Continuous distributions**

- [Normal distribution](https://github.com/BRushmere/BRushmere.github.io/blob/master/Normal_distribution.ipynb)
- [Chi-Squared](https://github.com/BRushmere/BRushmere.github.io/blob/master/ChiSquared.ipynb)
- Log-Normal distribution
- Exponential distribution

**Tests**

- Parametric
  - Pearson correlation
  - Two sample (Student) 𝑡-test: compare two means
  - [Skewness & Kurtosis test](https://github.com/BRushmere/BRushmere.github.io/blob/master/Skewness%20%26%20Kurtosis.ipynb)
- Non-parametric
  - Spearman-rank order
  - Wilcoxon signed rank
  - Mann-whitney U-test

**Regression Models**

- [Single Linear](https://github.com/BRushmere/BRushmere.github.io/blob/master/Simple%20Regression%20Model.py)
- [Single Linear (pandas)](https://github.com/BRushmere/BRushmere.github.io/blob/master/LinRegression%20Pandas.py)
- [Mulitple Linear(pandas)](https://github.com/BRushmere/BRushmere.github.io/blob/master/Multiple%20linear%20regression(pandas).ipynb)

**Goodness of Fit Tests**

- Chi^2 Goodness of Fit 
- [Kolmogorov-Smirnoff test](https://github.com/BRushmere/BRushmere.github.io/blob/master/Kolmogorov-Smirnoff%20test.py)

**Time Series**

- [Random walk](https://github.com/BRushmere/BRushmere.github.io/blob/master/Random%20walk.ipynb)
- Drift diffusion
- AR(p)
- MA(q)
- ARMA(p,q)
- GARCH
- Jump-diffusion

**Interest Rate Models**
- Cox-Ingersol model

[Monte-Carlo simulation](https://github.com/BRushmere/BRushmere.github.io/blob/master/MonteCarlo.ipynb)

[Black-Scholes-Merton Model](https://github.com/BRushmere/BRushmere.github.io/blob/master/BSM_call.py)

**Sampling**
- Stratified sampling
- Clustered random sampling

**Estimation**

[Central limit theorem](https://github.com/BRushmere/BRushmere.github.io/blob/master/Central%20limit%20theorem.ipynb)

## Portfolio management
- [Portfolio expected return, variance and covariance](https://github.com/BRushmere/BRushmere.github.io/blob/master/Std%26Variance%26%20Covariance.ipynb)

## Backtesting
- [Bollinger band backtesting strategy](https://github.com/BRushmere/BRushmere.github.io/blob/master/Bollinger%20band%20backtest.ipynb)

## Machine learning
- Supervised
  - Penealized Regression
  - KNN Classification
  - Decision Trees (CART)
  - Neural Networks
- Unsupervised
  - Clustering Algorithms
  - Dimension Reduction
