# Form implementation generated from reading ui file 'GUI_Trang_3_V3.ui'
#
# Created by: PyQt6 UI code generator 6.6.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
from APIHandler import APIHandler as ClickMethod


class Ui_MainWindow_Page_3(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1057, 974)
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
        self.frame_6.setStyleSheet(
            "background-color: rgb(255, 216, 228);\n"
            "border-style: solid;\n"
            "border-color: black;\n"
            "border-radius: 30px;\n"
            "border-style: solid;"
        )
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
        self.frame_7 = QtWidgets.QFrame(parent=self.frame_2)
        self.frame_7.setStyleSheet(
            "background-color: rgb(255, 216, 228);\n"
            "border-style: solid;\n"
            "border-color: black;\n"
            "border-radius: 30px;\n"
            "border-style: solid;"
        )
        self.frame_7.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_7.setObjectName("frame_7")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frame_7)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.frame_15 = QtWidgets.QFrame(parent=self.frame_7)
        self.frame_15.setStyleSheet(
            "background-color: rgb(255, 216, 228);\n"
            "border-style: solid;\n"
            "border-color: black;\n"
            "border-radius: 30px;\n"
            "border-style: solid;"
        )
        self.frame_15.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_15.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_15.setObjectName("frame_15")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.frame_15)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.dateEdit_FromDay = QtWidgets.QDateEdit(parent=self.frame_15)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.dateEdit_FromDay.sizePolicy().hasHeightForWidth()
        )
        self.dateEdit_FromDay.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.dateEdit_FromDay.setFont(font)
        self.dateEdit_FromDay.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.dateEdit_FromDay.setReadOnly(False)
        self.dateEdit_FromDay.setButtonSymbols(
            QtWidgets.QAbstractSpinBox.ButtonSymbols.NoButtons
        )
        self.dateEdit_FromDay.setCorrectionMode(
            QtWidgets.QAbstractSpinBox.CorrectionMode.CorrectToPreviousValue
        )
        self.dateEdit_FromDay.setDate(QtCore.QDate(2023, 11, 12))
        self.dateEdit_FromDay.setObjectName("dateEdit_FromDay")
        self.horizontalLayout_13.addWidget(self.dateEdit_FromDay)
        self.label_FromDay = QtWidgets.QLabel(parent=self.frame_15)
        font = QtGui.QFont()
        font.setFamily("American Typewriter")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_FromDay.setFont(font)
        self.label_FromDay.setStyleSheet(
            "color: rgb(49, 17, 29);\n" 'font: 20pt "American Typewriter";'
        )
        self.label_FromDay.setObjectName("label_FromDay")
        self.horizontalLayout_13.addWidget(self.label_FromDay)
        self.horizontalLayout_7.addWidget(self.frame_15)
        self.verticalLayout_3.addWidget(self.frame_7)
        self.frame_8 = QtWidgets.QFrame(parent=self.frame_2)
        self.frame_8.setStyleSheet(
            "background-color: rgb(255, 216, 228);\n"
            "border-style: solid;\n"
            "border-color: black;\n"
            "border-radius: 30px;\n"
            "border-style: solid;"
        )
        self.frame_8.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_8.setObjectName("frame_8")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.frame_8)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.frame_16 = QtWidgets.QFrame(parent=self.frame_8)
        self.frame_16.setStyleSheet(
            "background-color: rgb(255, 216, 228);\n"
            "border-style: solid;\n"
            "border-color: black;\n"
            "border-radius: 30px;\n"
            "border-style: solid;"
        )
        self.frame_16.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_16.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_16.setObjectName("frame_16")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout(self.frame_16)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.dateEdit_ToDay = QtWidgets.QDateEdit(parent=self.frame_16)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Expanding,
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.dateEdit_ToDay.sizePolicy().hasHeightForWidth()
        )
        self.dateEdit_ToDay.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.dateEdit_ToDay.setFont(font)
        self.dateEdit_ToDay.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.dateEdit_ToDay.setButtonSymbols(
            QtWidgets.QAbstractSpinBox.ButtonSymbols.NoButtons
        )
        self.dateEdit_ToDay.setDate(QtCore.QDate(2023, 12, 12))
        self.dateEdit_ToDay.setObjectName("dateEdit_ToDay")
        self.horizontalLayout_14.addWidget(self.dateEdit_ToDay)
        self.label_ToDay = QtWidgets.QLabel(parent=self.frame_16)
        font = QtGui.QFont()
        font.setFamily("American Typewriter")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_ToDay.setFont(font)
        self.label_ToDay.setStyleSheet(
            "color: rgb(49, 17, 29);\n" 'font: 20pt "American Typewriter";'
        )
        self.label_ToDay.setObjectName("label_ToDay")
        self.horizontalLayout_14.addWidget(self.label_ToDay)
        self.horizontalLayout_8.addWidget(self.frame_16)
        self.verticalLayout_3.addWidget(self.frame_8)
        self.pushButton = QtWidgets.QPushButton(parent=self.frame_2)
        self.pushButton.setMinimumSize(QtCore.QSize(250, 40))
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
        self.tableWidget = QtWidgets.QTableWidget(parent=self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Ignored
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.tableWidget.setAutoFillBackground(True)
        self.tableWidget.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.tableWidget.setLineWidth(0)
        self.tableWidget.setVerticalScrollBarPolicy(
            QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff
        )
        self.tableWidget.setHorizontalScrollBarPolicy(
            QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff
        )
        self.tableWidget.setSizeAdjustPolicy(
            QtWidgets.QAbstractScrollArea.SizeAdjustPolicy.AdjustToContentsOnFirstShow
        )
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setGridStyle(QtCore.Qt.PenStyle.DashLine)
        self.tableWidget.setWordWrap(True)
        self.tableWidget.setCornerButtonEnabled(True)
        self.tableWidget.setRowCount(10)
        self.tableWidget.setColumnCount(8)
        self.tableWidget.setObjectName("tableWidget")
        item = QtWidgets.QTableWidgetItem()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.NoBrush)
        item.setForeground(brush)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(False)
        self.verticalLayout_4.addWidget(
            self.tableWidget,
            0,
            QtCore.Qt.AlignmentFlag.AlignHCenter | QtCore.Qt.AlignmentFlag.AlignVCenter,
        )
        self.horizontalLayout.addWidget(self.frame_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # click Method
        self.pushButton.clicked.connect(
            lambda: ClickMethod.clickMethod_timesheets(self)
        )
        # click Method
        self.pushButton_2.clicked.connect(self.clear_text)

    def clear_text(self):
        self.lineEdit_NhapID.clear()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Bảng chấm công "))
        self.label_2.setText(_translate("MainWindow", "BẢNG CHẤM CÔNG NHÂN VIÊN"))
        self.lineEdit_NhapID.setPlaceholderText(
            _translate("MainWindow", "Nhập ID nhân viên...")
        )
        self.label__NhapID.setText(_translate("MainWindow", "Nhập ID"))
        self.dateEdit_FromDay.setDisplayFormat(_translate("MainWindow", "yyyy-MM-dd"))
        self.label_FromDay.setText(_translate("MainWindow", "Nhập Ngày Bắt Đầu"))
        self.dateEdit_ToDay.setDisplayFormat(_translate("MainWindow", "yyyy-MM-dd"))
        self.label_ToDay.setText(_translate("MainWindow", "Nhập Ngày Kết Thúc"))
        self.pushButton.setText(_translate("MainWindow", "   Tra Cứu Thông Tin"))
        self.pushButton_2.setText(
            _translate("MainWindow", "    Xóa để nhập lại thông tin")
        )
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Mã số NV"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Ngày công"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Lương cơ bản"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Phụ cấp onsite"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Ăn trưa"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Tổng thu nhập"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "BHXH"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Thực nhận"))
