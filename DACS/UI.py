# -*- coding: utf-8 -*-
import csv

# Form implementation generated from reading ui file 'UI.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QAbstractTableModel, Qt
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtSql import QSqlDatabase, QSqlQuery
from PyQt5.QtWidgets import QTableView, QHeaderView

import connectDB
from main import tinh


class Ui_Form(object):
    def setupUi(self, Form):
        self.tinh = tinh
        Form.setObjectName("Form")
        Form.resize(833, 841)
        font = QtGui.QFont()
        font.setUnderline(False)
        font.setStrikeOut(False)
        Form.setFont(font)
        Form.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        Form.setToolTipDuration(0)
        Form.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tableView = QtWidgets.QTableView(Form)
        self.tableView.setGeometry(QtCore.QRect(10, 330, 811, 501))
        self.tableView.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.tableView.setObjectName("tableView")
        self.model = QtGui.QStandardItemModel()
        self.tableView.setModel(self.model)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 50, 371, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.label.setFont(font)
        self.label.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setAutoFillBackground(False)
        self.label.setStyleSheet("color: rgb(255, 200, 0);\n"
"background-color: rgb(245, 245, 245);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(20, 110, 81, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(20, 150, 81, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(20, 190, 81, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(110, 110, 281, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox_2 = QtWidgets.QComboBox(Form)
        self.comboBox_2.setGeometry(QtCore.QRect(110, 150, 281, 22))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_3 = QtWidgets.QComboBox(Form)
        self.comboBox_3.setGeometry(QtCore.QRect(110, 190, 281, 22))
        self.comboBox_3.setObjectName("comboBox_3")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(450, 50, 361, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.label_5.setFont(font)
        self.label_5.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.label_5.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_5.setAutoFillBackground(False)
        self.label_5.setStyleSheet("color: rgb(255, 200, 0);\n"
"background-color: rgb(245, 245, 245);")
        self.label_5.setObjectName("label_5")
        self.horizontalSlider = QtWidgets.QSlider(Form)
        self.horizontalSlider.setGeometry(QtCore.QRect(540, 150, 271, 22))
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(450, 150, 81, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(450, 190, 91, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.horizontalSlider_2 = QtWidgets.QSlider(Form)
        self.horizontalSlider_2.setGeometry(QtCore.QRect(540, 190, 271, 22))
        self.horizontalSlider_2.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_2.setObjectName("horizontalSlider_2")
        self.spinBox = QtWidgets.QSpinBox(Form)
        self.spinBox.setGeometry(QtCore.QRect(540, 230, 42, 22))
        self.spinBox.setObjectName("spinBox")
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(450, 230, 81, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(Form)
        self.label_9.setGeometry(QtCore.QRect(660, 230, 81, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.spinBox_2 = QtWidgets.QSpinBox(Form)
        self.spinBox_2.setGeometry(QtCore.QRect(750, 230, 42, 22))
        self.spinBox_2.setObjectName("spinBox_2")
        self.label_10 = QtWidgets.QLabel(Form)
        self.label_10.setGeometry(QtCore.QRect(450, 110, 91, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.comboBox_4 = QtWidgets.QComboBox(Form)
        self.comboBox_4.setGeometry(QtCore.QRect(540, 110, 271, 22))
        self.comboBox_4.setObjectName("comboBox_4")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(10, 267, 250, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 200, 0);\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(570, 267, 250, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 200, 0);\n"
"")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(290, 267, 250, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 200, 0);\n"
"")
        self.pushButton_4.setObjectName("pushButton_4")


        self.pushButton.clicked.connect(self.load_data_from_csv)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "              THÔNG TIN VỊ TRÍ"))
        self.label_2.setText(_translate("Form", "Tỉnh thành:"))
        self.label_3.setText(_translate("Form", "Quận huyện:"))
        self.label_4.setText(_translate("Form", "Đường phố:"))
        self.label_5.setText(_translate("Form", "                THÔNG TIN KHÁC"))
        self.label_6.setText(_translate("Form", "Khoảng giá:"))
        self.label_7.setText(_translate("Form", "Diện tích:"))
        self.label_8.setText(_translate("Form", "Phòng ngủ:"))
        self.label_9.setText(_translate("Form", "Phòng tắm:"))
        self.label_10.setText(_translate("Form", "Loại nhà đất:"))
        self.pushButton.setText(_translate("Form", "TÌM KIẾM"))
        self.pushButton_3.setText(_translate("Form", "LẤY DỮ LIỆU"))
        self.pushButton_4.setText(_translate("Form", "LƯU THÔNG TIN"))


    def load_data_from_csv(self):
        # Đường dẫn đến tệp CSV của bạn
        csv_file_path = "UIdata.csv"
        try:
            with open(csv_file_path, 'r', newline='', encoding='utf-16') as file:
                # Đọc dữ liệu từ tệp CSV và thêm nó vào bảng
                reader = csv.reader(file, delimiter='\t')

                # Đọc dòng đầu tiên để sử dụng làm header
                header = next(reader)

                # Xóa dữ liệu cũ trong bảng và đặt header
                self.model.clear()
                self.model.setHorizontalHeaderLabels(header)

                # Thêm dữ liệu từ dòng thứ 2 trở đi
                for row_data in reader:
                    try:
                        items = [QtGui.QStandardItem(field) for field in row_data]
                        self.model.appendRow(items)
                    except Exception as e:
                        print("Error loading CSV:", str(e))
                        continue
        except Exception as e:
            print("Error loading CSV:", str(e))

    def load_data_from_mySQL(self):
        db = QSqlDatabase.addDatabase("QMYSQL")
        db.setHostName("127.0.0.1")  # Địa chỉ IP hoặc tên máy chủ MySQL
        db.setPort(3306)  # Port mặc định của MySQL là 3306
        db.setDatabaseName("giadat2")  # Tên cơ sở dữ liệu MySQL
        db.setUserName("root")  # Tên người dùng MySQL
        db.setPassword("123123")

        print(db.open())
        print(db.lastError().text())
        print(db.drivers())
        if not db.open():
            print("Không thể kết nối đến MySQL")
            return

        query = QSqlQuery()
        query.exec_(f"SELECT * FROM {tinh}")
        model = QStandardItemModel()

        print(query.size())

        if query.isActive():
            while query.next():
                column_value = query.value(4)  # Thay đổi column_index bằng chỉ số của cột bạn muốn truy cập
                print(column_value)

        model.setHorizontalHeaderLabels(
            [
                'type', 'Location', 'Name', 'Price',
                'Road_Surface_Area', 'Floor', 'Bedrooms', 'Parking',
                'Area', 'Size', 'Direction',  'Link'
            ])  #

        row = 0
        while query.next():
            if int(query.value(0)) == 1.1:
                item1 = QStandardItem("Nhà mặt tiền")
            elif int(query.value(0)) == 1.2:
                item1 = QStandardItem("Nhà trong hẻm")
            elif int(query.value(0)) == 2:
                item1 = QStandardItem("Mặt bằng")
            else:
                item1 = QStandardItem("Căn hộ chung cư")

            item2 = QStandardItem(str(query.value(1)) + str(query.value(2)) + str(query.value(3)))
            item3 = QStandardItem(str(query.value(4)))
            item4 = QStandardItem(str(query.value(13)))
            item5 = QStandardItem(str(query.value(6)))
            item6 = QStandardItem(str(query.value(7)))
            item7 = QStandardItem(str(query.value(8)))
            item8 = QStandardItem(str(query.value(9)))
            item9 = QStandardItem(str(query.value(10)))
            item10 = QStandardItem(str(query.value(11)))
            item11 = QStandardItem(str(query.value(12)))
            item12 = QStandardItem(str(query.value(14)))

            model.setItem(row, 0, item1)
            model.setItem(row, 1, item2)
            model.setItem(row, 2, item3)
            model.setItem(row, 3, item4)
            model.setItem(row, 4, item5)
            model.setItem(row, 5, item6)
            model.setItem(row, 6, item7)
            model.setItem(row, 7, item8)
            model.setItem(row, 8, item9)
            model.setItem(row, 9, item10)
            model.setItem(row, 10, item11)
            model.setItem(row, 11, item12)
            row += 1

        self.tableView.setModel(model)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())