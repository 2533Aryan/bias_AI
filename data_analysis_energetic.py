'''
There appear to be many distinct types of dogs in our dataset, but none of the cats appear to be energetic.
This is a correlated feature, which is one that is (unintentionally) correlated to an specific prediction or hidden category.
Understanding if something is energetic is a cheat for knowing it's a dog in this situation,
even if we didn't tell the model about dogs.

Because there was no data to tell it differently, my model may have learnt that if a pet is energetic, it makes owners happy.
By plotting energetic vs owner happiness, we can discover if this weird correlation is true.
'''

# Importing all the data from bias_input_data file
from bias_input_data import *

'''
Import libraries to generate a plot
'''

# Import matplotlib: plotting library
import matplotlib.pyplot as plt
# Import seaborn: data visualization library based on matplotlib
import seaborn as sns
# Import pandas:  data manipulation and analysis
import pandas as pd


# Plotting
fig, ax = plt.subplots(1, 1, figsize=(10,5))    # subplotting
ind = np.arange(0, 4)                           # ind = [0,1,2]


# Count how often each animal is relaxed or energetic
energetic = [0,0]
energetic_count = 0
relaxed = [0,0]
relaxed_count = 0

for entry in survey:
  if entry[0] == 0:
    relaxed[entry[-1]] += 1
    relaxed_count += 1
  else:
    energetic[entry[-1]] += 1
    energetic_count += 1

# Put the values in a a database
data = {'Feature':[], 'Happy':[], 'Probability':[]}
data["Feature"].append("Energetic")
data["Happy"].append("No")
data["Probability"].append(100*energetic[0]/energetic_count)

data["Feature"].append("Energetic")
data["Happy"].append("Yes")
data["Probability"].append(100*energetic[1]/energetic_count)

data["Feature"].append("walk")
data["Happy"].append("No")
data["Probability"].append(100*relaxed[0]/relaxed_count)

data["Feature"].append("walk")
data["Happy"].append("Yes")
data["Probability"].append(100*relaxed[1]/relaxed_count)

df = pd.DataFrame(data=data)

# Plot bar plot and put labels on everything
_ = sns.barplot(x='Feature', y='Probability', hue='Happy', data=df, ax=ax)
ax.set_xticklabels(['Energetic', 'Relaxed'])
ax.tick_params(axis = 'both', which = 'major', labelsize = 18)
_ = fig.suptitle('What makes people happy?', fontsize=18)
_ = plt.ylabel('Probability', fontsize=18)
_ = ax.set_ylim([0, 100])     # Y-axis limit
_ = plt.xlabel('', fontsize=18)
_ = plt.legend(loc='best', prop={'size':18})


# Save the plot
fig.savefig('Analysis Plots/[PLOT_4]energetic_distribution.png')

# Actually show the plot
plt.show()