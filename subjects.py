from datetime import datetime
global subject 
subject = list()
class Department:
	def __init__(self,dept,choices):
		self.subjects= dict()
		global dep_name
		global sem_number
		dep_name = dept
		sem_number = int(choices)
	def info(self):
		global subject	
		if (dep_name)=='CSE':
			self.subjects[1] = ['HS8151 CE - COMMUNICATIVE ENGLISH' , ' MA8151 Engineering Mathematics – I','PH8151 ENGINEERING PHYSICS','CY8151 Engineering Chemistry','GE8151 Problem Solving and Python Programming','GE8152 Engineering Graphics','GE8161 Problem Solving and Python Programming Laboratory','BS8161 Physics and Chemistry Laboratory']

			self.subjects[2] = ['HS8251 Technical English', 'MA8251 Engineering Mathematics - II','PH8252 Physics for Information Science','BE8255 BASIC ELECTRICAL ELECTRONICS AND MEASUREMENT ENGINEERING','GE8291 Environmental Science and Engineering (EVS)','CS8251 PROGRAMMING IN C','GE8261 ENGINEERING PRACTICES LABORATORY','CS8261 C PROGRAMMING LABORATORY']

			self.subjects[3] = ['CS8392 OBJECT ORIENTED PROGRAMMING','EC8395 Communication Engineering','CS8381 DATA STRUCTURES LABORATORY','CS8383 OBJECT ORIENTED PROGRAMMING LABORATORY','CS8382 DIGITAL SYSTEMS LABORATORY','HS8381 INTERPERSONAL SKILLS/LISTENING & SPEAKING']

			self.subjects[4] = ['MA8402 Probability and Queueing Theory','CS8491 Computer Architecture','CS8492 Database Management Systems','CS8451 Design and Analysis of Algorithms','CS8493 Operating Systems','CS8494 Software Engineering','CS8481 DATABASE MANAGEMENT SYSTEMS LABORATORY','CS8461 OPERATING SYSTEMS LABORATORY','HS8461 ADVANCED READING AND WRITING']

			self.subjects[5] = ['MA8551 Algebra and Number Theory','CS8591 Computer Networks','EC8691 Microprocessors and Microcontrollers','CS8501 Theory of Computation','CS8592 Object Oriented Analysis and Design','Open Elective I','EC8681 Microprocessors and Microcontrollers Laboratory','CS8582 Object Oriented Analysis and Design Laboratory','CS8581 Networks Laboratory']

			self.subjects[6] = ['CS8651 Internet Programming','CS8691 Artificial Intelligence','CS8601 Mobile Computing','CS8602 Compiler Design','CS8603 Distributed Systems','Professional Elective I','CS8661 Internet Programming Laboratory','CS8662 Mobile Application Development Laboratory','CS8611 Mini Project']

			self.subjects[7] = ['MG8591 Principles of Management','CS8792 Cryptography and Network Security','CS8791 Cloud Computing','Open Elective II','Professional Elective II','Professional Elective III','CS8711 Cloud Computing Laboratory','IT8761 Security Laboratory']

			self.subjects[8] = ['Professional Elective IV','Professional Elective V','CS8811 Project Work']

			subject = list(self.subjects[sem_number])
			print(subject)
			return subject

# d=Department('CSE','6')
# d.info()