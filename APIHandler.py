# click_method.py
from APIClient import APIClient
from PyQt6.QtWidgets import QTableWidgetItem

base_url = "https://bigquery-production.up.railway.app"
# Create an instance of the APIClient class
api_client = APIClient(base_url)
api_worker = "/api/worker?id"
api_worker_firstName = "/api/worker/firstName?firstName"
api_worker_lastName = "/api/worker/lastName?lastName"
api_worker_dayOff = "/api/worker/dayOff?id"
api_timesheets = "/api/timesheets?"
api_efficacy_day_in_week = "/api/dayinweek"
api_age_efficacy = "/api/age/ageEfficacy"
api_sex_property = "/api/sex?sex="


class APIHandler:
    @staticmethod
    def clickMethod_search_information(ui):
        # Get the text from self.lineEdit_ID
        input_text_ID = ui.lineEdit_ID.text()
        input_firstName = ui.lineEdit_firstName.text()
        input_lastName = ui.lineEdit_lastName.text()
        # input_dayOff = ui.label_dayOff.text()

        if input_text_ID != "":
            # Call the get_data method and pass the input_text as the endpoint path
            data = api_client.get_data(f"{api_worker}={input_text_ID}")
        if input_firstName != "":
            # Call the get_data method and pass the input_text as the endpoint path
            data = api_client.get_data(f"{api_worker_firstName}={input_firstName}")
            ui.lineEdit_ID.setDisabled(False)
            ui.lineEdit_lastName.setDisabled(False)
        if input_lastName != "":
            # Call the get_data method and pass the input_text as the endpoint path
            data = api_client.get_data(f"{api_worker_lastName}={input_lastName}")
            ui.lineEdit_firstName.setDisabled(False)
            ui.lineEdit_ID.setDisabled(False)
        APIHandler.search_employee_information(ui, data)

    @staticmethod
    def clickMethod_timesheets(ui):
        # Get the text from self.lineEdit_ID
        input_text_ID = ui.lineEdit_NhapID.text()
        input_fromDay = ui.dateEdit_FromDay.text().split("-")
        input_toDay = ui.dateEdit_ToDay.text().split("-")

        input_fromDay = "-".join(reversed(ui.dateEdit_FromDay.text().split("-")))
        input_toDay = "-".join(reversed(ui.dateEdit_ToDay.text().split("-")))

        output_data = None  # Initialize output_data to None

        if (input_text_ID != "") and (input_fromDay != "") and (input_toDay != ""):
            # Call the get_data method and pass the input_text as the endpoint path
            output_data = api_client.get_data(
                f"{api_timesheets}id={input_text_ID}&from={input_fromDay}&to={input_toDay}"
            )
        # Check if output_data is not None before calling loadProducts
        if output_data is not None:
            APIHandler.timesheets_information(ui, output_data)

    # Xóa toàn bộ dữ liệu hiện tại trong bảng
    def resetTable(tableWidget):
        tableWidget.setRowCount(0)  # Đặt số hàng về 0

    def search_employee_information(ui, data):
        data_empty = {
            "id": 0,
            "firstName": "",
            "lastName": "",
            "age": 0,
            "sex": "",
            "shift": "",
            "team": "",
            "role": "",
        }

        # Xóa toàn bộ dữ liệu hiện tại
        row_index = 0
        print("row_index:", row_index)
        APIHandler.resetTable(ui.tableWidget)
        ui.tableWidget.setRowCount(len(data))

        if data == data_empty:
            return

        # Kiểm tra kiểu dữ liệu của data
        if not isinstance(data, list):
            # Nếu data không phải là một list, thêm nó vào một list
            list_data = [data]
        else:
            # Nếu data đã là một list, thì sử dụng nó như là list_data
            list_data = data

        # list_data = data
        for item in list_data:
            output_ID = item["id"]
            output_firstName = item["firstName"]
            output_lastName = item["lastName"]
            output_age = item["age"]
            output_sex = item["sex"]
            output_shift = item["shift"]
            output_team = item["team"]
            output_role = item["role"]
            ui.tableWidget.setItem(row_index, 0, QTableWidgetItem(str(output_ID)))
            ui.tableWidget.setItem(
                row_index, 1, QTableWidgetItem(str(output_firstName))
            )
            ui.tableWidget.setItem(row_index, 2, QTableWidgetItem(str(output_lastName)))
            ui.tableWidget.setItem(row_index, 3, QTableWidgetItem(str(output_age)))
            ui.tableWidget.setItem(row_index, 4, QTableWidgetItem(str(output_sex)))
            ui.tableWidget.setItem(row_index, 5, QTableWidgetItem(str(output_shift)))
            ui.tableWidget.setItem(row_index, 6, QTableWidgetItem(str(output_team)))
            ui.tableWidget.setItem(row_index, 7, QTableWidgetItem(str(output_role)))
            row_index += 1

    def timesheets_information(ui, data):
        data_empty = {"id": 0, "workingDay": 0}
        # Xóa toàn bộ dữ liệu hiện tại
        row_index = 0
        APIHandler.resetTable(ui.tableWidget)
        ui.tableWidget.setRowCount(len(data))
        # ui.tableWidget.setColumnCount(2)

        if data == data_empty:
            return
        # ui.tableWidget.setColumnWidth(0, 150)

        # Kiểm tra kiểu dữ liệu của data
        if not isinstance(data, list):
            # Nếu data không phải là một list, thêm nó vào một list
            list_data = [data]
        else:
            # Nếu data đã là một list, thì sử dụng nó như là list_data
            list_data = data

        # list_data = data
        for item in list_data:
            output_ID = item["id"]
            output_workingDay = item["workingDay"]
            luong_co_ban = 12000
            phu_cap_onsite = 2000
            an_trua = 1500
            tong_thu_nhap = 3500 + 600 * output_workingDay
            BHXH = 0.1 * tong_thu_nhap
            thuc_nhan = tong_thu_nhap - BHXH

            ui.tableWidget.setItem(row_index, 0, QTableWidgetItem(str(output_ID)))
            ui.tableWidget.setItem(
                row_index, 1, QTableWidgetItem(str(output_workingDay))
            )
            ui.tableWidget.setItem(row_index, 2, QTableWidgetItem(str(luong_co_ban)))
            ui.tableWidget.setItem(row_index, 3, QTableWidgetItem(str(phu_cap_onsite)))
            ui.tableWidget.setItem(row_index, 4, QTableWidgetItem(str(an_trua)))
            ui.tableWidget.setItem(row_index, 5, QTableWidgetItem(str(tong_thu_nhap)))
            ui.tableWidget.setItem(row_index, 6, QTableWidgetItem(str(BHXH)))
            ui.tableWidget.setItem(row_index, 7, QTableWidgetItem(str(thuc_nhan)))
            row_index += 1

    def clickMethod_efficacy_day_in_week():
        output_dayInWeek = []
        output_actualEfficacy = []
        try:
            data = api_client.get_data(f"{api_efficacy_day_in_week}")
            if isinstance(data, list):
                for item in data:
                    output_dayInWeek.append(item.get("dayInWeek"))
                    output_actualEfficacy.append(
                        round((item.get("actualEfficacy")) * 100)
                    )
            else:
                print("Data is not in the expected list format.")
        except Exception as e:
            print(f"An error occurred while fetching data for day: {e}")
        return output_actualEfficacy

    def clickMethod_age_efficacy():
        output_age = []
        output_actualEfficacy = []
        try:
            data = api_client.get_data(f"{api_age_efficacy}")
            if isinstance(data, list):
                for item in data:
                    output_age.append(item.get("age"))
                    output_actualEfficacy.append(item.get("actualEfficacy"))
            else:
                print("Data is not in the expected list format.")
        except Exception as e:
            print(f"An error occurred while fetching data for day: {e}")
        return output_age, output_actualEfficacy

    def clickMethod_sex_efficacy():
        try:
            sex_M = api_client.get_data(f"{api_sex_property}M")
            sex_F = api_client.get_data(f"{api_sex_property}F")
            # Nhân dữ liệu lên thao phần trăm đồng thời làm tròn
            output_sex_M = (
                round(sex_M.get("coworkerSameSexRatio") * 100),
                round(sex_M.get("actualEfficacy") * 100),
            )
            output_sex_F = (
                round(sex_F.get("coworkerSameSexRatio") * 100),
                round(sex_F.get("actualEfficacy") * 100),
            )
        except Exception as e:
            print(f"An error occurred while fetching data for day: {e}")

        return output_sex_M, output_sex_F
