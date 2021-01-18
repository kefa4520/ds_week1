# Lines starting with # are comments and are not run by Python.
"""
Multi-line comments are possible with triple quotes like this.
"""
# import pandas and matplotlib
# Load the pandas library as pd
import pandas as pd
# Load the matplotlib library as plt
import matplotlib.pyplot as plt
# load the numpy library as np (called "aliasing")
import numpy as np 

# This data comes from the UCI ML repository:
# https://archive.ics.uci.edu/ml/datasets/Bike+Sharing+Dataset
# It is the daily number of users from a bike share program
df = pd.read_csv('day.csv')

# shows a preview of the data
df.head()
# shows some basic stats of the data
df.describe()

# Use the examples in the jupyter notebook to help you here.
# calculate the mean and standard deviation of the hourly data counts (the 'cnt' column)
# mean
df['cnt'].mean()
# standard deviation
df['cnt'].std()
# plot the counts ('cnt' column)
df['cnt'].plot()
# Carry out other EDA and analysis if you wish for more practice.
# You can also carry this out in a Jupyter Notebook.