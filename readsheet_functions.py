import xlrd as xl
from xlrd import open_workbook as op
from xlutils.copy import copy

from fuzzywuzzy import fuzz
from fuzzywuzzy import process

#------------------------------------------------
    
def find_cell(file_name,sheet_name,string,i=0,j=0):
    workbook = xl.open_workbook(file_name)
    worksheet = workbook.sheet_by_name(sheet_name)
    save1 = []
    temp =0
    string = string.lower()
## column = worksheet.col_values(c)
    cr = 0
    for r in range (i,worksheet.nrows):
        for c in range(j,worksheet.ncols):
            v = worksheet.cell(r,c)
            if(isinstance(v.value,str)):
                param = v.value
                param = param.lower()
                fr = fuzz.ratio(string,param)
                if (fr>50 and fr>cr):
                    cr = fr
                    temp =1
                    a = r
                    b = c
    save1.append(a)
    save1.append(b)

    if temp == 0:
        print("string not found")
## return 0
    else:
        return save1

def find_val(file_name,sheet_name,product,parameter1,parameter2='NULL'):
  
    cpro = find_cell(file_name,sheet_name,product)
    cpar1 = find_cell(file_name,sheet_name,parameter1)
      
    workbook = xl.open_workbook(file_name)
    worksheet = workbook.sheet_by_name(sheet_name)

    a = []
    if (parameter2!='NULL'):
        cpar2 = find_cell(file_name,sheet_name,parameter2,cpar1[0],cpar1[1])
        a.append(max(cpro[0],cpar2[0]))
        a.append(max(cpro[1],cpar2[1]))
    else:
        a.append(max(cpro[0],cpar1[0]))
        a.append(max(cpro[1],cpar1[1]))
    aval = worksheet.cell(a[0],a[1]).value
    return aval

def get_col(file_name,sheet_name,string,i=0,j=0):
    workbook = xl.open_workbook(file_name)
    worksheet = workbook.sheet_by_name(sheet_name)
    cpro = find_cell(file_name,sheet_name,string)
    column = worksheet.col_values(cpro[1])
    print(column)
    lc = len(column)
    while i<lc:
        if (column[i]==None or isinstance(column[i],str)):
            del column[i]
            lc = len(column)
            i = i-1
        i=i+1
    return column
    
