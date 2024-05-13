# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Main.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
    QGridLayout, QGroupBox, QHBoxLayout, QLabel,
    QLayout, QMainWindow, QMenu, QMenuBar,
    QProgressBar, QPushButton, QSizePolicy, QStatusBar,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1024, 768)
        MainWindow.setMinimumSize(QSize(1024, 768))
        MainWindow.setBaseSize(QSize(1280, 800))
        font = QFont()
        font.setFamilies([u"Product Sans"])
        MainWindow.setFont(font)
        icon = QIcon()
        icon.addFile(u"check-mark.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.actionQuit = QAction(MainWindow)
        self.actionQuit.setObjectName(u"actionQuit")
        self.actionGuide = QAction(MainWindow)
        self.actionGuide.setObjectName(u"actionGuide")
        self.actionAbout_Software = QAction(MainWindow)
        self.actionAbout_Software.setObjectName(u"actionAbout_Software")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(1024, 768))
        self.centralwidget.setMaximumSize(QSize(1920, 1080))
        self.centralwidget.setSizeIncrement(QSize(0, 0))
        self.centralwidget.setBaseSize(QSize(1280, 800))
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(16777215, 50))
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.AppTitle = QLabel(self.frame)
        self.AppTitle.setObjectName(u"AppTitle")
        self.AppTitle.setMaximumSize(QSize(16777215, 50))
        font1 = QFont()
        font1.setFamilies([u"Product Sans Medium"])
        font1.setPointSize(16)
        self.AppTitle.setFont(font1)
        self.AppTitle.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.AppTitle)


        self.verticalLayout_2.addWidget(self.frame)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMaximumSize(QSize(16777215, 100))
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.groupBox = QGroupBox(self.frame_2)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMaximumSize(QSize(1000, 100))
        self.groupBox.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.gridLayout.setHorizontalSpacing(20)
        self.gridLayout.setVerticalSpacing(0)
        self.gridLayout.setContentsMargins(10, 10, 10, 10)
        self.OkButton = QPushButton(self.groupBox)
        self.OkButton.setObjectName(u"OkButton")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.OkButton.sizePolicy().hasHeightForWidth())
        self.OkButton.setSizePolicy(sizePolicy)
        self.OkButton.setMaximumSize(QSize(400, 200))

        self.gridLayout.addWidget(self.OkButton, 6, 2, 1, 1)

        self.ComboCam = QComboBox(self.groupBox)
        self.ComboCam.setObjectName(u"ComboCam")
        sizePolicy.setHeightForWidth(self.ComboCam.sizePolicy().hasHeightForWidth())
        self.ComboCam.setSizePolicy(sizePolicy)
        self.ComboCam.setSizeAdjustPolicy(QComboBox.SizeAdjustPolicy.AdjustToContents)

        self.gridLayout.addWidget(self.ComboCam, 6, 1, 1, 1)

        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        font2 = QFont()
        font2.setFamilies([u"Product Sans"])
        font2.setPointSize(10)
        self.label.setFont(font2)
        self.label.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)

        self.gridLayout.addWidget(self.label, 5, 0, 1, 1)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font2)
        self.label_2.setScaledContents(False)
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)

        self.gridLayout.addWidget(self.label_2, 5, 1, 1, 1)

        self.ComboPort = QComboBox(self.groupBox)
        self.ComboPort.setObjectName(u"ComboPort")
        sizePolicy.setHeightForWidth(self.ComboPort.sizePolicy().hasHeightForWidth())
        self.ComboPort.setSizePolicy(sizePolicy)
        self.ComboPort.setSizeAdjustPolicy(QComboBox.SizeAdjustPolicy.AdjustToContents)

        self.gridLayout.addWidget(self.ComboPort, 6, 0, 1, 1)

        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setColumnStretch(1, 1)

        self.horizontalLayout_2.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.frame_2)
        self.groupBox_2.setObjectName(u"groupBox_2")
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setFlat(False)
        self.groupBox_2.setCheckable(False)
        self.horizontalLayout = QHBoxLayout(self.groupBox_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.AutoButton = QPushButton(self.groupBox_2)
        self.AutoButton.setObjectName(u"AutoButton")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.AutoButton.sizePolicy().hasHeightForWidth())
        self.AutoButton.setSizePolicy(sizePolicy1)
        self.AutoButton.setMaximumSize(QSize(500, 100))
        font3 = QFont()
        font3.setFamilies([u"Product Sans"])
        font3.setBold(True)
        self.AutoButton.setFont(font3)

        self.horizontalLayout.addWidget(self.AutoButton)

        self.ManualButton = QPushButton(self.groupBox_2)
        self.ManualButton.setObjectName(u"ManualButton")
        sizePolicy1.setHeightForWidth(self.ManualButton.sizePolicy().hasHeightForWidth())
        self.ManualButton.setSizePolicy(sizePolicy1)
        self.ManualButton.setMaximumSize(QSize(500, 100))
        self.ManualButton.setFont(font3)

        self.horizontalLayout.addWidget(self.ManualButton)


        self.horizontalLayout_2.addWidget(self.groupBox_2)


        self.verticalLayout_2.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMaximumSize(QSize(1920, 1080))
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setSpacing(6)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(10, 10, 10, 10)
        self.groupBox_4 = QGroupBox(self.frame_3)
        self.groupBox_4.setObjectName(u"groupBox_4")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.groupBox_4.sizePolicy().hasHeightForWidth())
        self.groupBox_4.setSizePolicy(sizePolicy2)
        self.groupBox_4.setMinimumSize(QSize(0, 70))
        self.groupBox_4.setMaximumSize(QSize(500, 80))
        self.horizontalLayout_4 = QHBoxLayout(self.groupBox_4)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.StartButton = QPushButton(self.groupBox_4)
        self.StartButton.setObjectName(u"StartButton")
        sizePolicy2.setHeightForWidth(self.StartButton.sizePolicy().hasHeightForWidth())
        self.StartButton.setSizePolicy(sizePolicy2)
        self.StartButton.setFont(font3)

        self.horizontalLayout_4.addWidget(self.StartButton)

        self.StopButton = QPushButton(self.groupBox_4)
        self.StopButton.setObjectName(u"StopButton")
        sizePolicy1.setHeightForWidth(self.StopButton.sizePolicy().hasHeightForWidth())
        self.StopButton.setSizePolicy(sizePolicy1)
        self.StopButton.setMaximumSize(QSize(300, 100))
        self.StopButton.setFont(font3)

        self.horizontalLayout_4.addWidget(self.StopButton)


        self.verticalLayout_4.addWidget(self.groupBox_4)

        self.groupBox_3 = QGroupBox(self.frame_3)
        self.groupBox_3.setObjectName(u"groupBox_3")
        sizePolicy2.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy2)
        self.groupBox_3.setMaximumSize(QSize(500, 80))
        self.horizontalLayout_3 = QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.GripButton = QPushButton(self.groupBox_3)
        self.GripButton.setObjectName(u"GripButton")
        sizePolicy2.setHeightForWidth(self.GripButton.sizePolicy().hasHeightForWidth())
        self.GripButton.setSizePolicy(sizePolicy2)
        self.GripButton.setFont(font3)

        self.horizontalLayout_3.addWidget(self.GripButton)

        self.RotateButton = QPushButton(self.groupBox_3)
        self.RotateButton.setObjectName(u"RotateButton")
        sizePolicy1.setHeightForWidth(self.RotateButton.sizePolicy().hasHeightForWidth())
        self.RotateButton.setSizePolicy(sizePolicy1)
        self.RotateButton.setMaximumSize(QSize(300, 100))
        self.RotateButton.setFont(font3)

        self.horizontalLayout_3.addWidget(self.RotateButton)


        self.verticalLayout_4.addWidget(self.groupBox_3)

        self.CaptureButton = QPushButton(self.frame_3)
        self.CaptureButton.setObjectName(u"CaptureButton")
        self.CaptureButton.setMinimumSize(QSize(0, 40))
        self.CaptureButton.setFont(font3)

        self.verticalLayout_4.addWidget(self.CaptureButton)

        self.groupBox_5 = QGroupBox(self.frame_3)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setMaximumSize(QSize(500, 600))
        self.GRcheck = QCheckBox(self.groupBox_5)
        self.GRcheck.setObjectName(u"GRcheck")
        self.GRcheck.setGeometry(QRect(30, 40, 76, 20))
        self.NRcheck = QCheckBox(self.groupBox_5)
        self.NRcheck.setObjectName(u"NRcheck")
        self.NRcheck.setGeometry(QRect(30, 70, 131, 20))
        self.Histocheck = QCheckBox(self.groupBox_5)
        self.Histocheck.setObjectName(u"Histocheck")
        self.Histocheck.setGeometry(QRect(30, 100, 111, 20))
        self.checkBox_7 = QCheckBox(self.groupBox_5)
        self.checkBox_7.setObjectName(u"checkBox_7")
        self.checkBox_7.setGeometry(QRect(30, 130, 111, 20))
        self.checkBox_8 = QCheckBox(self.groupBox_5)
        self.checkBox_8.setObjectName(u"checkBox_8")
        self.checkBox_8.setGeometry(QRect(30, 190, 121, 20))
        self.checkBox_9 = QCheckBox(self.groupBox_5)
        self.checkBox_9.setObjectName(u"checkBox_9")
        self.checkBox_9.setGeometry(QRect(30, 160, 131, 20))

        self.verticalLayout_4.addWidget(self.groupBox_5)


        self.horizontalLayout_5.addLayout(self.verticalLayout_4)

        self.frame_4 = QFrame(self.frame_3)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMaximumSize(QSize(1500, 16777215))
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_4)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.OriCamlabel = QLabel(self.frame_4)
        self.OriCamlabel.setObjectName(u"OriCamlabel")
        self.OriCamlabel.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.gridLayout_2.addWidget(self.OriCamlabel, 1, 0, 1, 1)

        self.ProcessedCapturedLabel = QLabel(self.frame_4)
        self.ProcessedCapturedLabel.setObjectName(u"ProcessedCapturedLabel")
        self.ProcessedCapturedLabel.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.gridLayout_2.addWidget(self.ProcessedCapturedLabel, 1, 1, 2, 1)

        self.groupBox_6 = QGroupBox(self.frame_4)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.groupBox_6.setMaximumSize(QSize(16777215, 100))
        self.gridLayout_3 = QGridLayout(self.groupBox_6)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.StoppButton = QPushButton(self.groupBox_6)
        self.StoppButton.setObjectName(u"StoppButton")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.StoppButton.sizePolicy().hasHeightForWidth())
        self.StoppButton.setSizePolicy(sizePolicy3)
        self.StoppButton.setFont(font3)

        self.gridLayout_3.addWidget(self.StoppButton, 0, 1, 2, 1)

        self.InspectButton = QPushButton(self.groupBox_6)
        self.InspectButton.setObjectName(u"InspectButton")
        sizePolicy3.setHeightForWidth(self.InspectButton.sizePolicy().hasHeightForWidth())
        self.InspectButton.setSizePolicy(sizePolicy3)
        self.InspectButton.setFont(font3)

        self.gridLayout_3.addWidget(self.InspectButton, 0, 0, 2, 1)

        self.progressBar = QProgressBar(self.groupBox_6)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(0)

        self.gridLayout_3.addWidget(self.progressBar, 0, 2, 1, 1)

        self.statsLabel = QLabel(self.groupBox_6)
        self.statsLabel.setObjectName(u"statsLabel")
        font4 = QFont()
        font4.setFamilies([u"Product Sans Black"])
        font4.setPointSize(20)
        self.statsLabel.setFont(font4)
        self.statsLabel.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.statsLabel.setIndent(2)

        self.gridLayout_3.addWidget(self.statsLabel, 1, 2, 1, 1)


        self.gridLayout_2.addWidget(self.groupBox_6, 0, 0, 1, 2)

        self.ProcessedCamlabel = QLabel(self.frame_4)
        self.ProcessedCamlabel.setObjectName(u"ProcessedCamlabel")
        self.ProcessedCamlabel.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.gridLayout_2.addWidget(self.ProcessedCamlabel, 2, 0, 1, 1)


        self.horizontalLayout_5.addWidget(self.frame_4)

        self.horizontalLayout_5.setStretch(1, 3)

        self.verticalLayout_2.addWidget(self.frame_3)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1024, 21))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuFile.addAction(self.actionQuit)
        self.menuHelp.addAction(self.actionGuide)
        self.menuHelp.addAction(self.actionAbout_Software)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionQuit.setText(QCoreApplication.translate("MainWindow", u"Quit", None))
        self.actionGuide.setText(QCoreApplication.translate("MainWindow", u"Guide", None))
        self.actionAbout_Software.setText(QCoreApplication.translate("MainWindow", u"About Software..", None))
        self.AppTitle.setText(QCoreApplication.translate("MainWindow", u"Recorder Inspection Monitor", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Initialization", None))
        self.OkButton.setText(QCoreApplication.translate("MainWindow", u"Confirm", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Select COM port", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Select Camera Device", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Program Mode", None))
        self.AutoButton.setText(QCoreApplication.translate("MainWindow", u"AUTO", None))
        self.ManualButton.setText(QCoreApplication.translate("MainWindow", u"MANUAL", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"Camera Command", None))
        self.StartButton.setText(QCoreApplication.translate("MainWindow", u"START", None))
        self.StopButton.setText(QCoreApplication.translate("MainWindow", u"STOP", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Holder Command", None))
        self.GripButton.setText(QCoreApplication.translate("MainWindow", u"GRIP", None))
        self.RotateButton.setText(QCoreApplication.translate("MainWindow", u"ROTATE", None))
        self.CaptureButton.setText(QCoreApplication.translate("MainWindow", u"Capture", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"Feature Selection", None))
        self.GRcheck.setText(QCoreApplication.translate("MainWindow", u"Grayscale", None))
        self.NRcheck.setText(QCoreApplication.translate("MainWindow", u"Noise Reduction", None))
        self.Histocheck.setText(QCoreApplication.translate("MainWindow", u"Histogram Eq", None))
        self.checkBox_7.setText(QCoreApplication.translate("MainWindow", u"Roi Extraction", None))
        self.checkBox_8.setText(QCoreApplication.translate("MainWindow", u"Blob Analysis", None))
        self.checkBox_9.setText(QCoreApplication.translate("MainWindow", u"Template Matching", None))
        self.OriCamlabel.setText("")
        self.ProcessedCapturedLabel.setText("")
        self.groupBox_6.setTitle(QCoreApplication.translate("MainWindow", u"Program Command | Status", None))
        self.StoppButton.setText(QCoreApplication.translate("MainWindow", u"STOP", None))
        self.InspectButton.setText(QCoreApplication.translate("MainWindow", u"INSPECT", None))
        self.statsLabel.setText(QCoreApplication.translate("MainWindow", u"STATUS: ", None))
        self.ProcessedCamlabel.setText("")
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
    # retranslateUi

