import numpy as np
np.random.seed(42)

inputs = np.random.randint(0,10,size = (4,3))
weights = np.random.random(size=(3,5))

print("Inputs Shape:", inputs.shape)
print("Weights Shape:", weights.shape)
print("-" * 50)

layer_outputs = inputs@weights
print("Layer outputs:\n",layer_outputs)
print("shape:",layer_outputs.shape)

