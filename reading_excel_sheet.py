import xlrd as xl
from xlrd import open_workbook as op
from xlutils.copy import copy
import readsheet_functions as rsf
import parameter_dictionary_PAC as PAC

from fuzzywuzzy import fuzz
from fuzzywuzzy import process

file = 'Dr-June-18.xlsx'

#------------------------------------------------

workbook = xl.open_workbook(file)
names = workbook.sheet_names()
sheet = names[0]

worksheet = workbook.sheet_by_name(sheet)
rowval=[]        
cell0=rsf.find_cell(file,sheet,"Products")

for r in range(cell0[0]+1,worksheet.nrows):
    v = worksheet.cell(r,cell0[1])
    rowval.append(v.value)


        
##print(rowval)
##  (correctness_ratio = fuzz.ratio(, "xx")
##x
##cpar1 = rsf.find_cell(file,sheet,'UOM')
##print(cpar1)
##for i in range(len(PAC.Parameter1S)):
##print(rsf.find_cell(file,sheet,'PRODUCTION  (MT)'))
##print(rsf.find_cell(file,sheet,'S40000000066'))
##print(worksheet.cell(5,3).value)
print(rsf.find_val(file,sheet,'OPENING BALANCE(MT)','S40000000066','A1/62'))

##print(correctness_ratio)
