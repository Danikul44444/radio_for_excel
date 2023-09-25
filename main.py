import openpyxl
from play_radio_fm import play_radio
import os.path
user_xlsx = str(input(">> "))
if os.path.exists(user_xlsx) == True:
	book = openpyxl.open(user_xlsx, read_only = True)
else:
	book = openpyxl.open('radio_listes/Record.xlsx', read_only = True)
sheet = book.active

maxium = sheet.max_row

for x in range(1, maxium + 1):
	print(x, sheet[f'A{x}'].value)
user_radio = int(input(">> "))

if user_radio >= 1 and user_radio <= maxium + 1:
	play_radio(sheet[f'B{user_radio}'].value)