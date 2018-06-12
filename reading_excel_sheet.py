import xlrd as xl
from xlrd import open_workbook as op
from xlutils.copy import copy
import readsheet_functions as rsf
import parameter_dictionary_PAC as PAC

from fuzzywuzzy import fuzz
from fuzzywuzzy import process

file = 'data_sheet.xlsx'
sheet = 'Sheet3'

#------------------------------------------------

workbook = xl.open_workbook(file)
worksheet = workbook.sheet_by_name(sheet)
rowval=[]        
cell0=rsf.find_cell(file,sheet,"Products")

for r in range(cell0[0]+1,worksheet.nrows):
    v = worksheet.cell(r,cell0[1])
    rowval.append(v.value)
        
##print(rowval)
##  (correctness_ratio = fuzz.ratio(, "xx")
##
##cpar1 = rsf.find_cell(file,sheet,'UOM')
##print(cpar1)
for i in range(len(PAC.Parameter1S)):
    print(rsf.find_val('data_sheet.xlsx','Sheet3','PAC 18',PAC.Parameter1S[i]))

##print(correctness_ratio)
