import numpy as np

study_hours=np.random.normal(5,1,100)
sleep_hours=np.random.normal(7,1,100)

X=np.column_stack((study_hours,sleep_hours))

threshold=15
scores=2*study_hours+sleep_hours

y=(scores>threshold).astype(int)

print("First 5 values of Feature Row")
print(X[:5])

print("First 5 Labels")
print(y[:5])

print("Class 0 count:", np.sum(y == 0))
print("Class 1 count:", np.sum(y == 1))
