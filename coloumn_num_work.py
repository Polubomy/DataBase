import sqlite3

conn = sqlite3.connect('company.db')
cursor = conn.cursor()

cursor.execute('''ALTER TABLE Поручения ADD COLUMN Номер_Работы INTEGER''')

cursor.execute("UPDATE Поручения SET Номер_Работы = ? WHERE Номер_Поручения = ?", (1, 1))
cursor.execute("UPDATE Поручения SET Номер_Работы = ? WHERE Номер_Поручения = ?", (2, 2))
cursor.execute("UPDATE Поручения SET Номер_Работы = ? WHERE Номер_Поручения = ?", (3, 3))
cursor.execute("UPDATE Поручения SET Номер_Работы = ? WHERE Номер_Поручения = ?", (4, 4))
cursor.execute("UPDATE Поручения SET Номер_Работы = ? WHERE Номер_Поручения = ?", (5, 5))
cursor.execute("UPDATE Поручения SET Номер_Работы = ? WHERE Номер_Поручения = ?", (6, 6))
cursor.execute("UPDATE Поручения SET Номер_Работы = ? WHERE Номер_Поручения = ?", (7, 7))
cursor.execute("UPDATE Поручения SET Номер_Работы = ? WHERE Номер_Поручения = ?", (8, 8))
cursor.execute("UPDATE Поручения SET Номер_Работы = ? WHERE Номер_Поручения = ?", (9, 9))
cursor.execute("UPDATE Поручения SET Номер_Работы = ? WHERE Номер_Поручения = ?", (10, 10))
cursor.execute("UPDATE Поручения SET Номер_Работы = ? WHERE Номер_Поручения = ?", (11, 11))
cursor.execute("UPDATE Поручения SET Номер_Работы = ? WHERE Номер_Поручения = ?", (12, 12))
cursor.execute("UPDATE Поручения SET Номер_Работы = ? WHERE Номер_Поручения = ?", (4, 13))
cursor.execute("UPDATE Поручения SET Номер_Работы = ? WHERE Номер_Поручения = ?", (4, 14))
cursor.execute("UPDATE Поручения SET Номер_Работы = ? WHERE Номер_Поручения = ?", (4, 15))

conn.commit()
conn.close()