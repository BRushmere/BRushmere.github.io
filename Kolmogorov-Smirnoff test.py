# -*- coding: utf-8 -*-
"""
Created on Thu Sep 20 09:22:30 2018

@author: KIIC
"""

#Compute the Kolmogorov-Smirnov statistic on 2 samples.

#This is a two-sided test for the null hypothesis that 2 independent samples 
#are drawn from the same continuous distribution.


import numpy as np
from scipy import stats
np.random.seed(12345678)  #fix random seed to get the same result
n1 = 200  # size of first sample
n2 = 300  # size of second sample
rvs1 = stats.norm.rvs(size=n1, loc=0., scale=1)
rvs2 = stats.norm.rvs(size=n2, loc=0.5, scale=1.5)
result = stats.ks_2samp(rvs1, rvs2)
print(result)