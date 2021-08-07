import json
import os

class Setting_db():
    def __init__(self, host='', user='', database='', password='', table=''):
        self.host = host
        self.user = user
        self.database = database
        self.password = password
        self.table = table

    # Додавання налаштувань MYSQL
    def set_settings_mysql(self):
        dict_setting = {
            "host": self.host,
            "user": self.user,
            "password": self.password,
            "database": self.database,
            "table": self.table
            }
        full_path = os.path.join(os.getcwd() + '/setting_db/', 'setting_db_mysql.json')
        file_setting = open(full_path, 'w')
        json_setting = json.dumps(dict_setting, indent=4)
        file_setting.write(json_setting)
        file_setting.close()
        return True

full_path2 = os.path.join(os.getcwd() + '/setting_db/', 'setting_db_mysql.json')

# Встановлює нове значення назви таблиці
def set_table_button(settings, new_table):
    settings['table'] = new_table
    file_setting = open(full_path2, 'w')
    json_setting = json.dumps(settings, indent=4)
    file_setting.write(json_setting)
    file_setting.close()

# Витяг данних про базу MYSQL
def get_setting_mysql():
    get_file_json = open(full_path2, 'r')
    json_setting = json.load(get_file_json)
    get_file_json.close()
    return json_setting






