import sqlite3
import tkinter as tk
from tkinter import ttk

conn = sqlite3.connect('company.db')
cursor = conn.cursor()

def show_table(table_name):
    """Выводит данные из выбранной таблицы в новом окне в виде таблицы."""
    new_window = tk.Toplevel(window)
    new_window.title(f"Таблица: {table_name}")
    new_window.geometry("1300x400")

    cursor.execute(f"SELECT * FROM {table_name}")
    rows = cursor.fetchall()

    tree = ttk.Treeview(new_window, columns=[col[0] for col in cursor.description], show="headings")
    for col in cursor.description:
        tree.heading(col[0], text=col[0])
    tree.pack(expand=True, fill="both")

    for row in rows:
        tree.insert("", tk.END, values=row)

def выборка_1():
    cursor.execute('''
          SELECT 
              p.Номер_Поручения,
              p.Дата_Выдачи,
              p.Плановая_Дата_Окончания,
              p.Реальная_Дата_Окончания,
              r.Название_Работы
          FROM 
              Поручения p
          JOIN 
              Работа r ON p.Номер_Поручения = r.Шифр_Работы
          WHERE 
              CAST(SUBSTR(p.Дата_Выдачи, 1, 4) AS INTEGER) = 2009
              AND CAST(SUBSTR(p.Плановая_Дата_Окончания, 1, 4) AS INTEGER) = 2009
              AND CAST(SUBSTR(p.Реальная_Дата_Окончания, 1, 4) AS INTEGER) = 2009
              AND p.Плановая_Дата_Окончания < p.Реальная_Дата_Окончания
      ''')
    rows = cursor.fetchall()

    new_window = tk.Toplevel(window)
    new_window.title("Hаботы в 2009 г., по которым плановые сроки выполнения превышают заданную дату завершения")
    new_window.geometry("1200x100")

    tree = ttk.Treeview(new_window, columns=[col[0] for col in cursor.description], show="headings")
    for col in cursor.description:
        tree.heading(col[0], text=col[0])
    tree.pack(expand=True, fill="both")

    for row in rows:
        tree.insert("", tk.END, values=row)

def выборка_2():
    """Выполняет выборку данных по заданному критерию."""
    cursor.execute('''
        SELECT 
            p.Номер_Поручения,
            p.Дата_Выдачи,
            p.Плановая_Дата_Окончания,
            p.Реальная_Дата_Окончания,
            r.Название_Работы
        FROM 
            Поручения p
        JOIN 
            Работа r ON p.Номер_Поручения = r.Шифр_Работы
        WHERE 
            CAST(SUBSTR(p.Дата_Выдачи, 1, 4) AS INTEGER) = 2011
            AND CAST(SUBSTR(p.Дата_Выдачи, 6, 2) AS INTEGER) BETWEEN 3 AND 5
            AND p.код_сотрудника = 102
    ''')
    rows = cursor.fetchall()

    # Вывод результатов выборки в новом окне
    new_window = tk.Toplevel(window)
    new_window.title("Общее количество работ, находившихся на выполнении у некоторого сотрудника  весной 2010 г.")
    new_window.geometry("1200x100")

    tree = ttk.Treeview(new_window, columns=[col[0] for col in cursor.description], show="headings")
    for col in cursor.description:
        tree.heading(col[0], text=col[0])
    tree.pack(expand=True, fill="both")

    for row in rows:
        tree.insert("", tk.END, values=row)

    count_window = tk.Toplevel(window)
    count_window.title("Количество Работ")
    count_window.geometry("200x50")
    label = tk.Label(count_window, text=f"Количество работ: {len(rows)}")
    label.pack()

def выборка_3():
    """Выполняет выборку данных по заданному критерию."""
    cursor.execute('''
      SELECT 
          p.Номер_Поручения,
          p.Дата_Выдачи,
          p.Плановая_Дата_Окончания,
          p.Реальная_Дата_Окончания,
          r.Название_Работы,
          p.Прогресс
      FROM 
          Поручения p
      JOIN 
          Работа r ON p.Номер_Поручения = r.Шифр_Работы
      WHERE 
          p.Прогресс <= 50
  ''')
    rows = cursor.fetchall()

    new_window = tk.Toplevel(window)
    new_window.title("Задачи, которые к дате завершения были выполнены не более, чем на 50%")
    new_window.geometry("1200x300")

    tree = ttk.Treeview(new_window, columns=[col[0] for col in cursor.description], show="headings")
    for col in cursor.description:
        tree.heading(col[0], text=col[0])
    tree.pack(expand=True, fill="both")

    for row in rows:
        tree.insert("", tk.END, values=row)

def выборка_4():
    """Выполняет выборку данных по заданному критерию."""
    cursor.execute('''
        SELECT DISTINCT s.Должность, s.ФИО, r.Название_Работы
        FROM Сотрудники s
        JOIN Поручения p ON s.Табельный_номер = p.код_сотрудника
        JOIN Работа r ON p.Номер_Работы = r.Шифр_Работы
        WHERE r.Название_Работы = 'Разработка мобильного приложения'
    ''')
    rows = cursor.fetchall()

    new_window = tk.Toplevel(window)
    new_window.title("Должностной состав сотрудников, выполняющих работу «Разработка Мобильного Приложения»")
    new_window.geometry("1200x160")

    tree = ttk.Treeview(new_window, columns=[col[0] for col in cursor.description], show="headings")
    for col in cursor.description:
        tree.heading(col[0], text=col[0])
    tree.pack(expand=True, fill="both")

    for row in rows:
        tree.insert("", tk.END, values=row)

# Создаем главное окно
window = tk.Tk()
window.title("Кнопочная форма    БД")
window.geometry("300x400")

label_tables = tk.Label(window, text="Таблицы", font=("Times New Roman", 12))
label_tables.pack(pady=5)
# Кнопки для выбора таблиц
button_work = ttk.Button(window, text="Работа", command=lambda: show_table("Работа"))
button_work.pack(pady=10)
button_employees = ttk.Button(window, text="Сотрудники", command=lambda: show_table("Сотрудники"))
button_employees.pack(pady=10)
button_assignments = ttk.Button(window, text="Поручения", command=lambda: show_table("Поручения"))
button_assignments.pack(pady=10)


label_queries = tk.Label(window, text="Запросы", font=("Times New Roman", 12))
label_queries.pack(pady=5)
# Кнопки для выполнения выборок
button_selection1 = ttk.Button(window, text="Выборка-1", command=выборка_1)
button_selection1.pack(pady=10)

button_selection2 = ttk.Button(window, text="Выборка-2", command=выборка_2)
button_selection2.pack(pady=10)

button_selection3 = ttk.Button(window, text="Выборка-3", command=выборка_3)
button_selection3.pack(pady=10)

button_selection4 = ttk.Button(window, text="Выборка-4", command=выборка_4)
button_selection4.pack(pady=10)

window.mainloop()