import itk
import numpy as np

image = itk.imread("reconFilteredNormalizedSinogram.mha")

array = itk.GetArrayFromImage(image)

minImage = np.min(array)
maxImage = np.max(array)
step = (maxImage - minImage) / 256

scaledArray = (array - minImage)/step 
    
print(minImage)
print(maxImage)   
print(step)

for i in range(360):
    newarr = scaledArray[:,:,i].astype(int)
    newImage = itk.GetImageFromArray(newarr)
    itk.imwrite(newImage, str(i)+".png")
