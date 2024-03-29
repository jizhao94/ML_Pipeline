# ML_Pipeline
For the results of running the codes, please refer to the Jupyter Notebook MLHW2.ipynb

## Part 1. Import Packages
pandas, sklearn, and matplotlib are imported
<br>
Also, the pipeline document 'hw2_pipeline.py', which contains the discretization and categorization functions, will be imported

## Part 2. Import Data
Import the csv file 'credit-data.csv'

## Part 3. Convert Datatypes
Convert the variable 'PersonID' and 'zipcode' to string, 'SeriousDlqin2yrs' to category

## Part 4. Find Distributions
Find the distributions of the variables 'SeriousDlqin2yrs', 'RevolvingUtilizationOfUnsecuredLines',
<br>
'age', ''NumberOfTime30-59DaysPastDueNotWorse', and 'DebtRatio'

## Part 5. Find Summaries
Find the summaries of all variables except PersonsID and zipcode

## Part 6. Find Correlation between Variables
Find the correlations between monthly income and age, between revolving utilization of unsecured lines and monthly income,
<br>
between 'NumberOfTime30-59DaysPastDueNotWorse' and monthly income, between 'NumberOfTime60-89DaysPastDueNotWorse' and montly income,
<br>
and between 'NumberOfTime30-59DaysPastDueNotWorse' and 'NumberOfTime60-89DaysPastDueNotWorse'

## Part 7. Fill in NA Values
Fill in each NA value with the mean of the variable that it belongs to

## Part 8. Discretize Continuous Variables
Apply the function that discretizes continuous variables, cutting them into three parts: which are
<br>
I. between the minimum value and the 25% quantile, represented by integer 0
<br>
II. between the 25% quantile and the 75% quantile, represented by integer 1
<br>
III. between 75% quantile and the maximum value, represented by 2
<br>
Use this function to discretize the variables 'age', 'MonthlyIncome', and ''RevolvingUtilizationOfUnsecuredLines',
<br>
which will be used as features in the machine learning model

## Part 9. Create Binary on Zipcode
Apply the function that converts the variable Zipcode to a binary variable
<br>
Knowing that in our dataset, zipcodes '60637' and '60629' refer to the neighborhoods in the South Side of the City of Chicago,
<br>
a binary variable is created to indicate if this person lives in the South Side(indicated by 1) or not (indicated by 0)

## Part 10. Decision Tree Classifier
Build the decision tree model using the DecisionTreeClassifier of sklearn package,
<br>
and fit the model with the features and the label

## Part 11. Evaluate Classifier
First predict the label using the decision tree classifier, then calculate the accuracy score of this model
