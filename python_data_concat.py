import pandas as pd

file = "file_name"

xl = pd.ExcelFile(file)

print(xl.sheet_names)

df = xl.parse('4')

df.head()

def years_bin(c):
    result = []
    for days in c:
        if days >= 0 and days <= 365:
            result.append('0 - 1')
        elif days >= 366 and days <= 730:
            result.append('1 - 2')
        elif days >= 731 and days <= 1095:
            result.append('2 - 3')
        elif days >= 1096 and days <= 1460:
            result.append('3 - 4')
        elif days >= 1461 and days <= 1825:
            result.append('4 - 5')
        elif days >= 1826 and days <= 2190:
            result.append('5 - 6')
        elif days >= 2191 and days <= 2555:
            result.append('6 - 7')
        elif days >= 2556 and days <= 2920:
            result.append('7 - 8')
        elif days >= 2921 and days <= 3285:
            result.append('8 - 9')
        elif days >= 3286 and days <= 3650:
            result.append('9 - 10')
        elif days >= 3651 and days <= 4014:
            result.append('10 - 11')
        else:
            result.append("NA")
    return result

res = years_bin(df[column_name])

res1 = pd.DataFrame({'Year_Bins':res})

final = pd.concat([df,res1], axis = 1)

type(final)

from pandas import ExcelWriter
writer = ExcelWriter("PythonExport.xls")
final.to_excel(writer,'Sheet1', index = False)
writer.save()

