#-*- coding:utf-8 -*-
import os
import sys
import csv
import MySQLdb

class DataBase(object):
	"""docstring for DataBase"""
	def __init__(self):
		print 'the DataBase is init'
		self.getConnection()
	def __del__(self):
		print 'the database is not connect'
		self.closeConnection()

	def getConnection(self):
		"'connect to the database"
		try:
			db = MySQLdb.connect("localhost","root","111111","toutiao",charset='utf8')
			cursor = db.cursor()
			self.__CURSOR__ = cursor
			self.__DB__ = db
		except Exception, e:
			raise e

	def closeConnection(self):
		"'the is used to close the connect"
		self.__CURSOR__.close()
		self.__DB__.close()

	def getInvitedInfoTrain(self):
		sql = 'select * from invitedinfo'
		# print sql
		self.__CURSOR__.execute(sql)
		data = self.__CURSOR__.fetchall()
		return data

	def getQuestionInfo(self):
		sql = 'select * from questioninfo'
		# print sql
		self.__CURSOR__.execute(sql)
		data = self.__CURSOR__.fetchall()
		return data

	def getUserInfo(self):
		sql = 'select * from userinfo'
		# print sql
		self.__CURSOR__.execute(sql)
		data = self.__CURSOR__.fetchall()
		return data

	def getQuestionLabelFromId(self,questionId_):
		getInfomation = ('questionlabel',questionId_)
		sql = 'select %s from questioninfo where questionid = "%s" ' %getInfomation
		# print sql
		self.__CURSOR__.execute(sql)
		data = self.__CURSOR__.fetchall()
		return data[0][0]

	def getUserLabelFromId(self,userId_):
		getInfomation = ('userlabel',userId_)
		sql = 'select %s from userinfo where userid = "%s" ' %getInfomation
		# print sql
		self.__CURSOR__.execute(sql)
		data = self.__CURSOR__.fetchall()
		return data[0][0]
		

if __name__ == '__main__':
	database = DataBase()
	
	data = database.getUserLabelFromId('c8412df1fb204d98684a25f203488ecb')
	print data

	

		