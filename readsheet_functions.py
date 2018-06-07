import xlrd as xl
from xlrd import open_workbook as op
from xlutils.copy import copy
#------------------------------------------------
    
def find_cell(file_name,sheet_name,string):
    workbook = xl.open_workbook(file_name)
    worksheet = workbook.sheet_by_name(sheet_name)
    save1 = []
    temp =0
    for r in range (0,worksheet.nrows):
        for c in range(0,worksheet.ncols):
            column = worksheet.col_values(c)
            v = worksheet.cell(r,c)
            if(v.value==string):
                temp =1
                save1.append(r)
                save1.append(c)
    if temp == 0:
        print("string not found")
        return 0
    else:
        return save1

def find_val(product,parameter,file_name,sheet_name):
    cpro = find_cell(file_name,sheet_name,product)
    cpar = find_cell(file_name,sheet_name,parameter)
    workbook = xl.open_workbook(file_name)
    worksheet = workbook.sheet_by_name(sheet_name)
    a = []
    a.append(cpro[0])
    a.append(cpar[1])
    aval = worksheet.cell(a[0],a[1]).value
    return aval
