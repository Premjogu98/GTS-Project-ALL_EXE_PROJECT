from openpyxl import Workbook


def Write_xls_File():
    File_Location = open("D:\\PycharmProjects\\All Python Examples\\Website List.txt", "r")  # Read The Text Form Website List Text File
    Website_List = File_Location.read()
    Website_List = [int(e) if e.isdigit() else e for e in Website_List.split('\n')]
    # print('You Select This website:', Website_List)
    book = Workbook()
    sheet = book.active
    column = 3
    for website in Website_List:
        sheet['A1'] = 'Org Name'
        sheet['A'+str(column)+''] = str(website)  # sheet[A1] or sheet[B1] this is an column names
        column += 1
    book.save("D:\\PycharmProjects\\All Python Examples\\Company Details.xlsx")  # save the file after write data


Write_xls_File()

