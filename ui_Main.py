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
    QProgressBar, QPushButton, QRadioButton, QSizePolicy,
    QSlider, QSpinBox, QStatusBar, QTabWidget,
    QVBoxLayout, QWidget)

from hold_button import HoldButton

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
        self.actionAll = QAction(MainWindow)
        self.actionAll.setObjectName(u"actionAll")
        self.actionCamera = QAction(MainWindow)
        self.actionCamera.setObjectName(u"actionCamera")
        self.actionArduino = QAction(MainWindow)
        self.actionArduino.setObjectName(u"actionArduino")
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

        self.tabWidget = QTabWidget(self.frame_3)
        self.tabWidget.setObjectName(u"tabWidget")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy3)
        self.tabWidget.setMaximumSize(QSize(16777215, 400))
        font4 = QFont()
        font4.setFamilies([u"Product Sans"])
        font4.setPointSize(9)
        self.tabWidget.setFont(font4)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout_6 = QVBoxLayout(self.tab)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.groupBox_5 = QGroupBox(self.tab)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setMaximumSize(QSize(500, 600))
        self.groupBox_5.setFont(font2)
        self.verticalLayout_3 = QVBoxLayout(self.groupBox_5)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.GRcheck = QCheckBox(self.groupBox_5)
        self.GRcheck.setObjectName(u"GRcheck")

        self.verticalLayout_3.addWidget(self.GRcheck)

        self.NRcheck = QCheckBox(self.groupBox_5)
        self.NRcheck.setObjectName(u"NRcheck")

        self.verticalLayout_3.addWidget(self.NRcheck)

        self.Histocheck = QCheckBox(self.groupBox_5)
        self.Histocheck.setObjectName(u"Histocheck")

        self.verticalLayout_3.addWidget(self.Histocheck)

        self.REcheck = QCheckBox(self.groupBox_5)
        self.REcheck.setObjectName(u"REcheck")

        self.verticalLayout_3.addWidget(self.REcheck)

        self.TMcheck = QCheckBox(self.groupBox_5)
        self.TMcheck.setObjectName(u"TMcheck")

        self.verticalLayout_3.addWidget(self.TMcheck)

        self.IDcheck = QCheckBox(self.groupBox_5)
        self.IDcheck.setObjectName(u"IDcheck")

        self.verticalLayout_3.addWidget(self.IDcheck)

        self.BAcheck = QCheckBox(self.groupBox_5)
        self.BAcheck.setObjectName(u"BAcheck")

        self.verticalLayout_3.addWidget(self.BAcheck)


        self.verticalLayout_6.addWidget(self.groupBox_5)

        self.SaveImgButton = QPushButton(self.tab)
        self.SaveImgButton.setObjectName(u"SaveImgButton")

        self.verticalLayout_6.addWidget(self.SaveImgButton)

        self.tabWidget.addTab(self.tab, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.verticalLayout_8 = QVBoxLayout(self.tab_4)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.setROIButton = QPushButton(self.tab_4)
        self.setROIButton.setObjectName(u"setROIButton")
        self.setROIButton.setMaximumSize(QSize(16777215, 40))

        self.verticalLayout_8.addWidget(self.setROIButton)

        self.label_6 = QLabel(self.tab_4)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMaximumSize(QSize(16777215, 40))
        self.label_6.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)

        self.verticalLayout_8.addWidget(self.label_6)

        self.spinBoxXofst = QSpinBox(self.tab_4)
        self.spinBoxXofst.setObjectName(u"spinBoxXofst")

        self.verticalLayout_8.addWidget(self.spinBoxXofst)

        self.label_7 = QLabel(self.tab_4)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMaximumSize(QSize(16777215, 40))
        self.label_7.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)

        self.verticalLayout_8.addWidget(self.label_7)

        self.spinBoxYofst = QSpinBox(self.tab_4)
        self.spinBoxYofst.setObjectName(u"spinBoxYofst")

        self.verticalLayout_8.addWidget(self.spinBoxYofst)

        self.ResolutionW = QLabel(self.tab_4)
        self.ResolutionW.setObjectName(u"ResolutionW")
        self.ResolutionW.setMaximumSize(QSize(16777215, 40))
        self.ResolutionW.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)

        self.verticalLayout_8.addWidget(self.ResolutionW)

        self.spinBoxRW = QSpinBox(self.tab_4)
        self.spinBoxRW.setObjectName(u"spinBoxRW")

        self.verticalLayout_8.addWidget(self.spinBoxRW)

        self.ResolutionH = QLabel(self.tab_4)
        self.ResolutionH.setObjectName(u"ResolutionH")
        self.ResolutionH.setMaximumSize(QSize(16777215, 40))
        self.ResolutionH.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)

        self.verticalLayout_8.addWidget(self.ResolutionH)

        self.spinBoxRH = QSpinBox(self.tab_4)
        self.spinBoxRH.setObjectName(u"spinBoxRH")

        self.verticalLayout_8.addWidget(self.spinBoxRH)

        self.UpdateBoundButton = QPushButton(self.tab_4)
        self.UpdateBoundButton.setObjectName(u"UpdateBoundButton")
        self.UpdateBoundButton.setMinimumSize(QSize(0, 40))
        font5 = QFont()
        font5.setFamilies([u"Product Sans"])
        font5.setPointSize(9)
        font5.setBold(True)
        self.UpdateBoundButton.setFont(font5)

        self.verticalLayout_8.addWidget(self.UpdateBoundButton)

        self.tabWidget.addTab(self.tab_4, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        sizePolicy.setHeightForWidth(self.tab_2.sizePolicy().hasHeightForWidth())
        self.tab_2.setSizePolicy(sizePolicy)
        self.verticalLayout_7 = QVBoxLayout(self.tab_2)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.groupBox_7 = QGroupBox(self.tab_2)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.groupBox_7.setMaximumSize(QSize(16777215, 100))
        self.horizontalLayout_7 = QHBoxLayout(self.groupBox_7)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.AutoExpButton = QRadioButton(self.groupBox_7)
        self.AutoExpButton.setObjectName(u"AutoExpButton")

        self.horizontalLayout_7.addWidget(self.AutoExpButton)

        self.ManualExpButton = QRadioButton(self.groupBox_7)
        self.ManualExpButton.setObjectName(u"ManualExpButton")

        self.horizontalLayout_7.addWidget(self.ManualExpButton)


        self.verticalLayout_7.addWidget(self.groupBox_7)

        self.label_3 = QLabel(self.tab_2)
        self.label_3.setObjectName(u"label_3")
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setMaximumSize(QSize(16777215, 40))
        self.label_3.setFont(font2)
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)

        self.verticalLayout_7.addWidget(self.label_3)

        self.expSlider = QSlider(self.tab_2)
        self.expSlider.setObjectName(u"expSlider")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Maximum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.expSlider.sizePolicy().hasHeightForWidth())
        self.expSlider.setSizePolicy(sizePolicy4)
        self.expSlider.setMaximumSize(QSize(16777215, 30))
        self.expSlider.setOrientation(Qt.Orientation.Horizontal)

        self.verticalLayout_7.addWidget(self.expSlider)

        self.label_4 = QLabel(self.tab_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(16777215, 60))
        self.label_4.setFont(font2)
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)

        self.verticalLayout_7.addWidget(self.label_4)

        self.gainSlider = QSlider(self.tab_2)
        self.gainSlider.setObjectName(u"gainSlider")
        sizePolicy4.setHeightForWidth(self.gainSlider.sizePolicy().hasHeightForWidth())
        self.gainSlider.setSizePolicy(sizePolicy4)
        self.gainSlider.setMaximumSize(QSize(16777215, 40))
        self.gainSlider.setOrientation(Qt.Orientation.Horizontal)

        self.verticalLayout_7.addWidget(self.gainSlider)

        self.frame_6 = QFrame(self.tab_2)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout_7.addWidget(self.frame_6)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.verticalLayout_5 = QVBoxLayout(self.tab_3)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_5 = QLabel(self.tab_3)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(16777215, 50))
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignHCenter)

        self.verticalLayout_5.addWidget(self.label_5)

        self.frame_5 = QFrame(self.tab_3)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMaximumSize(QSize(16777215, 200))
        self.frame_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.RGainSlider = QSlider(self.frame_5)
        self.RGainSlider.setObjectName(u"RGainSlider")
        self.RGainSlider.setOrientation(Qt.Orientation.Vertical)

        self.horizontalLayout_6.addWidget(self.RGainSlider)

        self.GGainSlider = QSlider(self.frame_5)
        self.GGainSlider.setObjectName(u"GGainSlider")
        self.GGainSlider.setOrientation(Qt.Orientation.Vertical)

        self.horizontalLayout_6.addWidget(self.GGainSlider)

        self.BGainSlider = QSlider(self.frame_5)
        self.BGainSlider.setObjectName(u"BGainSlider")
        self.BGainSlider.setOrientation(Qt.Orientation.Vertical)

        self.horizontalLayout_6.addWidget(self.BGainSlider)


        self.verticalLayout_5.addWidget(self.frame_5)

        self.AWBButton = QPushButton(self.tab_3)
        self.AWBButton.setObjectName(u"AWBButton")
        self.AWBButton.setMinimumSize(QSize(0, 50))

        self.verticalLayout_5.addWidget(self.AWBButton)

        self.tabWidget.addTab(self.tab_3, "")

        self.verticalLayout_4.addWidget(self.tabWidget)


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
        self.StoppButton = HoldButton(self.groupBox_6)
        self.StoppButton.setObjectName(u"StoppButton")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.StoppButton.sizePolicy().hasHeightForWidth())
        self.StoppButton.setSizePolicy(sizePolicy5)
        self.StoppButton.setFont(font3)

        self.gridLayout_3.addWidget(self.StoppButton, 0, 1, 2, 1)

        self.InspectButton = QPushButton(self.groupBox_6)
        self.InspectButton.setObjectName(u"InspectButton")
        sizePolicy5.setHeightForWidth(self.InspectButton.sizePolicy().hasHeightForWidth())
        self.InspectButton.setSizePolicy(sizePolicy5)
        self.InspectButton.setFont(font3)

        self.gridLayout_3.addWidget(self.InspectButton, 0, 0, 2, 1)

        self.progressBar = QProgressBar(self.groupBox_6)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(0)

        self.gridLayout_3.addWidget(self.progressBar, 0, 2, 1, 1)

        self.statsLabel = QLabel(self.groupBox_6)
        self.statsLabel.setObjectName(u"statsLabel")
        font6 = QFont()
        font6.setFamilies([u"Product Sans Black"])
        font6.setPointSize(20)
        self.statsLabel.setFont(font6)
        self.statsLabel.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.statsLabel.setIndent(2)

        self.gridLayout_3.addWidget(self.statsLabel, 1, 2, 1, 1)


        self.gridLayout_2.addWidget(self.groupBox_6, 0, 0, 1, 2)

        self.ProcessedCamlabel = QLabel(self.frame_4)
        self.ProcessedCamlabel.setObjectName(u"ProcessedCamlabel")
        self.ProcessedCamlabel.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.gridLayout_2.addWidget(self.ProcessedCamlabel, 2, 0, 1, 1)


        self.horizontalLayout_5.addWidget(self.frame_4)

        self.horizontalLayout_5.setStretch(1, 1)

        self.verticalLayout_2.addWidget(self.frame_3)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1024, 21))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuStop_Process = QMenu(self.menuFile)
        self.menuStop_Process.setObjectName(u"menuStop_Process")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuFile.addAction(self.menuStop_Process.menuAction())
        self.menuFile.addAction(self.actionQuit)
        self.menuStop_Process.addAction(self.actionAll)
        self.menuStop_Process.addAction(self.actionCamera)
        self.menuStop_Process.addAction(self.actionArduino)
        self.menuHelp.addAction(self.actionGuide)
        self.menuHelp.addAction(self.actionAbout_Software)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionQuit.setText(QCoreApplication.translate("MainWindow", u"Quit", None))
        self.actionGuide.setText(QCoreApplication.translate("MainWindow", u"Guide", None))
        self.actionAbout_Software.setText(QCoreApplication.translate("MainWindow", u"About Software..", None))
        self.actionAll.setText(QCoreApplication.translate("MainWindow", u"All", None))
        self.actionCamera.setText(QCoreApplication.translate("MainWindow", u"Camera", None))
        self.actionArduino.setText(QCoreApplication.translate("MainWindow", u"Arduino", None))
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
        self.groupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"Feature Selection", None))
        self.GRcheck.setText(QCoreApplication.translate("MainWindow", u"Grayscale", None))
        self.NRcheck.setText(QCoreApplication.translate("MainWindow", u"Noise Reduction", None))
        self.Histocheck.setText(QCoreApplication.translate("MainWindow", u"Histogram Eq", None))
        self.REcheck.setText(QCoreApplication.translate("MainWindow", u"Roi Extraction", None))
        self.TMcheck.setText(QCoreApplication.translate("MainWindow", u"Template Matching", None))
        self.IDcheck.setText(QCoreApplication.translate("MainWindow", u"Image Differencing", None))
        self.BAcheck.setText(QCoreApplication.translate("MainWindow", u"Blob Analysis", None))
        self.SaveImgButton.setText(QCoreApplication.translate("MainWindow", u"Capture", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Feature", None))
        self.setROIButton.setText(QCoreApplication.translate("MainWindow", u"SET CAM RESOLUTION", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"X offset", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Y offset", None))
        self.ResolutionW.setText(QCoreApplication.translate("MainWindow", u"Resolution Width", None))
        self.ResolutionH.setText(QCoreApplication.translate("MainWindow", u"Resolution Height", None))
        self.UpdateBoundButton.setText(QCoreApplication.translate("MainWindow", u"UPDATE BOUNDING BOX", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"Resolution", None))
        self.groupBox_7.setTitle(QCoreApplication.translate("MainWindow", u"Exposure Mode", None))
        self.AutoExpButton.setText(QCoreApplication.translate("MainWindow", u"Auto", None))
        self.ManualExpButton.setText(QCoreApplication.translate("MainWindow", u"Manual", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Exposure", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Gain", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Exposure", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Gain R    Gain G   Gain B", None))
        self.AWBButton.setText(QCoreApplication.translate("MainWindow", u"Auto White Balance", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Color", None))
        self.OriCamlabel.setText("")
        self.ProcessedCapturedLabel.setText("")
        self.groupBox_6.setTitle(QCoreApplication.translate("MainWindow", u"Program Command | Status", None))
        self.StoppButton.setText(QCoreApplication.translate("MainWindow", u"STOP", None))
        self.InspectButton.setText(QCoreApplication.translate("MainWindow", u"INSPECT", None))
        self.statsLabel.setText(QCoreApplication.translate("MainWindow", u"STATUS: ", None))
        self.ProcessedCamlabel.setText("")
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuStop_Process.setTitle(QCoreApplication.translate("MainWindow", u"Stop Process...", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
    # retranslateUi

