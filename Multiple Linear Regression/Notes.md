# Assumptions of a linear Regression
 1. Linearity
 2. Homoscedasticity
 3. Multivariate normality
 4. Independence of errors
 5. Lack of multicollinearity

## 5 methods of building a model:
 1. All-in
 2. Backward elimination
 3. Forward selection
 4. Bidirectional elimination
 5. Score comparison

## Backward elimination

### STEP 1: Select a significance level to stay in the model(eg. SL 0.05)
### STEP 2: Fit the full model with all possible predictors
### STEP 3: Consider the predictor with the highest P- value. If the P>SL, go to STEP 4, otherwise go tp FIN
### STEP 4: Remove the predictor
### STEP 5: Fit model without this variable


## Forward selection

### STEP 1: Select the significance level
### STEP 2: Fit simple regression models y-xn. Slect the one with the lowest P-value
### STEP 3: Keep this variable and fit all the possible models with one extra predictor added to the ones you have already have.
### STEP 4: Consider the predictor with the lowest P-value. If P<SL go to STEP 3 otherwise go to FIN

## Bidirectional Elimination

### STEP 1: Select a significance level to enter and to stay in the model, eg SLENTER=0.05, SLSTAY=0.05
### STEP 2: Perform the next step of the forward selection(new variables must have P<SLENTER)
### STEP 3: Perform all steps of backward elimination
