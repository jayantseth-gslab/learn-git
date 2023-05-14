from openpyxl import Workbook


# Method to write into excel
def write_data(ip_result):
    try:
        wb = Workbook()
        sheet = wb.active
        # Setting headers
        sheet['A1'].value = "IP"
        sheet["B1"].value = "Result"
        # Enumerating for easy use
        ip_result_obj = enumerate(ip_result, start=2)
        for index, ip in ip_result_obj:
            result = ip_result[ip]
            sheet[f'A{index}'].value = ip
            sheet[f'B{index}'].value = result
        wb.save("result.xlsx")
        return 0
    except BaseException as e:
        return e
