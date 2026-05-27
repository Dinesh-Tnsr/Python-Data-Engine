import numpy as np

mock_image = np.random.randint(0,256,size=(5,5,3))

red_layer = mock_image[:,:,0]

cropped_patch = mock_image[0:2,0:2,:]

print("red_layer:",red_layer)

print(cropped_patch)