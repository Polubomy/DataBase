import mysql.connector

# Подключение к базе данных
mydb = mysql.connector.connect(
  host="localhost",
  user="moonllee",
  password="i28d63h7",
  database="Local instance MySQL80"
)

# Создание курсора
mycursor = mydb.cursor()

# Вставка данных в таблицу "Гости"
sql = "INSERT INTO guests (name, passport_data, address, contact_information) VALUES (%s, %s, %s, %s)"
val = ("Иванов Иван Иванович", "1234 567890", "г. Москва, ул. Ленина, д. 1", "+7 (999) 123-45-67")
mycursor.execute(sql, val)
mydb.commit()

# Вставка данных в таблицу "Номера"
sql = "INSERT INTO rooms (room_type, price, status) VALUES (%s, %s, %s)"
val = ("Одноместный", 175.00, "Свободен")
mycursor.execute(sql, val)
mydb.commit()

# Вставка данных в таблицу "Бронирования"
sql = "INSERT INTO bookings (guest_id, room_id, arrival_date, departure_date, payment_method) VALUES (%s, %s, %s, %s, %s)"
val = (1, 1, "2023-07-15", "2023-07-17", "Наличные")
mycursor.execute(sql, val)
mydb.commit()

# Закрытие соединения с базой данных
mydb.close()