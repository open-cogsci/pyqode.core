# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'search_panel.ui'
#
# Created: Sat Aug 31 18:46:36 2013
#      by: pyside-uic 0.2.14 running on PySide 1.2.0
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_SearchPanel(object):
    def setupUi(self, SearchPanel):
        SearchPanel.setObjectName("SearchPanel")
        SearchPanel.resize(686, 81)
        SearchPanel.setStyleSheet("")
        self.verticalLayout = QtGui.QVBoxLayout(SearchPanel)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtGui.QFrame(SearchPanel)
        self.frame.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.frame)
        self.verticalLayout_2.setSpacing(9)
        self.verticalLayout_2.setContentsMargins(9, 9, 9, 9)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widgetSearch = QtGui.QWidget(self.frame)
        self.widgetSearch.setObjectName("widgetSearch")
        self.horizontalLayout = QtGui.QHBoxLayout(self.widgetSearch)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.labelSearch = QtGui.QLabel(self.widgetSearch)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelSearch.sizePolicy().hasHeightForWidth())
        self.labelSearch.setSizePolicy(sizePolicy)
        self.labelSearch.setMinimumSize(QtCore.QSize(0, 0))
        self.labelSearch.setMaximumSize(QtCore.QSize(18, 18))
        self.labelSearch.setText("")
        self.labelSearch.setPixmap(QtGui.QPixmap(":/pycode-icons/rc/edit-find.png"))
        self.labelSearch.setScaledContents(True)
        self.labelSearch.setObjectName("labelSearch")
        self.horizontalLayout.addWidget(self.labelSearch)
        self.lineEditSearch = QtGui.QLineEdit(self.widgetSearch)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditSearch.sizePolicy().hasHeightForWidth())
        self.lineEditSearch.setSizePolicy(sizePolicy)
        self.lineEditSearch.setMinimumSize(QtCore.QSize(200, 0))
        self.lineEditSearch.setObjectName("lineEditSearch")
        self.horizontalLayout.addWidget(self.lineEditSearch)
        self.pushButtonPrevious = QtGui.QPushButton(self.widgetSearch)
        self.pushButtonPrevious.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/pyqode_icons/rc/go-up.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonPrevious.setIcon(icon)
        self.pushButtonPrevious.setObjectName("pushButtonPrevious")
        self.horizontalLayout.addWidget(self.pushButtonPrevious)
        self.pushButtonNext = QtGui.QPushButton(self.widgetSearch)
        self.pushButtonNext.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/pycode-icons/rc/go-down.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonNext.setIcon(icon1)
        self.pushButtonNext.setObjectName("pushButtonNext")
        self.horizontalLayout.addWidget(self.pushButtonNext)
        self.checkBoxCase = QtGui.QCheckBox(self.widgetSearch)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        self.checkBoxCase.setPalette(palette)
        self.checkBoxCase.setStyleSheet("")
        self.checkBoxCase.setObjectName("checkBoxCase")
        self.horizontalLayout.addWidget(self.checkBoxCase)
        self.checkBoxWholeWords = QtGui.QCheckBox(self.widgetSearch)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        self.checkBoxWholeWords.setPalette(palette)
        self.checkBoxWholeWords.setObjectName("checkBoxWholeWords")
        self.horizontalLayout.addWidget(self.checkBoxWholeWords)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.labelMatches = QtGui.QLabel(self.widgetSearch)
        self.labelMatches.setObjectName("labelMatches")
        self.horizontalLayout.addWidget(self.labelMatches)
        self.pushButtonClose = QtGui.QPushButton(self.widgetSearch)
        self.pushButtonClose.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/pycode-icons/rc/close.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonClose.setIcon(icon2)
        self.pushButtonClose.setIconSize(QtCore.QSize(12, 12))
        self.pushButtonClose.setObjectName("pushButtonClose")
        self.horizontalLayout.addWidget(self.pushButtonClose)
        self.verticalLayout_2.addWidget(self.widgetSearch)
        self.widgetReplace = QtGui.QWidget(self.frame)
        self.widgetReplace.setObjectName("widgetReplace")
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.widgetReplace)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.labelReplace = QtGui.QLabel(self.widgetReplace)
        self.labelReplace.setMaximumSize(QtCore.QSize(18, 18))
        self.labelReplace.setText("")
        self.labelReplace.setPixmap(QtGui.QPixmap(":/pycode-icons/rc/edit-find-replace.png"))
        self.labelReplace.setScaledContents(True)
        self.labelReplace.setObjectName("labelReplace")
        self.horizontalLayout_2.addWidget(self.labelReplace)
        self.lineEditReplace = QtGui.QLineEdit(self.widgetReplace)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditReplace.sizePolicy().hasHeightForWidth())
        self.lineEditReplace.setSizePolicy(sizePolicy)
        self.lineEditReplace.setMinimumSize(QtCore.QSize(200, 0))
        self.lineEditReplace.setObjectName("lineEditReplace")
        self.horizontalLayout_2.addWidget(self.lineEditReplace)
        self.pushButtonReplace = QtGui.QPushButton(self.widgetReplace)
        self.pushButtonReplace.setObjectName("pushButtonReplace")
        self.horizontalLayout_2.addWidget(self.pushButtonReplace)
        self.pushButtonReplaceAll = QtGui.QPushButton(self.widgetReplace)
        self.pushButtonReplaceAll.setObjectName("pushButtonReplaceAll")
        self.horizontalLayout_2.addWidget(self.pushButtonReplaceAll)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout_2.addWidget(self.widgetReplace)
        self.verticalLayout.addWidget(self.frame)
        self.actionSearch = QtGui.QAction(SearchPanel)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/pycode-icons/rc/edit-find.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSearch.setIcon(icon3)
        self.actionSearch.setIconVisibleInMenu(True)
        self.actionSearch.setObjectName("actionSearch")
        self.actionActionSearchAndReplace = QtGui.QAction(SearchPanel)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/pycode-icons/rc/edit-find-replace.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionActionSearchAndReplace.setIcon(icon4)
        self.actionActionSearchAndReplace.setIconVisibleInMenu(True)
        self.actionActionSearchAndReplace.setObjectName("actionActionSearchAndReplace")
        self.actionFindNext = QtGui.QAction(SearchPanel)
        self.actionFindNext.setIcon(icon1)
        self.actionFindNext.setIconVisibleInMenu(True)
        self.actionFindNext.setObjectName("actionFindNext")
        self.actionFindPrevious = QtGui.QAction(SearchPanel)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/pycode-icons/rc/go-up.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionFindPrevious.setIcon(icon5)
        self.actionFindPrevious.setIconVisibleInMenu(True)
        self.actionFindPrevious.setObjectName("actionFindPrevious")

        self.retranslateUi(SearchPanel)
        QtCore.QMetaObject.connectSlotsByName(SearchPanel)
        SearchPanel.setTabOrder(self.lineEditSearch, self.lineEditReplace)
        SearchPanel.setTabOrder(self.lineEditReplace, self.pushButtonPrevious)
        SearchPanel.setTabOrder(self.pushButtonPrevious, self.pushButtonNext)
        SearchPanel.setTabOrder(self.pushButtonNext, self.checkBoxCase)
        SearchPanel.setTabOrder(self.checkBoxCase, self.checkBoxWholeWords)
        SearchPanel.setTabOrder(self.checkBoxWholeWords, self.pushButtonReplace)
        SearchPanel.setTabOrder(self.pushButtonReplace, self.pushButtonReplaceAll)
        SearchPanel.setTabOrder(self.pushButtonReplaceAll, self.pushButtonClose)

    def retranslateUi(self, SearchPanel):
        SearchPanel.setWindowTitle(QtGui.QApplication.translate("SearchPanel", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBoxCase.setText(QtGui.QApplication.translate("SearchPanel", "Match case", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBoxWholeWords.setText(QtGui.QApplication.translate("SearchPanel", "Whole words", None, QtGui.QApplication.UnicodeUTF8))
        self.labelMatches.setText(QtGui.QApplication.translate("SearchPanel", "0 matches", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonReplace.setText(QtGui.QApplication.translate("SearchPanel", "Replace", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonReplaceAll.setText(QtGui.QApplication.translate("SearchPanel", "Replace All", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSearch.setText(QtGui.QApplication.translate("SearchPanel", "Search", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSearch.setToolTip(QtGui.QApplication.translate("SearchPanel", "Show the search panel", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSearch.setShortcut(QtGui.QApplication.translate("SearchPanel", "Ctrl+F", None, QtGui.QApplication.UnicodeUTF8))
        self.actionActionSearchAndReplace.setText(QtGui.QApplication.translate("SearchPanel", "Search and replace", None, QtGui.QApplication.UnicodeUTF8))
        self.actionActionSearchAndReplace.setToolTip(QtGui.QApplication.translate("SearchPanel", "Show the search and replace panel", None, QtGui.QApplication.UnicodeUTF8))
        self.actionActionSearchAndReplace.setShortcut(QtGui.QApplication.translate("SearchPanel", "Ctrl+R", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFindNext.setText(QtGui.QApplication.translate("SearchPanel", "Find next", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFindNext.setToolTip(QtGui.QApplication.translate("SearchPanel", "Find the next occurrence (downward)", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFindNext.setShortcut(QtGui.QApplication.translate("SearchPanel", "F3", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFindPrevious.setText(QtGui.QApplication.translate("SearchPanel", "Find previous", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFindPrevious.setToolTip(QtGui.QApplication.translate("SearchPanel", "Find previous occurrence (upward)", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFindPrevious.setShortcut(QtGui.QApplication.translate("SearchPanel", "Shift+F3", None, QtGui.QApplication.UnicodeUTF8))

from . import pyqode_core_rc