import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

study_hours=np.random.normal(5,1,100)
sleep_hours=np.random.normal(7,1,100)

X=np.column_stack((study_hours,sleep_hours))

model=LogisticRegression()

score=2*study_hours+sleep_hours

threshold=15
y=(score>threshold).astype(int)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model.fit(X_train,y_train)
print(f"Weights:{model.coef_}")
print(f"Bias:{model.intercept_}")

y_pred=model.predict(X_train)
y_prob=model.predict_proba(X_train)

print("First 5 predicted classes:")
print(y_pred[:5])
print("First 5 predicted Probabilities")
print(y_prob[:5])
