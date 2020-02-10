#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 29 11:56:02 2019

@author: alfaceor
"""

import IgorModel
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
pd_pgen = pd.read_csv("../tests/ReDoTRbeta/NewTRbeta_output/Pgen_counts.csv", delimiter=';', index_col=0)
#pgen_data = np.loadtxt("ReDoTRbeta/NewTRbeta_output/Pgen_counts.csv", delimiter=';', skiprows=1)

pd_pgen.sort_index().dropna()
fig, ax = plt.subplots( figsize=(8,6))




pgen = pd_pgen.dropna()['Pgen_estimate'].values
counts, bins = np.histogram(pgen, bins=np.logspace(-30,-1,100))
binsX = 0.5*(bins[:1] + bins[:-1])
histo = counts/float(counts.sum())
ax.set_xscale("log")
ax.set_xlabel("$Pgen$")
ax.set_ylabel("Density")
ax.plot(binsX, histo, marker='o')

fig.tight_layout()


#
#pd_pgen.loc[0]
#pd_pgen.loc[99995]
#
#np.linspace()
#3.49*log10_pgen.std()*len(log10_pgen)**(-0.3333)
#print(log10_pgen.min(), log10_pgen.max() )
