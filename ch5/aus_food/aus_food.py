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

# Problem Introduction
# The csv file aus_food.csv contains records of total monthly expenditure on
# cafes, restaurants and takeaway food services in Australia ($billion) from
# 2004 through 2016. (Hyndman, R.J., & Athanasopoulos, G. (2018)
# Forecasting: principles and practice, 2nd edition,
# OTexts: Melbourne, Australia. OTexts.com/fpp2. Accessed on July 22, 2019.)

# The file contains two variables: `expenditure` is the monthly expenditure
# on food services, and `time` encodes the year and month. For example,
# January 2004 is coded as 2004, and February 2004 is encoded as 2004.0833...
# since 1/12 is about 0.083.
# In this example we will build a model to forecast monthly food expenditures.

# 1. Read the data in.  Make a plot that has food expenditures on the vertical
# axis and time on the horizontal axis.
aus_food = pd.read_csv("aus_food.csv")
plt.plot(aus_food['time'], aus_food['expenditure'])

# 2. Your plot in part 1 showed an increasing trend in food expenditures over
# time, with fairly consistent seasonal patterns (for instance, there is a
# regular peak in food expenditures in December of each year).  Let's use a
# model for food expenditures that has a linear function of time to capture
# the long-term increasing trend, and sine and cosine terms to capture
# seasonality around that trend. Specifically, if we use y_t to denote food
# expenditures at time t, we have:
# y_t \approx \alpha_0 + \alpha_1 t + \sum_{k = 1}^K \{\gamma_{k} sin(2 \pi k / 12) + \gamma^*_{k} cos(2 \pi k / 12) \}
# We can express this model in matrix form as y \approx X \beta, where
# y = \begin{bmatrix} y_1 \\ \vdots \\ y_t
