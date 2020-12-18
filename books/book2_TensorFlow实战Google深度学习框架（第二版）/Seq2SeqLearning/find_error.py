#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# coding=utf-8 

"""
@author: Li Tian
@contact: 694317828@qq.com
@software: pycharm
@file: find_error.py
@time: 2019/4/29 12:17
@desc: 报错参数名字不一样，检查问题
"""

import os
from tensorflow.python import pywrap_tensorflow

model_dir = './'
checkpoint_path = os.path.join(model_dir, 'attention_ckpt-2800')
reader = pywrap_tensorflow.NewCheckpointReader(checkpoint_path)
var_to_shape_map = reader.get_variable_to_shape_map()
for key in var_to_shape_map:
    print("tensor_name: ", key)
    print(reader.get_tensor(key))