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
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1092, 643)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        MainWindow.setToolTip("")
        MainWindow.setStatusTip("")
        MainWindow.setWhatsThis("")
        MainWindow.setAccessibleName("")
        MainWindow.setAccessibleDescription("")
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
        self.Eyemouselabel.setGeometry(QtCore.QRect(170, 0, 761, 91))
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
        self.cameralabel_3.setGeometry(QtCore.QRect(310, 560, 421, 61))
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
        self.cameralabel_4.setGeometry(QtCore.QRect(310, 590, 421, 61))
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
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "EYE MOUSE "))
        self.EnterButton.setText(_translate("MainWindow", "Enter"))
        self.EnterButton.setShortcut(_translate("MainWindow", "Return"))
        self.Eyemouselabel.setText(_translate("MainWindow", "Eye Mouse Controller"))
        self.cameralabel.setText(_translate("MainWindow", "Camera Number"))
        self.lineEdit.setText(_translate("MainWindow", "1"))
        self.cameralabel_3.setText(_translate("MainWindow", "NOTE: Only one person in frame is needed for program to work fine"))
        self.cameralabel_4.setText(_translate("MainWindow", "If no result after pressing enter then camera number is wrong "))
    def Enterbuttonclicked(self):#this function is added manually too
        camerainput=int(self.lineEdit.text())
        eyemouse=eyetracking.eye_mouse(camerainput)
        eyemouse.eyetrack()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
