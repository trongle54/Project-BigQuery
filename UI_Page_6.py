# Form implementation generated from reading ui file 'GUI_Trang_6.ui'
#
# Created by: PyQt6 UI code generator 6.6.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
from Out_file_images import qt_resource_data
from Prediction_Feature import Prediction as ClickMethod


class Ui_MainWindow_Page_6(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 974)
        MainWindow.setMinimumSize(QtCore.QSize(0, 974))
        MainWindow.setLayoutDirection(QtCore.Qt.LayoutDirection.RightToLeft)
        MainWindow.setStyleSheet("background-image: url(:/newPrefix/desktop.png);")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_3 = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame_3.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Expanding,
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setMaximumSize(QtCore.QSize(16777, 16777))
        self.frame_3.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.frame = QtWidgets.QFrame(parent=self.frame_3)
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(parent=self.frame)
        font = QtGui.QFont()
        font.setFamily("American Typewriter")
        font.setPointSize(48)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(
            "color: rgb(49, 17, 29);\n"
            'font: 48pt "American Typewriter";\n'
            "font-weight:bold;"
        )
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(
            self.label_2,
            0,
            QtCore.Qt.AlignmentFlag.AlignHCenter | QtCore.Qt.AlignmentFlag.AlignBottom,
        )
        self.frame_2 = QtWidgets.QFrame(parent=self.frame)
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_6 = QtWidgets.QFrame(parent=self.frame_2)
        self.frame_6.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_6.setObjectName("frame_6")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_6)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_10 = QtWidgets.QFrame(parent=self.frame_6)
        self.frame_10.setStyleSheet(
            "background-color: rgb(255, 216, 228);\n"
            "border-style: solid;\n"
            "border-color: black;\n"
            "border-radius: 30px;\n"
            "border-style: solid;"
        )
        self.frame_10.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_10.setObjectName("frame_10")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.frame_10)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.lineEdit_NhapID = QtWidgets.QLineEdit(parent=self.frame_10)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lineEdit_NhapID.setFont(font)
        self.lineEdit_NhapID.setObjectName("lineEdit_NhapID")
        self.horizontalLayout_12.addWidget(self.lineEdit_NhapID)
        self.label__NhapID = QtWidgets.QLabel(parent=self.frame_10)
        font = QtGui.QFont()
        font.setFamily("American Typewriter")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label__NhapID.setFont(font)
        self.label__NhapID.setStyleSheet(
            "color: rgb(49, 17, 29);\n" 'font: 20pt "American Typewriter";'
        )
        self.label__NhapID.setObjectName("label__NhapID")
        self.horizontalLayout_12.addWidget(self.label__NhapID)
        self.horizontalLayout_2.addWidget(self.frame_10)
        self.verticalLayout_3.addWidget(self.frame_6)
        self.pushButton = QtWidgets.QPushButton(parent=self.frame_2)
        self.pushButton.setMinimumSize(QtCore.QSize(200, 40))
        self.pushButton.setMaximumSize(QtCore.QSize(16777215, 200))
        self.pushButton.setStyleSheet(
            "background-color: rgb(153, 102, 51);\n"
            "border-style: solid;\n"
            "border-radius: 20px;\n"
            "\n"
            "color: rgb(49, 17, 29);\n"
            'font: 20pt "American Typewriter";'
        )
        icon = QtGui.QIcon()
        icon.addPixmap(
            QtGui.QPixmap(":/newPrefix/srearch.png"),
            QtGui.QIcon.Mode.Normal,
            QtGui.QIcon.State.Off,
        )
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(28, 28))
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_3.addWidget(
            self.pushButton, 0, QtCore.Qt.AlignmentFlag.AlignHCenter
        )
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.frame_2)
        self.pushButton_2.setMinimumSize(QtCore.QSize(300, 40))
        self.pushButton_2.setMaximumSize(QtCore.QSize(16777215, 200))
        self.pushButton_2.setStyleSheet(
            "background-color: rgb(153, 102, 51);\n"
            "border-style: solid;\n"
            "border-radius: 20px;\n"
            "\n"
            "color: rgb(49, 17, 29);\n"
            'font: 20pt "American Typewriter";'
        )
        icon1 = QtGui.QIcon()
        icon1.addPixmap(
            QtGui.QPixmap(":/newPrefix/clearn-removebg-preview.png"),
            QtGui.QIcon.Mode.Normal,
            QtGui.QIcon.State.Off,
        )
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setIconSize(QtCore.QSize(18, 18))
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_3.addWidget(
            self.pushButton_2,
            0,
            QtCore.Qt.AlignmentFlag.AlignHCenter | QtCore.Qt.AlignmentFlag.AlignVCenter,
        )
        self.verticalLayout_2.addWidget(self.frame_2)
        self.verticalLayout_4.addWidget(
            self.frame, 0, QtCore.Qt.AlignmentFlag.AlignVCenter
        )
        self.horizontalLayout.addWidget(self.frame_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # click Method
        self.pushButton_2.clicked.connect(self.clear_text)

        # click Method
        self.pushButton.clicked.connect(
            lambda: ClickMethod.clickMethod_prediction(self)
        )

    def clear_text(self):
        self.lineEdit_NhapID.clear()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(
            _translate("MainWindow", "Dự đoán hiệu suất làm việc")
        )
        self.label_2.setText(_translate("MainWindow", "DỰ ĐOÁN NĂNG SUẤT LÀM VIỆC"))
        self.lineEdit_NhapID.setPlaceholderText(
            _translate("MainWindow", "Nhập ID nhân viên...")
        )
        self.label__NhapID.setText(_translate("MainWindow", "Nhập Mã ID"))
        self.pushButton.setText(_translate("MainWindow", "  Tra Cứu Thông Tin"))
        self.pushButton_2.setText(
            _translate("MainWindow", "    Xóa để nhập lại thông tin")
        )
