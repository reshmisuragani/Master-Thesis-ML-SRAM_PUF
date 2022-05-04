

import os
import numpy as np
import shutil
import random
# # Creating Train / Val / Test folders (One time use)
root_dir = r'E:\thesis-smalldataset\raw_dataset_2016'
path =r'E:\thesis-smalldataset\raw_dataset_2016'
classes_dir = []
for filename in os.listdir(path):
    if filename.startswith('board'):
        classes_dir.append('/'+filename)



val_ratio = 0.20
test_ratio = 0.20

for cls in classes_dir:
    os.makedirs(root_dir +'/train' + cls)
    os.makedirs(root_dir +'/val' + cls)
    os.makedirs(root_dir +'/test' + cls)

    # Creating partitions of the data after shuffeling
    src = root_dir + cls # Folder to copy images from

    allFileNames = os.listdir(src)
    np.random.shuffle(allFileNames)
    train_FileNames, test_FileNames = np.split(np.array(allFileNames),
                                                              [
                                                               int(len(allFileNames)* (1 - test_ratio))])


    train_FileNames = [src+'/'+ name for name in train_FileNames.tolist()]

    test_FileNames = [src+'/' + name for name in test_FileNames.tolist()]

    print('Total images: ', len(allFileNames))
    print('Training: ', len(train_FileNames))
    print('Validation: ', len(val_FileNames))
    print('Testing: ', len(test_FileNames))

    # Copy-pasting images
    for name in train_FileNames:
        shutil.copy(name, root_dir +'/train' + cls)

    for name in test_FileNames:
        shutil.copy(name, root_dir +'/test' + cls)

