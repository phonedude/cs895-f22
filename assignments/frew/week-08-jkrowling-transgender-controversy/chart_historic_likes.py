# chart_historic_likes.py
#   Input: a CSV file representing historic tweet likes
#   Output: a plot of the data
# Lesley Frew
# October 10, 2022

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
sns.set_style("whitegrid");

#Read the data
timemaps = pd.read_csv('out3merge.csv')
timemaps['memento-datetime'] = pd.to_datetime(timemaps['memento-datetime'], format = '%Y-%m-%d')
timemaps.sort_values(by=['memento-datetime'], ascending=True, inplace=True)

#Set up the plot
plt.figure(figsize=(9,9))
ax = sns.scatterplot(x="memento-datetime", y="likes", data=timemaps, s=10, linewidth=0)
ax.set_xlabel ('Memento-datetime')
ax.set_ylabel ('Likes')
ax.set_title('Historic likes for J.K. Rowling\'s tweet about Maya')

#Adjust the ticks and grid lines
ax.set_ylim(bottom=0) 
ticks = ax.get_yticks()
labels = ['{:,.0f}'.format(y) for y in ticks]
ax.set_yticklabels(labels); 
ax.grid(linestyle='dotted')
plt.xticks(rotation=45)

#Show the plot
plt.show()