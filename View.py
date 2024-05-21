import sqlite3

conn = sqlite3.connect('company.db')
cursor = conn.cursor()

# Вывод всех таблиц в базе данных
cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
tables = cursor.fetchall()
print("Таблицы в базе данных:")
for table in tables:
    print(table[0])


cursor.execute("SELECT * FROM Работа")
rows = cursor.fetchall()
print("\nДанные из таблицы 'Работа':")
for row in rows:
    print(row)

cursor.execute("SELECT * FROM Сотрудники")
rows = cursor.fetchall()
print("\nДанные из таблицы 'Сотрудники':")
for row in rows:
    print(row)

cursor.execute("SELECT * FROM Поручения")
rows = cursor.fetchall()
print("\nДанные из таблицы 'Поручения':")
for row in rows:
    print(row)

conn.close()