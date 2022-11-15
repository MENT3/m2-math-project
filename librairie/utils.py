import numpy as np
import matplotlib.pyplot as plt

def scatter_with_outliers(x, y, outliers_x=None, outliers_y=None, type="values"):
  plt.scatter(x, y)
  if type == "values":
    plt.scatter(outliers_x, outliers_y, c="r")
  elif type == "htresh":
    plt.axhline(y=outliers_y, color="r")

def corr_mask(shape):
  return np.triu(np.ones(shape)).astype(bool)