import numpy as np

randomArray = np.random.randint(1, 20, 15)
print(randomArray)

reshaped = randomArray.reshape(3, 5)
print(reshaped)
print(np.where(reshaped != np.max(reshaped, axis=1, keepdims=True), reshaped, 0))

