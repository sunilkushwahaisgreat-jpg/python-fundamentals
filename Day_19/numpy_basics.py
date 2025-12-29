import numpy as np

# Creating array using numpy
arr=np.array([1,2,3,4,5])
print(arr)

# List to array
l1=[1,2,3,4,5]
arr=np.array(l1)
print(arr)

# Ones array
arr=np.ones(5,dtype=int)
print(arr)

# Zeros array
arr=np.zeros(5,dtype=int)
print(arr)

# Numpy arrange
arr=np.arange(5)
print(arr)

# Element wise sum
arr1=np.array([1,2,3,4,5])
arr2=np.array([1,2,3,4,5])

print(arr1+arr2)

#Element wise subtraction
arr1=np.array([1,2,3,4,5])
arr2=np.array([1,2,3,4,5])

print(arr1-arr2)

# Element wise multiplication
arr1=np.array([1,2,3,4,5])
arr2=np.array([1,2,3,4,5])

print(arr1*arr2)

# Square
arr1=np.array([1,2,3,4,5])

print(arr1**2)

# Mean
arr1=np.array([1,2,3,4,5])
print(np.mean(arr1))

# Sum
arr1=np.array([1,2,3,4,5])
print(arr1.sum())

# Dot Prodeuct
arr1=np.array([1,2,3,4,5])
arr2=np.array([1,2,3,4,5])

print(f"Dot product of {arr1} and {arr2} is:{arr1@arr2}")

# Vector Magnitude(L2 norm)
arr1=np.array([1,2,3,4,5])

mag=np.linalg.norm(arr1)
print(f"Vector:{arr1} , Magnitude:{mag}")

# Cosine similarity
arr1=np.array([1,2,3,4,5])
arr2=np.array([1,2,3,4,5])

dot_product=arr1@arr2

norm_arr1=np.linalg.norm(arr1)
norm_arr2=np.linalg.norm(arr2)

similarity=dot_product/(norm_arr1*norm_arr2)

print(similarity)

# Matrix transpose
matrix=np.array([[1,2],[3,4]])

b=np.transpose(matrix)
print(f"Original Matrix:{matrix}")
print(f"Transpose of matrix:{b}")

# Matrix Multiplication
arr1=np.array([[1,2],[3,4]])
arr2=np.array([[1,2],[3,4]])

print(f"Matrix multiplicatof of {arr1} and {arr2} is:{arr1@arr2}")

# Row/Column access
mat=np.array([[1,2],[3,4]])

print(f"Row :{mat[0]}")
print(f"Coloumn: {mat[:,0]}")

# Normalize Values to range 0-1

arr1=np.array([1,2,3,4,5],dtype=float)

arr_min=arr1.min()
arr_max=arr1.max()

normalized_arr=(arr1-arr_min)/(arr_max-arr_min)

print(f"Normalized vector of range [0 1] is:{normalized_arr}")

# Standardize array

arr1=np.array([1,2,3,4,5])
mean=np.mean(arr1)
std=np.std(arr1)

standardized_arr=(arr1-mean)/std
print(f"Standardized Array:{standardized_arr}")
