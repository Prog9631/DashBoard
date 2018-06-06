import xlrd as xl
from xlrd import open_workbook as op
from xlutils.copy import copy
import Python_GUI as PG

workbook = xl.open_workbook('chemophilia.xlsx')
worksheet = workbook.sheet_by_name('Sheet3')
#------------------------------------------------

for r in range (0,worksheet.nrows):
    for c in range(0,worksheet.ncols):
        column = worksheet.col_values(c)
        v = worksheet.cell(r,c)
        if(v.value=="col1"):
            print(column)

rb = op('chemophilia.xlsx')
wb = copy(rb)

s = wb.get_sheet(2)

    ##s.write(0,0,PG.inp)
    ##wb.save('chemophilia.xlsx')
    ##print(worksheet.cell(0,0).value)
