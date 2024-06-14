# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ROIwidget.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QGroupBox, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

from labelimage import Labelimage

class Ui_ROIWidget(object):
    def setupUi(self, ROIWidget):
        if not ROIWidget.objectName():
            ROIWidget.setObjectName(u"ROIWidget")
        ROIWidget.resize(409, 700)
        ROIWidget.setMaximumSize(QSize(645, 16777215))
        font = QFont()
        font.setFamilies([u"Product Sans"])
        font.setBold(True)
        ROIWidget.setFont(font)
        self.verticalLayout = QVBoxLayout(ROIWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.ShowImage = Labelimage(ROIWidget)
        self.ShowImage.setObjectName(u"ShowImage")
        self.ShowImage.setMaximumSize(QSize(640, 480))
        self.ShowImage.setFont(font)

        self.verticalLayout.addWidget(self.ShowImage)

        self.groupBox = QGroupBox(ROIWidget)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setVerticalSpacing(1)
        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(16777215, 40))
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)

        self.gridLayout.addWidget(self.label_4, 2, 2, 1, 1)

        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(16777215, 40))
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)

        self.gridLayout.addWidget(self.label_5, 0, 2, 1, 1)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(16777215, 40))
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)

        self.lineYofst = QLineEdit(self.groupBox)
        self.lineYofst.setObjectName(u"lineYofst")

        self.gridLayout.addWidget(self.lineYofst, 3, 0, 1, 2)

        self.lineXofst = QLineEdit(self.groupBox)
        self.lineXofst.setObjectName(u"lineXofst")

        self.gridLayout.addWidget(self.lineXofst, 1, 0, 1, 1)

        self.lineFocusW = QLineEdit(self.groupBox)
        self.lineFocusW.setObjectName(u"lineFocusW")

        self.gridLayout.addWidget(self.lineFocusW, 1, 2, 1, 1)

        self.SetImgButton = QPushButton(self.groupBox)
        self.SetImgButton.setObjectName(u"SetImgButton")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SetImgButton.sizePolicy().hasHeightForWidth())
        self.SetImgButton.setSizePolicy(sizePolicy)
        self.SetImgButton.setMaximumSize(QSize(16777215, 40))
        font1 = QFont()
        font1.setFamilies([u"Product Sans"])
        font1.setPointSize(10)
        font1.setBold(True)
        self.SetImgButton.setFont(font1)

        self.gridLayout.addWidget(self.SetImgButton, 4, 2, 1, 1)

        self.RefreshImgButton = QPushButton(self.groupBox)
        self.RefreshImgButton.setObjectName(u"RefreshImgButton")
        sizePolicy.setHeightForWidth(self.RefreshImgButton.sizePolicy().hasHeightForWidth())
        self.RefreshImgButton.setSizePolicy(sizePolicy)
        self.RefreshImgButton.setMaximumSize(QSize(16777215, 40))
        self.RefreshImgButton.setFont(font1)

        self.gridLayout.addWidget(self.RefreshImgButton, 4, 0, 1, 2)

        self.lineFocusH = QLineEdit(self.groupBox)
        self.lineFocusH.setObjectName(u"lineFocusH")

        self.gridLayout.addWidget(self.lineFocusH, 3, 2, 1, 1)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(16777215, 40))
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)

        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)

        self.gridLayout.setRowStretch(4, 1)

        self.verticalLayout.addWidget(self.groupBox)

        self.verticalLayout.setStretch(0, 1)

        self.retranslateUi(ROIWidget)

        QMetaObject.connectSlotsByName(ROIWidget)
    # setupUi

    def retranslateUi(self, ROIWidget):
        ROIWidget.setWindowTitle(QCoreApplication.translate("ROIWidget", u"Form", None))
        self.ShowImage.setText(QCoreApplication.translate("ROIWidget", u"Test", None))
        self.groupBox.setTitle(QCoreApplication.translate("ROIWidget", u"ROI Manual Setting", None))
        self.label_4.setText(QCoreApplication.translate("ROIWidget", u"Focus Height", None))
        self.label_5.setText(QCoreApplication.translate("ROIWidget", u"Focus Width", None))
        self.label_3.setText(QCoreApplication.translate("ROIWidget", u"Y Offset", None))
        self.SetImgButton.setText(QCoreApplication.translate("ROIWidget", u"Set", None))
        self.RefreshImgButton.setText(QCoreApplication.translate("ROIWidget", u"Refresh Image", None))
        self.label_2.setText(QCoreApplication.translate("ROIWidget", u"X Offset", None))
    # retranslateUi

