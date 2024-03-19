# sclassifier
This python module allows to perform radio source classification analysis using different ML methods in a supervised/self-supervised or unsupervised way: 
* convolutional neural networks (CNNs)    
* convolutional autoencoders (CAEs)   
* decision trees & LightGBM  
* HDBSCAN clustering algorithm   
* UMAP dimensionality reduction   
* SimCLR & BYOL self-supervised frameworks   

## **Status**
This software is under development. It requires python3 + tensorflow 2.x. 

## **Credit**
This software is distributed with GPLv3 license. If you use it for your research, please add repository link or acknowledge authors in your papers.   

## **Installation**  

To build and install the package:    

* Clone this repository in a local directory (e.g. $SRC_DIR):   
  ```git clone https://github.com/SKA-INAF/sclassifier.git```
* Create a virtual environment with your preferred python version (e.g. python3.6) in a local install directory (e.g. INSTALL_DIR):   
  ``` python3.6 -m venv $INSTALL_DIR```   
* Activate your virtual environment:   
  ```source $INSTALL_DIR/bin/activate```
* Install module dependencies listed in ```requirements.txt```:    
  ``` pip install -r requirements.txt```  
* Build and install package:   
  ``` python setup build```   
  ``` python setup install```   
* If required (e.g. outside virtual env), add installation path to your ```PYTHONPATH``` environment variable:   
  ``` export PYTHONPATH=$PYTHONPATH:$INSTALL_DIR/lib/python3.6/site-packages ```

## **Usage**
Several python scripts are provided in the ```scripts``` directory to run desired tasks, described below.  

### **Image supervised classification with CNNs**
The script `run_classifier_nn.py` allows to perform binary and multi-class (single or multi-label) radio image (single- or multi-channel, FITS format) classification using customized or predefined CNN architectures (resnet18/resnet34/resnet50/resnet101). Customized networks can be built by user through input options, piling up stacks of Conv2D/MaxPool/BatchNorm/Dropout layers, enabled or disabled when desired. Several user options are provided to customize network architecture, data pre-processing and augmentation. A list if available with: ```python run_classifier_nn.py --help```.    

Input data (train/validation) must be given in json format with the following structure:    

```
{  
  "data": [    
    {    
      "filepaths": [     
        "G340.743+00.313_ch1.fits",    
        "G340.743+00.313_ch2.fits",    
        "G340.743+00.313_ch3.fits"   
      ],    
      "sname": "G340.743+00.313",   
      "id": 6,   
      "label": "HII"    
    },    
    ...
    ...
  ]   
}   
```    

For multilabel classification the ```id``` and ```label``` keys must be lists.    

Two run modes are supported: training, inference. To perform inference you need to specify the ```--predict``` option. To perform binary or multi-class classification you must specify the options ```--binary_class``` and ```--multilabel```, respectively. 

To customize the desired class id/label names and relative targets, eventually remapping them with respect to values given in the input data list, you must specify the following options:   

```
--nclasses=$NCLASSES     
--classid_remap=$CLASSID_REMAP    
--target_label_map=$TARGET_LABEL_MAP      
--classid_label_map=$CLASSID_LABEL_MAP     
--target_names=$TARGET_NAMES     
```

For example:   
     
```
NCLASSES=4     
CLASS_PROBS='{"BACKGROUND":1.0,"COMPACT":0.1,"EXTENDED":1.0,"DIFFUSE":1.0}'    
CLASSID_REMAP='{0:-1,1:0,2:1,3:2,4:3}'    
TARGET_LABEL_MAP='{-1:"UNKNOWN",0:"BACKGROUND",1:"COMPACT",2:"EXTENDED",3:"DIFFUSE"}'    
CLASSID_LABEL_MAP='{0:"UNKNOWN",1:"BACKGROUND",2:"COMPACT",3:"EXTENDED",4:"DIFFUSE"}'    
TARGET_NAMES="BACKGROUND,COMPACT,EXTENDED,DIFFUSE"
```    

Below we report some run examples:

* To train a custom model (2 conv layers + 1 dense layer) from scratch:   
  ```
  python run_classifier_nn.py --datalist=$DATALIST_TRAIN --datalist_cv=$DATALIST_CV --nepochs=10 \    
    --nfilters_cnn=16,32 --kernsizes_cnn=3,3 --strides_cnn=1,1 --add_maxpooling_layer \    
    --add_dense_layer --dense_layer_sizes=16 \    
    --add_dropout --dropout_rate=0.4 --add_conv_dropout --conv_dropout_rate=0.2 \  
    --batch_size=64 --optimizer=adam --learning_rate=1e-4 \    
    --augment --augmenter=cnn --augment_scale_factor=5 \    
    --resize_size=64 --scale_to_abs_max
  ```   
  
* To train a predefined model (resnet18) using pre-trained backbone .h5 weights (e.g. $WEIGHTFILE):    
  ```
  python run_classifier_nn.py --datalist=$DATALIST_TRAIN --datalist_cv=$DATALIST_CV [OPTIONS] \    
    --use_predefined_arch --predefined_arch=resnet18 --weightfile_backbone=$WEIGHTFILE 
  ```    

* To perform inference with a saved .h5 model (e.g. $WEIGHTFILE) and weights (e.g. $WEIGHTFILE):     
  ```
  python run_classifier_nn.py --datalist=$DATALIST_TEST [OPTIONS] \    
    --modelfile=$MODELFILE --weightfile=$WEIGHTFILE [OPTIONS] \    
    --predict
  ```    

### **Image feature extraction with CAE**
WRITE ME

### **Image feature extraction with SimCLR**
WRITE ME

### **Feature reduction with UMAP**
WRITE ME

### **Clustering feature data with HDBSCAN**
WRITE ME
