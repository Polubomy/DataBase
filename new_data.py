import sqlite3
import random

conn = sqlite3.connect('company.db')
cursor = conn.cursor()

# Функция для генерации случайной даты
def generate_random_date(start_year, end_year):
    """Генерирует случайную дату в формате YYYY-MM-DD."""
    year = random.randint(start_year, end_year)
    month = random.randint(1, 12)
    day = random.randint(1, 28)  # Максимальное число дней в феврале
    return f"{year}-{month:02}-{day:02}"

# Изменяем данные в таблице "Работа"
cursor.execute("SELECT Шифр_Работы FROM Работа")
work_ids = [row[0] for row in cursor.fetchall()]

for work_id in work_ids:
    # Генерируем случайную дату завершения
    completion_date = generate_random_date(2009, 2024)
    cursor.execute("UPDATE Работа SET Дата_Завершения_работы = ? WHERE Шифр_Работы = ?", (completion_date, work_id))

# Изменяем данные в таблице "Поручения"
cursor.execute("SELECT Номер_Поручения FROM Поручения")
assignment_ids = [row[0] for row in cursor.fetchall()]

for assignment_id in assignment_ids:
    # Генерируем случайные даты выдачи, планового завершения и реального завершения
    issue_date = generate_random_date(2009, 2024)
    planned_completion_date = generate_random_date(2009, 2024)
    actual_completion_date = generate_random_date(2009, 2024)

    # Убеждаемся, что реальное завершение не раньше планового
    while actual_completion_date < planned_completion_date:
        actual_completion_date = generate_random_date(2009, 2024)

    cursor.execute("UPDATE Поручения SET Дата_Выдачи = ?, Плановая_Дата_Окончания = ?, Реальная_Дата_Окончания = ? WHERE Номер_Поручения = ?", (issue_date, planned_completion_date, actual_completion_date, assignment_id))




conn.commit()
conn.close()