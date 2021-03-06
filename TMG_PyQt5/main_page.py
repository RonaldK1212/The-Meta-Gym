from PyQt5 import QtCore, QtGui, QtWidgets
import threading
import helper_functions

user_id = 999888777


    


def scan_card():
    global user_id
    scanner = helper_functions.scan_card_f
    while True:
        user_id = scanner()
    

                       
                       
class Ui_MainWindow(object):
    scanner_thread = threading.Thread(target=scan_card)
    
    def registerWindow(self):
        import registration_page 
        self.window = QtWidgets.QMainWindow()
        self.ui = registration_page.Ui_RegisterWindow()
        self.ui.setupUi(self.window)
        self.window.show()
        
        
        
        self.ui.idOutput.setText(str(user_id))
    scanner_thread.start()
    #scanner_thread.join()
    #openRegisterWindow = threading.Thread(target=registerWindow)

    def loginWindow(self):
        import login_page
        from helper_functions import getUserData
        self.window = QtWidgets.QMainWindow()
        self.ui = login_page.Ui_LoginWindow()
        self.ui.setupUi(self.window)
        self.window.show()
        login_page.user_id = str(user_id)
        print('login_page.user_id =  ', login_page.user_id)
        user_data = getUserData(login_page.user_id)
        #print(user_data)
        self.ui.firstNameOutput.setText(str(user_data[0][2]))
        self.ui.lastNameOutput.setText(str(user_data[0][3]))
        self.ui.emailOutput.setText(str(user_data[0][4]))
        self.ui.phoneOutput.setText(str(user_data[0][5]))
        self.ui.sexOutput.setText(str(user_data[0][6]))
        self.ui.dobOutput.setText(str(user_data[0][7]))
        self.ui.weightOutput.setText(str(user_data[0][8]))
        self.ui.idOutput.setText(str(user_data[0][0]))
        self.ui.dorOutput.setText(str(user_data[0][1]))

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1024, 600)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("assets/TMG_Logo_only.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("")
        
        MainWindow.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.loginButton = QtWidgets.QPushButton(self.centralwidget , clicked = lambda: self.loginWindow())
        self.loginButton.setEnabled(True)
        self.loginButton.setGeometry(QtCore.QRect(220, 380, 230, 80))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.loginButton.sizePolicy().hasHeightForWidth())
        self.loginButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("BR Cobane")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        self.loginButton.setFont(font)
        self.loginButton.setAutoFillBackground(False)
        self.loginButton.setStyleSheet("background-color: rgb(41, 41, 41);\n"
        "border: 2px solid rgb(255, 200, 21);\n"
        "color: rgb(255, 200, 21);")
        self.loginButton.setDefault(False)
        self.loginButton.setFlat(False)
        self.loginButton.setObjectName("loginButton")
        self.registerButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.registerWindow())
        #self.registerButton.clicked.connect(MainWindow.close)
        self.registerButton.setGeometry(QtCore.QRect(570, 380, 230, 80))
        font = QtGui.QFont()
        font.setFamily("BR Cobane")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.registerButton.setFont(font)
        self.registerButton.setAutoFillBackground(False)
        self.registerButton.setStyleSheet("color: rgb(41, 41, 41);\n"
        "border-color: rgba(255, 255, 255, 0);\n"
        "background-color: rgb(255, 200, 21);\n"
        "border: transparent;\n"
        "alternate-background-color: rgb(41, 41, 41);\n"
        "")
        self.registerButton.setAutoDefault(False)
        self.registerButton.setDefault(False)
        self.registerButton.setFlat(False)
        self.registerButton.setObjectName("registerButton")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setEnabled(True)
        self.frame.setGeometry(QtCore.QRect(0, 0, 1024, 600))
        self.frame.setStyleSheet("background-image: url(:/background/assets/main.png);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame.raise_()
        self.loginButton.raise_()
        self.registerButton.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.loginButton, self.registerButton)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Home"))
        self.loginButton.setText(_translate("MainWindow", "LOGIN"))
        self.registerButton.setText(_translate("MainWindow", "REGISTER"))
        

       # ui.idOutput.setText(user_id)
    
    

import resources_rc



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
