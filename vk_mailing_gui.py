# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'vk-mailing.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_vkmailing(object):
    def setupUi(self, vkmailing):
        vkmailing.setObjectName("vkmailing")
        vkmailing.resize(356, 470)
        self.gridLayout = QtWidgets.QGridLayout(vkmailing)
        self.gridLayout.setObjectName("gridLayout")
        self.btn_send = QtWidgets.QPushButton(vkmailing)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_send.setFont(font)
        self.btn_send.setObjectName("btn_send")
        self.gridLayout.addWidget(self.btn_send, 5, 2, 1, 1)
        self.txtedit_attachments = QtWidgets.QPlainTextEdit(vkmailing)
        self.txtedit_attachments.setEnabled(False)
        self.txtedit_attachments.setObjectName("txtedit_attachments")
        self.gridLayout.addWidget(self.txtedit_attachments, 4, 0, 1, 3)
        self.txtedit_msg = QtWidgets.QPlainTextEdit(vkmailing)
        self.txtedit_msg.setObjectName("txtedit_msg")
        self.gridLayout.addWidget(self.txtedit_msg, 5, 0, 2, 2)
        self.txtedit_links = QtWidgets.QPlainTextEdit(vkmailing)
        self.txtedit_links.setObjectName("txtedit_links")
        self.gridLayout.addWidget(self.txtedit_links, 3, 0, 1, 3)
        self.btn_exit = QtWidgets.QPushButton(vkmailing)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_exit.setFont(font)
        self.btn_exit.setObjectName("btn_exit")
        self.gridLayout.addWidget(self.btn_exit, 6, 2, 1, 1)
        self.lbl_header = QtWidgets.QLabel(vkmailing)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lbl_header.setFont(font)
        self.lbl_header.setObjectName("lbl_header")
        self.gridLayout.addWidget(self.lbl_header, 0, 0, 1, 3)
        self.lbl_status = QtWidgets.QLabel(vkmailing)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lbl_status.setFont(font)
        self.lbl_status.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_status.setObjectName("lbl_status")
        self.gridLayout.addWidget(self.lbl_status, 1, 0, 2, 3)

        self.retranslateUi(vkmailing)
        QtCore.QMetaObject.connectSlotsByName(vkmailing)

    def retranslateUi(self, vkmailing):
        _translate = QtCore.QCoreApplication.translate
        vkmailing.setWindowTitle(_translate("vkmailing", "Form"))
        self.btn_send.setText(_translate("vkmailing", "Send"))
        self.txtedit_attachments.setPlaceholderText(_translate("vkmailing", "Attachments (in progress)"))
        self.txtedit_msg.setPlaceholderText(_translate("vkmailing", "Enter you message"))
        self.txtedit_links.setPlaceholderText(_translate("vkmailing", "Receiver\'s links (one link - one string)"))
        self.btn_exit.setText(_translate("vkmailing", "Exit"))
        self.lbl_header.setText(_translate("vkmailing", "VK Mailing by Oleg Voevodin"))
        self.lbl_status.setText(_translate("vkmailing", "No account logged in"))
