# Form implementation generated from reading ui file '.\removebookwidget.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 100)
        Form.setMinimumSize(QtCore.QSize(400, 100))
        Form.setMaximumSize(QtCore.QSize(400, 100))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(".\\../assets/logo.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        Form.setWindowIcon(icon)
        Form.setLocale(QtCore.QLocale(QtCore.QLocale.Language.English, QtCore.QLocale.Country.UnitedStates))
        self.formLayout = QtWidgets.QFormLayout(Form)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(parent=Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label)
        self.removetitle = QtWidgets.QLineEdit(parent=Form)
        self.removetitle.setObjectName("removetitle")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.removetitle)
        self.removeButton = QtWidgets.QPushButton(parent=Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.removeButton.setFont(font)
        self.removeButton.setObjectName("removeButton")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.removeButton)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Remove Book"))
        self.label.setText(_translate("Form", "Book Title"))
        self.removeButton.setText(_translate("Form", "Remove"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())
