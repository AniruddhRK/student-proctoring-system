import os
import csv
from datetime import date,datetime
global path

def CreateFiles(name,dep_name,sem_number,section_name,subject_name,timing):
	global path
	# path = 'C:\\Users\\Aniruddh RK\\Desktop\\KNN'
	path = 'C:\\Users\\Aniruddh RK\\Desktop\\Main Project Files'
	Dep_file_name = dep_name
	sem_file_name = str(sem_number)
	Subject_file_name = subject_name
	section_file_name = str(section_name)
	today = date.today()
	today = today.strftime("%d-%m-%Y")
	Date_file_name = today
	List = os.listdir(path)
	new_path = os.path.join(path,Date_file_name)

	if Date_file_name not in List:
		os.mkdir(new_path)
		# print("Created Date File")
	else:
		# print('Date file is already created')
		pass
	List = os.listdir(new_path)

	new_path = os.path.join(new_path,Dep_file_name)

	if Dep_file_name not in List:
		os.mkdir(new_path)
		# print('Created Department File')
	else:
		# print('Department File is already Created')
		pass

	List = os.listdir(new_path)		
	new_path = os.path.join(new_path,sem_file_name)

	if sem_file_name not in List:
		print(sem_file_name)
		os.mkdir(new_path)
		# print('Created Sem File')
	else:
		# print('Sem File is already created')
		pass

	List = os.listdir(new_path)

	new_path = os.path.join(new_path,section_file_name)

	if section_file_name not in List:
		print(section_file_name)
		os.mkdir(new_path)
		# print('Created section File')
	else:
		# print('Section File is already  Created')
		pass


	List = os.listdir(new_path)

	if subject_name!='BREAK TIME':
		Subject_file_name = subject_name+str(timing)+str('.csv')	

		new_path = os.path.join(new_path,Subject_file_name)

		if Subject_file_name not in List:

			with open(new_path,'w+',newline='') as f:
				thewriter = csv.writer(f)
				thewriter.writerow(['Name','Time'])
				myDataList = f.readlines()
				# print(myDataList)
				nameList=[]
				for line in myDataList:
					entry = line.split(',')
					nameList.append(entry[0])
					print(nameList)
				if name not in nameList:
					now = datetime.now()
					dtString = now.strftime('%H:%M:%S')
					f.writelines("{},{}".format(name,dtString))
		else:
			with open(new_path,'r+') as f:
				myDataList = f.readlines()
				# print(myDataList)
				nameList = []
				for line in myDataList:
					entry = line.split(',')
					nameList.append(entry[0])
				if name not in nameList:
					now = datetime.now()
					dtString = now.strftime('%H:%M:%S')
					f.writelines("\n{},{}".format(name,dtString))