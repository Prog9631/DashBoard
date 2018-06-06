import xlrd as xl
from xlrd import open_workbook as op
from xlutils.copy import copy
import readsheet_functions as rsf

file = 'data_sheet.xlsx'
sheet = 'Sheet3'
#------------------------------------------------

##if save1[0]>save2[0] :
##    cord.append(save1[0])
##    cord.append(save2[1])
##else:
##    cord.append(save2[0])
##    cord.append(save1[1])
workbook = xl.open_workbook(file)
worksheet = workbook.sheet_by_name(sheet)
cell=[]        
cell0=rsf.find_cell(file,sheet,"Products")

for r in range (cell0[0]+1,worksheet.nrows):
    v = worksheet.cell(r,cell0[1])
    cell.append(v.value)

print(cell)
##desired_cell[1]=rsf.find_val("PAC 18","OP stock",file,sheet)
##print("value:",desired_cell[2])
