import openpyxl

wb = openpyxl.load_workbook('example.xlsx')
sheet = wb.active
sheet['A1']=3
sheet['A1']=7

wb.save('example_copy.xlsx')


