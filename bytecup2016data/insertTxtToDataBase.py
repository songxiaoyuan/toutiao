#-*- coding:utf-8 -*-
import os
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import csv
import MySQLdb

def insertInoDataBase():
	try:
		db = MySQLdb.connect(host = "localhost",user = "root",passwd="111111",db="toutiao", charset='utf8')
		cursor = db.cursor()
		Path = './user_info.txt'
		File = open(Path)
		l =1
		while True:
			line = File.readline()
			if line:
				# linearray = line.split('\t')
				insertRow = []
				for item in line.split('\t'):
					insertRow.append(item.strip())
				insertSql = 'insert into userinfo values(%s,%s,%s,%s)'
				cursor.execute(insertSql,insertRow)
				# if insertRow[0] =='000002':
				# 	print insertRow
				# if l==1:
				# 	print insertRow
				# 	l +=1
				# else:
				# 	break;
				# print insertRow
			else:
				break
		# for line in csvFile:
		# 	cells =line.split(',')
		# 	insertRow = []
		# 	for x in xrange(0,3):
		# 		# print type(cells[x].strip())
		# 		# print cells[x].strip()
		# 		# tmp = cells[x].decode('utf-8')
		# 		insertRow.append(cells[x].strip())
		# 	print len(insertRow)
		# 	# import pdb
		# 	# pdb.set_trace()
		# 	insertSql = 'insert into keyhotwords values(%s,%s,%s)'
		# 	cursor.execute(insertSql,insertRow)
			# if index ==2 :
			# 	break
		db.commit()
		cursor.close()
		db.close()
	except Exception, e:
		raise e
		# pass
	
if __name__ == '__main__':
	# for x in xrange(0,7):
	# 	print x
	insertInoDataBase()

# def creatTableInvestmentRelation():
# 	sql = 'create table investmentrelation (
# 		Company_code  char(100) 
# 		Year   date
# 		AcquireeName  char(100)
# 		DateToGetStock  date
		# CostToGetStock  double(30,10)
# 		ProportionOfGetStock  double(30,10)
# 		StyleOfGetStock  char(100)
# 	)'

