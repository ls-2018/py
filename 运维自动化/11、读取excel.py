from openpyxl import load_workbook

wb = load_workbook('balances.xlsx', read_only=True, data_only=True)
# 控制带有公式的单元格是否具有公式(默认值)   Excel上次读取工作表时存储的值

print(wb.sheetnames)  # ['New Title', 'Sheet', 'Mysheet']
wb1 = wb['New Title']

print(wb1['B4'].value)
print(wb1.cell(row=4, column=2).value)

print(wb1.max_row)  # 最大行数
print(wb1.max_column)  # 最大列数

# ######################## 获取行和列 ####################################
# 因为按行，所以返回A1, B1, C1这样的顺序
for row in wb1.rows:
    for cell in row:
        print(cell.value)

# A1, A2, A3这样的顺序
# for column in wb1.columns:    # read_only=False
#     for cell in column:
#         print(cell.value)

for row_cell in wb1['A1':'B3']:
    for cell in row_cell:
        print(cell.value)

# ######################## 设置字体 ####################################
from openpyxl.styles import Font, colors

bold_itatic_24_font = Font(name='等线', size=24, italic=True, color=colors.RED, bold=True)
wb1['A1'].font = bold_itatic_24_font

# ######################## 对齐方式 ####################################
from openpyxl.styles import Alignment

wb1['B1'].alignment = Alignment(horizontal='center', vertical='center')  # right,left

# ######################## 设置行高和列宽 ####################################
