import sqlite3

# Создание соединения с базой данных
conn = sqlite3.connect('company.db')
cursor = conn.cursor()

# Создание таблицы "Работа"
cursor.execute('''
CREATE TABLE Работа (
  Шифр_Работы INTEGER PRIMARY KEY,
  Название_Работы TEXT,
  Трудоёмкость REAL,
  Дата_Завершения_работы DATE
)
''')

# Создание таблицы "Сотрудники"
cursor.execute('''
CREATE TABLE Сотрудники (
  Табельный_номер INTEGER PRIMARY KEY,
  ФИО TEXT,
  Должность TEXT
)
''')

# Создание таблицы "Поручения"
cursor.execute('''
CREATE TABLE Поручения (
  Номер_Поручения INTEGER PRIMARY KEY,
  Дата_Выдачи DATE,
  Трудоёмкость REAL,
  Плановая_Дата_Окончания DATE,
  Реальная_Дата_Окончания DATE
)
''')



conn.commit()
conn.close()