'''
This file contains a database of 4 common features of dogs and cats.

We created our own dataset instead of importing one!
We chose four common features of dogs and cats: cuddly, soft, quiet, and energetic.

Our goal is to find out if people are happy with their pets.

For the data collection portion of this procedure: 
We distributed a five-question yes/no survey to 30 respondents who own one cat or one dog.
'''

# NumPy: adding support for large, multi-dimensional arrays and matrices.
import numpy as np



# For neural network, the results must be converted into features and labels. 
# So we can compile responses into a single long list, with each row representing one survey response.
# "Yes" is represented by 1 while "no" is represented by 0.


# Column names:  Energetic, Cuddly, Soft, Quiet, Happiness
survey = np.array([
  [1, 0, 1, 1, 1],     #   Energetic,     Not Cuddly, Soft, Quiet,     Happy
  [1, 1, 1, 1, 1],     #   Energetic,         Cuddly, Soft, Quiet,     Happy
  [1, 0, 1, 0, 1],     #   Energetic,     Not Cuddly, Soft, Loud,      Happy
  [0, 0, 1, 0, 0],     #   Not Energetic, Not Cuddly, Soft, Loud,  Not happy
  [0, 1, 0, 1, 0],     #   ...
  [0, 0, 0, 1, 0],
  [1, 1, 0, 0, 1],
  [0, 1, 0, 0, 0],
  [0, 1, 0, 1, 0],
  [0, 1, 0, 0, 0],
  [1, 0, 1, 1, 1],
  [0, 1, 1, 1, 0],
  [1, 0, 1, 0, 1],
  [0, 0, 1, 0, 0],
  [0, 1, 0, 1, 0],
  [0, 0, 0, 1, 0],
  [1, 1, 0, 0, 1],
  [0, 0, 0, 0, 0],
  [1, 0, 1, 1, 1],
  [1, 1, 1, 1, 0],
  [1, 0, 1, 0, 1],
  [1, 1, 1, 0, 1],
  [0, 0, 0, 0, 1],
  [0, 0, 0, 1, 1],
  [0, 0, 1, 1, 1],
  [0, 1, 1, 1, 1]
])


# We must divide this dataset into the training and testing sets. 
# Training set: To train the neural network.
# Testing set:  This is kept hidden from the neural network during training so that we may later evaluate the network's accuracy.

# First four columns are our features
features_train = survey[:,0:4]

# Last column is our label
labels_train = survey[:,4]


# Keeping four surveys as our test set
test_survey = np.array([
  [1, 1, 1, 0, 1],
  [0, 0, 0, 1, 0],
  [0, 0, 1, 0, 0],
  [1, 0, 1, 0, 1]
])


features_test = test_survey[:, 0:4]
labels_test = test_survey[:,4]