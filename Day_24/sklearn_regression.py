import numpy as np
from sklearn.model_selection import train_test_split

# Generate Synthetic Data

study_hours=np.random.normal(5,1,100)
sleep_hours=np.random.normal(7,1,100)
practice_problems=np.random.normal(20,5,100)

X=np.column_stack((study_hours,sleep_hours,practice_problems))
W=np.array([5,2,0.5])
b=10
noise=np.random.normal(0,2,100)

y=np.dot(X,W)+b+noise

# The Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print("Train X shape:", X_train.shape)
print("Test X shape:", X_test.shape)
print("Train y shape:", y_train.shape)
print("Test y shape:", y_test.shape)

from sklearn.linear_model import LinearRegression
model=LinearRegression()

model.fit(X_train,y_train)

#Learned Parameters
print(f"Learned Weights:{model.coef_}")
print(f"Learned Bias:{model.intercept_}")

y_pred_train=model.predict(X_train)
y_pred_test=model.predict(X_test)

from sklearn.metrics import r2_score
print("Train R2:", r2_score(y_train, y_pred_train))
print("Test R2:", r2_score(y_test, y_pred_test))

from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

pipe = Pipeline([
    ("scaler", StandardScaler()),
    ("model", LinearRegression())
])

pipe.fit(X_train, y_train)

y_pred_train_p = pipe.predict(X_train)
y_pred_test_p  = pipe.predict(X_test)

print("\nWITH STANDARD SCALER (PIPELINE)")
print("Train R2:", r2_score(y_train, y_pred_train_p))
print("Test R2:", r2_score(y_test, y_pred_test_p))
