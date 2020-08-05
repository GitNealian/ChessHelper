# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainFrame.ui'
##
## Created by: Qt User Interface Compiler version 5.15.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


class Ui_MainFrame(object):
    def setupUi(self, MainFrame):
        if not MainFrame.objectName():
            MainFrame.setObjectName(u"MainFrame")
        MainFrame.resize(415, 405)
        self.frame = QFrame(MainFrame)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(11, 24, 391, 111))
        self.frame.setStyleSheet(u" font-size: 12px")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Plain)
        self.frame.setLineWidth(1)
        self.frame.setMidLineWidth(0)
        self.horizontalLayoutWidget = QWidget(self.frame)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(10, 20, 371, 31))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 1)
        self.label_2 = QLabel(self.horizontalLayoutWidget)
        self.label_2.setObjectName(u"label_2")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMinimumSize(QSize(40, 0))
        self.label_2.setStyleSheet(u"font-s")

        self.horizontalLayout.addWidget(self.label_2)

        self.leCCBridge = QLineEdit(self.horizontalLayoutWidget)
        self.leCCBridge.setObjectName(u"leCCBridge")
        self.leCCBridge.setEnabled(True)
        font = QFont()
        font.setFamily(u"\u5fae\u8f6f\u96c5\u9ed1")
        self.leCCBridge.setFont(font)
        self.leCCBridge.setStyleSheet(u"")
        self.leCCBridge.setReadOnly(True)

        self.horizontalLayout.addWidget(self.leCCBridge)

        self.btnBrowseCCBridge = QPushButton(self.horizontalLayoutWidget)
        self.btnBrowseCCBridge.setObjectName(u"btnBrowseCCBridge")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.MinimumExpanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btnBrowseCCBridge.sizePolicy().hasHeightForWidth())
        self.btnBrowseCCBridge.setSizePolicy(sizePolicy1)
        self.btnBrowseCCBridge.setStyleSheet(u"")

        self.horizontalLayout.addWidget(self.btnBrowseCCBridge)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 5)
        self.horizontalLayout.setStretch(2, 1)
        self.horizontalLayoutWidget_4 = QWidget(self.frame)
        self.horizontalLayoutWidget_4.setObjectName(u"horizontalLayoutWidget_4")
        self.horizontalLayoutWidget_4.setGeometry(QRect(10, 60, 371, 31))
        self.horizontalLayout_5 = QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer)

        self.btnDeduce = QPushButton(self.horizontalLayoutWidget_4)
        self.btnDeduce.setObjectName(u"btnDeduce")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.MinimumExpanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.btnDeduce.sizePolicy().hasHeightForWidth())
        self.btnDeduce.setSizePolicy(sizePolicy2)

        self.horizontalLayout_5.addWidget(self.btnDeduce)

        self.btnSearch = QPushButton(self.horizontalLayoutWidget_4)
        self.btnSearch.setObjectName(u"btnSearch")
        sizePolicy2.setHeightForWidth(self.btnSearch.sizePolicy().hasHeightForWidth())
        self.btnSearch.setSizePolicy(sizePolicy2)

        self.horizontalLayout_5.addWidget(self.btnSearch)

        self.cbAutoSearch = QCheckBox(self.horizontalLayoutWidget_4)
        self.cbAutoSearch.setObjectName(u"cbAutoSearch")
        self.cbAutoSearch.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_5.addWidget(self.cbAutoSearch)

        self.label = QLabel(MainFrame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(40, 10, 61, 31))
        font1 = QFont()
        font1.setFamily(u"Agency FB")
        font1.setPointSize(11)
        self.label.setFont(font1)
        self.label.setAutoFillBackground(True)
        self.frame_2 = QFrame(MainFrame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(10, 153, 391, 241))
        self.frame_2.setStyleSheet(u" font-size: 12px")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Plain)
        self.frame_2.setLineWidth(1)
        self.frame_2.setMidLineWidth(0)
        self.horizontalLayoutWidget_3 = QWidget(self.frame_2)
        self.horizontalLayoutWidget_3.setObjectName(u"horizontalLayoutWidget_3")
        self.horizontalLayoutWidget_3.setGeometry(QRect(10, 20, 371, 31))
        self.horizontalLayout_4 = QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 1)
        self.label_6 = QLabel(self.horizontalLayoutWidget_3)
        self.label_6.setObjectName(u"label_6")
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setMinimumSize(QSize(40, 0))
        font2 = QFont()
        font2.setFamily(u"Agency FB")
        self.label_6.setFont(font2)
        self.label_6.setStyleSheet(u"f")

        self.horizontalLayout_4.addWidget(self.label_6)

        self.leUcci = QLineEdit(self.horizontalLayoutWidget_3)
        self.leUcci.setObjectName(u"leUcci")
        self.leUcci.setEnabled(True)
        self.leUcci.setFont(font)
        self.leUcci.setStyleSheet(u"")
        self.leUcci.setReadOnly(True)

        self.horizontalLayout_4.addWidget(self.leUcci)

        self.btnBrowseUcci = QPushButton(self.horizontalLayoutWidget_3)
        self.btnBrowseUcci.setObjectName(u"btnBrowseUcci")
        sizePolicy1.setHeightForWidth(self.btnBrowseUcci.sizePolicy().hasHeightForWidth())
        self.btnBrowseUcci.setSizePolicy(sizePolicy1)
        self.btnBrowseUcci.setStyleSheet(u"")

        self.horizontalLayout_4.addWidget(self.btnBrowseUcci)

        self.horizontalLayout_4.setStretch(0, 1)
        self.horizontalLayout_4.setStretch(1, 5)
        self.horizontalLayout_4.setStretch(2, 1)
        self.horizontalLayoutWidget_5 = QWidget(self.frame_2)
        self.horizontalLayoutWidget_5.setObjectName(u"horizontalLayoutWidget_5")
        self.horizontalLayoutWidget_5.setGeometry(QRect(10, 60, 371, 33))
        self.horizontalLayout_6 = QHBoxLayout(self.horizontalLayoutWidget_5)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_8 = QLabel(self.horizontalLayoutWidget_5)
        self.label_8.setObjectName(u"label_8")
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        self.label_8.setMinimumSize(QSize(40, 0))

        self.horizontalLayout_6.addWidget(self.label_8)

        self.lbScore = QLabel(self.horizontalLayoutWidget_5)
        self.lbScore.setObjectName(u"lbScore")
        self.lbScore.setFont(font2)
        self.lbScore.setStyleSheet(u"font-size: 16px")
        self.lbScore.setFrameShape(QFrame.StyledPanel)
        self.lbScore.setAlignment(Qt.AlignBottom|Qt.AlignRight|Qt.AlignTrailing)

        self.horizontalLayout_6.addWidget(self.lbScore)

        self.label_3 = QLabel(self.horizontalLayoutWidget_5)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_6.addWidget(self.label_3)

        self.sbScoreDepth = QSpinBox(self.horizontalLayoutWidget_5)
        self.sbScoreDepth.setObjectName(u"sbScoreDepth")
        sizePolicy1.setHeightForWidth(self.sbScoreDepth.sizePolicy().hasHeightForWidth())
        self.sbScoreDepth.setSizePolicy(sizePolicy1)

        self.horizontalLayout_6.addWidget(self.sbScoreDepth)

        self.btnValuate = QPushButton(self.horizontalLayoutWidget_5)
        self.btnValuate.setObjectName(u"btnValuate")
        sizePolicy2.setHeightForWidth(self.btnValuate.sizePolicy().hasHeightForWidth())
        self.btnValuate.setSizePolicy(sizePolicy2)

        self.horizontalLayout_6.addWidget(self.btnValuate)

        self.cbAutoValuate = QCheckBox(self.horizontalLayoutWidget_5)
        self.cbAutoValuate.setObjectName(u"cbAutoValuate")

        self.horizontalLayout_6.addWidget(self.cbAutoValuate)

        self.horizontalLayout_6.setStretch(0, 1)
        self.horizontalLayout_6.setStretch(1, 2)
        self.horizontalLayout_6.setStretch(4, 1)
        self.horizontalLayout_6.setStretch(5, 1)
        self.horizontalLayoutWidget_6 = QWidget(self.frame_2)
        self.horizontalLayoutWidget_6.setObjectName(u"horizontalLayoutWidget_6")
        self.horizontalLayoutWidget_6.setGeometry(QRect(10, 100, 371, 31))
        self.horizontalLayout_7 = QHBoxLayout(self.horizontalLayoutWidget_6)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.label_9 = QLabel(self.horizontalLayoutWidget_6)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_7.addWidget(self.label_9)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_2)

        self.label_4 = QLabel(self.horizontalLayoutWidget_6)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_7.addWidget(self.label_4)

        self.sbHelpDepth = QSpinBox(self.horizontalLayoutWidget_6)
        self.sbHelpDepth.setObjectName(u"sbHelpDepth")
        sizePolicy1.setHeightForWidth(self.sbHelpDepth.sizePolicy().hasHeightForWidth())
        self.sbHelpDepth.setSizePolicy(sizePolicy1)

        self.horizontalLayout_7.addWidget(self.sbHelpDepth)

        self.btnHelp = QPushButton(self.horizontalLayoutWidget_6)
        self.btnHelp.setObjectName(u"btnHelp")
        sizePolicy1.setHeightForWidth(self.btnHelp.sizePolicy().hasHeightForWidth())
        self.btnHelp.setSizePolicy(sizePolicy1)

        self.horizontalLayout_7.addWidget(self.btnHelp)

        self.tbHelp = QTextBrowser(self.frame_2)
        self.tbHelp.setObjectName(u"tbHelp")
        self.tbHelp.setEnabled(True)
        self.tbHelp.setGeometry(QRect(10, 140, 371, 81))
        self.label_5 = QLabel(MainFrame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(40, 139, 81, 31))
        self.label_5.setFont(font1)
        self.label_5.setAutoFillBackground(True)

        self.retranslateUi(MainFrame)

        QMetaObject.connectSlotsByName(MainFrame)
    # setupUi

    def retranslateUi(self, MainFrame):
        MainFrame.setWindowTitle(QCoreApplication.translate("MainFrame", u"ChessHelper", None))
        self.label_2.setText(QCoreApplication.translate("MainFrame", u"\u4f4d\u7f6e", None))
        self.btnBrowseCCBridge.setText(QCoreApplication.translate("MainFrame", u"\u6d4f\u89c8", None))
        self.btnDeduce.setText(QCoreApplication.translate("MainFrame", u"\u4ece\u5f53\u524d\u5c40\u9762\u63a8\u6f14", None))
        self.btnSearch.setText(QCoreApplication.translate("MainFrame", u"\u641c\u7d22\u5f53\u524d\u5c40\u9762", None))
        self.cbAutoSearch.setText(QCoreApplication.translate("MainFrame", u"\u81ea\u52a8\u641c\u7d22", None))
        self.label.setText(QCoreApplication.translate("MainFrame", u"  \u8c61\u68cb\u6865    ", None))
        self.label_6.setText(QCoreApplication.translate("MainFrame", u"\u4f4d\u7f6e", None))
        self.btnBrowseUcci.setText(QCoreApplication.translate("MainFrame", u"\u6d4f\u89c8", None))
        self.label_8.setText(QCoreApplication.translate("MainFrame", u"\u5c40\u9762\u5206", None))
        self.lbScore.setText(QCoreApplication.translate("MainFrame", u"1024", None))
        self.label_3.setText(QCoreApplication.translate("MainFrame", u"\u6df1\u5ea6", None))
        self.btnValuate.setText(QCoreApplication.translate("MainFrame", u"\u8ba1\u7b97", None))
        self.cbAutoValuate.setText(QCoreApplication.translate("MainFrame", u"\u81ea\u52a8\u8ba1\u7b97", None))
        self.label_9.setText(QCoreApplication.translate("MainFrame", u"\u63d0\u793a", None))
        self.label_4.setText(QCoreApplication.translate("MainFrame", u"\u6df1\u5ea6", None))
        self.btnHelp.setText(QCoreApplication.translate("MainFrame", u"\u63d0\u793a", None))
        self.tbHelp.setHtml(QCoreApplication.translate("MainFrame", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'SimSun'; font-size:12px; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("MainFrame", u"  \u8c61\u68cb\u5f15\u64ce", None))
    # retranslateUi

