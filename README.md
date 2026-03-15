# Customer Churn Prediction

A machine learning project that predicts whether a customer is likely to leave a service (churn) based on their usage patterns, service subscriptions, and billing information.

Customer churn prediction helps businesses identify customers at risk of leaving and take proactive actions to improve retention.

🎯 ## Project Objective

The goal of this project is to:

Analyze customer behavior and service usage patterns

Identify factors contributing to customer churn

Build machine learning models to predict churn

Provide business insights to improve customer retention

📂 Dataset

Dataset used: Telco Customer Churn Dataset

The dataset contains customer information such as:

Feature	Description
customerID	Unique customer identifier
gender	Customer gender
SeniorCitizen	Whether customer is a senior citizen
Partner	Whether the customer has a partner
Dependents	Whether the customer has dependents
tenure	Number of months with the company
PhoneService	Phone service subscription
InternetService	Type of internet service
Contract	Contract type
PaymentMethod	Payment method used
MonthlyCharges	Monthly bill amount
TotalCharges	Total amount paid
Churn	Whether the customer left the company

Target variable: Churn

🛠 Tools & Technologies

Python

Jupyter Notebook

Scikit-learn

Pandas

Seaborn

🔎 Project Workflow
1️⃣ Data Cleaning

Removed unnecessary columns

Handled missing values

Converted data types

Encoded categorical variables

2️⃣ Exploratory Data Analysis (EDA)

EDA was performed to identify churn patterns.

Key visualizations:

Churn distribution

Contract type vs churn

Tenure vs churn

Monthly charges vs churn

3️⃣ Machine Learning Models

The following classification models were trained:

Logistic Regression

Random Forest

XGBoost

4️⃣ Model Evaluation

Models were evaluated using:

Accuracy

Recall

ROC-AUC Score
