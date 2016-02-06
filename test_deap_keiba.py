# -*- coding: utf-8 -*-
##上記がないと日本語のコメントがエラーになる http://linux.oboe-gaki.com/archives/000379.html

import numpy as np
import chainer
from chainer import cuda, Function, gradient_check, Variable, optimizers, serializers, utils
from chainer import Link, Chain, ChainList
import chainer.functions as F
import chainer.links as L

import scipy as sp
import matplotlib.pyplot as plt
import sklearn
from sklearn import svm
from sklearn import cross_validation