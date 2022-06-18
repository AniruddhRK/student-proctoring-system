from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer
from splash import Ui_SplashScreen
from page1 import Ui_Form
import sys
from week import Ui_Week
from timetable import Ui_TimeTable
import datetime
counter = 0
import recognition as rec
from subjects import Department
import excel as Excel
global DepartmentName, SectionName, Semester,Day
today = datetime.datetime.today()
day = today.strftime('%A')
class TimeTable(QtWidgets.QMainWindow):
	def __init__(self):
		super(TimeTable,self).__init__()
		self.ui = Ui_TimeTable()
		self.ui.setupUi(self)
		global DepartmentName,Semester
		d =  Department(DepartmentName,Semester)
		self.subjectsList=d.info()
		print(self.subjectsList)
		self.ui.hour1ComboBox.addItems(self.subjectsList)
		self.ui.hour2ComboBox.addItems(self.subjectsList)
		self.ui.hour3ComboBox.addItems(self.subjectsList)
		self.ui.hour4ComboBox.addItems(self.subjectsList)
		self.ui.hour5ComboBox.addItems(self.subjectsList)
		self.ui.hour6ComboBox.addItems(self.subjectsList)
		self.ui.hour7ComboBox.addItems(self.subjectsList)
		self.ui.hour8ComboBox.addItems(self.subjectsList)
		self.ui.submitButton.clicked.connect(self.connectExcel)
	def connectExcel(self):
		global Day
		subjects = [self.ui.hour1ComboBox.currentText(),self.ui.hour2ComboBox.currentText(),self.ui.hour3ComboBox.currentText(),self.ui.hour4ComboBox.currentText(),self.ui.hour5ComboBox.currentText(),self.ui.hour6ComboBox.currentText(),self.ui.hour7ComboBox.currentText(),self.ui.hour8ComboBox.currentText()]
		workBookName = DepartmentName+'_'+SectionName+'_'+Semester+'.xlsx'
		print(workBookName)
		Excel.workingonExcel(Day,subjects,workBookName)
		self.pageWindow = Page()
		self.pageWindow.show()
		self.close()
class WeekScreen(QtWidgets.QMainWindow):
	def __init__(self):
		super(WeekScreen,self).__init__()
		self.ui = Ui_Week()
		self.ui.setupUi(self)
		self.ui.MondayButton.clicked.connect(lambda:self.respond('Monday'))
		self.ui.TuesdayButton.clicked.connect(lambda :self.respond('Tuesday'))
		self.ui.WednesdayButton.clicked.connect(lambda :self.respond('Wednesday'))
		self.ui.ThursdayButton.clicked.connect(lambda :self.respond('Thursday'))
		self.ui.FridayButton.clicked.connect(lambda :self.respond('Friday'))
		self.ui.SaturdayButton.clicked.connect(lambda :self.respond('Saturday'))
	def respond(self,weekDay):
		global Day
		Day = weekDay
		self.timetableWindow = TimeTable()
		self.timetableWindow.show()
		print(weekDay)
		self.close()
class Page(QtWidgets.QMainWindow):
	def __init__(self):
		super(Page,self).__init__()
		self.ui = Ui_Form()
		self.ui.setupUi(self)
		global day
		self.ui.dayLabel.setText(day)
		self.ui.editButton.clicked.connect(self.editing)
		self.ui.submitButton.clicked.connect(self.proceed)
	def proceed(self):
		global DepartmentName,SectionName,Semester
		DepartmentName=self.ui.departmentCBox.currentText()
		SectionName = self.ui.sectionCBox.currentText()
		Semester = self.ui.semesterCBox.currentText()
		print(DepartmentName)
		print(SectionName)
		print(Semester)
		self.close()
		rec.recog(DepartmentName,SectionName,Semester)
	def editing(self):
		global DepartmentName,SectionName,Semester
		DepartmentName=self.ui.departmentCBox.currentText()
		SectionName = self.ui.sectionCBox.currentText()
		Semester = self.ui.semesterCBox.currentText()
		print(DepartmentName)
		print(SectionName)
		print(Semester)
		self.weekWindow = WeekScreen()
		self.weekWindow.show()
		self.close()
class SplashScreen(QtWidgets.QMainWindow):
	def __init__(self):
		super(SplashScreen,self).__init__()
		self.ui = Ui_SplashScreen()
		self.ui.setupUi(self)
		self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
		self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
		print('Going to start')
		self.timer = QTimer()
		self.timer.timeout.connect(self.progress)
		self.timer.start(35)
		self.show()
	def progress(self):
		global counter
		if counter<=100:
			self.ui.progressBar.setValue(counter)
			counter+=1
		else:
			print('loading completed')
			self.timer.stop()
			self.pageWindow = Page()
			self.pageWindow.show()
			self.close()
if __name__ == '__main__':
	app = QtWidgets.QApplication(sys.argv)
	window = SplashScreen()
	sys.exit(app.exec_())