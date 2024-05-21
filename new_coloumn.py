import sqlite3

conn = sqlite3.connect('company.db')
cursor = conn.cursor()

# Добавление столбца 'код_сотрудника' в таблицу 'Поручения'
cursor.execute('''
ALTER TABLE Поручения
ADD COLUMN код_сотрудника INTEGER;
''')

# Заполнение столбца 'код_сотрудника' табельными номерами из 'Сотрудники'
cursor.execute("SELECT Номер_Поручения FROM Поручения")
assignment_ids = [row[0] for row in cursor.fetchall()]
for i, assignment_id in enumerate(assignment_ids):
    employee_id = 101 + (i % 6)  # Присваиваем табельный номер, циклически перебирая сотрудников
    cursor.execute("UPDATE Поручения SET код_сотрудника = ? WHERE Номер_Поручения = ?", (employee_id, assignment_id))

conn.commit()
conn.close()