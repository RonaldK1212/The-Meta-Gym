from PyQt5 import QtCore, QtGui, QtWidgets
import helper_functions
user_data = None
user_id = None

class Ui_LoginWindow(object):
        
        def listWorkouts(self):
                from list_workuts import Ui_WorkoutsWindow
                
                self.window = QtWidgets.QMainWindow()
                self.ui = Ui_WorkoutsWindow()
                #self.ui.user_id = user_id
                self.ui.setupUi(self.window)
                self.window.show()
                self.addWorkouts()
                
        def addWorkouts(self):
            global user_id
            from helper_functions import getUserWorkouts
            from datetime import datetime
            from list_workuts import workoutsList
            
            data = getUserWorkouts(str(user_id))
            workoutsList = data
            #list_workuts.workoutsList = data
            print([data, user_id])
            count=1
            for _ in data:
                date_str = _[1]
                date_obj = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S.%f") 
                name = 'Workout ' + str(count) +"   " + date_obj.strftime("%Y-%m-%d")
                self.ui.comboBox.addItem(name, _)
                count += 1
        def startWorkout(self):
            from helper_functions import recordWorkout
            recordWorkout(user_id)
        
        def setupUi(self, LoginWindow):
                LoginWindow.setObjectName("LoginWindow")
                LoginWindow.resize(1024, 600)
                LoginWindow.setWindowFlag(QtCore.Qt.FramelessWindowHint)
                icon = QtGui.QIcon()
                icon.addPixmap(QtGui.QPixmap("assets/TMG_Logo_only.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                LoginWindow.setWindowIcon(icon)
                self.centralwidget = QtWidgets.QWidget(LoginWindow)
                self.centralwidget.setObjectName("centralwidget")
                self.label = QtWidgets.QLabel(self.centralwidget)
                self.label.setGeometry(QtCore.QRect(70, 60, 791, 51))
                font = QtGui.QFont()
                font.setFamily("BR Cobane")
                font.setPointSize(32)
                font.setBold(True)
                font.setWeight(75)
                self.label.setFont(font)
                self.label.setStyleSheet("color: rgb(255, 200, 21);")
                self.label.setObjectName("label")
                self.startWorkoutButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.startWorkout())
                self.startWorkoutButton.setGeometry(QtCore.QRect(600, 460, 230, 80))
                font = QtGui.QFont()
                font.setFamily("BR Cobane")
                font.setPointSize(16)
                font.setBold(False)
                font.setWeight(50)
                self.startWorkoutButton.setFont(font)
                self.startWorkoutButton.setAutoFillBackground(False)
                self.startWorkoutButton.setStyleSheet("color: rgb(41, 41, 41);\n"
                "border-color: rgba(255, 255, 255, 0);\n"
                "background-color: rgb(255, 200, 21);\n"
                "border: 2px solid rgb(41, 41, 41);\n"
                "alternate-background-color: rgb(41, 41, 41);\n"
                "")
                self.startWorkoutButton.setAutoDefault(False)
                self.startWorkoutButton.setDefault(False)
                self.startWorkoutButton.setFlat(False)
                self.startWorkoutButton.setObjectName("startWorkoutButton")
                self.yourWorkoutsButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.listWorkouts())
                self.yourWorkoutsButton.setEnabled(True)
                self.yourWorkoutsButton.setGeometry(QtCore.QRect(260, 460, 230, 80))
                sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(self.yourWorkoutsButton.sizePolicy().hasHeightForWidth())
                self.yourWorkoutsButton.setSizePolicy(sizePolicy)
                font = QtGui.QFont()
                font.setFamily("BR Cobane")
                font.setPointSize(16)
                font.setBold(False)
                font.setWeight(50)
                font.setKerning(True)
                self.yourWorkoutsButton.setFont(font)
                self.yourWorkoutsButton.setAutoFillBackground(False)
                self.yourWorkoutsButton.setStyleSheet("background-color: rgb(41, 41, 41);\n"
                "border: 2px solid rgb(255, 200, 21);\n"
                "color: rgb(255, 200, 21);")
                self.yourWorkoutsButton.setDefault(False)
                self.yourWorkoutsButton.setFlat(False)
                self.yourWorkoutsButton.setObjectName("yourWorkoutsButton")
                self.frame = QtWidgets.QFrame(self.centralwidget)
                self.frame.setGeometry(QtCore.QRect(80, 140, 631, 291))
                self.frame.setStyleSheet("font: 63 14pt \"BR Cobane SemiBold\";\n"
                "color: rgb(255, 200, 21);")
                self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
                self.frame.setObjectName("frame")
                self.formLayoutWidget_2 = QtWidgets.QWidget(self.frame)
                self.formLayoutWidget_2.setGeometry(QtCore.QRect(70, 0, 601, 291))
                self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
                self.formLayout_2 = QtWidgets.QFormLayout(self.formLayoutWidget_2)
                self.formLayout_2.setLabelAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
                self.formLayout_2.setFormAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
                self.formLayout_2.setContentsMargins(0, 0, 0, 0)
                self.formLayout_2.setObjectName("formLayout_2")
                self.firstNameLabel = QtWidgets.QLabel(self.formLayoutWidget_2)
                self.firstNameLabel.setObjectName("firstNameLabel")
                self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.firstNameLabel)
                self.firstNameOutput = QtWidgets.QLabel(self.formLayoutWidget_2)
                self.firstNameOutput.setText("")
                self.firstNameOutput.setObjectName("firstNameOutput")
                self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.firstNameOutput)
                self.lastNameLabel = QtWidgets.QLabel(self.formLayoutWidget_2)
                self.lastNameLabel.setObjectName("lastNameLabel")
                self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.lastNameLabel)
                self.lastNameOutput = QtWidgets.QLabel(self.formLayoutWidget_2)
                self.lastNameOutput.setText("")
                self.lastNameOutput.setObjectName("lastNameOutput")
                self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lastNameOutput)
                self.emailLabel = QtWidgets.QLabel(self.formLayoutWidget_2)
                self.emailLabel.setObjectName("emailLabel")
                self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.emailLabel)
                self.emailOutput = QtWidgets.QLabel(self.formLayoutWidget_2)
                self.emailOutput.setText("")
                self.emailOutput.setObjectName("emailOutput")
                self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.emailOutput)
                self.phoneLabel = QtWidgets.QLabel(self.formLayoutWidget_2)
                self.phoneLabel.setObjectName("phoneLabel")
                self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.phoneLabel)
                self.phoneOutput = QtWidgets.QLabel(self.formLayoutWidget_2)
                self.phoneOutput.setText("")
                self.phoneOutput.setObjectName("phoneOutput")
                self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.phoneOutput)
                self.sexLabel = QtWidgets.QLabel(self.formLayoutWidget_2)
                self.sexLabel.setObjectName("sexLabel")
                self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.sexLabel)
                self.sexOutput = QtWidgets.QLabel(self.formLayoutWidget_2)
                self.sexOutput.setText("")
                self.sexOutput.setObjectName("sexOutput")
                self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.sexOutput)
                self.dobLabel = QtWidgets.QLabel(self.formLayoutWidget_2)
                self.dobLabel.setObjectName("dobLabel")
                self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.dobLabel)
                self.dobOutput = QtWidgets.QLabel(self.formLayoutWidget_2)
                self.dobOutput.setText("")
                self.dobOutput.setObjectName("dobOutput")
                self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.dobOutput)
                self.weightLabel = QtWidgets.QLabel(self.formLayoutWidget_2)
                self.weightLabel.setObjectName("weightLabel")
                self.formLayout_2.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.weightLabel)
                self.weightOutput = QtWidgets.QLabel(self.formLayoutWidget_2)
                self.weightOutput.setText("")
                self.weightOutput.setObjectName("weightOutput")
                self.formLayout_2.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.weightOutput)
                self.idLabel = QtWidgets.QLabel(self.formLayoutWidget_2)
                self.idLabel.setObjectName("idLabel")
                self.formLayout_2.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.idLabel)
                self.idOutput = QtWidgets.QLabel(self.formLayoutWidget_2)
                self.idOutput.setText("Please scan your ID card")
                self.idOutput.setObjectName("idOutput")
                self.formLayout_2.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.idOutput)
                self.dorLabel = QtWidgets.QLabel(self.formLayoutWidget_2)
                self.dorLabel.setObjectName("dorLabel")
                self.formLayout_2.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.dorLabel)
                self.dorOutput = QtWidgets.QLabel(self.formLayoutWidget_2)
                self.dorOutput.setText("")
                self.dorOutput.setObjectName("dorOutput")
                self.formLayout_2.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.dorOutput)
                self.frame_2 = QtWidgets.QFrame(self.centralwidget)
                self.frame_2.setGeometry(QtCore.QRect(0, 0, 1024, 600))
                self.frame_2.setStyleSheet("background-image: url(:/background/assets/login_bg_reversed.png);")
                self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
                self.frame_2.setObjectName("frame_2")
                self.commandLinkButton = QtWidgets.QCommandLinkButton(self.frame_2)
                self.commandLinkButton.clicked.connect(LoginWindow.close)
                self.commandLinkButton.setGeometry(QtCore.QRect(20, 20, 80, 40))
                self.commandLinkButton.setStyleSheet("color: rgb(255, 200, 21);\n"
                "selection-background-color: rgba(255, 255, 255, 0);\n"
                "selection-color: rgba(255, 255, 255, 0);\n"
                "border: transparent;")
                icon1 = QtGui.QIcon()
                icon1.addPixmap(QtGui.QPixmap("assets/arrow-left-solid-yellow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                self.commandLinkButton.setIcon(icon1)
                self.commandLinkButton.setObjectName("commandLinkButton")
                self.frame_2.raise_()
                self.label.raise_()
                self.startWorkoutButton.raise_()
                self.yourWorkoutsButton.raise_()
                self.frame.raise_()
                LoginWindow.setCentralWidget(self.centralwidget)

                self.retranslateUi(LoginWindow)
                QtCore.QMetaObject.connectSlotsByName(LoginWindow)

        def retranslateUi(self, LoginWindow):
                _translate = QtCore.QCoreApplication.translate
                LoginWindow.setWindowTitle(_translate("LoginWindow", "Login"))
                self.label.setText(_translate("LoginWindow", "THE META-GYM USER LOGIN"))
                self.startWorkoutButton.setText(_translate("LoginWindow", "START WORKOUT"))
                self.yourWorkoutsButton.setText(_translate("LoginWindow", "YOUR WORKOUTS"))
                self.firstNameLabel.setText(_translate("LoginWindow", "First Name:   "))
                self.lastNameLabel.setText(_translate("LoginWindow", "Last Name:   "))
                self.emailLabel.setText(_translate("LoginWindow", "Email:   "))
                self.phoneLabel.setText(_translate("LoginWindow", "Phone Number:   "))
                self.sexLabel.setText(_translate("LoginWindow", "Sex:   "))
                self.dobLabel.setText(_translate("LoginWindow", "Date of Birth:   "))
                self.weightLabel.setText(_translate("LoginWindow", "Weight:   "))
                self.idLabel.setText(_translate("LoginWindow", "ID:   "))
                self.dorLabel.setText(_translate("LoginWindow", "Date of Registration:"))
                self.commandLinkButton.setText(_translate("LoginWindow", "Home"))


import resources_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LoginWindow = QtWidgets.QMainWindow()
    ui = Ui_LoginWindow()
    ui.setupUi(LoginWindow)
    LoginWindow.show()
    sys.exit(app.exec_())

