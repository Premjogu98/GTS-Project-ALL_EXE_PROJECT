from openpyxl import Workbook

book = Workbook()
sheet = book.active

rows = (
    (88, 46,42554),
    (89, 38, 12)
)

for row in rows:
    sheet.append(row)

book.save('D:\\PycharmProjects\\All Python Examples\\Company Details.xlsx')
