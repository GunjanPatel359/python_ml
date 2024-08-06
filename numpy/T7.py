import numpy as np

print(np.random.random(1))
print(np.random.random(2))
print(np.random.random((2,2)))
print(np.random.random((3,3,3)))
print(np.random.randint(1,10))
print(np.random.randint(1,10,(2,2)))
print(np.random.randint(1,10,(3,4,5)))
print(np.random.rand(2,2))
print(np.random.randn(2,2))

a=np.arange(1,10)
print(a)
np.random.choice(a)