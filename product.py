from tkinter import *
from tkinter import ttk, messagebox
import sqlite3
class productClass:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1130x500+220+130")
        self.root.title("Система управления для компании ООО Тесла | Разработчик: Разумова Е.В.")
        self.root.config(bg="white")
        self.root.focus_force()

        #=====================
        self.var_cat=StringVar()
        self.cat_list=[]
        self.var_sup=StringVar()
        self.sup_list=[]
        self.fetch_cat_sup()

        self.var_name=StringVar()
        self.var_price=StringVar()
        self.var_qty=StringVar()
        self.var_status=StringVar()

        self.var_searchby = StringVar()
        self.var_searchtxt = StringVar()

        product_Frame = Frame(self.root, bd=2, bg="white",relief=RIDGE)
        product_Frame.place(x=10,y=10,width=450,height=480)

        #===================title======================
        title = Label(product_Frame, text="Управление товарами", bg="#0f4d7d", fg="white", font=("Verdana", 14)).pack(side=TOP, fill=X)

        #======================column1===============================
        lbl_category = Label(product_Frame, text="Категория",bg="white", font=("Verdana", 10)).place(x=20,y=60)
        lbl_supplier = Label(product_Frame, text="Поставщик",bg="white", font=("Verdana", 10)).place(x=20,y=110)
        lbl_product_name = Label(product_Frame, text="Название товара",bg="white", font=("Verdana", 10)).place(x=20,y=160)
        lbl_price = Label(product_Frame, text="Цена",bg="white", font=("Verdana", 10)).place(x=20,y=210)
        lbl_qty = Label(product_Frame, text="Количество",bg="white", font=("Verdana", 10)).place(x=20,y=260)
        lbl_status = Label(product_Frame, text="Статус",bg="white", font=("Verdana", 10)).place(x=20,y=310)


        #txt_category = Label(product_Frame, text="Категория",bg="white", font=("Verdana", 10)).place(x=30,y=60)

        #========================column2=============================
        cmb_cat = ttk.Combobox(product_Frame, textvariable=self.var_cat, values=self.cat_list, state='readonly', justify=CENTER)
        cmb_cat.place(x=150, y=63, width=200)
        cmb_cat.current(0)

        cmb_sup = ttk.Combobox(product_Frame, textvariable=self.var_sup, values=self.sup_list, state='readonly',justify=CENTER)
        cmb_sup.place(x=150, y=113, width=200)
        #cmb_sup.current(0)

        txt_name = Entry(product_Frame, textvariable=self.var_name).place(x=150, y=163, width=200)
        txt_price = Entry(product_Frame, textvariable=self.var_price).place(x=150, y=213, width=200)
        txt_qty = Entry(product_Frame, textvariable=self.var_qty).place(x=150, y=263, width=200)
        #txt_status = Entry(product_Frame, textvariable=self.var_status).place(x=150, y=263, width=200)

        cmb_status = ttk.Combobox(product_Frame, textvariable=self.var_status, values=("Активно","Не активно"), state='readonly',justify=CENTER)
        cmb_status.place(x=150, y=313, width=200)
        cmb_status.current(0)

        #==================button===================
        btn_add = Button(product_Frame, text="Сохранить",command=self.add, bg="#2196f3", fg="white", cursor="hand2").place(x=10, y=405, width=100, height=28)
        btn_update = Button(product_Frame, text="Обновить", bg="#4caf50", fg="white", cursor="hand2").place(x=120, y=405, width=100, height=28)
        btn_delete = Button(product_Frame, text="Удалить карточку", bg="#f44336", fg="white", cursor="hand2").place(x=230, y=405, width=130, height=28)
        btn_clear = Button(product_Frame, text="Очистить", bg="#607d8b", fg="white", cursor="hand2").place(x=370, y=405, width=70, height=28)

        #==========search_frame=================
        SearchFrame = LabelFrame(self.root, text="Поиск по сотрудникам", bg="white", font=("Calibri",12,"bold"))
        SearchFrame.place(x=480, y=10, width=600, height=80)

        #=====================options=======================
        cmb_search = ttk.Combobox(SearchFrame, textvariable=self.var_searchby,values=("Выбрать", "Категория", "Поставщик", "Название"), state='readonly', justify=CENTER)
        cmb_search.place(x=10, y=10, width=180)
        cmb_search.current(0)

        txt_search = Entry(SearchFrame, textvariable=self.var_searchtxt, font=("Verdana", 10), bg="#fae6b4").place(x=200, y=8, width=200)
        btn_search = Button(SearchFrame, command=self.search, text="Поиск", bg="#4caf50", fg="white", cursor="hand2").place(x=410, y=7, width=150, height=30)

        #================product details===================

        p_frame = Frame(self.root, bd=3)
        p_frame.place(x=480, y=100, width=600, height=390)
        scrolly = Scrollbar(p_frame, orient=VERTICAL)
        scrollx = Scrollbar(p_frame, orient=HORIZONTAL)

        self.product_table = ttk.Treeview(p_frame, columns=(
            "pID", "Категория", "Поставщик", "Название", "Цена",
            "Количество", "Статус"), yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.product_table.xview)
        scrolly.config(command=self.product_table.yview)
        self.product_table.heading("pID", text="P ID")
        self.product_table.heading("Категория", text="Категория")
        self.product_table.heading("Поставщик", text="Поставщик")
        self.product_table.heading("Название", text="Название")
        self.product_table.heading("Цена", text="Цена")
        self.product_table.heading("Количество", text="Количество")
        self.product_table.heading("Статус", text="Статус")

        self.product_table["show"] = "headings"

        self.product_table.column("pID", width=50)
        self.product_table.column("Категория", width=150)
        self.product_table.column("Поставщик", width=200)
        self.product_table.column("Название", width=200)
        self.product_table.column("Цена", width=100)
        self.product_table.column("Количество", width=100)
        self.product_table.column("Статус", width=100)

        self.product_table.pack(fill=BOTH, expand=1)
        self.product_table.bind("<ButtonRelease-1>", self.get_data)
        self.show()


    #==========================================================

    def fetch_cat_sup(self):
        con = sqlite3.connect(database=r"diplom_project.db")
        cur = con.cursor()
        try:
            cur.execute("SELECT name FROM category")
            cat=cur.fetchall()
            self.cat_list.append("Пусто")
            if len(cat) > 0:
                del self.cat_list[:]
                self.cat_list.append("Выбрать")
                for i in cat:
                    self.cat_list.append(i[0])

            cur.execute("SELECT name FROM supplier")
            sup = cur.fetchall()
            print(sup)


        except Exception as ex:
            messagebox.showerror("Error", f"Ошибка с {str(ex)}", parent=self.root)

    def add(self):
        con = sqlite3.connect(database=r"diplom_project.db")
        cur = con.cursor()
        try:
            if self.var_cat.get() == "Выбрать" or self.var_sup.get()=="Выбрать" or self.var_name.get()=="":
                messagebox.showerror("Error", "Все поля должны быть заполнены", parent=self.root)
            else:
                cur.execute("SELECT * FROM product WHERE name=?", (self.var_name.get(),))
                row=cur.fetchone()
                if row != None:
                    messagebox.showerror("Error", "Ошибка. Товар с таким названием уже создан. Назначьте другое название", parent=self.root)
                else:
                    #cur.execute("Insert into employee (ID,Пол,Телефон,ФИО,Отдел,Должность,Email,Пароль,Тип пользователя,Адрес,Зп) values (?,?,?,?,?,?,?,?,?,?,?)",
                    cur.execute("Insert into product (Category, Supplier, name, price, qty, status) values (?,?,?,?,?,?)",(
                        self.var_cat.get(),
                        self.var_sup.get(),
                        self.var_name.get(),
                        self.var_price.get(),
                        self.var_qty.get(),
                    ))
                    con.commit()
                    messagebox.showinfo("Успешно", "Товар успешно добавлен в базу",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Ошибка с {str(ex)}", parent=self.root)


    def show(self):
        con = sqlite3.connect(database=r"diplom_project.db")
        cur = con.cursor()
        try:
            cur.execute("select * from product")
            rows=cur.fetchall()
            self.product_table.delete(*self.product_table.get_children())
            for row in rows:
                self.product_table.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Error", f"Ошибка с {str(ex)}", parent=self.root)

    def get_data(self,ev):
        f= self.product_table.focus()
        content=(self.product_table.item(f))
        row=content['values']
        #print(row)
        self.var_emp_id.set(row[0])
        self.var_gender.set(row[1])
        self.var_contact.set(row[2])
        self.var_name.set(row[3])

        self.var_dob.set(row[4])
        self.var_doj.set(row[5])

        self.var_email.set(row[6])
        self.var_pass.set(row[7])
        self.var_utype.set(row[8])
        self.txt_address.delete('1.0', END)
        self.txt_address.insert(END, row[9])
        self.var_salary.set(row[10])

    def update(self):
        con = sqlite3.connect(database=r"diplom_project.db")
        cur = con.cursor()
        try:
            if self.var_emp_id.get() == "":
                messagebox.showerror("Error", "ID сотрудника должно быть заполнено", parent=self.root)
            else:
                cur.execute("SELECT * FROM employee WHERE ID=?", (self.var_emp_id.get(),))
                row=cur.fetchone()
                if row == None:
                    messagebox.showerror("Error", "Неккоректный ID", parent=self.root)
                else:
                    #cur.execute("Insert into employee (ID,Пол,Телефон,ФИО,Отдел,Должность,Email,Пароль,Тип пользователя,Адрес,Зп) values (?,?,?,?,?,?,?,?,?,?,?)",
                    cur.execute("Update employee set gender=?,phone=?,fio=?,dob=?,doj=?,email=?,pass=?,utype=?,address=?,salary=? where ID=?",(
                        self.var_gender.get(),
                        self.var_contact.get(),

                        self.var_name.get(),
                        self.var_dob.get(),
                        self.var_doj.get(),

                        self.var_email.get(),
                        self.var_pass.get(),
                        self.var_utype.get(),

                        self.txt_address.get('1.0', END),
                        self.var_salary.get(),
                        self.var_emp_id.get(),
                    ))
                    con.commit()
                    messagebox.showinfo("Успешно", "Данные сотрудника успешно обновлены", parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Ошибка с {str(ex)}", parent=self.root)

    def delete(self):
        con = sqlite3.connect(database=r"diplom_project.db")
        cur = con.cursor()
        try:
            if self.var_emp_id.get() == "":
                messagebox.showerror("Error", "ID сотрудника должно быть заполнено", parent=self.root)
            else:
                cur.execute("SELECT * FROM employee WHERE ID=?", (self.var_emp_id.get(),))
                row=cur.fetchone()
                if row == None:
                    messagebox.showerror("Error", "Неккоректный ID", parent=self.root)
                else:
                    op=messagebox.askyesno("Подтверждение", "Вы действительно хотите удалить карточку сотрудника?", parent=self.root)
                    if op==True:
                        cur.execute("delete from employee where id=?",(self.var_emp_id.get(),))
                        con.commit()
                        messagebox.showinfo("Удалить", "Карточка сотрудника успешно удалена", parent=self.root)
                        self.clear()
        except Exception as ex:
            messagebox.showerror("Error", f"Ошибка с {str(ex)}", parent=self.root)


    def clear(self):
        self.var_emp_id.set("")
        self.var_gender.set("Выбрать")
        self.var_contact.set("")
        self.var_name.set("")

        self.var_dob.set("Выбрать")
        self.var_doj.set("")

        self.var_email.set("")
        self.var_pass.set("")
        self.var_utype.set("Сотрудник")
        self.txt_address.delete('1.0', END)
        self.var_salary.set("")
        self.show()

    def search(self):
        con = sqlite3.connect(database=r"diplom_project.db")
        cur = con.cursor()
        try:
            if self.var_searchby.get=="Выбрать":
                messagebox.showerror("Ошибка", "Не выбран критерий поиска", parent=self.root)
            elif self.var_searchtxt.get()=="":
                messagebox.showerror("Ошибка", "Задана пустая строка, введите значение",  parent=self.root)
            else:
                if self.var_searchby.get() == "Телефон":
                    cur.execute(
                        "select * from employee where phone LIKE '%" + self.var_searchtxt.get() + "%'")
                elif self.var_searchby.get() == "ФИО":
                    cur.execute(
                        "select * from employee where fio LIKE '%" + self.var_searchtxt.get() + "%'")
                rows = cur.fetchall()
                if len(rows)!=0:
                    self.product_table.delete(*self.product_table.get_children())
                    for row in rows:
                        self.product_table.insert('', END, values=row)
                else:
                    messagebox.showerror("Ошибка", "Ничего не найдено",  parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error", f"Ошибка с {str(ex)}", parent=self.root)
            print(str(self.var_searchby.get()))

if __name__=="__main__":
    root = Tk()
    obj = productClass(root)
    root.mainloop()