'''
This file construct and train a neural network to help us in making predictions.


This neural network contains:
An input layer       :  for features
Some hidden layers   :  for learning representations
A final output layer :  for making predictions

The hidden layers find relationships between features to generate more accurate predictions.

Parameters for our neural network:
4 input features, 1 hidden layer (4 neurons of same size as our input), and 2 outputs (YES - happiness or NO - unhappiness).
SKLearn automatically counts the size of our input and output neurons, so we just need to define the hidden layers in the code.
'''


# Importing all the datasets (data) from input_data file 
from bias_input_data import *

# Importing the SKLearn library: To create a simple multi-layer perceptron neural network or MLP.
from sklearn.neural_network import MLPClassifier

# Importing warning library: Suppress Warnings
from warnings import filterwarnings
filterwarnings('ignore')


'''
During one epoch (cycle) of training: 
The hidden layer will detect patterns in the input features and deliver a prediction to one of two output neurons.

Since an iteration and an epoch are the same thing in the method we're employing, the code refers to this as a "iteration."

The neural network's predictions should improve across successive epochs of the same training dataset!
So we'll stick with 1000 epochs for the time being.
'''


# Define the model
mlp = MLPClassifier(hidden_layer_sizes=(4,),   # Size of the hidden layers
                    activation='tanh',         # Activation method (here tangent hyperbolic function)
                    max_iter=1000,             # Epoch (cycle or number of iterations)
                    random_state=1             # Random State (controls the shuffling process) 
                   )


# Train the model
mlp.fit(features_train, labels_train)



# # Testing our AI classifier on the original training data and evaluate it's accuracy
# print("Training set score: %f" % mlp.score(features_train, labels_train))

# # Testing our AI classifier on the original test data (that was set aside) and evaluate it's accuracy
# print("Testing set score: %f" % mlp.score(features_test, labels_test))


'''
Output (Results):
Training set score: 0.846154
Testing set score: 1.000000    # pretty good score!
'''
