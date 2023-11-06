import sys
import random
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5 import QtCore, QtGui, QtWidgets

class ChartWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Vẽ Biểu Đồ")
        self.setGeometry(0, 0, 1920, 1080)  # Đặt vị trí và kích thước của cửa sổ

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout(central_widget)
        layout.setGeometry(QtCore.QRect(1080, 50, 821, 381))  # Đặt vị trí và kích thước của layout

        self.canvas = FigureCanvas(plt.figure())
        layout.addWidget(self.canvas)

        self.button = QPushButton("Vẽ Biểu Đồ")
        layout.addWidget(self.button)

        self.button.clicked.connect(self.plot_chart)

    def plot_chart(self):
        # Tạo dữ liệu ngẫu nhiên để vẽ biểu đồ
        data = [random.randint(1, 10) for _ in range(5)]

        # Xóa biểu đồ cũ trước khi vẽ biểu đồ mới
        self.canvas.figure.clear()

        # Vẽ biểu đồ cột sử dụng Matplotlib
        ax = self.canvas.figure.add_subplot(111)
        ax.bar(range(1, 6), data)
        ax.set_xlabel("Dữ Liệu")
        ax.set_ylabel("Giá Trị")
        ax.set_title("Biểu Đồ Cột Ngẫu Nhiên")

        # Cập nhật biểu đồ trên giao diện
        self.canvas.draw()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ChartWindow()
    window.show()
    sys.exit(app.exec_())
