import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot([0, 1, 2, 3, 4, 5], hist=False)

plt.show()

from numpy import random

# x = random.normal(loc=1, scale=2, size=(2, 3))
#
# print(x)

sns.distplot(random.normal(size=1000), hist=False)

plt.show()
