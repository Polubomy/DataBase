import sqlite3

# Подключение к базе данных
conn = sqlite3.connect('company.db')  # Замените 'your_database.db' на имя вашей базы данных
cursor = conn.cursor()

# Добавление столбца "Прогресс"
cursor.execute('''ALTER TABLE Поручения ADD COLUMN Прогресс INTEGER''')

# Заполнение столбца "Прогресс"

cursor.execute("UPDATE Поручения SET Прогресс = ? WHERE Номер_Поручения = ?", (42, 1))
cursor.execute("UPDATE Поручения SET Прогресс = ? WHERE Номер_Поручения = ?", (100, 2))
cursor.execute("UPDATE Поручения SET Прогресс = ? WHERE Номер_Поручения = ?", (39, 3))
cursor.execute("UPDATE Поручения SET Прогресс = ? WHERE Номер_Поручения = ?", (21, 4))
cursor.execute("UPDATE Поручения SET Прогресс = ? WHERE Номер_Поручения = ?", (100, 5))
cursor.execute("UPDATE Поручения SET Прогресс = ? WHERE Номер_Поручения = ?", (100, 6))
cursor.execute("UPDATE Поручения SET Прогресс = ? WHERE Номер_Поручения = ?", (100, 7))
cursor.execute("UPDATE Поручения SET Прогресс = ? WHERE Номер_Поручения = ?", (100, 8))
cursor.execute("UPDATE Поручения SET Прогресс = ? WHERE Номер_Поручения = ?", (100, 9))
cursor.execute("UPDATE Поручения SET Прогресс = ? WHERE Номер_Поручения = ?", (100, 10))
cursor.execute("UPDATE Поручения SET Прогресс = ? WHERE Номер_Поручения = ?", (100, 11))
cursor.execute("UPDATE Поручения SET Прогресс = ? WHERE Номер_Поручения = ?", (100, 12))
cursor.execute("UPDATE Поручения SET Прогресс = ? WHERE Номер_Поручения = ?", (100, 13))
cursor.execute("UPDATE Поручения SET Прогресс = ? WHERE Номер_Поручения = ?", (100, 14))
cursor.execute("UPDATE Поручения SET Прогресс = ? WHERE Номер_Поручения = ?", (100, 15))

conn.commit()
conn.close()