#Intro to Deep Learning

"""
#Lesson 1: A Single Neuron
#Deep learning is an approach to machine learning characterized by deep stacks of computations.
#This depth of computation is what has enabled deep learning models to disentangle the kinds of complex and hierarchical patterns found in the most challenging real-world datasets.
#In the linear unit (y = wx + b), w is the weight and b is the bias.
#Whenever a value flows through a neuron, it is multiplied by the connection's weight (w * x).
#The bias enables the neuron to modify the output independently of its inputs.
#Now, let's create a model using Keras
from tensorflow import keras
from keras import layers
#A model with 1 linear input
model = keras.Sequential([layers.Dense(units=1, input_shape=[3])])
#Units define how many outputs we want
#Input_shape tells the model to accept 3 inputs
"""

"""
#Lesson 2: Deep Neural Networks
#Modularity involves building complex networks from simpler functional units.
#A dense layer is a collection of linear units having a common set of inputs.
#An activation function is simply some function we apply to each of a layer's outputs (its activations). 
#The most common is the rectifier function max(0,x). The negative part of this function is rectified to zero.
#Attaching the rectifier function to a linear unit gives the ReLU function. Thus: output = max(0, w * x+ b).
from tensorflow import keras
from keras import layers
model = keras.Sequential([
    layers.Dense(units=1, activation='relu', input_shape=[2]),
    layers.Dense(units=1, activation='relu'),
    layers.Dense(units=1)
])
#The activation arguments can be written as a function on their own
model_1 = keras.Sequential([
    layers.Dense(32, input_shape=[8]),
    layers.Activation('relu'),
    layers.Dense(32),
    layers.Activation('relu'),
    layers.Dense(1)
])
#There are alternatives to ReLU: elu, selu and swish 
"""

"""
#Lesson 3: Stochastic Gradient Descent
#SGD is an optimization algorithm used to minimize the loss function during the training process.
#SGD is an iterative method that makes incremental updates to the model's parameters based on the gradient.
#The loss function measures the disparity between the the target's true value and the value the model predicts. E.g.: MAE (for regression problems), MSE (mean square error) and Huber loss.
#The optimizer is an algorithm that adjusts the weights to minimize the loss. To do this:
#   - Sample some training data and run it through the network to make predictions.
#   - Measure the loss between the predictions and the true values.
#   - Adjust the weights in a direction that makes the value smaller.
#   - Then do it over and over again until the loss is effectively minimized.
#To add the loss and optimizer:
from tensorflow import keras
from keras import layers
model_1 = keras.Sequential([
    layers.Dense(32, input_shape=[8]),
    layers.Activation('relu'),
    layers.Dense(32),
    layers.Activation('relu'),
    layers.Dense(1)
])
model_1.compile(optimizer='adam', loss='mae')

#Now applying to an actual model
import pandas as pd
import matplotlib.pyplot as plt
red_wine = pd.read_csv("C:/Users/DEKATECH/Road to Dev (Python)/redwine.csv")
#Create training data and validation splits
df_train = red_wine.sample(frac=0.7, random_state=0)
df_valid = red_wine.drop(df_train.index)
print(df_train.head(4))
#Scale to [0,1]
max_ = df_train.max(axis=0)
min_ = df_train.min(axis=0)
df_train = (df_train - min_) / (max_ - min_)
df_valid = (df_valid - min_) / (max_ - min_)
#Split features and target
X_train = df_train.drop('quality', axis=1)
X_valid = df_valid.drop('quality', axis=1)
y_train = df_train['quality']
y_valid = df_valid['quality']
#Check the number of inputs
print(X_train.shape)
#For the network, we use a 3-layer network with over 1500 neurons.
from tensorflow import keras
from keras import layers
redmodel = keras.Sequential([
    layers.Dense(512, activation='relu', input_shape=[11]),
    layers.Dense(512, activation='relu'),
    layers.Dense(512, activation='relu'),
    layers.Dense(1)
])
#Add the optimizer
redmodel.compile(optimizer='adam', loss='mae')
#Let's start training
history = redmodel.fit(X_train, y_train, validation_data=(X_valid, y_valid), batch_size=256, epochs=10)
#Let's plot the loss
history_df = pd.DataFrame(history.history)
history_df['loss'].plot()
plt.show()
"""

"""
#Lesson 4: Overfitting and Underfitting
#In training data, we have signals and noise.
#Signal is the part that generalizes and help the model make predictions from new data.
#Noise is the part that is only true of the training data.
#A model's capacity refers to the size and complexity of the patterns it is able to learn.
#Underfitting can be solved by increasing the model's capacity either by widening it (adding more units) or deepening it (adding more layers).
#Early stopping can be used to control the number of noise a model learns.
import pandas as pd
import matplotlib.pyplot as plt
red_wine = pd.read_csv("C:/Users/DEKATECH/Road to Dev (Python)/redwine.csv")
df_train = red_wine.sample(frac=0.7, random_state=0)
df_valid = red_wine.drop(df_train.index)
print(df_train.head(4))
max_ = df_train.max(axis=0)
min_ = df_train.min(axis=0)
df_train = (df_train - min_) / (max_ - min_)
df_valid = (df_valid - min_) / (max_ - min_)
X_train = df_train.drop('quality', axis=1)
X_valid = df_valid.drop('quality', axis=1)
y_train = df_train['quality']
y_valid = df_valid['quality']
from tensorflow import keras
from keras import callbacks 
from keras import layers
early_stopping = callbacks.EarlyStopping(
    min_delta = 0.001,
    patience = 20,
    restore_best_weights = True
)
model = keras.Sequential([
    layers.Dense(512, activation='relu', input_shape=[11]),
    layers.Dense(512, activation='relu'),
    layers.Dense(512, activation='relu'),
    layers.Dense(1),
])
model.compile(
    optimizer='adam',
    loss='mae',
)
history = model.fit(
    X_train, y_train,
    validation_data=(X_valid, y_valid),
    batch_size=256,
    epochs=500,
    callbacks=[early_stopping], # put your callbacks in a list
    verbose=0,  # turn off training log
)
history_df = pd.DataFrame(history.history)
history_df.loc[:, ['loss', 'val_loss']].plot();
print("Minimum validation loss: {}".format(history_df['val_loss'].min()))
"""

"""
#Lesson 5: Dropout and Batch Normalization
#Dropout is a regularization technique that randomly sets a fraction rate of neurons to zero during training, which helps prevent overfitting.
#Batch Normalization normalizes the activations of the layers for each mini-batch, which helps improve the stability and speed of training.
from tensorflow import keras
from keras import layers
drop = keras.Sequential([
    layers.Dense(units=512, activation='relu', input_shape=[8]),
    layers.Dense(units=512, activation='relu'),
    layers.BatchNormalization(),
    layers.Dense(units=512, activation='relu'),
    layers.Dropout(rate=0.3),
    layers.Dense(1)
])

#Example
import matplotlib.pyplot as plt
import pandas as pd
redwine = pd.read_csv("C:/Users/DEKATECH/Road to Dev (Python)/redwine.csv")
df_train = redwine.sample(frac=0.7, random_state=0)
df_valid = redwine.drop(df_train.index)
X_train = df_train.drop('quality', axis=1)
X_valid = df_valid.drop('quality', axis=1)
y_train = df_train['quality']
y_valid = df_valid['quality']
from tensorflow import keras
from keras import layers
redmodel = keras.Sequential([
    layers.Dense(units=1024, activation='relu', input_shape=[11]),
    layers.Dropout(rate=0.3),
    layers.BatchNormalization(),
    layers.Dense(units=1024, activation='relu'),
    layers.Dropout(rate=0.3),
    layers.BatchNormalization(),
    layers.Dense(units=1024, activation='relu'),
    layers.Dropout(rate=0.3),
    layers.BatchNormalization(),
    layers.Dense(1)
])
redmodel.compile(optimizer='adam', loss='mae')
history = redmodel.fit(X_train, y_train, validation_data=(X_valid, y_valid), batch_size=256, epochs=100, verbose=0)
history_df = pd.DataFrame(history.history)
history_df.loc[:, ['loss', 'val_loss']].plot();
plt.show()
"""

"""
#Lesson 6: Binary Classification
#Common classification problems in machine learning:
#   -Whether or not a customer is likely to make a purchase.
#   -Whether or not a credit card transaction was fraudulent.
#   -Whether deep space signals show evidence of a new planet.
#Assigning numeric labels puts the data in a form a neural network can use.
#Accuracy is the ratio of correct predictions to total predictions: accuracy = number_correct / total
#However, it can't be used as a loss function. Thus we use the cross-entropy function
#Cross-entropy is a sort of measure for the distance from one probability distribution to another.
#The idea is that we want our network to predict the correct class with probability 1.0. The further away the predicted probability is from 1.0, the greater will be the cross-entropy loss.
#The cross-entropy and accuracy functions both require probabilities as inputs, meaning, numbers from 0 to 1.
#To covert the real-valued outputs produced by a dense layer into probabilities, we attach a new kind of activation function, the sigmoid activation.
#To get the final class prediction, we define a threshold probability.
#Typically this will be 0.5, so that rounding will give us the correct class: below 0.5 means the class with label 0 and 0.5 or above means the class with label 1.
#Binary classification is a special case of multi-class classification where there are only two classes.
#The sigmoid activation function is used for binary classification problems, where the output is a probability between 0 and 1.
#The output of the sigmoid function is a value between 0 and 1, which can be interpreted as a probability. 
#The sigmoid function is defined as follows: sigmoid(x) = 1 / (1 + exp(-x))
#Example
import pandas as pd
import matplotlib.pyplot as plt
from tensorflow import keras
from keras import layers
from keras import callbacks
ion = pd.read_csv("C:/Users/DEKATECH/road to Dev (Python)/ion.csv", index_col=0)
df = ion.copy()
df['Class'] = df['Class'].map({'good':0, 'bad':1})
df_train = df.sample(frac=0.7, random_state=0)
df_valid = df.drop(df_train.index)
max_ = df_train.max(axis=0)
min_ = df_train.min(axis=0)
df_train = (df_train - min_) / (max_ - min_)
df_valid = (df_train - min_) / (max_ - min_)
df_train.dropna(axis=1, inplace=True)
df_valid.dropna(axis=1, inplace=True)
X_train = df_train.drop('Class', axis=1)
X_valid = df_valid.drop('Class', axis=1)
y_train = df_train['Class']
y_valid = df_valid['Class']
ion_model = keras.Sequential([
    layers.Dense(units=4, activation='relu', input_shape=[33]),
    layers.Dense(units=4, activation='relu'),
    layers.Dense(units=1, activation='sigmoid')
])
#Add cross-entropy and accuracy
ion_model.compile(
    optimizer='adam',
    loss = 'binary_crossentropy',
    metrics = ['binary_accuracy']
)
early_stopping = callbacks.EarlyStopping(
    patience=10,
    min_delta=0.001,
    restore_best_weights=True
)
history = ion_model.fit(
    X_train, y_train, validation_data=(X_valid, y_valid),batch_size=512, 
    epochs=1000, callbacks=early_stopping, verbose=0
)
history_df = pd.DataFrame(history.history)
history_df.loc[5:, ['loss', 'val_loss']].plot();
history_df.loc[5:, ['binary_accuracy', 'val_binary_accuracy']].plot()
print(("Best validation loss: {:.4f}\nBest validation accuracy: {:.4f}")\
        .format(history_df['val_loss'].min(), history_df['val_binary_accuracy'].max()))
plt.show()
"""


