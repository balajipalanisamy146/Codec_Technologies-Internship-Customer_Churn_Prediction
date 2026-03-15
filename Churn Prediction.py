import pandas as pd

data = pd.read_csv("Telco_Customer_Churn_Dataset.csv")

from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
for col in data.columns:
    if data[col].dtype == "object":
       data[col] = le.fit_transform(data[col])

X = data.drop("Churn", axis=1)
y = data["Churn"]

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)

from sklearn.ensemble import RandomForestClassifier
rf = RandomForestClassifier()
rf.fit(X_train, y_train)

y_predict = rf.predict(X_test)

from sklearn.metrics import accuracy_score
accuracy = accuracy_score(y_test, y_predict)
print("Accuracy",accuracy)

from sklearn.metrics import recall_score
recall = recall_score(y_test, y_predict)
print("Recall", recall)

from sklearn.metrics import roc_auc_score
roc_auc = roc_auc_score(y_test, y_predict)
print("ROC-AUC", roc_auc)