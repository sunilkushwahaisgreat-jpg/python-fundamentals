import numpy as np
def sigmoid(x):
    
    return 1/(1+np.exp(-np.array(x)))

x=np.array([-10,-2,0,2,10])

print(sigmoid(x))

