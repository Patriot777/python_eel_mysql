import eel
from Setting import Setting
import db_setting
from db_connect import get_all_record, show_columns, update_db, get_setting_db, get_tables, connection_check, insert_db, del_row_db
import logicProgram
import export_modul

            ###########################
            # РОЗДІЛ ГОЛОВНА СТОРІНКА #
            ###########################

# Функція виводу бази на головній сторінці
@eel.expose
def click_db():
    show_data_table = get_all_record()
    show_columns_name = show_columns()
    eel.get_dbs(show_data_table, show_columns_name)

# Функція обробки експорту у ексель
@eel.expose
def export_from_exel():
    export_modul.export_xlsx(show_columns(), get_all_record())

            ######################
            # РОЗДІЛ РЕДАГУВАННЯ #
            ######################

# Відправляє стовбчики в js для розбивки комірок
@eel.expose
def send_value_db():
    value = get_all_record()
    eel.add_row(value)

# Функція передечі параметрів для вставки рядка
@eel.expose
def add_rows(set_value):
    value_str = ''
    for j in set_value:
        value_str = value_str + str(j) + ' '
    cut_values = value_str[:-1]
    arr_values = cut_values.split()
    finally_values = tuple(arr_values)
    insert_db(finally_values)

# Видалення рядка з таблиці
@eel.expose
def delete_row(id_row):
    del_row_db(id_row)

# Передача параметрів для виводу редагування комірок
@eel.expose
def edit_db_python():
    show_content_tables = get_all_record()
    show_columns_name2 = show_columns()
    eel.edit_db_in(show_content_tables, show_columns_name2)

# Оновлення таблиці якщо внесено нові дані
@eel.expose
def update_value_db(new_value):
    current_value_db = get_all_record()
    the_result_comparing_arrays = logicProgram.equals_arr(current_value_db, new_value)
    try:
        for two_dimensional_list in the_result_comparing_arrays:
            for one_dimensional_list in two_dimensional_list:
                column_name = str(one_dimensional_list[0])
                new_value_column = str(one_dimensional_list[1])
                row_id = int(one_dimensional_list[2])
                update_db(column_name, new_value_column, row_id)
    except:
        print("Не було внесено змін до таблиці")

    eel.send_ok()


            ######################
            # РОЗДІЛ НАЛАШТУВАНЬ #
            ######################

# Оновлення назви таблиці в JSON  
@eel.expose
def accepts_the_table_name(table_name):
    setting_db_for_json = db_setting.get_setting_mysql()
    db_setting.set_table_button(setting_db_for_json, table_name)

# Викликає функція з JS яка показує поточні налаштування
@eel.expose
def show_current_setting():
    current_setting = get_setting_db()
    eel.show_cerrent_settings_db(current_setting)

# Витягує налаштування таблиці та передає у JS для показу поточних налаштувань
@eel.expose
def get_sett():
    current_table = db_setting.get_setting_mysql()['table']
    status_code = connection_check()
    if status_code == 200:
        show_tables = get_tables()
        eel.show_current_settings(status_code , show_tables, current_table)
    else:
        eel.show_current_settings(status_code , '777')

# Викликається при першому запуску програми та введенням данних
@eel.expose
def setting_db(host, user, database, password):
    db = db_setting.Setting_db(host=host, 
                                user=user, 
                                database=database, 
                                password=password)
    db.set_settings_mysql()
    Setting().set_first_start()

width = Setting().get_width()
height = Setting().get_height()
first_start = Setting().get_first_start()

# Функція перевірки першого запуску програми
def start_p():

    if first_start == 1:
        eel.init('web')
        eel.start("greeting_page.html", size=(width, height))
    else:
        eel.init('web')
        eel.start("index.html", size=(width, height))

start_p()