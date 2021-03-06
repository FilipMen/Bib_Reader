# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1010, 586)
        Dialog.setAutoFillBackground(False)
        self.filename = QtWidgets.QLineEdit(Dialog)
        self.filename.setGeometry(QtCore.QRect(10, 20, 641, 22))
        self.filename.setObjectName("filename")
        self.browse = QtWidgets.QPushButton(Dialog)
        self.browse.setGeometry(QtCore.QRect(660, 20, 51, 21))
        self.browse.setObjectName("browse")
        self.abstract_2 = QtWidgets.QPlainTextEdit(Dialog)
        self.abstract_2.setEnabled(True)
        self.abstract_2.setGeometry(QtCore.QRect(10, 140, 531, 401))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.abstract_2.setFont(font)
        self.abstract_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.abstract_2.setReadOnly(True)
        self.abstract_2.setObjectName("abstract_2")
        self.keywords = QtWidgets.QPlainTextEdit(Dialog)
        self.keywords.setEnabled(True)
        self.keywords.setGeometry(QtCore.QRect(550, 140, 181, 401))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.keywords.setFont(font)
        self.keywords.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.keywords.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.keywords.setLineWidth(0)
        self.keywords.setReadOnly(True)
        self.keywords.setObjectName("keywords")
        self.title = QtWidgets.QPlainTextEdit(Dialog)
        self.title.setEnabled(True)
        self.title.setGeometry(QtCore.QRect(10, 60, 641, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.title.setFont(font)
        self.title.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.title.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.title.setLineWidth(0)
        self.title.setReadOnly(True)
        self.title.setObjectName("title")
        self.year = QtWidgets.QPlainTextEdit(Dialog)
        self.year.setEnabled(True)
        self.year.setGeometry(QtCore.QRect(660, 60, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.year.setFont(font)
        self.year.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.year.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.year.setFrameShadow(QtWidgets.QFrame.Raised)
        self.year.setLineWidth(0)
        self.year.setReadOnly(True)
        self.year.setObjectName("year")
        self.next = QtWidgets.QPushButton(Dialog)
        self.next.setGeometry(QtCore.QRect(450, 550, 75, 23))
        self.next.setObjectName("next")
        self.previous = QtWidgets.QPushButton(Dialog)
        self.previous.setGeometry(QtCore.QRect(220, 550, 75, 23))
        self.previous.setObjectName("previous")
        self.discard = QtWidgets.QPushButton(Dialog)
        self.discard.setGeometry(QtCore.QRect(340, 550, 61, 23))
        self.discard.setObjectName("discard")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 130, 47, 13))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(550, 125, 61, 21))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(10, 50, 47, 13))
        self.label_3.setObjectName("label_3")
        self.progressBar = QtWidgets.QProgressBar(Dialog)
        self.progressBar.setGeometry(QtCore.QRect(10, 550, 191, 23))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.number = QtWidgets.QLCDNumber(Dialog)
        self.number.setGeometry(QtCore.QRect(920, 540, 81, 41))
        self.number.setObjectName("number")
        self.link = QtWidgets.QPushButton(Dialog)
        self.link.setGeometry(QtCore.QRect(660, 100, 61, 23))
        self.link.setObjectName("link")
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(740, 10, 261, 531))
        self.groupBox.setObjectName("groupBox")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(10, 20, 47, 13))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(10, 50, 71, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(10, 80, 47, 13))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setGeometry(QtCore.QRect(10, 170, 121, 16))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.groupBox)
        self.label_8.setGeometry(QtCore.QRect(10, 280, 121, 16))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.groupBox)
        self.label_9.setGeometry(QtCore.QRect(10, 390, 121, 16))
        self.label_9.setObjectName("label_9")
        self.save = QtWidgets.QPushButton(self.groupBox)
        self.save.setGeometry(QtCore.QRect(200, 510, 51, 21))
        self.save.setObjectName("save")
        self.control = QtWidgets.QComboBox(self.groupBox)
        self.control.setGeometry(QtCore.QRect(90, 20, 161, 22))
        self.control.setEditable(True)
        self.control.setObjectName("control")
        self.optimization = QtWidgets.QComboBox(self.groupBox)
        self.optimization.setGeometry(QtCore.QRect(90, 50, 161, 22))
        self.optimization.setEditable(True)
        self.optimization.setObjectName("optimization")
        self.type = QtWidgets.QComboBox(self.groupBox)
        self.type.setGeometry(QtCore.QRect(90, 80, 161, 22))
        self.type.setEditable(True)
        self.type.setObjectName("type")
        self.k1 = QtWidgets.QComboBox(self.groupBox)
        self.k1.setGeometry(QtCore.QRect(90, 110, 161, 22))
        self.k1.setEditable(True)
        self.k1.setObjectName("k1")
        self.label_10 = QtWidgets.QLabel(self.groupBox)
        self.label_10.setGeometry(QtCore.QRect(10, 110, 47, 13))
        self.label_10.setObjectName("label_10")
        self.k2 = QtWidgets.QComboBox(self.groupBox)
        self.k2.setGeometry(QtCore.QRect(90, 140, 161, 22))
        self.k2.setEditable(True)
        self.k2.setObjectName("k2")
        self.label_11 = QtWidgets.QLabel(self.groupBox)
        self.label_11.setGeometry(QtCore.QRect(10, 140, 47, 13))
        self.label_11.setObjectName("label_11")
        self.pkl_name = QtWidgets.QLineEdit(self.groupBox)
        self.pkl_name.setGeometry(QtCore.QRect(10, 510, 181, 20))
        self.pkl_name.setObjectName("pkl_name")
        self.methodology = QtWidgets.QTextEdit(self.groupBox)
        self.methodology.setGeometry(QtCore.QRect(10, 190, 241, 91))
        self.methodology.setObjectName("methodology")
        self.results = QtWidgets.QTextEdit(self.groupBox)
        self.results.setGeometry(QtCore.QRect(10, 300, 241, 91))
        self.results.setObjectName("results")
        self.conclusions = QtWidgets.QTextEdit(self.groupBox)
        self.conclusions.setGeometry(QtCore.QRect(10, 410, 241, 91))
        self.conclusions.setObjectName("conclusions")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.browse.setText(_translate("Dialog", "Open"))
        self.abstract_2.setPlainText(_translate("Dialog", "Abstract"))
        self.keywords.setPlainText(_translate("Dialog", "Keywords\n"
""))
        self.title.setPlainText(_translate("Dialog", "Title"))
        self.year.setPlainText(_translate("Dialog", "Year"))
        self.next.setText(_translate("Dialog", "Next"))
        self.previous.setText(_translate("Dialog", "Previous"))
        self.discard.setText(_translate("Dialog", "Discard"))
        self.label.setText(_translate("Dialog", "Abstract:"))
        self.label_2.setText(_translate("Dialog", "Keywords:"))
        self.label_3.setText(_translate("Dialog", "Title:"))
        self.link.setText(_translate("Dialog", "link"))
        self.groupBox.setTitle(_translate("Dialog", "Comments"))
        self.label_4.setText(_translate("Dialog", "Control:"))
        self.label_5.setText(_translate("Dialog", "Optimization:"))
        self.label_6.setText(_translate("Dialog", "Type:"))
        self.label_7.setText(_translate("Dialog", "Methodology:"))
        self.label_8.setText(_translate("Dialog", "Results:"))
        self.label_9.setText(_translate("Dialog", "Conclusions:"))
        self.save.setText(_translate("Dialog", "Save"))
        self.label_10.setText(_translate("Dialog", "Keyword1:"))
        self.label_11.setText(_translate("Dialog", "Keyword2"))
        self.methodology.toPla
        self.pkl_name.te
        self.methodology.setText


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
