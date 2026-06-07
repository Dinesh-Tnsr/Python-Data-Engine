import numpy as np
# Step 1: The Raw Extraction
# Generate a flat 1D NumPy array of exactly 60 random integers between 10 and 50.
raw = np.random.randint(10, 50, size=60)

# Step 2: The Architecture (Dimensional Manipulation)
# Reshape into (Stores, Days, Products) = (3, 4, 5)
tensor = raw.reshape((3, 4, 5))

# Step 3: The Tax (Vectorization)
# Subtract exactly 2 from every element in the tensor
tax_effected_tensor = tensor - 2

# Step 4: The Pricing Engine (Broadcasting)
# Product multipliers (shape (5,)) will broadcast over the last axis
multipliers = np.array([1.5, 2.0, 1.0, 0.5, 3.0])
priced_tensor = tax_effected_tensor * multipliers

# Step 5: The Weekly Aggregation (The `axis` Crush)
# Sum over the Days axis (axis=1) to get shape (3, 5)
aggregated = np.sum(priced_tensor, axis=1)

# Step 6: The AI Forward Pass (Dot Product)
# Create dummy weight matrix of shape (5, 2) and do matrix multiplication
weights = np.random.random(size=(5, 2))
ai_output = aggregated @ weights  # result shape (3,2)

# Step 7: The Final Merge (Concatenation)
# Create store ID column vector and prepend it to the AI output
store_IDs = np.array([[101], [102], [103]])
final_output = np.hstack((store_IDs, ai_output))  # final shape (3,3)

print("final AI output:\n", final_output)
print("shape:", final_output.shape)