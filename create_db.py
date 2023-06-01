import sqlite3
def create_db():
	con=sqlite3.connect(database=r'diplom_project.db')
	cur=con.cursor()
	cur.execute("CREATE TABLE IF NOT EXISTS employee(ID INTEGER PRIMARY KEY AUTOINCREMENT, fio TEXT, gender TEXT, phone TEXT, email TEXT, dob TEXT, doj TEXT, utype TEXT, address TEXT, salary TEXT)")
	con.commit()

	cur.execute("CREATE TABLE IF NOT EXISTS supplier(invoice INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, contact TEXT, desc TEXT)")
	con.commit()

	cur.execute("CREATE TABLE IF NOT EXISTS category(cid INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT)")
	con.commit()

	cur.execute("CREATE TABLE IF NOT EXISTS product(pid INTEGER PRIMARY KEY AUTOINCREMENT, Category TEXT, Supplier TEXT, name TEXT, price INTEGER, qty TEXT, status TEXT)")
	con.commit()

create_db()