import xlrd as xl
from xlrd import open_workbook as op
from xlutils.copy import copy
import readsheet_functions as rsf

file = 'data_sheet.xlsx'
sheet = 'Sheet3'

#------------------------------------------------

workbook = xl.open_workbook(file)
worksheet = workbook.sheet_by_name(sheet)
rowval=[]        
cell0=rsf.find_cell(file,sheet,"Products")

for r in range (cell0[0]+1,worksheet.nrows):
    v = worksheet.cell(r,cell0[1])
    rowval.append(v.value)
        
##print(rowval)

print(rsf.find_val('PAC 18','OP stock','data_sheet.xlsx','Sheet3'))
