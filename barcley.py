# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 12:40:01 2023

@author: SANA
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
bcs = pd.read_csv('BCS_ann.csv')
bp = pd.read_csv('BP_ann.csv')
tsco = pd.read_csv('TSCO_ann.csv')
vod = pd.read_csv("VOD_ann.csv")
plt.figure()
plt.hist(bcs["ann_return"],label="barclays")
plt.legend()
plt.xlabel("return (%)")
plt.ylabel("N")
plt.show()