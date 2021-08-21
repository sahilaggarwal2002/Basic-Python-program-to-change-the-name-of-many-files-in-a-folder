import os
path = '/Users/sahil/Downloads/panasonic'
files = os.listdir(path)


for index, file in enumerate(files):
    
    dst='Object_panasonicphone '+ str(index+1)+'.jpg'
    os.rename(os.path.join(path, file), os.path.join(path, dst))
    
