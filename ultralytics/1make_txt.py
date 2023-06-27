import os
import random

trainval_percent = 1
train_percent = 0.9
xmlfilepath = 'D:/研究生/PV-Multi-Defect/Annotations'
txtsavepath = 'datasets/ImageSets'
total_xml = os.listdir(xmlfilepath)
num = len(total_xml)
list = range(num)
tv = int(num * trainval_percent)
tr = int(tv * train_percent)
trainval = random.sample(list, tv)
train = random.sample(trainval, tr)
ftrainval = open('yolo/data/ImageSets/trainval.txt', 'w')
ftest = open('yolo/data/ImageSets/test.txt', 'w')
ftrain = open('yolo/data/ImageSets/train.txt', 'w')
fval = open('yolo/data/ImageSets/val.txt', 'w')
for i in list:
    name = total_xml[i][:-4] + '\n'
    if i in trainval:
        ftrainval.write(name)
        if i in train:
            ftest.write(name)
        else:
            fval.write(name)
    else:
        ftrain.write(name)
ftrainval.close()
ftrain.close()
fval.close()
ftest.close()
