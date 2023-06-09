from PyQt5 import QtCore,  QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QRegExp

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)

        # 添加菜单栏功能
        self.menubar = MainWindow.menuBar()
        self.fileMenu = self.menubar.addMenu("File")
        self.import_csv_action = QtWidgets.QAction('load csv',MainWindow)
        self.exitAction = QtWidgets.QAction("Exit", MainWindow)
        self.exitAction.triggered.connect(QtWidgets.qApp.quit)
        self.fileMenu.addAction(self.exitAction)
        self.fileMenu.addAction(self.import_csv_action)

        # self.menubar = QtWidgets.QMenuBar(MainWindow)
        # self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        # self.menubar.setObjectName("menubar")
        # MainWindow.setMenuBar(self.menubar)

        # 在原有按钮之后添加排序按钮

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.add_employee_button = QtWidgets.QPushButton(self.centralwidget)
        self.add_employee_button.setObjectName("add_employee_button")
        self.gridLayout.addWidget(self.add_employee_button, 3, 0, 1, 1)
        self.remove_employee_button = QtWidgets.QPushButton(self.centralwidget)
        self.remove_employee_button.setObjectName("remove_employee_button")
        self.gridLayout.addWidget(self.remove_employee_button, 3, 1, 1, 1)
        self.update_employee_button = QtWidgets.QPushButton(self.centralwidget)
        self.update_employee_button.setObjectName("update_employee_button")
        self.gridLayout.addWidget(self.update_employee_button, 3, 2, 1, 1)
        self.find_employee_button = QtWidgets.QPushButton(self.centralwidget)
        self.find_employee_button.setObjectName("find_employee_button")
        self.gridLayout.addWidget(self.find_employee_button, 3, 3, 1, 1)
        self.sort_employee_button = QtWidgets.QPushButton(self.centralwidget)
        self.sort_employee_button.setObjectName("sort_employee_button")
        self.gridLayout.addWidget(self.sort_employee_button, 3, 4, 1, 1)

        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.name_label = QtWidgets.QLabel(self.centralwidget)
        self.name_label.setObjectName("name_label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.name_label)
        self.name_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.name_edit.setObjectName("name_edit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.name_edit)
        self.gender_label = QtWidgets.QLabel(self.centralwidget)
        self.gender_label.setObjectName("gender_label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.gender_label)
        self.gender_edit = QComboBox()
        self.gender_edit.addItems(['男', '女'])
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.gender_edit)
        self.birth_date_label = QtWidgets.QLabel(self.centralwidget)
        self.birth_date_label.setObjectName("birth_date_label")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.birth_date_label)
        self.birth_date_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.birth_date_edit.setObjectName("birth_date_edit")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.birth_date_edit)
        self.hire_date_label = QtWidgets.QLabel(self.centralwidget)
        self.hire_date_label.setObjectName("hire_date_label")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.hire_date_label)
        self.hire_date_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.hire_date_edit.setObjectName("hire_date_edit")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.hire_date_edit)
        self.education_label = QtWidgets.QLabel(self.centralwidget)
        self.education_label.setObjectName("education_label")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.education_label)
        self.education_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.education_edit.setObjectName("education_edit")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.education_edit)
        self.title_label = QtWidgets.QLabel(self.centralwidget)
        self.title_label.setObjectName("title_label")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.title_label)
        self.title_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.title_edit.setObjectName("title_edit")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.title_edit)
        self.address_label = QtWidgets.QLabel(self.centralwidget)
        self.address_label.setObjectName("address_label")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.address_label)
        self.address_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.address_edit.setObjectName("address_edit")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.address_edit)
        self.phone_label = QtWidgets.QLabel(self.centralwidget)
        self.phone_label.setObjectName("phone_label")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.phone_label)
        self.phone_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.phone_edit.setObjectName("phone_edit")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.phone_edit)
        self.gridLayout.addLayout(self.formLayout, 1, 0, 1, 3)
        
        # 设置 birth_date_edit 只能输入四位数的数字
        birth_date_validator = QIntValidator(1000, 9999)
        self.birth_date_edit.setValidator(birth_date_validator)

        # 设置 hire_date_edit 只能输入四位数的数字
        hire_date_validator = QIntValidator(1000, 9999)
        self.hire_date_edit.setValidator(hire_date_validator)
        # 设置 gender_edit 只能输入 '男' 或 '女'
        gender_regex = QRegExp("^(男|女)$")
        gender_validator = QRegExpValidator(gender_regex, self.gender_edit)
        self.gender_edit.setValidator(gender_validator)
        self.employee_table = QtWidgets.QTableWidget(self.centralwidget)
        self.employee_table.setObjectName("employee_table")
        self.employee_table.setColumnCount(0)
        self.employee_table.setRowCount(0)
        self.gridLayout.addWidget(self.employee_table, 2, 0, 1, 5)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.sort_employee_button.setText(_translate("MainWindow", "以入职年份排序"))
        self.add_employee_button.setText(_translate("MainWindow", "添加员工"))
        self.remove_employee_button.setText(_translate("MainWindow", "删除员工"))
        self.update_employee_button.setText(_translate("MainWindow", "更新员工信息"))
        self.find_employee_button.setText(_translate("MainWindow", "据提示查找员工"))
        self.name_label.setText(_translate("MainWindow", "名字"))
        self.gender_label.setText(_translate("MainWindow", "性别"))
        self.birth_date_label.setText(_translate("MainWindow", "出生年份"))
        self.hire_date_label.setText(_translate("MainWindow", "入职年份"))
        self.education_label.setText(_translate("MainWindow", "学历"))
        self.title_label.setText(_translate("MainWindow", "职位"))
        self.address_label.setText(_translate("MainWindow", "住址"))
        self.phone_label.setText(_translate("MainWindow", "电话"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


