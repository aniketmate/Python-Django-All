import openpyxl
from openpyxl import workbook



FILE_PATH = r"E:\aniket mate\Employee_Excel\Emp_data.xlsx"
def get_workbook_sheet():
    workbook = openpyxl.load_workbook(FILE_PATH)
    # sheet = workbook.active
    sheet = workbook["Employee Data adresses"]
    # sheet = workbook.create_sheet("Employee Data adresses")
    # del workbook["Sheet1"]
    workbook.save(FILE_PATH)
    return workbook, sheet

# print(get_workbook_sheet())
# wb , sheet = get_workbook_sheet()
# print(wb)
# print(sheet)

if __name__ ==  '__main__':
    get_workbook_sheet()