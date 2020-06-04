#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from numba import vectorize, float64, int64

#%% Smoothing
temper = 0.1
cold= 1/temper

@vectorize([float64(float64), float64(int64)], nopython= True)
def pos(x):
    return x if x>0 else 0

@vectorize([float64(float64), float64(int64)], nopython= True)
def derPos(x):
    return 1 if x>0 else 0

@vectorize([float64(int64), float64(float64)], nopython= True)
def smPos(x):
    if x<=-temper/2:
        res = 0
    elif x<=temper/2:
        res = 0.5/temper*(x+0.5*temper)**2
    else: res = x
    return res
    # return temper*np.logaddexp(0,cold*x)

@vectorize([float64(int64), float64(float64)], nopython= True)
def derSmPos(x):
    if x<=-temper/2:
        res = 0
    elif x<=temper/2:
        res = x/temper + 0.5
    else: res = 1
    return res

@vectorize([float64(int64), float64(float64)], nopython= True)
def smAbs(x):
    return smPos(x) + smPos(-x)
    # return smPos2(x) + smPos2(-x)


@vectorize([float64(int64), float64(float64)], nopython= True)
def derSmAbs(x):
    return derSmPos(x) - derSmPos(-x)

#%% Plotting the proxies
    

# from matplotlib import pyplot as plt
# vec =  np.linspace(-2e-1,2e-1,101)

# fig = plt.figure()
# plt.plot(vec, pos(vec), '--')
# plt.plot(vec, smPos(vec))
# plt.legend(["positive part", "smooth proxy"])
# plt.ticklabel_format(useMathText= True, useOffset= True)
# plt.grid('on')
# plt.savefig("pos_proxy.pdf", format = "pdf", bbox_inches='tight')

# #%
# fig = plt.figure()
# plt.plot(vec, np.abs(vec), '--')
# plt.plot(vec, smAbs(vec))
# plt.legend(["absolute value", "smooth proxy"])
# plt.grid('on')
# plt.savefig("abs_proxy.pdf", format = "pdf", bbox_inches='tight')
