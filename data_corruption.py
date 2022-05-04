import os,glob
import random
from itertools import cycle,islice
from PIL import Image
import numpy as np      
import numpy
import cv2
path = r'E:\thesis-smalldataset\raw_dataset-split\test'
dest_path = r"E:\thesis-smalldataset\corrupted-2\test"


folders = []
for filename in os.listdir(path):
    if filename.startswith('board'):
        folders.append(filename)

for folder in folders:
    os.mkdir(os.path.join(dest_path,folder))
    
def file_to_image(folder):
  name =[]
  for file in os.listdir(os.path.join(path,folder)):
    name.append(file)
  for file in name:
    if file.startswith('board'):
        f = open(os.path.join(path,folder,file), "rb")
        s =f.read()
        binvalue = list(bytearray(s))
        n  =int(len(binvalue)*0.25) # percentage of bits to be corrupted (25% ~ 0.25)
        binvalue[-n:] =  [0] * n 
        new=[]
        for i in binvalue:
            new.append(bin(int(i))[2:].zfill(8))
        str1 = ''.join(str(e) for e in new)
        string_2_int =[int(i) for element in str1 for i in element]
        string_2_int = np.array(string_2_int)
        length = int(len(string_2_int)/1024)    
        data_2_img = string_2_int.reshape(length,1024)
        image = Image.fromarray((data_2_img * 255).astype('uint8'), mode ='L')
        new_filename = file.split(' ')[0] + '.png'
        image.save(os.path.join(dest_path,folder,new_filename))
        
        
    
for folder in folders:
    images = file_to_image(folder)


