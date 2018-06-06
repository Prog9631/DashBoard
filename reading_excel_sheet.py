import xlrd as xl
from xlrd import open_workbook as op
from xlutils.copy import copy
#import Python_GUI as PG

workbook = xl.open_workbook('data_sheet.xlsx')
worksheet = workbook.sheet_by_name('Sheet3')
#------------------------------------------------
save1 = []
save2 = []
cord = []
#hello
for r in range (0,worksheet.nrows):
    for c in range(0,worksheet.ncols):
        column = worksheet.col_values(c)
        v = worksheet.cell(r,c)
      #  print(v.value)
        if(v.value=="PAC 18"):
            save1.append(r)
            save1.append(c)
        if(v.value=="OP stock"):
            save2.append(r)
            save2.append(c)

if save1[0]>save2[0] :
    cord.append(save1[0])
else:
    cord.append(save2[0])
        
if save1[1]>save2[1] :
    cord.append(save1[1])
else:
    cord.append(save2[1])
        
#print(save1)
desired_cell=worksheet.cell(cord[0],cord[1])
print("value:",desired_cell.value)
##rb = op('chemophilia.xlsx')
##wb = copy(rb)
##
##s = wb.get_sheet(2)
##
##s.write(0,0,PG.inp)
##wb.save('chemophilia.xlsx')
##print(worksheet.cell(0,0).value)
