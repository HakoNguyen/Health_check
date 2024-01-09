import sys
# pip install pyqt5
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLabel, QStackedWidget, QMessageBox
from app_ui import Ui_MainWindow

class MainWindow:
    def __init__(self):
        self.main_win = QMainWindow()
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self.main_win)

#khai báo button
        self.uic.pushButton.clicked.connect(self.showpage1)
        self.uic.pushButton_2.clicked.connect(self.showpage2)
        self.uic.pushButton_3.clicked.connect(self.showpage3)
        self.uic.pushButton_4.clicked.connect(self.showpage4)

#Khai bao Submit Button
        self.uic.pushButton_5.clicked.connect(self.tinh_toan)

#define hàm mở các page
    def showpage1(self):
        self.uic.stackedWidget.setCurrentWidget(self.uic.page)
    def showpage2(self):
        self.uic.stackedWidget.setCurrentWidget(self.uic.page_2)
    def showpage3(self):
        self.uic.stackedWidget.setCurrentWidget(self.uic.page_3)
    def showpage4(self):
        self.uic.stackedWidget.setCurrentWidget(self.uic.page_4)

#define hàm tinh_toan
    def tinh_toan(self):
        name = self.uic.lineEdit_5.text()
        age = int(self.uic.lineEdit_6.text())
        calorie_in = int(self.uic.lineEdit.text())
        calorie_out = int(self.uic.lineEdit_2.text())
        weight= int(self.uic.lineEdit_3.text())
        height = int(self.uic.lineEdit_4.text())
        bmr = self.calculate_bmr(weight, height, age)


        #kiểm tra điều kiện cho chỉ số BMR
        bmr_condition = " "
        if self.uic.checkBox.isChecked():
            if bmr > 2500:
                bmr_condition = "Vượt quá mức tiêu chuẩn!"
            elif 1500 < bmr <= 2500:
                bmr_condition = "Cơ thể bạn đang ổn định."
            else:
                bmr_condition = "Thấp hơn so với mức tiêu chuẩn."
        elif self.uic.checkBox_2.isChecked():
            if bmr > 2000:
                bmr_condition = "Vượt quá mức tiêu chuẩn!"
            elif 1000 < bmr <= 1500:
                bmr_condition = "Cơ thể bạn đang ổn định."
            else:
                bmr_condition = "Thấp hơn so với mức tiêu chuẩn."

       #Kiểm tra điều kiện cho calories
            calorie_condition = ""
        calorie_diff = calorie_in - calorie_out
        if calorie_diff > 200:
            calorie_condition = "Bạn nên tập thể dục"
        elif calorie_diff < -400:
            calorie_condition = "Bạn nên ăn gì đó"
        else:
            calorie_condition = "Cơ thể ổn định"



        msg = QMessageBox()
        msg.setWindowTitle("YOUR RESULT")

        message = f"Name: {name}\nAge: {age}\nCalories In: {calorie_in}\nCalories Out: {calorie_out}\n" \
                  f"Weight: {weight} kg\nHeight: {height} cm\n\nBMR: {bmr}\nBMR Condition: {bmr_condition}\n" \
                  f"Calorie Condition: {calorie_condition}"

        msg.setText(message)

        msg.exec_()

        #định nghĩa cách tính BMR
    def calculate_bmr(self, weight, height, age):
# Tính chỉ số BMR theo công thức Harris-Benedict (cho nam và nữ)
        if self.uic.checkBox.isChecked():  # Nam
            bmr = 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
        elif self.uic.checkBox_2.isChecked():  # Nữ
            bmr = 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)
        else:
            bmr = 0  # Trường hợp không chọn giới tính

        return bmr




    def show(self):
        # command to run
        self.main_win.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())
