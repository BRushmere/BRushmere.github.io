# -*- coding: utf-8 -*-
"""
Created on Thu Sep 20 09:13:46 2018

@author: KIIC
"""

import numpy as np
import pandas as pd
x = np.linspace(-5, 5, 20)
np.random.seed(1)
# normal distributed noise
y = -5 + 3*x + 4 * np.random.normal(size=x.shape)
# Create a data frame containing all the relevant variables
data = pd.DataFrame({'x': x, 'y': y})

from statsmodels.formula.api import ols
model = ols("y ~ x", data).fit()

print(model.summary())