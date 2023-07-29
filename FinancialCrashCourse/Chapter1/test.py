import numpy as n

""" European Option Valuation """

S0 = 100
k = 105
t = 1
r = 0.05
sigma = 0.2

I = 100000

# Valuation Algorithm
z = n.random.standard_normal(I)
ST = S0 * n.exp((r - 0.5 * sigma ** 2) * t + sigma * n.sqrt(t) * z)

# Index Values at maturity 
hT = n.maximum(ST - k, 0)
C0 = n.exp(-r * t) * sum(hT) / I

print("Value of the European Call Option {}".format(C0))