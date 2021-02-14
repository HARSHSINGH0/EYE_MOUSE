from PyQt5 import QtCore, QtGui, QtWidgets
import eyetracking
from PyQt5 import sip
import cv2 as cv
cv2=cv
import dlib
import mousecontrol_eye
from win32.win32api import GetSystemMetrics
from pynput.mouse import Listener,Button,Controller
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import time 
import webbrowser

class Ui_MainWindow(object):
    def __init__(self):
        self.f=open("cameranumbersaved.txt","r+")#this is for saved camera number to access on startup
        self.cameranumbersaved=self.f.read()
        if(self.cameranumbersaved==""):
            open("cameranumbersaved.txt","r+").write("1")#this will save default value 1 if no number is saved in cameranumbersaved
            self.cameranumbersaved=self.f.read()
        self.f.close()
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1092, 684)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setToolTip("")
        MainWindow.setStatusTip("")
        MainWindow.setWhatsThis("")
        MainWindow.setAccessibleName("")
        MainWindow.setAccessibleDescription("")
        MainWindow.setAutoFillBackground(False)
        MainWindow.setWindowFilePath("")
        MainWindow.setDocumentMode(False)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        MainWindow.setDockNestingEnabled(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.EnterButton = QtWidgets.QPushButton(self.centralwidget)
        self.EnterButton.setGeometry(QtCore.QRect(590, 520, 121, 51))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(18)
        self.EnterButton.setFont(font)
        self.EnterButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.EnterButton.setIconSize(QtCore.QSize(16, 16))
        self.EnterButton.setObjectName("EnterButton")
        self.EnterButton.clicked.connect(self.Enterbuttonclicked)
        self.Eyemouselabel = QtWidgets.QLabel(self.centralwidget)
        self.Eyemouselabel.setGeometry(QtCore.QRect(130, -10, 761, 91))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Eyemouselabel.sizePolicy().hasHeightForWidth())
        self.Eyemouselabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.Eyemouselabel.setFont(font)
        self.Eyemouselabel.setTextFormat(QtCore.Qt.AutoText)
        self.Eyemouselabel.setAlignment(QtCore.Qt.AlignCenter)
        self.Eyemouselabel.setWordWrap(False)
        self.Eyemouselabel.setObjectName("Eyemouselabel")
        self.instructionimagelabel = QtWidgets.QLabel(self.centralwidget)
        self.instructionimagelabel.setGeometry(QtCore.QRect(180, 70, 721, 441))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.instructionimagelabel.sizePolicy().hasHeightForWidth())
        self.instructionimagelabel.setSizePolicy(sizePolicy)
        self.instructionimagelabel.setText("")
        self.instructionimagelabel.setPixmap(QtGui.QPixmap("instruction.png"))
        self.instructionimagelabel.setAlignment(QtCore.Qt.AlignCenter)
        self.instructionimagelabel.setObjectName("instructionimagelabel")
        self.cameralabel = QtWidgets.QLabel(self.centralwidget)
        self.cameralabel.setGeometry(QtCore.QRect(310, 510, 211, 61))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cameralabel.sizePolicy().hasHeightForWidth())
        self.cameralabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.cameralabel.setFont(font)
        self.cameralabel.setTextFormat(QtCore.Qt.AutoText)
        self.cameralabel.setAlignment(QtCore.Qt.AlignCenter)
        self.cameralabel.setWordWrap(False)
        self.cameralabel.setObjectName("cameralabel")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(530, 520, 51, 51))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(18)
        self.lineEdit.setFont(font)
        self.lineEdit.setMaxLength(1)
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.cameralabel_3 = QtWidgets.QLabel(self.centralwidget)
        self.cameralabel_3.setGeometry(QtCore.QRect(310, 590, 421, 61))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cameralabel_3.sizePolicy().hasHeightForWidth())
        self.cameralabel_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.cameralabel_3.setFont(font)
        self.cameralabel_3.setTextFormat(QtCore.Qt.AutoText)
        self.cameralabel_3.setAlignment(QtCore.Qt.AlignCenter)
        self.cameralabel_3.setWordWrap(False)
        self.cameralabel_3.setObjectName("cameralabel_3")
        self.cameralabel_4 = QtWidgets.QLabel(self.centralwidget)
        self.cameralabel_4.setGeometry(QtCore.QRect(310, 620, 421, 61))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cameralabel_4.sizePolicy().hasHeightForWidth())
        self.cameralabel_4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.cameralabel_4.setFont(font)
        self.cameralabel_4.setTextFormat(QtCore.Qt.AutoText)
        self.cameralabel_4.setAlignment(QtCore.Qt.AlignCenter)
        self.cameralabel_4.setWordWrap(False)
        self.cameralabel_4.setObjectName("cameralabel_4")
        self.cameralabel_5 = QtWidgets.QLabel(self.centralwidget)
        self.cameralabel_5.setGeometry(QtCore.QRect(420, 560, 111, 61))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cameralabel_5.sizePolicy().hasHeightForWidth())
        self.cameralabel_5.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.cameralabel_5.setFont(font)
        self.cameralabel_5.setTextFormat(QtCore.Qt.AutoText)
        self.cameralabel_5.setAlignment(QtCore.Qt.AlignCenter)
        self.cameralabel_5.setWordWrap(False)
        self.cameralabel_5.setObjectName("cameralabel_5")
        self.inversecameracheck = QtWidgets.QCheckBox(self.centralwidget)
        self.inversecameracheck.setGeometry(QtCore.QRect(540, 580, 20, 21))
        self.inversecameracheck.setAutoFillBackground(False)
        self.inversecameracheck.setText("")
        self.inversecameracheck.setIconSize(QtCore.QSize(16, 16))
        self.inversecameracheck.setObjectName("inversecameracheck")
        self.GithubLogo = QtWidgets.QLabel(self.centralwidget)
        self.GithubLogo.setGeometry(QtCore.QRect(660, 0, 71, 71))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.GithubLogo.sizePolicy().hasHeightForWidth())
        self.GithubLogo.setSizePolicy(sizePolicy)
        self.GithubLogo.setText("")
        self.GithubLogo.setPixmap(QtGui.QPixmap("githublogo.png"))
        self.GithubLogo.setAlignment(QtCore.Qt.AlignCenter)
        self.GithubLogo.setObjectName("GithubLogo")
        self.GithubButton = QtWidgets.QPushButton(self.centralwidget)
        self.GithubButton.setGeometry(QtCore.QRect(660, 0, 71, 71))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(18)
        self.GithubButton.setFont(font)
        self.GithubButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.GithubButton.setStyleSheet("\n"
"background-color: rgba(255, 255, 255, 0);")
        self.GithubButton.setText("")
        self.GithubButton.setIconSize(QtCore.QSize(16, 16))
        self.GithubButton.setObjectName("GithubButton")
        url="https://github.com/HARSHSINGH0/EYE_MOUSE"
        self.GithubButton.clicked.connect(lambda:self.linktogithub(url))#edited
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Eye Mouse Controller"))
        self.EnterButton.setText(_translate("MainWindow", "Enter"))
        self.EnterButton.setShortcut(_translate("MainWindow", "Return"))
        self.Eyemouselabel.setText(_translate("MainWindow", "Eye Mouse Controller"))
        self.cameralabel.setText(_translate("MainWindow", "Camera Number"))
        self.lineEdit.setText(_translate("MainWindow", "1"))
        self.cameralabel_3.setText(_translate("MainWindow", "NOTE: Only one person in frame is needed for program to work fine"))
        self.cameralabel_4.setText(_translate("MainWindow", "If no result after pressing enter then camera number is wrong "))
        self.cameralabel_5.setText(_translate("MainWindow", "Inverse Camera:"))
        self.GithubButton.setShortcut(_translate("MainWindow", "Return"))
    def Enterbuttonclicked(self,savedornot):#this function is added manually too
        try:
            if savedornot==False:#this will only run if cameranumbersaved file has some value
                camerainput=int(self.lineEdit.text())
                cameracheck=self.inversecameracheck.isChecked()
                open("cameranumbersaved.txt","r+").truncate()
                if camerainput==None:#this is no values in camernumbersaved file:ValueError: invalid literal for int() with base 10: ''
                    camerainput=1

                open("cameranumbersaved.txt","r+").write(str(camerainput))#this will save previous used camera number data for easy use
                eyemouse=eyetracking.eye_mouse(camerainput,cameracheck)
                eyemouse.eyetrack()
            else:
                self.lineEdit.setText(self.cameranumbersaved)
                camerainput=int(self.lineEdit.text())#this runs on startup and prints value
                cameracheck=self.inversecameracheck.isChecked()
                eyemouse=eyetracking.eye_mouse(camerainput,cameracheck)
                eyemouse.eyetrack()
        except(Exception):
            pass
    def linktogithub(self, link):
        self.link=link
        webbrowser.open(self.link, new=0)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    ui.Enterbuttonclicked(True)#this is for running it on startup of program without any clicks
    sys.exit(app.exec_())
