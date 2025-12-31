import numpy as np

# Generate Synthetic Data

study_hours=np.random.normal(5,1,100)
sleep_hours=np.random.normal(7,1,100)
practice_problems=np.random.normal(20,5,100)

X=np.column_stack((study_hours,sleep_hours,practice_problems))

W=np.array([5,2,0.5])
b=10
noise=np.random.normal(0,2,100)

y_actual=np.dot(X,W)+b+noise

print(f"X Shape:{X.shape}")
print(f"y Shape:{y_actual.shape}")

print(f"First five rows of X: {X[:5]}")
print(f"First five Values of y:{y_actual[:5]}")

# Hypothesis Matrix Form

weights=np.zeros(3)
bias=0

y_pred=np.dot(X,weights)+bias

print(f"Current Weight(w):{weights} Shape:{weights.shape}")
print(f"Current Bias (b):{bias}")
print("First 5 predictions:",y_pred[:5])
print("Shape or y_pred:",y_pred.shape)


# Compute Loss (MSE)
error=y_actual-y_pred

squared_error=np.square(error)

loss=np.mean(squared_error)

print(f"Mean Squared Error (loss): {loss:.4f}")

# Compute gradients
learning_rate=0.001
itr=500
n=float(len(X))

print(f"Starting Loss:{loss}")

for i in range(itr):
    y_pred=np.dot(X,weights)+bias

    error=y_actual-y_pred
    dw=(-2/n)*(X.T@error)
    db=(-2/n)*np.sum(error)

    weights=weights-learning_rate*dw
    bias=bias-learning_rate*db

    if i%50==0:
        current_loss=np.mean(np.square(y_actual-y_pred))
        print(f"Step {i}: Loss={current_loss},weights={weights},bias={bias}")

final_loss=np.mean((y_actual-y_pred)**2)
print("BASELINE")
print(f"Loss:{final_loss}")
print(f"Weights:{weights}")
print(f"Bias:{bias}")

X_min=X.min(axis=0)
X_max=X.max(axis=0)

X_scaled=(X-X_min) / (X_max-X_min)

weights=np.zeros(3)
bias=0

for i in range(itr):
    y_pred=np.dot(X_scaled,weights)+bias

    error=y_actual-y_pred
    dw=(-2/n)*(X_scaled.T@error)
    db=(-2/n)*np.sum(error)

    weights=weights-learning_rate*dw
    bias=bias-learning_rate*db


final_loss=np.mean((y_actual-y_pred)**2)
print("MIN-MAX NORMALISED")
print(f"Loss:{final_loss}")
print(f"Weights:{weights}")
print(f"Bias:{bias}")


X_mean=np.mean(X,axis=0)
X_std=np.std(X,axis=0)
X_standard=(X-X_mean) / X_std

weights=np.zeros(3)
bias=0

for i in range(itr):
    y_pred=np.dot(X_standard,weights)+bias

    error=y_actual-y_pred
    dw=(-2/n)*(X_standard.T@error)
    db=(-2/n)*np.sum(error)

    weights=weights-learning_rate*dw
    bias=bias-learning_rate*db


final_loss=np.mean((y_actual-y_pred)**2)

print("STANDARDIZED")
print(f"Loss:{final_loss}")
print(f"Weights:{weights}")
print(f"Bias:{bias}")

