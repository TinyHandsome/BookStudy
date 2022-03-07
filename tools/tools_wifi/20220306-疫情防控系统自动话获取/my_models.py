#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# coding=utf-8 

"""
@author: Liyingjun
@contact: 694317828@qq.com
@software: pycharm
@file: my_models.py
@time: 2022/3/6 7:55
@desc: 建立模型
"""
from dataclasses import dataclass


@dataclass
class UnRevised:
    """未修正"""
    address: str
    age: int
    area: str
    areaCode: str
    arriveLuTime: int
    arriveTime: int
    auditStatus: str
    cardId: str
    carryHesuanProof: str
    checkUnit: str
    cityName: str
    cityNameStreet: str
    comeArea: str
    comeAreaFull: str
    comeAreaFullStreet: str
    comeMode: str
    comeProvinceCityCounty: str
    controlInfo: str
    correctStreet: str
    correctTime: int
    countyName: str
    countyNameStreet: str
    covidFlag: str
    creatTime: int
    dataFrom: str
    handlerStreet: str
    hesuanCheckType: str
    id: int
    intimateFlag: str
    keyAreaType: str
    leaveTheRiskAreaTime: int
    midId: str
    name: str
    params: dict
    phone: str
    provinceName: str
    provinceNameStreet: str
    relieveIsolation: str
    remarkStreet: str
    reportSrc: str
    reportStreet: str
    reportTime: int
    reporterName: str
    reporterPhone: str
    results: str
    sex: str
    sourceDir: str
    updateBy: str
    updateFlag: str
    updateTime: int


@dataclass
class UnVerified:
    """未审核"""
    address: str
    area: str
    areaCode: str
    arriveLuTime: int
    arriveTime: int
    cardId: str
    carryHesuanProof: str
    cityName: str
    comeAreaFull: str
    comeMode: str
    countyName: str
    creatTime: int
    createBy: str
    createFrom: str
    createTime: int
    declarationStatus: str
    destinationStation: str
    destinationStationType: str
    detectionAbnormal: str
    healthCodeAbnormal: str
    hesuanTime: int
    id: int
    leaveTheRiskAreaTime: int
    name: str
    params: dict
    phone: str
    provinceName: str
    quarantineStatus: str
    registeredResidenceAddress: str
    registeredResidenceCity: str
    reportStreet: str
    transportStatus: str
    travelCodeAbnormal: str
    twoCodeOneReportStatus: str
    twonName: str
    viaProvince: str
