import xlrd as xl
from xlrd import open_workbook as op
from xlutils.copy import copy
#------------------------------------------------
    
def find_cell(file_name,sheet_name,string,i=0,j=0):
    workbook = xl.open_workbook(file_name)
    worksheet = workbook.sheet_by_name(sheet_name)
    save1 = []
    temp =0
    for r in range (i,worksheet.nrows):
        for c in range(j,worksheet.ncols):
            column = worksheet.col_values(c)
            v = worksheet.cell(r,c)
##            print(v)
            if(v.value==string):
                temp =1
##                print(v)
                save1.append(r)
                save1.append(c)
    if temp == 0:
        print("string not found")
        return 0
    else:
        return save1

def find_val(file_name,sheet_name,product,parameter1,parameter2='NULL'):
    cpro = find_cell(file_name,sheet_name,product)
    if (parameter1!='void'):
        cpar1 = find_cell(file_name,sheet_name,parameter1)
    else:
        cpar1 = [0,0]

    cpar2 = find_cell(file_name,sheet_name,parameter2,cpar1[0],cpar1[1])
    
    workbook = xl.open_workbook(file_name)
    worksheet = workbook.sheet_by_name(sheet_name)
    a = []
    a.append(cpro[0])
    a.append(cpar2[1])
    aval = worksheet.cell(a[0],a[1]).value
    return aval
