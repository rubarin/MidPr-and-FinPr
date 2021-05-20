import matplotlib.pyplot as plt
import numpy as np
import random
import seaborn as sns
coin = [random.randrange(1, 3) for i in range(600)]
values, frequencies = np.unique(coin, return_counts=True)
title = f'Flipping a coin {len(coin):,} Times'
sns.set_style("whitegrid") 
axes = sns.barplot(values, frequencies, palette='bright') 
axes.set_title(title) 
axes.set(xlabel='Coin Value', ylabel='Frequency')  
axes.set_ylim(top=max(frequencies) * 1.10)

plt.show()
