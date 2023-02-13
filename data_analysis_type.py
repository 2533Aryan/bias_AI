'''
According to happy distributions analysis, 100 % cat owners are happy.
However, when we put the features for a cat, our AI frequently indicates that it will not make the owner happy. 
What's the problem?

Consider another dimension of our data and plot the total number of survey responses from dog and cat owners.
'''


# Importing all the data from bias_input_data file
from bias_input_data import *

# Import matplotlib: plotting library
import matplotlib.pyplot as plt


# Split the survey up into the cat and dog entries
dog_survey = survey[:-4]   # Dog entries
cat_survey = survey[-4:]   # Cat entries


# Plotting
fig, ax = plt.subplots()
ind = np.arange(1, 3)      # ind = [1,2]


# Count the number of dog vs cat owners 
dog = dog_survey.shape[0]
cat = cat_survey.shape[0]


# Make a bar chart
pd, pc = plt.bar(ind, (dog, cat))


# Assign colors to bars
pd.set_facecolor('r')
pc.set_facecolor('g')


# Put labels
ax.set_xticks(ind)
ax.set_xticklabels(['# Dog', '# Cat'])
ax.set_ylim([0, 25])     # Y-axis limit
ax.set_ylabel('Number')
_ = ax.set_title('Pet Type')


# Save the plot
fig.savefig('Analysis Plots/[PLOT_2]number_distribution.png')


# Actually show the plot
plt.show()
