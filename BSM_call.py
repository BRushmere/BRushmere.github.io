# Black-Merton- Scholes Option model 
#on non-dividend paying stocks

import scipy as sc
import scipy.stats as sts
def bms_call(S,X,T,r,sigma):
    d1 = (sc.log(S/X)+(r+sigma*sigma/2)*T)/(sigma*sc.sqrt(T))
    d2 =d1 - sigma*sc.sqrt(T)
    return S*sts.norm.cdf(d1)-X*sc.exp(-r*T)*sts.norm.cdf(d2)

c = bms_call(40,42,0.5,0.015,0.2)
print(c)