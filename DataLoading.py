# © Ashok-777
# GitHub: https://github.com/Ashok-777
# Part 1/4: Setup & Data Loading

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_absolute_error as mae
from xgboost import XGBRegressor
from sklearn.linear_model import LinearRegression, Lasso, Ridge
from datetime import datetime, timedelta
import holidays
import warnings

warnings.filterwarnings('ignore')

# Load dataset
df = pd.read_csv("../data/StoreDemand.csv")

# Inspect the data
print("Head of dataset:")
print(df.head())

print("\nTail of dataset:")
print(df.tail())

print("\nDataset Shape:", df.shape)

print("\nDataset Info:")
df.info()

print("\nSummary Statistics:")
print(df.describe())
# © Ashok-777
# GitHub: https://github.com/Ashok-777
