# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'recordMainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_PyQt5Recording(object):
    def setupUi(self, PyQt5Recording):
        PyQt5Recording.setObjectName("PyQt5Recording")
        PyQt5Recording.resize(510, 228)
        font = QtGui.QFont()
        font.setFamily("Monotype Corsiva")
        font.setPointSize(12)
        font.setItalic(True)
        PyQt5Recording.setFont(font)
        PyQt5Recording.setMouseTracking(False)
        PyQt5Recording.setToolTipDuration(6)
        self.centralwidget = QtWidgets.QWidget(PyQt5Recording)
        self.centralwidget.setObjectName("centralwidget")
        self.start_stop_btn = QtWidgets.QPushButton(self.centralwidget)
        self.start_stop_btn.setGeometry(QtCore.QRect(30, 20, 111, 28))
        self.start_stop_btn.setObjectName("start_stop_btn")
        self.file_path_btn = QtWidgets.QPushButton(self.centralwidget)
        self.file_path_btn.setGeometry(QtCore.QRect(360, 60, 51, 31))
        self.file_path_btn.setObjectName("file_path_btn")
        self.file_path_text = QtWidgets.QLineEdit(self.centralwidget)
        self.file_path_text.setGeometry(QtCore.QRect(30, 60, 331, 31))
        self.file_path_text.setText("")
        self.file_path_text.setObjectName("file_path_text")
        self.file_name_text = QtWidgets.QLineEdit(self.centralwidget)
        self.file_name_text.setGeometry(QtCore.QRect(30, 110, 211, 31))
        self.file_name_text.setObjectName("file_name_text")
        self.tips_label = QtWidgets.QLabel(self.centralwidget)
        self.tips_label.setGeometry(QtCore.QRect(430, 150, 81, 21))
        self.tips_label.setAlignment(QtCore.Qt.AlignCenter)
        self.tips_label.setObjectName("tips_label")
        self.system_cbx = QtWidgets.QCheckBox(self.centralwidget)
        self.system_cbx.setGeometry(QtCore.QRect(170, 20, 121, 19))
        self.system_cbx.setChecked(True)
        self.system_cbx.setObjectName("system_cbx")
        self.microphone_cbx = QtWidgets.QCheckBox(self.centralwidget)
        self.microphone_cbx.setGeometry(QtCore.QRect(300, 20, 131, 19))
        self.microphone_cbx.setObjectName("microphone_cbx")
        self.record_label = QtWidgets.QLabel(self.centralwidget)
        self.record_label.setGeometry(QtCore.QRect(0, 150, 91, 21))
        self.record_label.setAlignment(QtCore.Qt.AlignCenter)
        self.record_label.setObjectName("record_label")
        PyQt5Recording.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(PyQt5Recording)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 510, 30))
        self.menubar.setObjectName("menubar")
        self.options_menu = QtWidgets.QMenu(self.menubar)
        self.options_menu.setObjectName("options_menu")
        PyQt5Recording.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(PyQt5Recording)
        self.statusbar.setObjectName("statusbar")
        PyQt5Recording.setStatusBar(self.statusbar)
        self.menubar.addAction(self.options_menu.menuAction())

        self.retranslateUi(PyQt5Recording)
        QtCore.QMetaObject.connectSlotsByName(PyQt5Recording)

    def retranslateUi(self, PyQt5Recording):
        _translate = QtCore.QCoreApplication.translate
        PyQt5Recording.setWindowTitle(_translate("PyQt5Recording", "PyQt5录屏"))
        self.start_stop_btn.setText(_translate("PyQt5Recording", "开始/结束"))
        self.file_path_btn.setText(_translate("PyQt5Recording", "..."))
        self.file_path_text.setPlaceholderText(_translate("PyQt5Recording", "存储路径"))
        self.file_name_text.setPlaceholderText(_translate("PyQt5Recording", "文件名"))
        self.tips_label.setText(_translate("PyQt5Recording", "提示"))
        self.system_cbx.setText(_translate("PyQt5Recording", "系统声音"))
        self.microphone_cbx.setText(_translate("PyQt5Recording", "麦克风声音"))
        self.record_label.setText(_translate("PyQt5Recording", "未在录制"))
        self.options_menu.setTitle(_translate("PyQt5Recording", "选项"))
