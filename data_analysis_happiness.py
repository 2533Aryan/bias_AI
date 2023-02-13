'''
Despite AI's higher performance, its predictions are irrational - There appears to be a preference for dogs.

We gathered survey data and built the AI - It must be our mistake that the AI has an anti-cat bias.
We can analyze our AI to figure out what it is.

This program will plot the percentage of dog owners who are happy, the percentage of cat owners who are happy, 
and the percentage of all people surveyed who are happy with their pets.
'''


# Importing all the data from bias_input_data file
from bias_input_data import *

# Import matplotlib: plotting library
import matplotlib.pyplot as plt



'''
Previously, we decided to combine all of the survey results, but now we'll separate them. 
'''
# Split the survey up into the cat and dog entries
dog_survey = survey[:-4]   # Dog entries
cat_survey = survey[-4:]   # Cat entries



# Plotting
fig, ax = plt.subplots()
ind = np.arange(1, 4)      # ind = [1,2,3]


# Add up the number of survey participants who are happy and
# divide by the total number of participants of each type
happy_dog = 100*np.sum(dog_survey,axis=0)[-1]/dog_survey.shape[0]
happy_cat = 100*np.sum(cat_survey,axis=0)[-1]/cat_survey.shape[0]
happy = 100*np.sum(survey, axis=0)[-1]/survey.shape[0]


# Make a bar chart
pt, pd, pc = plt.bar(ind, (happy, happy_dog, happy_cat))


# Assign colors to bars
pt.set_facecolor('b')  # Blue
pd.set_facecolor('r')  # Red
pc.set_facecolor('g')  # Green


# Put labels
ax.set_xticks(ind)
ax.set_xticklabels(['Happy', 'Happy - Dog', 'Happy - Cat'])
ax.set_ylim([0, 100])     # Y-axis limit
ax.set_ylabel('Percent')
_ = ax.set_title('Pet Type')


# Save the plot
fig.savefig('Analysis Plots/[PLOT_1]happiness_distribution.png')


# Actually show the plot
plt.show()
