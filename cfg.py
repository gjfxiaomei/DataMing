##数据集的类别
NUM_CLASSES = 3

#训练时batch的大小
BATCH_SIZE = 64

#网络默认输入图像的大小
INPUT_SIZE = 224

##预训练模型的存放位置
#下载地址：https://download.pytorch.org/models/densenet169-b2777c0a.pth
PRETRAINED_MODEL = './dense121.pth'

##训练完成，权重文件的保存路径,默认保存在trained_model下
TRAINED_MODEL = './trained_model/dense121_110.pth'

#数据集的存放位置
TRAIN_DATASET_DIR = './data/trainimg/continuum'
VAL_DATASET_DIR = './data/testimg/continuum'

##
labels_to_classes = {
    '0':'alpha',
    '1':'beta',
    '2':'betax'
}


