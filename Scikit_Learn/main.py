from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pandas as pd
import numpy as np

dataset = pd.read_csv('dataset.csv') 

"""
> Setting the variables for the linear regression
> X = input variable, Y = output variable
"""
x = np.array(dataset['horas_estudo_mes'], dtype = float)
x = x.reshape(-1, 1)
y = dataset['salario']


# 20% of the data is used for testing and 80% for training.
# random state = 42 is the seed for the random number generator (but it's not necessary, it's just to make the results reproducible).
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 42)


# Creating the model
model = LinearRegression()

# Training the model
model.fit(x_train, y_train)

score = model.score(x_test, y_test)
print('Accuracy (R^2): {:.2f}'.format(score))


# DEPLOYMENT

# Define a new value for study hours
new_study_hours = np.array([[48]])

# Predicting the salary for the new study hours
predict_salary = model.predict(new_study_hours)

print(f'If you study for {new_study_hours} hours, your salary will be ${predict_salary}')

# Proving the result
y_new = model.intercept_ + model.coef_ * new_study_hours # y = w0 + w1 * x

# the model training is for obtain the w0 and w1 values, 
# so we can use the formula y = w0 + w1 * x to predict the salary for a new study hours value.
print(f'If you study for {new_study_hours} hours, your salary will be ${y_new}')