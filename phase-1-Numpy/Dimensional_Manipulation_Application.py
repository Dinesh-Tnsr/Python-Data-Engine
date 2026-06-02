import numpy as np 

pixel_stream = np.arange(1,25)

print("raw pixel stream shape:",pixel_stream.shape)

print("-"*40)

image_tensor = pixel_stream.reshape(2,3,4)
print("Image tensor:\n",image_tensor)

first_channel = image_tensor[0,:,:]

rotated_channel = first_channel.T

print("Rotated first channel:\n",rotated_channel,"\nunrotated first channel:\n",first_channel)

ai_input = rotated_channel.flatten()

print("AI input:\n",ai_input)