from openpyxl import Workbook

wb = Workbook() # 默认有一个Sheet工作薄

# 创作一个新的工作薄
ws1 = wb.create_sheet('Mysheet')  # 在最后添加
ws2 = wb.create_sheet('Mysheeta', 0)  # 在第一个添加
#　修改工作薄的名称
ws2.title = "New Title"


# 保存
wb.save('balances.xlsx')
