import db_connect
# ФУНКЦІЯ ПОРІВНЯННЯ ТА ГЕНЕРАЦІЇ ДВОМІРНОГО МАСИВУ
# ПОВЕРТАЄ ДВОМІРНИЙ МАСИВ ЯКЩО В БАЗІ БУЛИ ЯКІСТЬ ЗМІНИ.    
def equals_arr(old_arr, new_arr):
    # Масив з назвами колонок
    arr_columns = db_connect.show_columns()
    # Ітерація циклу по кількості рядків у БД
    iter_len_arr = 0
    # Ітерація циклу по кількості колонок у БД
    iter_len_arr_col = 0
    # Довжина масиву - кількість рядків у БД
    len_arr = len(old_arr)
    # Довжина масиву - кількість колоонок у БД
    len_arr_col = len(old_arr[0])
    # Створюється пустий масив який буде віддаватися функцією
    result_arr = []

    # Цикл проходження по рядках
    while iter_len_arr < len_arr:

        new_loop_string = new_arr[iter_len_arr]
        old_loop_string = old_arr[iter_len_arr]
        # Допоміжний масив
        auxiliary_array = []

        # Цикл проходження по колонках в рядку
        while iter_len_arr_col < len_arr_col:
            
            # Нічого не відбувається якщо ячейки однакові
            if str(old_loop_string[iter_len_arr_col]) != str(new_loop_string[iter_len_arr_col]):
                # Назва колонки
                сolumn_name = arr_columns[iter_len_arr_col][0]
                # До масиву приєднується назва колонки
                auxiliary_array.append(сolumn_name)
                # До масиву приєднується нове значення ячейки
                auxiliary_array.append(new_arr[iter_len_arr][iter_len_arr_col])
                # До масиву приєднується ID рядка
                auxiliary_array.append(new_arr[iter_len_arr][0])
            else:
                pass
            iter_len_arr_col += 1

        # Перевірка допоміжного масиву на пустоту
        if not auxiliary_array:
            pass      
        # Виконується запис в основний масив
        else:
            aa = ArrayBreakdown(auxiliary_array)
            result_arr.append(aa)
            auxiliary_array = []
        
        iter_len_arr_col = 0
        iter_len_arr += 1

    if not result_arr:
        return "База пуста"
    else:
        return result_arr


# Метод розбивки масиву
def ArrayBreakdown(arr):
    old_arr = arr
    result_arr = []
    if len(old_arr) > 3:
        gg_arr = []
        j = 0
        for one_arr in old_arr:
            if j < 3:
                gg_arr.append(one_arr)
                j += 1
            else:
                pass
            if j == 3:
                result_arr.append(gg_arr)
                gg_arr = []
                j = 0
        return result_arr
    else:
        result_arr.append(old_arr)
        return result_arr