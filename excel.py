from openpyxl import *


global sheet
global workbook

'''
monday = A2				hour 1 = B[2-7]			hour 7 = H[2-7]
tuesday = A3			hour 2 = C[2-7]			hour 8 = I[2-7]
wednesday = A4			hour 3 = D[2-7]
thursday = A5			hour 4 = E[2-7]
friday = A6				hour 5 = F[2-7]
Saturday = A7 			hour 6 = G[2-7]
'''
# print(sheet)

# print(sheet['A3'].value)

# print(sheet['B5'].value)

def changeHour(cell,i,subjectName,workBookName):
	global sheet  	
	global workbook
	# print(sheet[cell].value)
	print(subjectName)
	sheet[cell].value = subjectName
	print(sheet[cell].value)
	workbook.save(workBookName)


def workingonExcel(day,subjectList,workBookName):
	global sheet
	global workbook
	hour_Alpha = ['B','C','D','E','F','G','H','I']
	week_day = {'Monday':'2','Tuesday' : '3','Wednesday' : '4', 'Thursday' : '5', 'Friday' : '6', 'Saturday' : '7'}
	print(subjectList)
	workbook = load_workbook(filename=workBookName)
	sheet = workbook.active
	for i in range(0,8):	
		param = hour_Alpha[i] + week_day[day]
		changeHour(param,i,subjectList[i],workBookName)


def ReturnSubject(i,day):
	global sheet
	hour_Alpha = ['B','C','D','E','F','G','H','I']
	week_day = {'Monday':'2','Tuesday' : '3','Wednesday' : '4', 'Thursday' : '5', 'Friday' : '6', 'Saturday' : '7'}
	parem = hour_Alpha[i]+week_day[day]
	return sheet[parem].value
def readSubject(day,workBookName,Time):
	global sheet
	global workbook
	workbook = load_workbook(filename=workBookName)
	sheet = workbook.active
	Time = int(Time)
	print(Time)
	if Time>=830 and Time<=915:
		subjectName = ReturnSubject(0,day)
		return subjectName,1
	elif Time>915 and Time<=1000:
		subjectName = ReturnSubject(1,day)
		return subjectName,2
	elif Time>1015 and Time<=1100:
		subjectName = ReturnSubject(2,day)
		return subjectName,3
	elif Time>1100 and Time<=1145:
		subjectName = ReturnSubject(3,day)
		return subjectName,4
	elif Time>1230 and Time<=1315:
		subjectName = ReturnSubject(4,day)
		return subjectName,5
	elif Time>1315 and Time<=1400:
		subjectName = ReturnSubject(5,day)
		return subjectName,6
	elif Time>1410 and Time<=1455:
		subjectName = ReturnSubject(6,day)
		return subjectName,7
	elif Time>1455 and Time<=1540:
		subjectName = ReturnSubject(7,day)
		return subjectName,8
	else:
		print('Break EHHH')
		return 'BREAK TIME',0

# def workingonExcel('Monday',['A','B','C','D','E','F','G','H'])
# day = input('Enter the day you wanted to edit: ')
# hour = input('Enter the hour you wanted to edit: ')
 
