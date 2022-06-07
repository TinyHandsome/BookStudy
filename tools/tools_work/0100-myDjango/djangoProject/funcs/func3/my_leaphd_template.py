#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# coding=utf-8 

"""
@author: Liyingjun
@contact: 694317828@qq.com
@software: pycharm
@file: my_leaphd_template.py
@time: 2022/2/16 8:54
@desc: LeapHD流程的模板
"""
import json
import os
import copy

from djangoProject.settings import MY_RESOURCE_URL


class MYLeapHDTemplate:
    my_json = ''

    def get_value(self, loc):
        """获取层级的值"""
        layers = loc.split('.')
        aim = copy.deepcopy(self.my_json)
        for layer in layers:
            aim = aim[layer]

        return aim

    def set_value(self, aim_json_dict, loc, value):
        """设置层级的值"""
        layers = loc.split('.')
        my_json_dict = aim_json_dict

        for i in range(len(layers)):
            layer = layers[i]
            if i + 1 == len(layers):
                my_json_dict[layer] = value
            else:
                my_json_dict = my_json_dict[layer]

        return aim_json_dict


class QuanLiang(MYLeapHDTemplate):
    json_url = 'func3_leaphddosave/全量模板.json'

    def __init__(self):
        with open(os.path.join(MY_RESOURCE_URL, self.json_url), 'r', encoding='utf-8') as f:
            self.my_json = json.load(f)

        self.my_component_id_1 = 'states.rect3.props.taskId.value'
        self.my_hivesql_1 = 'states.rect3.props.hsql.value'
        self.my_component_id_2 = 'states.rect4.props.taskId.value'
        self.my_hivesql_2 = 'states.rect4.props.sourceData.value'
        self.my_target = 'states.rect4.props.destData.value'
        self.my_schedule_name = 'props.props.processName.value'
        self.my_keys = [self.my_component_id_1, self.my_hivesql_1, self.my_component_id_2, self.my_hivesql_2,
                        self.my_target, self.my_schedule_name]

    def set_values_return_json(self, values):
        temp_json = copy.deepcopy(self.my_json)
        for k, v in zip(self.my_keys, values):
            temp_json = self.set_value(temp_json, k, v)
        return json.dumps(temp_json, ensure_ascii=False)


if __name__ == '__main__':
    a = QuanLiang()
    x = a.set_values_return_json(['asdfasdf\nasdfasdf\nas', 2, 3, 4, 5, 'aaaaaaaaaaaaaaa'])
    print(x)
