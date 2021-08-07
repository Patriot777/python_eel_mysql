import mysql.connector
import db_setting

class DataBases():
  # Отримую масив з налаштуваннями бази данних, з файлу JSON
  data_user_db = db_setting.get_setting_mysql()
  host = data_user_db['host']
  user = data_user_db['user']
  password = data_user_db['password']
  database = data_user_db['database']
  table = data_user_db['table']

  @staticmethod
  def connection():
    try:
      mydbs = mysql.connector.connect(
        host = DataBases.host,
        user = DataBases.user,
        password = DataBases.password,
        database = DataBases.database
      )
      return mydbs
    except:
      return 404


def get_setting_db():
  cla = db_setting.get_setting_mysql()
  result = []
  result.append(cla['host'])
  result.append(cla['user'])
  result.append(cla['database'])
  result.append(cla['password'])
  result.append(cla['table'])
  return result

def connection_check():
  status = DataBases.connection()
  if status == 404:
    return 404
  else:
    return 200

def get_tables():
  mydb = DataBases.connection()
  mycursor = mydb.cursor()
  mycursor.execute("SHOW TABLES")
  result = mycursor.fetchall()
  mydb.close()
  return result

# Повертає всі записи з бази данних  
def get_all_record(): 
  mydb = DataBases.connection()
  table = get_setting_db()[4]
  mycursor = mydb.cursor()
  mycursor.execute("SELECT * FROM {0}".format(table))
  myresult = mycursor.fetchall()
  mydb.close()
  return myresult

# Повертає масив з назвами колонок бази данних
def show_columns():
  mydb = DataBases.connection()
  table = get_setting_db()[4]
  mycursor = mydb.cursor()
  mycursor.execute("SHOW COLUMNS FROM {0}".format(table))
  result = mycursor.fetchall()
  mydb.close()
  return result

# Повертає ім'я id (Тобто деякі програмісти можуть не називати просто id а наприклад user_id)
def get_id_for_table(list_table):
  i = 0
  while i < len(list_table): 
    j = 0
    while j < len(list_table[i]):
      if list_table[i][j] == 'auto_increment':
        return list_table[i][0]
        
      j += 1
    i += 1


# Оновлення бази данних
def update_db(column_name, column_value, row_id):
  id_row = get_id_for_table(show_columns())
  table = get_setting_db()[4]
  mydb = DataBases.connection()
  mycursor = mydb.cursor()
  mycursor.execute("UPDATE {0} SET {1} = '{2}' WHERE {3} = {4}".format(table, column_name, column_value, id_row, row_id))
  mydb.commit()
  mydb.close()


# Форматує масив для запису в рядок таблиці бази даних
def return_format_cols_name(arr_cols):
  arr_name = []
  i = 0
  while i < len(arr_cols):
    arr_name.append(arr_cols[i][0])  
    i += 1

  str_cols_name = ''
  for one_col in arr_name:
    str_cols_name = str_cols_name + one_col + ', '
  new_col = str_cols_name[:-2]  
  return new_col

# Вставка рядка у таблицю
def insert_db(*args):
  values_row = tuple(args[0])
  mydb = DataBases.connection()
  cursor = mydb.cursor()
  table = get_setting_db()[4]
  col_name = return_format_cols_name(show_columns())
  
  sql = "INSERT INTO {0} ({1}) VALUES {2}".format(table, col_name, values_row)
  print(sql)
  cursor.execute(sql)

  mydb.commit()

# Видалення рядка
def del_row_db(row_id):
  mydb = DataBases.connection()
  cursor = mydb.cursor()
  table = get_setting_db()[4]
  id_row = get_id_for_table(show_columns())
  sql = "DELETE FROM {0} WHERE {1} = {2}".format(table, id_row, row_id)
  cursor.execute(sql)
  mydb.commit()


