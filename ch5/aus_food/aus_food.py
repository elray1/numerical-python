#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 11:50:59 2019

@author: eray
"""

import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy.linalg as la

# 1.
aus_food = pd.read_csv("aus_food.csv")
plt.plot(aus_food['time'], aus_food['expenditure'])

# 2.
t_vals = aus_food['time'].values
t_vals = t_vals[t_vals < 2016]

X = np.empty((len(t_vals), 14))

X[:, 0] = 1.0
X[:, 1] = t_vals

for k in range(6):
   X[:, 2 * (k + 1)] = np.sin(2 * np.pi * (k + 1) / 1 * t_vals)
   X[:, 2 * (k + 1) + 1] = np.cos(2 * np.pi * (k + 1) / 1 * t_vals)

fig, ax = plt.subplots()
ax.plot(t_vals, X[:, 2], color = "red", label = "line 1")
ax.plot(t_vals, X[:, 3], color = "red", label = "line 1")
ax.plot(t_vals, X[:, 4], color = "blue", label = "line 1")
ax.plot(t_vals, X[:, 5], color = "blue", label = "line 1")

# 3.
y = aus_food['expenditure'].values[range(len(t_vals))]
sol, r, rank, sv = la.lstsq(X, y)

# 4.
t_vals_new = aus_food['time'].values
t_vals_new = t_vals_new[t_vals_new >= 2016]

X_new = np.empty((len(t_vals_new), 14))

X_new[:, 0] = 1.0
X_new[:, 1] = t_vals_new

for k in range(6):
   X_new[:, 2 * (k + 1)] = np.sin(2 * np.pi * (k + 1) / 1 * t_vals_new)
   X_new[:, 2 * (k + 1) + 1] = np.cos(2 * np.pi * (k + 1) / 1 * t_vals_new)

# 5.
y_hat_new = np.matmul(X_new, sol)

# 6.
y_obs = aus_food['expenditure'].values[range(len(t_vals))]

fig, ax = plt.subplots()
ax.plot(aus_food['time'], aus_food['expenditure'], label = "Observed Expenditure")
ax.plot(t_vals_new, y_hat_new, color = "orange", ls = "dashed", label = "Predicted Expenditure")

