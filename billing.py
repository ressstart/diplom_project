import sqlite3
from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk,messagebox

class BillClass:
	def __init__(self, root):
		self.root = root
		self.root.geometry("1680x800+0+0")
		self.root.title("Система управления для компании ООО Тесла")
		self.root.config(bg="white")

		# ===title===
		title = Label(self.root, text="Система управления для компании ООО Тесла",
		              font=("Verdana", 30, "bold"), bg="#694717", fg="white").place(x=0, y=0, relwidth=1, height=70)
		btn_logout = Button(self.root, text="Выйти", font=("Verdana", 13, "bold"), bg="white", fg="#694717").place(
			x=1400, y=10, height=30, width=150)

		#===product_frame1===
		ProductFrame1 = Frame(self.root, bd=4, relief=RIDGE, bg="white")
		ProductFrame1.place(x=6, y=110, width=410, height=550)
		pTitle = Label(ProductFrame1, text="Все товары", font=("Arial",14), bg="#262626", fg="white").pack(side=TOP,fill=X)


		#====================product frame2==============================
		self.var_search = StringVar()
		ProductFrame2 = Frame(ProductFrame1, bd=2, relief=RIDGE, bg="white")
		ProductFrame2.place(x=2, y=42, width=398, height=90)

		lbl_search = Label(ProductFrame2, text="Поиск товаров", bg="white", fg="green", font=("verdana",10, "bold")).place(x=2,y=5)

		lbl_search = Label(ProductFrame2, text="Наименование", font=("verdana",10,"bold"), bg="white").place(x=5, y=45)
		txt_search = Entry(ProductFrame2, textvariable=self.var_search, font=("verdana",12), bg="#fffaad").place(x=130, y=47,width=150,height=22)
		btn_search = Button(ProductFrame2, text="Поиск", command=self.search, bg="#2196f3", cursor="hand2", fg="white").place(x=285,y=45,width=100,height=25)
		btn_show_all = Button(ProductFrame2, text="Показать все", command=self.show, bg="#083531", cursor="hand2", fg="white").place(x=285,y=10,width=100,height=25)

		#======productFrame3======
		ProductFrame3 = Frame(ProductFrame1, bd=3)
		ProductFrame3.place(x=2, y=140, width=398, height=385)

		scrolly = Scrollbar(ProductFrame3, orient=VERTICAL)
		scrollx = Scrollbar(ProductFrame3, orient=HORIZONTAL)

		self.product_Table = ttk.Treeview(ProductFrame3, columns=("pid", "наименование", "цена", "количество", "статус"), yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)
		scrollx.pack(side=BOTTOM, fill=X)
		scrolly.pack(side=RIGHT, fill=Y)
		scrollx.config(command=self.product_Table.xview)
		scrolly.config(command=self.product_Table.yview)

		self.product_Table.heading("pid", text="PID")
		self.product_Table.heading("наименование", text="Наименование")
		self.product_Table.heading("цена", text="Цена")
		self.product_Table.heading("количество", text="Количество")
		self.product_Table.heading("статус", text="статус")
		self.product_Table["show"] = "headings"
		self.product_Table.column("pid", width=50)
		self.product_Table.column("наименование", width=150)
		self.product_Table.column("цена", width=70)
		self.product_Table.column("количество", width=100)
		self.product_Table.column("статус", width=100)

		self.product_Table.pack(fill=BOTH, expand=1)
		#self.product_Table.bind("<ButtonRelease-1>", self.get_data)

		lbl_note =Label(ProductFrame1,text="Заметка: 'Введите количество 0 для удаления товара'", anchor="w",font=("Verdana",8), bg="white", fg="red").pack(side=BOTTOM,fill=X)

		#=======CustomerFrame========
		self.var_cname = StringVar()
		self.var_contact = StringVar()
		CustomerFrame = Frame(self.root, bd=4, relief=RIDGE, bg="white")
		CustomerFrame.place(x=420, y=110, width=630, height=70)

		cTitle = Label(CustomerFrame, text="Покупатель", font=("Verdana", 12), bg="lightgrey").pack(side=TOP, fill=X)
		lbl_name = Label(CustomerFrame, text="Фамилия", font=("verdana", 10, "bold"), bg="white").place(x=5, y=35)
		txt_name = Entry(CustomerFrame, textvariable=self.var_cname, font=("verdana", 12), bg="#fffaad").place(x=90, y=35, width=180)

		lbl_contact = Label(CustomerFrame, text="Телефон", font=("verdana", 10, "bold"), bg="white").place(x=290, y=35)
		txt_contact = Entry(CustomerFrame, textvariable=self.var_cname, font=("verdana", 12), bg="#fffaad").place(x=370, y=35, width=140)

		# ===========Cal Cart Frame================
		Cal_Cart_Frame = Frame(self.root, bd=2, relief=RIDGE, bg="white")
		Cal_Cart_Frame.place(x=420, y=190, width=630, height=360)

		# ===========Calculator Frame================
		self.var_cal_input=StringVar()
		Cal_Frame = Frame(Cal_Cart_Frame, bd=9, relief=RIDGE, bg="white")
		Cal_Frame.place(x=5, y=10, width=268, height=340)

		self.txt_cal_input = Entry(Cal_Frame, textvariable=self.var_cal_input, font=("Verdana",10,'bold'), width=26, bd=10, relief=GROOVE, state='readonly', justify=RIGHT)
		self.txt_cal_input.grid(row=0, columnspan=4)

		btn_7 = Button(Cal_Frame, text='7', font=("Verdana",13,'bold'), command=lambda:self.get_input(7), bd=5, width=4, pady=15, cursor='hand2').grid(row=1, column=0)
		btn_8 = Button(Cal_Frame, text='8', font=("Verdana", 13,'bold'), command=lambda:self.get_input(8), bd=5, width=4, pady=15, cursor='hand2').grid(row=1,column=1)
		btn_9 = Button(Cal_Frame, text='9', font=("Verdana", 13,'bold'), command=lambda:self.get_input(9), bd=5, width=4, pady=15, cursor='hand2').grid(row=1,column=2)
		btn_add = Button(Cal_Frame, text='+', font=("Verdana", 13,'bold'), command=lambda:self.get_input('+'), bd=5, width=4, pady=15, cursor='hand2').grid(row=1,column=3)

		btn_4 = Button(Cal_Frame, text='4', font=("Verdana", 13,'bold'), command=lambda:self.get_input(4), bd=5, width=4, pady=15, cursor='hand2').grid(row=2,column=0)
		btn_5 = Button(Cal_Frame, text='5', font=("Verdana", 13,'bold'), command=lambda:self.get_input(5), bd=5, width=4, pady=15, cursor='hand2').grid(row=2,column=1)
		btn_6 = Button(Cal_Frame, text='6', font=("Verdana", 13,'bold'), command=lambda:self.get_input(6), bd=5, width=4, pady=15, cursor='hand2').grid(row=2,column=2)
		btn_sub = Button(Cal_Frame, text='-', font=("Verdana", 13,'bold'), command=lambda:self.get_input('-'), bd=5, width=4, pady=15, cursor='hand2').grid(row=2,column=3)

		btn_1 = Button(Cal_Frame, text='1', font=("Verdana", 13,'bold'), command=lambda:self.get_input(1), bd=5, width=4, pady=15, cursor='hand2').grid(row=3,column=0)
		btn_2 = Button(Cal_Frame, text='2', font=("Verdana", 13,'bold'), command=lambda:self.get_input(2), bd=5, width=4, pady=15, cursor='hand2').grid(row=3,column=1)
		btn_3 = Button(Cal_Frame, text='3', font=("Verdana", 13,'bold'), command=lambda:self.get_input(3), bd=5, width=4, pady=15, cursor='hand2').grid(row=3,column=2)
		btn_mul = Button(Cal_Frame, text='*', font=("Verdana", 13,'bold'), command=lambda:self.get_input('*'), bd=5, width=4, pady=15, cursor='hand2').grid(row=3,column=3)

		btn_0 = Button(Cal_Frame, text='0', font=("Verdana", 13,'bold'), command=lambda:self.get_input(0), bd=5, width=4, pady=20, cursor='hand2').grid(row=4,column=0)
		btn_c = Button(Cal_Frame, text='C', font=("Verdana", 13,'bold'), command=self.clear_cal, bd=5, width=4, pady=20, cursor='hand2').grid(row=4,column=1)
		btn_eq = Button(Cal_Frame, text='=', font=("Verdana", 13,'bold'), command=self.perform_call ,bd=5, width=4, pady=20, cursor='hand2').grid(row=4,column=2)
		btn_div = Button(Cal_Frame, text='/', font=("Verdana", 13,'bold'), command=lambda:self.get_input('/'), bd=5, width=4, pady=20, cursor='hand2').grid(row=4,column=3)

		#===========Cart Frame================
		cart_Frame = Frame(Cal_Cart_Frame, bd=3)
		cart_Frame.place(x=280, y=8, width=345, height=342)
		cartTitle = Label(cart_Frame, text="Корзина \t\t\t Выбрано: [0]", font=("Verdana", 10), bg="lightgrey").pack(side=TOP, fill=X)

		scrolly = Scrollbar(cart_Frame, orient=VERTICAL)
		scrollx = Scrollbar(cart_Frame, orient=HORIZONTAL)

		self.CartTable = ttk.Treeview(cart_Frame, columns=("pid", "наименование", "цена", "количество", "статус"),
		                                  yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)
		scrollx.pack(side=BOTTOM, fill=X)
		scrolly.pack(side=RIGHT, fill=Y)
		scrollx.config(command=self.CartTable.xview)
		scrolly.config(command=self.CartTable.yview)

		self.CartTable.heading("pid", text="PID")
		self.CartTable.heading("наименование", text="Наименование")
		self.CartTable.heading("цена", text="Цена")
		self.CartTable.heading("количество", text="Количество")
		self.CartTable.heading("статус", text="Статус")
		self.CartTable["show"] = "headings"
		self.CartTable.column("pid", width=50)
		self.CartTable.column("наименование", width=150)
		self.CartTable.column("цена", width=70)
		self.CartTable.column("количество", width=100)
		self.CartTable.column("статус", width=100)

		self.CartTable.pack(fill=BOTH, expand=1)
		# self.CartTable.bind("<ButtonRelease-1>", self.get_data)

		#===============Add Cart Widgets Frame====================
		self.var_pid = StringVar()
		self.var_pname = StringVar()
		self.var_price = StringVar()
		self.var_qty = StringVar()
		self.var_stock = StringVar()

		Add_CartWidgetsFrame = Frame(self.root, bd=2, relief=RIDGE, bg="white")
		Add_CartWidgetsFrame.place(x=420, y=550, width=630, height=110)

		lbl_p_name = Label(Add_CartWidgetsFrame, text="Наименование", font=("verdana", 10, "bold"), bg="white").place(x=5, y=5)
		txt_p_name = Entry(Add_CartWidgetsFrame, textvariable=self.var_pname, font=("verdana", 12), bg="#fffaad", state='readonly').place(x=8, y=35, width=190, height=22)

		lbl_p_price = Label(Add_CartWidgetsFrame, text="Цена за шт./кг/м3", font=("verdana", 10, "bold"), bg="white").place(x=230, y=5)
		txt_p_price = Entry(Add_CartWidgetsFrame, textvariable=self.var_price, font=("verdana", 12), bg="#fffaad",state='readonly').place(x=233, y=35, width=170, height=22)

		lbl_p_qty = Label(Add_CartWidgetsFrame, text="Количество", font=("verdana", 10, "bold"), bg="white").place(x=440, y=5)
		txt_p_qty = Entry(Add_CartWidgetsFrame, textvariable=self.var_qty, font=("verdana", 12), bg="#fffaad",).place(x=443, y=35, width=100, height=22)

		self.lbl_inStock = Label(Add_CartWidgetsFrame, text="В корзине [9999]", font=("verdana", 10, "bold"), bg="white").place(x=5, y=70)

		btn_clear_cart = Button(Add_CartWidgetsFrame, text = "Очистить", font=("verdana", 10, "bold"), bg="lightgrey", cursor="hand2").place(x=280, y =70, width=150, height=30)
		btn_add_cart = Button(Add_CartWidgetsFrame, text = "Добавить | Обновить", font=("verdana", 10, "bold"), bg="orange", cursor="hand2").place(x=440, y =70, width=180, height=30)

		#=========billing area=================
		billFrame = Frame(self.root, bd=2, relief=RIDGE, bg='white')
		billFrame.place(x=1055, y=110, width=520, height=370)

		BTitle = Label(billFrame, text="Итого", font=("Arial", 14), bg="#262626", fg="white").pack(side=TOP, fill=X)
		scrolly = Scrollbar(billFrame, orient=VERTICAL)
		scrolly.pack(side=RIGHT, fill=Y)

		self.txt_bill_area = Text(billFrame, yscrollcommand=scrolly.set)
		self.txt_bill_area.pack(fill=BOTH, expand=1)
		scrolly.config(command=self.txt_bill_area.yview)

		#===================billing buttons===========================
		billMenuFrame = Frame(self.root, bd=2, relief=RIDGE, bg='white')
		billMenuFrame.place(x=1055, y=480, width=520, height=180)

		self.lbl_amount=Label(billMenuFrame,text='Итого:\n[0]', font=("Arial", 14), bg="#3f51b5", fg="white")
		self.lbl_amount.place(x=5, y=5, width=160, height=70)

		self.lbl_dsc = Label(billMenuFrame, text='Скидка\n[5%]', font=("Arial", 14), bg="#8bc34a", fg="white")
		self.lbl_dsc.place(x=170, y=5, width=165, height=70)

		self.lbl_net_pay = Label(billMenuFrame, text='Прибыль\n[0]', font=("Arial", 14), bg="#607d8b", fg="white")
		self.lbl_net_pay.place(x=340, y=5, width=170, height=70)

		#btn_print = Label(billMenuFrame, text='Итого:\n[0]', font=("Arial", 14), bg="#3f51b5", fg="white")
		#btn_print.place(x=5, y=5, width=160, height=70)

		btn_clear_all = Button(billMenuFrame, text='Очистить все', cursor='hand2', font=("Arial", 14), bg="grey", fg="white")
		btn_clear_all.place(x=170, y=80, width=165, height=70)

		btn_generate = Button(billMenuFrame, text='Создать чек', cursor='hand2', font=("Arial", 14), bg="#009688", fg="white")
		btn_generate.place(x=340, y=80, width=170, height=70)

		self.show()
	#==============functions===============
	def get_input(self,num):
		xnum = self.var_cal_input.get() + str(num)
		self.var_cal_input.set(xnum)

	def clear_cal(self):
		self.var_cal_input.set('')

	def perform_call(self):
		result = self.var_cal_input.get()
		self.var_cal_input.set(eval(result))

	def show(self):
		con = sqlite3.connect(database=r"diplom_project.db")
		cur = con.cursor()
		try:
			#self.product_Table = ttk.Treeview(ProductFrame3, columns=("pid", "наименование", "цена", "количество", "статус"), yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)

			cur.execute("select pid, name, price, qty, status from product")
			rows = cur.fetchall()
			self.product_Table.delete(*self.product_Table.get_children())
			for row in rows:
				self.product_Table.insert('', END, values=row)
		except Exception as ex:
			messagebox.showerror("Error", f"Ошибка с {str(ex)}", parent=self.root)


	def search(self):
		con = sqlite3.connect(database=r"diplom_project.db")
		cur = con.cursor()
		try:
			if self.var_search.get() == "":
				messagebox.showerror("Ошибка", "Задана пустая строка, введите значение", parent=self.root)

			else:
				# fio LIKE '%" + self.var_searchtxt.get() + "%'"
				cur.execute("select pid, name, price, qty, status from product where name LIKE '%" + self.var_search.get() + "%'")
				rows = cur.fetchall()
				if len(rows) != 0:
					self.product_Table.delete(*self.product_Table.get_children())
					for row in rows:
						self.product_Table.insert('', END, values=row)
				else:
					messagebox.showerror("Ошибка", "Ничего не найдено", parent=self.root)
		except Exception as ex:
			messagebox.showerror("Error", f"Ошибка с {str(ex)}", parent=self.root)
			print(str(self.var_searchby.get()))


if __name__=="__main__":
    root = Tk()
    obj = BillClass(root)
    root.mainloop()