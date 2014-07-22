"""xlutils and xlrd practice file"""

from xlrd import open_workbook, empty_cell

book = open_workbook(r'\\kcow00\Jobs2\48253\Bridges\Design\Sub\Excel\FromFIGG_20140408_Piers4-8Loads\Scour\load_comparison\20131226_loads\Pier04L_Loads_12.xls')

sheet = book.sheet_by_index(1)

i = 1
load_names = []
cell_name = sheet.cell(13, 0)

while cell_name.value != '':
	load_names.append(cell_name.value)
	cell_name = sheet.cell(13 + i, 0)
	i = i + 1
	
for name in load_names:
	print load_names