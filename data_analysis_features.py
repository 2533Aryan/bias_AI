'''
According to type distributions analysis, majority of people have dogs. 

The initial error: 
The dataset employed did not have the same distributions as the real world.
Data was unintentionally sampled from a dog-biased collection.

However, that analysis does not explain why the model is biased against cats.
Cats and dogs may both be energetic, cuddly, quiet, and soft (these features are common by both pets).

This program will plot: how frequently each feature occurs for both pets by dividing 
the number of times each feature occurs for each animal by the total number of survey responses for each pet.
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


# Split the survey up into the cat and dog entries
dog_survey = survey[:-4]   # Dog entries
cat_survey = survey[-4:]   # Cat entries



# Plotting
fig, ax = plt.subplots(1, 1, figsize=(10,5))    # subplotting
ind = np.arange(0, 4)                           # ind = [0,1,2]


# Count number of dog and cat surveys
total_dog = dog_survey.shape[0]
total_cat = cat_survey.shape[0]


# Divide the number of dogs and cats we have by the number of times each feature is true
cat_probabilities = 100*cat_survey[:,:4].sum(axis=0)/total_cat
dog_probabilities = 100*dog_survey[:,:4].sum(axis=0)/total_dog


# Input the data into a bar plot
data = {'Feature':[], 'Animal':[], 'Probability':[]}

for feature in range(4):
  data['Feature'].append(feature)
  data['Animal'].append('dog')
  data['Probability'].append(dog_probabilities[feature])

  data['Feature'].append(feature)
  data['Animal'].append('cat')
  data['Probability'].append(cat_probabilities[feature])
df = pd.DataFrame(data=data)


_ = sns.barplot(x='Feature', y='Probability', hue='Animal', data=df, ax=ax)


# Put labels
ax.set_xticklabels(['Energetic', 'Cuddly', 'Soft', 'Quiet'])
ax.tick_params(axis = 'both', which = 'major', labelsize = 18)
_ = fig.suptitle('Pet features', fontsize=18)
_ = plt.ylabel('Probability', fontsize=18)
_ = ax.set_ylim([0, 100])     # Y-axis limit
_ = plt.xlabel('', fontsize=18)
_ = plt.legend(loc='best', prop={'size':18})


# Save the plot
fig.savefig('Analysis Plots/[PLOT_3]features_distribution.png')


# Actually show the plot
plt.show()
