import sqlite3
def create_db():
	con=sqlite3.connect(database=r'diplom_project.db')
	cur=con.cursor()
	'''columns = (
		"ID", "Пол", "Телефон",  "ФИО", "Отдел",
		"Должность", "Email", "Пароль", "Тип пользователя", "Адрес", "Зп")'''
	cur.execute("CREATE TABLE IF NOT EXISTS employee(ID INTEGER PRIMARY KEY AUTOINCREMENT, fio TEXT, gender TEXT, phone TEXT, email TEXT, dob TEXT, doj TEXT, utype TEXT, address TEXT, salary TEXT)")
	con.commit()

create_db()