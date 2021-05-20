import matplotlib.pyplot as plt
import numpy as np
import random
import seaborn as sns
x = input('Please enter the amount of coin flips: ')
x = int(x)
coin = [random.randrange(1, 3) for i in range(x)]
values, frequencies = np.unique(coin, return_counts=True)
title = f'Flipping coin {len(coin):,} Times'
sns.set_style("whitegrid") 
axes = sns.barplot(values, frequencies, palette='bright') 
axes.set_title(title) 
axes.set(xlabel='Coin Value', ylabel='Frequency')  
axes.set_ylim(top=max(frequencies) * 1.10)
for bar, frequency in zip(axes.patches, frequencies):
    text_x = bar.get_x() + bar.get_width() / 2.0  
    text_y = bar.get_height() 
    text = f'{frequency:,}\n{frequency / len(coin):.3%}'
    axes.text(text_x, text_y, text, 
              fontsize=11, ha='center', va='bottom')
plt.show()

# Yes, I get approximately 50% heads and 50% tails.
