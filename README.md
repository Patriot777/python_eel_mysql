# Програма для перегляду, редагування та експорту в Exel бази даних

## Написана на мові Python, бібліотека eel.
### УВАГА програма не призначена для професійного використання адміністраторами баз даних.
______
![img](https://github.com/Patriot777/python_eel_mysql/blob/main/header_md/header.png)

### Встановлення
1. Для роботи у програмі у вас повинен бути встановлений браузер Chrome, [завантажити можна тут](https://www.google.com/chrome/?brand=BNSD&gclid=CjwKCAjw3riIBhAwEiwAzD3TiUO7b8yjsiC1Py8bazCA3BG0fLeArFPW1SwbF5u3f9MRBTw7ggFyeBoCyhAQAvD_BwE&gclsrc=aw.ds)
2. Встановлений Python 3.6+ версії, [завантажити](https://www.python.org/downloads/)
3. Встановлений модуль eel ```pip install eel```
4. Встановлений модуль xlsxwriter ```pip install XlsxWriter```
5. Встановлений модуль mysql-connector ```pip install mysql-connector-python```
6. Завантажити файли з репозиторію.
7. Запустити файл main.py

### Версії
**1.0.0**<br>
- **Головна сторінка:** перегляд таблиці з бази. Експорт у xlsx формат, файл зберігається у директорії **export** з назвою таблиці.
- **Редагування:** можна редагувати таблицю, змінювати дані та додавати/видаляти рядки.
- **Налаштування:** зліва можна вводити налаштування підключення до бази даних. З правої сторони показано поточні налаштування підключення до бази. В нижній частині виводиться підключення та вибір таблиць які доступні у базі.
