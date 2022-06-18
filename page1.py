# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'page1.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import ui 

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(578, 517)
        Form.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        Form.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        Form.setStyleSheet("background-color: rgb(56, 58,89);\n"
"")
        self.departmentCBox = QtWidgets.QComboBox(Form)
        self.departmentCBox.setGeometry(QtCore.QRect(260, 80, 281, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.departmentCBox.setFont(font)
        self.departmentCBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.departmentCBox.setStyleSheet("color: rgb(255, 111, 253);\n"
"border: 1px solid gray;\n"
"    border-radius: 3px;\n"
"    padding: 1px 18px 1px 3px;\n"
"    min-width: 6em;")
        self.departmentCBox.setInsertPolicy(QtWidgets.QComboBox.InsertAtBottom)
        self.departmentCBox.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.departmentCBox.setObjectName("departmentCBox")
        self.departmentCBox.addItem("")
        self.departmentCBox.addItem("")
        self.departmentCBox.addItem("")
        self.departmentCBox.addItem("")
        self.departmentCBox.addItem("")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(80, 80, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(80, 170, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.sectionCBox = QtWidgets.QComboBox(Form)
        self.sectionCBox.setGeometry(QtCore.QRect(260, 170, 281, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.sectionCBox.setFont(font)
        self.sectionCBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.sectionCBox.setStyleSheet("color: rgb(255, 111, 253);\n"
"border: 1px solid gray;\n"
"    border-radius: 3px;\n"
"    padding: 1px 18px 1px 3px;\n"
"    min-width: 6em;")
        self.sectionCBox.setInsertPolicy(QtWidgets.QComboBox.InsertAtBottom)
        self.sectionCBox.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.sectionCBox.setObjectName("sectionCBox")
        self.sectionCBox.addItem("")
        self.sectionCBox.addItem("")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(80, 350, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.dayLabel = QtWidgets.QLabel(Form)
        self.dayLabel.setGeometry(QtCore.QRect(260, 345, 281, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.dayLabel.setFont(font)
        self.dayLabel.setStyleSheet("color: rgb(255, 111, 253);")
        self.dayLabel.setObjectName("dayLabel")
        self.editButton = QtWidgets.QPushButton(Form)
        self.editButton.setGeometry(QtCore.QRect(210, 460, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.editButton.setFont(font)
        self.editButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"\n"
"background-color: rgba(255,255,255,40)\n"
"\n"
"")
        self.editButton.setObjectName("editButton")
        self.semesterCBox = QtWidgets.QComboBox(Form)
        self.semesterCBox.setGeometry(QtCore.QRect(260, 260, 281, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.semesterCBox.setFont(font)
        self.semesterCBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.semesterCBox.setStyleSheet("color: rgb(255, 111, 253);\n"
"border: 1px solid gray;\n"
"    border-radius: 3px;\n"
"    padding: 1px 18px 1px 3px;\n"
"    min-width: 6em;")
        self.semesterCBox.setInsertPolicy(QtWidgets.QComboBox.InsertAtBottom)
        self.semesterCBox.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.semesterCBox.setObjectName("semesterCBox")
        self.semesterCBox.addItem("")
        self.semesterCBox.addItem("")
        self.semesterCBox.addItem("")
        self.semesterCBox.addItem("")
        self.semesterCBox.addItem("")
        self.semesterCBox.addItem("")
        self.semesterCBox.addItem("")
        self.semesterCBox.addItem("")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(80, 260, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_5.setObjectName("label_5")
        self.submitButton = QtWidgets.QPushButton(Form)
        self.submitButton.setGeometry(QtCore.QRect(210, 410, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.submitButton.setFont(font)
        self.submitButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"\n"
"background-color: rgba(255,255,255,40)\n"
"\n"
"")
        self.submitButton.setObjectName("submitButton")
        self.exitButton = QtWidgets.QPushButton(Form)
        self.exitButton.setGeometry(QtCore.QRect(550, 10, 16, 16))
        self.exitButton.setStyleSheet("border-image: url(:/images/cancel.png);")
        self.exitButton.setText("")
        self.exitButton.setObjectName("exitButton")

        self.retranslateUi(Form)
        self.exitButton.clicked.connect(lambda:Form.close())
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.departmentCBox.setCurrentText(_translate("Form", "CSE"))
        self.departmentCBox.setItemText(0, _translate("Form", "CSE"))
        self.departmentCBox.setItemText(1, _translate("Form", "ECE"))
        self.departmentCBox.setItemText(2, _translate("Form", "EEE"))
        self.departmentCBox.setItemText(3, _translate("Form", "MECH"))
        self.departmentCBox.setItemText(4, _translate("Form", "CIVIL"))
        self.label.setText(_translate("Form", "Department"))
        self.label_2.setText(_translate("Form", "Section"))
        self.sectionCBox.setCurrentText(_translate("Form", "A"))
        self.sectionCBox.setItemText(0, _translate("Form", "A"))
        self.sectionCBox.setItemText(1, _translate("Form", "B"))
        self.label_3.setText(_translate("Form", "Time Table"))
        self.dayLabel.setText(_translate("Form", "Monday"))
        self.editButton.setText(_translate("Form", "Edit TimeTable"))
        self.semesterCBox.setCurrentText(_translate("Form", "1"))
        self.semesterCBox.setItemText(0, _translate("Form", "1"))
        self.semesterCBox.setItemText(1, _translate("Form", "2"))
        self.semesterCBox.setItemText(2, _translate("Form", "3"))
        self.semesterCBox.setItemText(3, _translate("Form", "4"))
        self.semesterCBox.setItemText(4, _translate("Form", "5"))
        self.semesterCBox.setItemText(5, _translate("Form", "6"))
        self.semesterCBox.setItemText(6, _translate("Form", "7"))
        self.semesterCBox.setItemText(7, _translate("Form", "8"))
        self.label_5.setText(_translate("Form", "Semester"))
        self.submitButton.setText(_translate("Form", "Submit"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())