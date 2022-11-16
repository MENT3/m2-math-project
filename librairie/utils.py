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

# Lorenz curve
# https://zhiyzuo.github.io/Plot-Lorenz/
def gini(arr):
  sorted_arr = arr.copy()
  sorted_arr = np.sort(sorted_arr)
  n = arr.size
  coef_ = 2. / n
  const_ = (n + 1.) / n
  weighted_sum = sum([(i+1)*yi for i, yi in enumerate(sorted_arr)])
  return coef_*weighted_sum/(sorted_arr.sum()) - const_

def lorenz_curve(X):
  X_lorenz = np.sort(X)
  X_lorenz = X_lorenz.cumsum()/X_lorenz.sum()
  X_lorenz = np.insert(X_lorenz, 0, 0) 

  fig, ax = plt.subplots(figsize=[6, 6])
  # scatter plot of Lorenz curve
  ax.scatter(np.arange(X_lorenz.size)/(X_lorenz.size-1), X_lorenz, marker="x", s=100)
  # line plot of equality
  ax.plot([0, 1], [0, 1], color="k")
  plt.show()