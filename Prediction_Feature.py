import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

from APIClient import APIClient
import matplotlib.pyplot as plt

base_url = "https://bigquery-production.up.railway.app"
# Create an instance of the APIClient class
api_client = APIClient(base_url)
api_prediction = "/api/worker/getWorkerActucalEfficacy?id="


class Prediction:
    @staticmethod
    def clickMethod_prediction(ui):
        # Get the text from self.lineEdit_ID
        text_id = ui.lineEdit_NhapID.text()
        if text_id != "":
            # Call the get_data method and pass the input_text as the endpoint path
            data = api_client.get_data(f"{api_prediction}{text_id}")
            (
                original_value,
                predict_value,
                rate,
            ) = Prediction.prediction(data)
            Prediction.plot_chart_prediction(original_value, predict_value, rate)

    def plot_chart_prediction(original_value, predict_value, rate):
        x = ["Thực tế", "Dự đoán"]
        y = [original_value, predict_value]
        title = "Dự đoán năng suất làm việc"

        # Create a new figure and axis
        fig, ax = plt.subplots()

        # Plot the data
        bars = ax.bar(x, y)
        ax.set_ylabel("Hiệu quả làm việc")
        ax.set_title(
            title,
            fontsize=13,
            fontweight="bold",
            color="red",
        )

        # Set the Y-axis limits from 0 to 100
        ax.set_ylim(0, 400)

        # Set the Y-axis tick intervals to 5 units
        ax.set_yticks(range(0, 401, 20))

        # Add labels for each bar
        for bar, value in zip(bars, y):
            ax.text(
                bar.get_x() + bar.get_width() / 2,
                value,
                str(value),
                ha="center",
                va="bottom",
            )
        # Add text to the plot
        ax.text(
            0.5,
            -0.1,
            "Độ lệch so với giá trị ban đầu {:.2f} %".format(rate),
            transform=ax.transAxes,
            ha="center",
            fontsize=13,
            color="brown",
        )
        # Show the plot
        plt.show()

    def prediction(data_prediction):
        # 1. Đọc dữ liệu từ tệp CSV
        data = pd.read_csv(
            "/Users/mac/Documents/Study/Project/Data_Engineering/BigQuery/employee_data.csv"
        )

        # 2. Xử lý dữ liệu nếu cần (loại bỏ dữ liệu nhiễu, xử lý dữ liệu thiếu, mã hóa biến phân loại, ...)

        # 3. Chia dữ liệu thành tập huấn luyện và tập kiểm tra
        X = data[
            ["sub_health_h", "sub_sociality_h", "un_efficient_date", "efficacy_date"]
        ]
        y = data["actual_efficacy"]
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=0
        )

        # 4. Tạo mô hình Random Forest Regressor
        model = RandomForestRegressor(n_estimators=100, random_state=0)

        # 5. Huấn luyện mô hình trên tập huấn luyện
        model.fit(X_train, y_train)

        # 6. Đánh giá mô hình sử dụng R-squared
        scores = cross_val_score(model, X_train, y_train, cv=10, scoring="r2")
        print("Cross-Validation R-squared Scores:")
        print(scores)
        print(f"Mean R-squared: {np.mean(scores)}")

        # 7. Dự đoán trên tập kiểm tra
        y_pred = model.predict(X_test)

        # 8. Đánh giá mô hình trên tập kiểm tra (sử dụng Mean Squared Error)
        mse = mean_squared_error(y_test, y_pred)
        print("Mean Squared Error on Test Set:", mse)

        # Make predictions for a new employee
        # get data by employee from API here
        sub_health_h = data_prediction.get("health")
        sub_sociality_h = data_prediction.get("sociality")
        un_efficient_date = data_prediction.get("unEfficacyDate")
        efficacy_date = data_prediction.get("efficacyDate")
        actual_efficacy = data_prediction.get("actualEfficacy")

        new_employee = np.array(
            [[sub_health_h, sub_sociality_h, un_efficient_date, efficacy_date]]
        )  # Replace with the actual values
        prediction = model.predict(new_employee)

        rate = abs(prediction[0] - actual_efficacy) / actual_efficacy * 10
        actual_efficacy = round(actual_efficacy)
        prediction[0] = round(prediction[0])
        return actual_efficacy, prediction[0], rate
