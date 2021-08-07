import xlsxwriter
import os
from db_setting import get_setting_mysql

def export_xlsx(title, datas):
    name = get_setting_mysql()
    full_name = name['table'] + '.xlsx'
    print(full_name)
    full_path = os.path.join(os.getcwd() + '/export/', full_name)
    workbook = xlsxwriter.Workbook(full_path)
    worksheet = workbook.add_worksheet()

    bold = workbook.add_format({'bold': True})

    new_arr_title = []
    iter_append_title = 0
    while iter_append_title < len(title):
        new_arr_title.append(title[iter_append_title][0])
        iter_append_title += 1

    iter_write_title = 0
    while iter_write_title < len(new_arr_title):
        worksheet.write(0, iter_write_title, new_arr_title[iter_write_title], bold)
        worksheet.set_column(0, 2, width=25)
        iter_write_title += 1

    iter_row = 0
    iter_write_row = 1
    while iter_row < len(datas):
        iter_write_col = 0
        while iter_write_col < len(datas[0]):
            worksheet.write(iter_write_row, iter_write_col, datas[iter_row][iter_write_col])
            iter_write_col += 1
        iter_write_row += 1
        iter_row += 1
    workbook.close()

