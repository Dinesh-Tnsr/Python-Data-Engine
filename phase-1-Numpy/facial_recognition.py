import numpy as np
np.random.seed(77)

raw_image = np.random.randint(0,256,size=(4,4,3))

print("shape of raw image:",raw_image)

print("-"*40)

green_channel = raw_image[:,:,1]
print("Green channel:",green_channel)

center_crop = raw_image[1:3,1:3,:]
print("center crop:",center_crop)