"""
Impact of Various Techniques on Minority Subject Area News Text Classification
CS7643

Calculate weights to be passed into loss functions.

REFERENCES
# https://androidkt.com/how-to-use-class-weight-in-crossentropyloss-for-an-imbalanced-dataset/
# https://medium.com/gumgum-tech/handling-class-imbalance-by-introducing-sample-weighting-in-the-loss-function-3bdebd8203b4        
# https://github.com/vandit15/Class-balanced-loss-pytorch/blob/master/class_balanced_loss.py
# https://discuss.pytorch.org/t/per-class-and-per-sample-weighting/25530/4
# https://pytorch.org/docs/stable/generated/torch.sort.html

"""

import torch
import numpy as np
import sklearn as sk
import torch.nn as nn
import torch.nn.functional as F
from torch.autograd import Variable

def weightweight(cls_num_list, type= "ins", beta=0.9999):
    if type == "classbal":
        weights = (1-beta)/(1-np.power(beta,cls_num_list))
    elif type == "ins":
        weights = 1.0/np.array(cls_num_list)
    elif type == "isns":
        weights = 1.0/np.sqrt(cls_num_list)
    elif type == "uniform":
        weights = torch.empty(41).uniform_(0, 1)
        weights, indices = torch.sort(weights)
    elif type == "simple":
        weights = 1 - cls_num_list/np.sum(cls_num_list)

    weights = torch.as_tensor(weights)
    weights = weights.float()

    return weights