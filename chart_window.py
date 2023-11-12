import sys
import numpy as np
import matplotlib.pyplot as plt
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from matplotlib.backends.backend_qt5agg import FigureCanvas
from APIHandler import APIHandler


class WindowEfficacyDayInWeek(QMainWindow):
    def __init__(self):
        super().__init__()

        # Create a main widget
        main_widget = QWidget(self)
        self.setCentralWidget(main_widget)

        # Create a figure and a canvas for Matplotlib
        self.figure, self.ax = plt.subplots()
        self.canvas = FigureCanvas(self.figure)

        # Create a vertical layout and add the canvas to it
        layout = QVBoxLayout(main_widget)
        layout.addWidget(self.canvas)

        self.plot_chart()

    def plot_chart(self):
        x = ["Thứ 2", "Thứ 3", "Thứ 4", "Thứ 5", "Thứ 6", "Thứ 7"]
        y = APIHandler.clickMethod_efficacy_day_in_week()

        # Plot the data
        bars = self.ax.bar(x, y)
        self.ax.set_xlabel("Ngày trong tuần")
        self.ax.set_ylabel("Năng suất (%)")
        self.ax.set_title(
            "Năng suất làm việc theo ngày trong tuần",
            fontsize=13,
            fontweight="bold",
            color="red",
        )

        # Set the Y-axis limits from 0 to 100
        self.ax.set_ylim(0, 100)
        # Set the Y-axis tick intervals to 5 units
        self.ax.set_yticks(range(0, 101, 5))

        # Add labels for each bar
        for bar, value in zip(bars, y):
            self.ax.text(
                bar.get_x() + bar.get_width() / 2,
                value,
                str(value),
                ha="center",
                va="bottom",
            )

        # Show the plot using plt.show()
        plt.show()


class WindowAgeEfficacy(QMainWindow):
    def __init__(self):
        super().__init__()

        # Create a main widget
        main_widget = QWidget(self)
        self.setCentralWidget(main_widget)

        # Create a figure and a canvas for Matplotlib
        self.figure, self.ax = plt.subplots()
        self.canvas = FigureCanvas(self.figure)

        # Create a vertical layout and add the canvas to it
        layout = QVBoxLayout(main_widget)
        layout.addWidget(self.canvas)

        self.plot_chart()

    def plot_chart(self):
        x, y = APIHandler.clickMethod_age_efficacy()

        # Kết hợp cặp (x, y) bằng zip
        couples = list(
            zip(x, [val * 100 for val in y])
        )  # Nhân mỗi giá trị trục y lên 100

        # Sắp xếp cặp theo giá trị x
        sorted_couples = sorted(couples, key=lambda pair: pair[0])

        # Tách cặp thành các mảng x và y
        x, y = zip(*sorted_couples)

        # Vẽ biểu đồ line
        plt.plot(x, y, marker="o", linestyle="-")

        # Đặt nhãn cho trục X và Y
        plt.xlabel("Độ tuổi")
        plt.ylabel("Năng suất (%)")

        # Đặt tiêu đề biểu đồ
        plt.title(
            "Ảnh hưởng độ tuổi đến hiệu quả làm việc trung bình hàng ngày",
            fontsize=13,
            fontweight="bold",
            color="red",
        )

        # Đặt độ chia trục x là đơn vị 5
        plt.xticks([i for i in range(min(x), max(x) + 1, 2)])

        # # Đặt khoảng chia trục y là 5 đơn vị
        # plt.yticks([i / 20 for i in range(21)])  # 20 đơn vị tương ứng với 1

        # Đặt khoảng chia trục y là 5 đơn vị bắt đầu từ 30
        self.ax.set_yticks(range(30, 101, 5))

        # Đặt giới hạn cho trục y từ 30 đến 100
        self.ax.set_ylim(30, 100)

        # Hiển thị biểu đồ
        plt.show()


class WindowSexEfficacy(QMainWindow):
    def __init__(self):
        super().__init__()

        # Create a main widget
        main_widget = QWidget(self)
        self.setCentralWidget(main_widget)

        # Create a figure and a canvas for Matplotlib
        self.figure, self.ax = plt.subplots()
        self.canvas = FigureCanvas(self.figure)

        # Create a vertical layout and add the canvas to it
        layout = QVBoxLayout(main_widget)
        layout.addWidget(self.canvas)

        self.plot_chart()

    def plot_chart(self):
        men_means, women_means = APIHandler.clickMethod_sex_efficacy()
        ind = np.arange(len(men_means))  # the x locations for the groups
        width = 0.35  # the width of the bars

        rects1 = self.ax.bar(ind - width / 2, men_means, width, label="Men")
        rects2 = self.ax.bar(ind + width / 2, women_means, width, label="Women")

        # Add some text for labels, title, and custom x-axis tick labels
        self.ax.set_ylabel("Phần Trăm")
        self.ax.set_title(
            "Ảnh hưởng giới tính đến hiệu quả làm việc",
            fontsize=13,
            fontweight="bold",
            color="red",
        )
        self.ax.set_xticks(ind)
        self.ax.set_xticklabels(("Tỉ lệ cùng giới", "Hiệu quả"))
        self.ax.legend()

        # Add values above each bar
        for rect in rects1:
            height = rect.get_height()
            self.ax.annotate(
                "{}".format(height),
                xy=(rect.get_x() + rect.get_width() / 2, height),
                xytext=(0, 3),  # 3 points vertical offset
                textcoords="offset points",
                ha="center",
                va="bottom",
            )

        for rect in rects2:
            height = rect.get_height()
            self.ax.annotate(
                "{}".format(height),
                xy=(rect.get_x() + rect.get_width() / 2, height),
                xytext=(0, 3),  # 3 points vertical offset
                textcoords="offset points",
                ha="center",
                va="bottom",
            )
        plt.show()
