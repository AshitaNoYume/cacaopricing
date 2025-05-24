import xgboost as xg
import yfinance as yf
import matplotlib as mpl
import arch as a
import sys
import numpy as np
import math

cacao_data = yf.download("CC=F", start="2020-01-01", end="2025-05-20")