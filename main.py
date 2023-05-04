import json
import sys
import csv
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QFileDialog
from employee_management_ui import Ui_MainWindow


class Employee:
    def __init__(self, name, gender, birth_date, hire_date, education, title, address, phone):
        self.name = name
        self.gender = gender
        self.birth_date = birth_date
        self.hire_date = hire_date
        self.education = education
        self.title = title
        self.address = address
        self.phone = phone


class EmployeeManagementSystem:
    def __init__(self, file_name):
        self.file_name = file_name
        try:
            with open(self.file_name, "r") as f:
                self.employees = json.load(f)
        except FileNotFoundError:
            self.employees = {}

    def add_employee(self, employee):
        self.employees[employee.name] = employee.__dict__
        self._save()

    def remove_employee(self, name):
        if name in self.employees:
            del self.employees[name]
            self._save()
        else:
            print(f"Employee '{name}' not found")

    def find_employee(self, **kwargs):
        results = []
        for employee in self.employees.values():
            match = True
            for key, value in kwargs.items():# 对每一位员工的键和值进行匹配
                if employee[key] != value:
                    match = False
                    break
            if match:# 匹配成功就添加到list
                results.append(employee)
        return results

    def update_employee(self, name, **kwargs):
        if name in self.employees:
            for key, value in kwargs.items():
                self.employees[name][key] = value
            self._save()
        else:
            print(f"Employee '{name}' not found")

    def sort_employee_by_attribute(self, attribute):
        self.employees = {k: v for k, v in sorted(self.employees.items(), key=lambda item: item[1][attribute])}
    def sort_employee_by_name(self):
        self.employees = {k: v for k, v in sorted(self.employees.items(), key=lambda item: item[1]['name'])}

    def _save(self):
        with open(self.file_name, "w") as f:
            json.dump(self.employees, f, ensure_ascii=False, indent=4)


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.ems = EmployeeManagementSystem("employees.json")
        self.init_table()

        self.add_employee_button.clicked.connect(self.add_employee)
        self.remove_employee_button.clicked.connect(self.remove_employee)
        self.update_employee_button.clicked.connect(self.update_employee)
        self.find_employee_button.clicked.connect(self.find_employee)

        # 添加新的按钮事件
        self.import_csv_action.triggered.connect(self.import_csv)
        self.sort_employee_button.clicked.connect(self.sort_employee)

    def init_table(self):
        self.employee_table.setRowCount(len(self.ems.employees))
        self.employee_table.setColumnCount(8)
        self.employee_table.setHorizontalHeaderLabels(
            ["姓名", "性别", "出生年月", "工作年月", "学历", "职务", "住址", "电话"])
        self.refresh_table()

    def refresh_table(self):
        for row, employee in enumerate(self.ems.employees.values()):
            for col, key in enumerate(employee):
                item = QTableWidgetItem(str(employee[key]))
                self.employee_table.setItem(row, col, item)

    def add_employee(self):
        employee = Employee(
            self.name_edit.text(),
            self.gender_edit.text(),
            self.birth_date_edit.text(),
                        self.hire_date_edit.text(),
            self.education_edit.text(),
            self.title_edit.text(),
            self.address_edit.text(),
            self.phone_edit.text()
        )
        self.ems.add_employee(employee)
        self.refresh_table()

    def remove_employee(self):
        name = self.name_edit.text()
        self.ems.remove_employee(name)
        self.refresh_table()

    def update_employee(self):
        name = self.name_edit.text()
        update_values = {
            "gender": self.gender_edit.text(),
            "birth_date": self.birth_date_edit.text(),
            "hire_date": self.hire_date_edit.text(),
            "education": self.education_edit.text(),
            "title": self.title_edit.text(),
            "address": self.address_edit.text(),
            "phone": self.phone_edit.text()
        }
        self.ems.update_employee(name, **update_values)
        self.refresh_table()

    def find_employee(self):
        search_values = {
            "name": self.name_edit.text(),
            "gender": self.gender_edit.text(),
            "birth_date": self.birth_date_edit.text(),
            "hire_date": self.hire_date_edit.text(),
            "education": self.education_edit.text(),
            "title": self.title_edit.text(),
            "address": self.address_edit.text(),
            "phone": self.phone_edit.text()
        }
        search_values = {key: value for key, value in search_values.items() if value}
        results = self.ems.find_employee(**search_values)
        self.show_results(results)

    def show_results(self, results):
        self.employee_table.setRowCount(len(results))
        for row, employee in enumerate(results):
            for col, key in enumerate(employee):
                item = QTableWidgetItem(str(employee[key]))
                self.employee_table.setItem(row, col, item)
    def import_csv(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Open CSV", "", "CSV Files (*.csv)")
        if not file_name:
            return

        with open(file_name, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                employee = Employee(
                    row['name'],
                    row['gender'],
                    row['birth_date'],
                    row['hire_date'],
                    row['education'],
                    row['title'],
                    row['address'],
                    row['phone']
                )
                self.ems.add_employee(employee)
        self.refresh_table()
    def sort_employee(self):
        
        self.ems.sort_employee_by_name()
        self.refresh_table()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
