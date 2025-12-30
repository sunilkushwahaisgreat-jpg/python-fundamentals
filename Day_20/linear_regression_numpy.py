import numpy as np

# Generate Synthetic Data
x=np.array([1,2,3,4,5])
noise=np.random.normal(0,1,size=len(x))

y_actual=5*x+3+noise

print(f"x:{x[:5]}")
print(f"y:{y_actual[:5]}")
print("Shapes:",x.shape, y_actual.shape)

# Hypothesis function

m=0
c=0

y_pred=m*x+c

print("Current Weight(m):",m)
print("Current Bias (c):",c)
print("-"*30)
print("First 5 predictions:",y_pred[:5])
print("Shape or y_pred:",y_pred.shape)

# Compute Loss (MSE)
error=y_actual-y_pred

squared_error=np.square(error)

loss=np.mean(squared_error)

print(f"Mean Squared Error (loss): {loss:.4f}")

# Compute gradients
#HuperParamenters
learning_rate=0.01
itr=1000
n=float(len(x))

print(f"Starting Loss:{loss}")

for i in range(itr):
    y_pred=m*x+c

    error=y_actual-y_pred
    dm=(-2/n)*np.sum(x*error)
    dc=(-2/n)*np.sum(error)

    m=m-learning_rate*dm
    c=c-learning_rate*dc

    if i%100==0:
        current_loss=np.mean(np.square(y_actual-y_pred))
        print(f"Step {i}: Loss={current_loss},m={m},c={c}")

print(f"Final Results; m={m},c={c}")
print(f"Final Loss:{np.mean(np.square(y_actual-(m*x+c)))}")
