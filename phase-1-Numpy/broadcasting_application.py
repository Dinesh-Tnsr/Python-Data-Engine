import numpy as np
shipment_weights = np.array([
    [15.5, 20.0, 10.2],
    [5.0,  12.5, 8.0],
    [25.0, 30.0, 15.0],
    [8.5,  10.0, 5.5],
    [18.0, 22.5, 11.1]
])

packaging_weights = np.array([2.5, 3.0, 1.5])
print("Raw Shipment Weights:")
print(shipment_weights)
print("-" * 40)

print("gross weights:\n",shipment_weights+packaging_weights)
print("shape of gross weights:",np.shape(shipment_weights+packaging_weights))