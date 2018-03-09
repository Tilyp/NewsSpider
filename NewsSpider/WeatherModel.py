# -*- coding:utf-8 -*-
from __future__ import print_function
import logging
import numpy as np
from optparse import OptionParser
import sys
from time import time
import matplotlib.pyplot as plt
import os
from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import HashingVectorizer
from sklearn.feature_selection import SelectKBest
from sklearn.linear_model import RidgeClassifier
from sklearn.pipeline import Pipeline
from sklearn.svm import LinearSVC
from sklearn.linear_model import SGDClassifier
from sklearn.linear_model import Perceptron
from sklearn.linear_model import PassiveAggressiveClassifier
from sklearn.naive_bayes import BernoulliNB, MultinomialNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neighbors import NearestCentroid
from sklearn.ensemble import RandomForestClassifier
from sklearn.utils.extmath import density
from sklearn import metrics
import jieba
import random
import cPickle




class WeatherModel():
    model = None
    vectorizer = None
    chi2 = None
    keywordpath = None
    def __init__(self , model_path , vectorizer_path, chi2_path,keywords_path):
        self.model_path = model_path
        self.vectorizer_path = vectorizer_path
        self.chi2_path = chi2_path
        self.keywordpath = keywords_path
        # print(self.vectorizer_path)
        WeatherModel.vectorizer = cPickle.load(open(self.vectorizer_path, "rb"))
        WeatherModel.chi2 = cPickle.load(open(self.chi2_path, "rb"))
        WeatherModel.model = cPickle.load(open(self.model_path, "rb"))

    def predict(self, sentense):
        try:
            train = []
            jieba.load_userdict(self.keywordpath)
            seg = jieba.cut(sentense, cut_all=False)
            seglist = []
            for w in seg:
                # print w
                w = w.strip().encode("utf-8")
                seglist.append(w)
            # print  ( i ,",".join(seglist))
            train.append(" ".join(seglist))
            X_test = WeatherModel.vectorizer.transform(train)
            #  print (X_test)
            X_test = WeatherModel.chi2.transform(X_test)
            pred = WeatherModel.model.predict(X_test)
        except AttributeError:
            print ("NoneType Error")
        return pred


if __name__ == "__main__":
    wm = WeatherModel("weatheroutput/weatheroutput/LinearSVCl2.model", "weatheroutput/weatheroutput/vectorizer.data",
                      "weatheroutput/weatheroutput/ch2.data", "keywords.txt")
    sentenst = "中国天气网讯今天日随着北方冷空气的东移内蒙古大部甘肃东部华北中北部东北地区大部气温将下跌局地降温幅度可达以上并出现大范围降雨天气苏皖降雨减弱但今明天陕西四川一带雨水又起目前华南高温持续明天南下的冷空气将影响到江南南部和华南炎热天气将有所缓解日强降雨致重庆城口县沿河乡河水猛涨彭远寿摄冷空气横扫北方华北开启入秋进程昨天冷空气的影响主要停留在南疆甘肃中西部内蒙古西部等地这些地方普遍出现了降温陕西山西河北南部到黄淮一带地区受到阴雨天气以及前一股弱冷空气的影响也出现了的小幅降温今天冷空气影响向东延伸日至日较强冷空气将继续自西向东自北向南影响我国中东部大部地区内蒙古大部甘肃东部华北中北部东北地区大部西南地区东部江汉江南等地的平均气温或最低气温将下降局地降温幅度可达以上北方大部地区伴有级偏北风省会级城市中像是北京今天最高气温就将降至长春的最高气温也将只有这两个城市今天最高气温都将比昨天下滑明天过后黑龙江吉林部分地区将出现初霜冻或对农收不利随着冷空气的东移北方降雨明显增多从西北地区东南部黄淮西部东北等地都将出现大范围的小到中雨甚至强降雨尤其在东北要防范强对流的发生冷空气和降雨将共同携手扭转北方大部地区气温偏高的局面北方气温将纷纷降至与常年同期持平或偏低的水平气温回归正常之后华北"
    print(str(wm.predict(sentenst)))

