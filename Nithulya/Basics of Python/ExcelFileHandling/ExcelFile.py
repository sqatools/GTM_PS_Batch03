import openpyxl

#1.
# def readExcelFile(filename,row,col):
#     wb=openpyxl.load_workbook(filename)
#     sheet=wb.active
#     cell=sheet.cell(row=row,column=col)
#     print(cell.value)
#
# readExcelFile("SqlData.xlsx",row=2,col=2)         # ANJU THOMAS
# readExcelFile("SqlData.xlsx",row=2,col=3)         # 17

#2.
# def read_excel_file_with_sheetname(filename, sheet_name, cell_name):
#     wb=openpyxl.load_workbook(filename)
#     sheet=wb[sheet_name]
#     cell=sheet[cell_name]
#     print(cell.value)
#
# read_excel_file_with_sheetname("SqlData.xlsx", sheet_name="Sheet1", cell_name="B1")      # NAME
# read_excel_file_with_sheetname("SqlData.xlsx", sheet_name="Sheet1", cell_name="B2")      # ANJU THOMAS


#3.
# def read_excel_file_with_sheetname(filename, sheet_name, cell_name):
#     wb=openpyxl.load_workbook(filename)
#     sheet=wb[sheet_name]
#     cell=sheet[cell_name]
#     print(cell.value)
#
# for i in range(1, 11):                                           # We will get all the data from that particular cell ({B{i}).
#     read_excel_file_with_sheetname("SqlData.xlsx", sheet_name="Sheet1", cell_name=f"B{i}")

#4.
def read_excel_file_with_sheetname(filename, sheet_name, cell_name):
    wb=openpyxl.load_workbook(filename)
    sheet=wb[sheet_name]
    cell=sheet[cell_name]
    print(cell.value)

for i in range(1, 11):         # We will get whole data that particular cell(B{i}) and matching value of cell(C{i})
    read_excel_file_with_sheetname("SqlData.xlsx", sheet_name="Sheet1", cell_name=f"B{i}")
    read_excel_file_with_sheetname("SqlData.xlsx", sheet_name="Sheet1", cell_name=f"C{i}")