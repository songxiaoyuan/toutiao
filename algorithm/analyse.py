#-*- coding:utf-8 -*-
import os
import sys
import csv
import MySQLdb
import dataBase
import pickle
import numpy as np
import matplotlib.pyplot as plt
import apriori as ap

def getTotalUserLabels():
	db = dataBase.DataBase()
	data = db.getUserInfo()
	labelSet =set()
	for line in data:
		userid = line[0]
		labels = line[1].split('/')
		# print userid
		# print labels
		for label in labels:
			labelSet.add(label)
	print len(labelSet)
	print labelSet
def getTotalQuestionLabels():
	db = dataBase.DataBase()
	data = db.getQuestionInfo()
	labelSet = set()
	for line in data:
		label = line[1]
		labelSet.add(label)
	print len(labelSet)
	print labelSet

def getQuestionLabelAndUserLabel():
	"'主要是用来获取回答的问题的label以及回答此问题专家的兴趣的label的集合，这样可以看看label和label的对应关系'"
	labelDic =dict()
	db = dataBase.DataBase()
	data = db.getInvitedInfoTrain()
	for line in data:
		isanswer = line[2]
		if isanswer ==1:
			questioninId = line[0]
			userId = line[1]
			print questioninId
			questionLabel = db.getQuestionLabelFromId(questioninId)
			# print questionLabel
			userLabel = db.getUserLabelFromId(userId).split('/')
			# print userLabel
			if questionLabel not in labelDic:
				labelDic[questionLabel] = dict()
			for userl in userLabel:
				if userl not in labelDic[questionLabel]:
					labelDic[questionLabel][userl] = 0
				labelDic[questionLabel][userl] +=1
				# print labelDic
			# print userLabel
			# print 'yes'
			# print isanswer
		else:
			continue
			# print isanswer
	return labelDic


def getQuestionLabelAndUserLabelSet():
	"'主要是用来获取回答的问题的label以及回答此问题专家的兴趣的label的集合，这样可以看看label和label的对应关系'"
	labelDic =dict()
	db = dataBase.DataBase()
	data = db.getInvitedInfoTrain()
	for line in data:
		isanswer = line[2]
		if isanswer ==1:
			questioninId = line[0]
			userId = line[1]
			# print questioninId
			questionLabel = db.getQuestionLabelFromId(questioninId)
			# print questionLabel
			# userLabel = db.getUserLabelFromId(userId).split('/')
			# print userLabel
			if questionLabel not in labelDic:
				labelDic[questionLabel] = set()
			labelDic[questionLabel].add(userId)
		else:
			continue
			# print isanswer
	return labelDic

def getQuestionLabelAprioriLable():
	db = dataBase.DataBase()
	retDic = dict()
	labelDic = getQuestionLabelAndUserLabelSet()
	for questionLabel in labelDic:
		print questionLabel
		userIds = labelDic[questionLabel]
		labelArrays = []
		for userid in userIds:
			userLabel = db.getUserLabelFromId(userid).split('/')
			labelArrays.append(userLabel)
		aprioriLabel = ap.apriori(labelArrays,0.1)
		retDic[questionLabel] = aprioriLabel
	return retDic


def lineChart(dataDic):
	'"draw the line chart the input is dictionary x is the label y is the number of"'
	x= []
	y = []
	for item in dataDic:
		x.append(item)
		y.append(dataDic[item])
	plt.plot(x,y)
	plt.show()



if __name__ == '__main__':
	# database = dataBase.DataBase()
	# getTotalUserLabels()
	# labelDic = getQuestionLabelAndUserLabel()
	# f = open('labelDic.txt','wb')
	# pickle.dump(labelDic,f)
	# f.close()
	f = open('labelDic.txt','rb')
	data = pickle.load(f)
	f.close()
	for item in data:
		print item
		print data[item]
	# # print data[1]
	# # lineChart(data[1])
	# for item in data:
	# 	lineChart(data[item])
	# labelDic = getQuestionLabelAndUserLabelSet()
	# f = open('labelDicSet.txt','wb')
	# pickle.dump(labelDic,f)
	# f.close()
	# tmpdic = set()
	# tmpdic.add(1)
	# tmpdic.add(1)
	# print tmpdic
	# aprioriLabelDic = getQuestionLabelAprioriLable()
	# f = open('aprioriLabelDic.txt','wb')
	# pickle.dump(aprioriLabelDic,f)
	# f.close()
	# # f = open('aprioriLabelDic.txt','rb')
	# # data = pickle.load(f)
	# # f.close()
	# for item in aprioriLabelDic:
	# 	print item
	# 	print aprioriLabelDic[item]

	
