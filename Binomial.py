# -*- coding: utf-8 -*-

from math import factorial as fac

def manual_pmf(p, n, k):
    return fac(n) / (fac(k) * fac(n - k)) * p**k * (1-p)**(n-k)

print(manual_pmf(p=0.25, n=3, k=2))