# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_rank.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem
import json


class Ui_MainWindow(object):
    def __init__(self):
        self.Dialog = QtWidgets.QDialog()
        self.setupUi(self.Dialog)
        self.Dialog.setWindowIcon(QtGui.QIcon("media/cat.ico"))
        self.loadRank()
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(366, 419)
        MainWindow.setFixedSize(366, 419)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 366, 419))
        self.tabWidget.setObjectName("tabWidget")
        self.tab_1 = QtWidgets.QWidget()
        self.tab_1.setObjectName("tab_1")
        self.tableWidget_1 = QtWidgets.QTableWidget(self.tab_1)
        self.tableWidget_1.setGeometry(QtCore.QRect(0, 0, 360, 391))
        self.tableWidget_1.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.tableWidget_1.setObjectName("tableWidget_1")
        self.tableWidget_1.setColumnCount(3)
        self.tableWidget_1.setRowCount(10)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_1.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_1.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_1.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_1.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_1.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_1.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_1.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_1.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_1.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_1.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_1.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_1.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_1.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_1.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_1.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_1.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_1.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_1.setItem(3, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_1.setItem(4, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_1.setItem(5, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_1.setItem(6, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_1.setItem(7, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_1.setItem(8, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_1.setItem(9, 0, item)
        self.tableWidget_1.horizontalHeader().setVisible(True)
        self.tableWidget_1.horizontalHeader().setDefaultSectionSize(90)
        self.tableWidget_1.horizontalHeader().setHighlightSections(True)
        self.tableWidget_1.horizontalHeader().setMinimumSectionSize(90)
        self.tableWidget_1.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget_1.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_1.verticalHeader().setVisible(False)
        self.tableWidget_1.verticalHeader().setDefaultSectionSize(36)
        self.tableWidget_1.verticalHeader().setMinimumSectionSize(36)
        self.tabWidget.addTab(self.tab_1, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tableWidget_2 = QtWidgets.QTableWidget(self.tab_2)
        self.tableWidget_2.setGeometry(QtCore.QRect(0, 0, 360, 391))
        self.tableWidget_2.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(3)
        self.tableWidget_2.setRowCount(10)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setItem(3, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setItem(4, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setItem(5, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setItem(6, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setItem(7, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setItem(8, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setItem(9, 0, item)
        self.tableWidget_2.horizontalHeader().setVisible(True)
        self.tableWidget_2.horizontalHeader().setDefaultSectionSize(90)
        self.tableWidget_2.horizontalHeader().setHighlightSections(True)
        self.tableWidget_2.horizontalHeader().setMinimumSectionSize(90)
        self.tableWidget_2.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget_2.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_2.verticalHeader().setVisible(False)
        self.tableWidget_2.verticalHeader().setDefaultSectionSize(36)
        self.tableWidget_2.verticalHeader().setMinimumSectionSize(36)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.tableWidget_3 = QtWidgets.QTableWidget(self.tab_3)
        self.tableWidget_3.setGeometry(QtCore.QRect(0, 0, 360, 391))
        self.tableWidget_3.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.tableWidget_3.setObjectName("tableWidget_3")
        self.tableWidget_3.setColumnCount(3)
        self.tableWidget_3.setRowCount(10)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setItem(3, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setItem(4, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setItem(5, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setItem(6, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setItem(7, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setItem(8, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setItem(9, 0, item)
        self.tableWidget_3.horizontalHeader().setVisible(True)
        self.tableWidget_3.horizontalHeader().setDefaultSectionSize(90)
        self.tableWidget_3.horizontalHeader().setHighlightSections(True)
        self.tableWidget_3.horizontalHeader().setMinimumSectionSize(90)
        self.tableWidget_3.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget_3.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_3.verticalHeader().setVisible(False)
        self.tableWidget_3.verticalHeader().setDefaultSectionSize(36)
        self.tableWidget_3.verticalHeader().setMinimumSectionSize(36)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.tableWidget_4 = QtWidgets.QTableWidget(self.tab_4)
        self.tableWidget_4.setGeometry(QtCore.QRect(0, 0, 360, 391))
        self.tableWidget_4.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.tableWidget_4.setObjectName("tableWidget_4")
        self.tableWidget_4.setColumnCount(3)
        self.tableWidget_4.setRowCount(10)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setItem(3, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setItem(4, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setItem(5, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setItem(6, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setItem(7, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setItem(8, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setItem(9, 0, item)
        self.tableWidget_4.horizontalHeader().setVisible(True)
        self.tableWidget_4.horizontalHeader().setDefaultSectionSize(90)
        self.tableWidget_4.horizontalHeader().setHighlightSections(True)
        self.tableWidget_4.horizontalHeader().setMinimumSectionSize(90)
        self.tableWidget_4.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget_4.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_4.verticalHeader().setVisible(False)
        self.tableWidget_4.verticalHeader().setDefaultSectionSize(36)
        self.tableWidget_4.verticalHeader().setMinimumSectionSize(36)
        self.tabWidget.addTab(self.tab_4, "")
        #MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "本机战绩"))
        item = self.tableWidget_1.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.tableWidget_1.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "2"))
        item = self.tableWidget_1.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "3"))
        item = self.tableWidget_1.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "4"))
        item = self.tableWidget_1.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "5"))
        item = self.tableWidget_1.verticalHeaderItem(5)
        item.setText(_translate("MainWindow", "6"))
        item = self.tableWidget_1.verticalHeaderItem(6)
        item.setText(_translate("MainWindow", "7"))
        item = self.tableWidget_1.verticalHeaderItem(7)
        item.setText(_translate("MainWindow", "8"))
        item = self.tableWidget_1.verticalHeaderItem(8)
        item.setText(_translate("MainWindow", "9"))
        item = self.tableWidget_1.verticalHeaderItem(9)
        item.setText(_translate("MainWindow", "10"))
        item = self.tableWidget_1.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "名次"))
        item = self.tableWidget_1.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "姓名"))
        item = self.tableWidget_1.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "成绩(秒)"))
        __sortingEnabled = self.tableWidget_1.isSortingEnabled()
        self.tableWidget_1.setSortingEnabled(False)
        self.tableWidget_1.setSortingEnabled(__sortingEnabled)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), _translate("MainWindow", "初级"))
        item = self.tableWidget_2.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.tableWidget_2.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "2"))
        item = self.tableWidget_2.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "3"))
        item = self.tableWidget_2.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "4"))
        item = self.tableWidget_2.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "5"))
        item = self.tableWidget_2.verticalHeaderItem(5)
        item.setText(_translate("MainWindow", "6"))
        item = self.tableWidget_2.verticalHeaderItem(6)
        item.setText(_translate("MainWindow", "7"))
        item = self.tableWidget_2.verticalHeaderItem(7)
        item.setText(_translate("MainWindow", "8"))
        item = self.tableWidget_2.verticalHeaderItem(8)
        item.setText(_translate("MainWindow", "9"))
        item = self.tableWidget_2.verticalHeaderItem(9)
        item.setText(_translate("MainWindow", "10"))
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "名次"))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "姓名"))
        item = self.tableWidget_2.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "成绩(秒)"))
        __sortingEnabled = self.tableWidget_2.isSortingEnabled()
        self.tableWidget_2.setSortingEnabled(False)
        self.tableWidget_2.setSortingEnabled(__sortingEnabled)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "中级"))
        item = self.tableWidget_3.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.tableWidget_3.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "2"))
        item = self.tableWidget_3.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "3"))
        item = self.tableWidget_3.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "4"))
        item = self.tableWidget_3.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "5"))
        item = self.tableWidget_3.verticalHeaderItem(5)
        item.setText(_translate("MainWindow", "6"))
        item = self.tableWidget_3.verticalHeaderItem(6)
        item.setText(_translate("MainWindow", "7"))
        item = self.tableWidget_3.verticalHeaderItem(7)
        item.setText(_translate("MainWindow", "8"))
        item = self.tableWidget_3.verticalHeaderItem(8)
        item.setText(_translate("MainWindow", "9"))
        item = self.tableWidget_3.verticalHeaderItem(9)
        item.setText(_translate("MainWindow", "10"))
        item = self.tableWidget_3.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "名次"))
        item = self.tableWidget_3.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "姓名"))
        item = self.tableWidget_3.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "成绩(秒)"))
        __sortingEnabled = self.tableWidget_3.isSortingEnabled()
        self.tableWidget_3.setSortingEnabled(False)
        self.tableWidget_3.setSortingEnabled(__sortingEnabled)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "高级"))
        item = self.tableWidget_4.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.tableWidget_4.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "2"))
        item = self.tableWidget_4.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "3"))
        item = self.tableWidget_4.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "4"))
        item = self.tableWidget_4.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "5"))
        item = self.tableWidget_4.verticalHeaderItem(5)
        item.setText(_translate("MainWindow", "6"))
        item = self.tableWidget_4.verticalHeaderItem(6)
        item.setText(_translate("MainWindow", "7"))
        item = self.tableWidget_4.verticalHeaderItem(7)
        item.setText(_translate("MainWindow", "8"))
        item = self.tableWidget_4.verticalHeaderItem(8)
        item.setText(_translate("MainWindow", "9"))
        item = self.tableWidget_4.verticalHeaderItem(9)
        item.setText(_translate("MainWindow", "10"))
        item = self.tableWidget_4.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "名次"))
        item = self.tableWidget_4.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "姓名"))
        item = self.tableWidget_4.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "成绩(3BV/s)"))
        __sortingEnabled = self.tableWidget_4.isSortingEnabled()
        self.tableWidget_4.setSortingEnabled(False)
        self.tableWidget_4.setSortingEnabled(__sortingEnabled)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "自定义"))

    def loadRank(self):
        self.tableWidget_1.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget_2.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget_3.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget_4.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        with open('scoreB.json', mode='r', encoding='utf-8') as fp:
            listB = json.load(fp)
            lenB = len(listB)
            for i in list(range(lenB)):
                if i >= 10:
                    break
                tmpitem = QTableWidgetItem(str(i + 1))
                tmpitem.setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
                self.tableWidget_1.setItem(i, 0, tmpitem)
                tmpitem = QTableWidgetItem(listB[i]["name"])
                tmpitem.setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
                self.tableWidget_1.setItem(i, 1, tmpitem)
                tmpitem = QTableWidgetItem(listB[i]["time"])
                tmpitem.setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
                self.tableWidget_1.setItem(i, 2, tmpitem)
        with open('scoreI.json', mode='r', encoding='utf-8') as fp:
            listI = json.load(fp)
            lenI = len(listI)
            for i in list(range(lenI)):
                if i >= 10:
                    break
                tmpitem = QTableWidgetItem(str(i + 1))
                tmpitem.setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
                self.tableWidget_2.setItem(i, 0, tmpitem)
                tmpitem = QTableWidgetItem(listI[i]["name"])
                tmpitem.setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
                self.tableWidget_2.setItem(i, 1, tmpitem)
                tmpitem = QTableWidgetItem(listI[i]["time"])
                tmpitem.setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
                self.tableWidget_2.setItem(i, 2, tmpitem)
        with open('scoreE.json', mode='r', encoding='utf-8') as fp:
            listE = json.load(fp)
            lenE = len(listE)
            for i in list(range(lenE)):
                if i >= 10:
                    break
                tmpitem = QTableWidgetItem(str(i + 1))
                tmpitem.setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
                self.tableWidget_3.setItem(i, 0, tmpitem)
                tmpitem = QTableWidgetItem(listE[i]["name"])
                tmpitem.setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
                self.tableWidget_3.setItem(i, 1, tmpitem)
                tmpitem = QTableWidgetItem(listE[i]["time"])
                tmpitem.setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
                self.tableWidget_3.setItem(i, 2, tmpitem)
        with open('scoreC.json', mode='r', encoding='utf-8') as fp:
            listC = json.load(fp)
            lenC = len(listC)
            for i in list(range(lenC)):
                if i >= 10:
                    break
                tmpitem = QTableWidgetItem(str(i + 1))
                tmpitem.setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
                self.tableWidget_4.setItem(i, 0, tmpitem)
                tmpitem = QTableWidgetItem(listC[i]["name"])
                tmpitem.setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
                self.tableWidget_4.setItem(i, 1, tmpitem)
                tmpitem = QTableWidgetItem(listC[i]["3bv/s"])
                tmpitem.setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
                self.tableWidget_4.setItem(i, 2, tmpitem)

        '''
        test = [{"name": "自定义1", "time": "15.001", "3bv/s": "1.51"}, {"name": "自定义2", "time": "16.001", "3bv/s": "0.51"}, {"name": "自定义3", "time": "16.101", "3bv/s": "0.10"}]
        with open('scoreC.json', 'w', encoding='utf-8') as fp:
            json.dump(test, fp, ensure_ascii=False)
        '''


