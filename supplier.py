from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
import sqlite3
class supplierClass:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1130x500+220+130")
        self.root.title("Система управления для компании ООО Тесла | Разработчик: Разумова Е.В.")
        self.root.config(bg="white")
        self.root.focus_force()
        #=====================

        #all variables
        self.var_searchby = StringVar()
        self.var_searchtxt = StringVar()

        self.var_sup_invoice = StringVar()
        self.var_name = StringVar()
        self.var_contact = StringVar()

        #===search_frame===
        SearchFrame=LabelFrame(self.root, text="Поиск по поставщикам", bg="white")
        SearchFrame.place(x=230, y=20, width=620, height=70)

        #===options===
        lbl_search = Label(SearchFrame, text="Поиск по номеру счет-фактуры:", font= ("Verdana",10),justify=CENTER)
        lbl_search.place(x=10, y=10)

        txt_search = Entry(SearchFrame, textvariable=self.var_searchtxt, font=("Verdana", 10),bg="#fae6b4").place(x=245,y=8, width=200, height=25)
        btn_search = Button(SearchFrame, command=self.search, text = "Поиск", bg="#4caf50", cursor="hand2", fg="white", font=("Verdana",14,"bold")).place(x=455, y=6, width=150, height=30)

        #===title===
        title = Label(self.root,text="Данные о поставщиках",bg="grey",fg="white").place(x=50, y=100, width=1000)

        #===content===
        #===row1===
        lbl_supplier_invoice = Label(self.root, text="Номер счет-фактуры", bg="white").place(x=50, y=150)
        txt_supplier_invoice = Entry(self.root, textvariable=self.var_sup_invoice, bg="white").place(x=200, y=150, width=180)

        #===row2===
        lbl_name = Label(self.root, text="ФИО поставщика", bg="white").place(x=50, y=190)
        txt_name = Entry(self.root, textvariable=self.var_name, bg="white").place(x=200, y=190, width=180)

        #===row3===
        lbl_contact = Label(self.root, text="Телефон", bg="white").place(x=50, y=230)
        txt_contact = Entry(self.root, textvariable=self.var_contact, bg="white").place(x=200, y=230, width=180)

        #===row4===
        lbl_desc = Label(self.root, text="Описание", bg="white").place(x=50, y=270)
        self.txt_desc = Text(self.root, bg="white")
        self.txt_desc.place(x=200, y=270, width=240, height=60)

        #===button===
        btn_add = Button(self.root, text="Сохранить", command=self.add, bg="#2196f3", fg= "white", cursor="hand2").place(x=500, y=305, width=90, height=28)
        btn_update = Button(self.root, text="Обновить", command=self.update, bg="#4caf50", fg= "white", cursor="hand2").place(x=610, y=305, width=90, height=28)
        btn_delete = Button(self.root, text="Удалить карточку", command=self.delete, bg="#f44336", fg= "white", cursor="hand2").place(x=720, y=305, width=115, height=28)
        btn_clear = Button(self.root, text="Очистить", command=self.clear, bg="#607d8b", fg= "white", cursor="hand2").place(x=855, y=305, width=90, height=28)

        #===employee details===

        emp_frames=Frame(self.root, bd=3)
        emp_frames.place(x=0, y=350, relwidth=1, height=150)
        scrolly = Scrollbar(emp_frames, orient=VERTICAL)
        scrollx = Scrollbar(emp_frames, orient=HORIZONTAL)

        self.SupplierTable = ttk.Treeview(emp_frames, columns=(
            "счет-фактура", "ФИО", "Телефон",
            "Описание"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)

        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.SupplierTable.xview)
        scrolly.config(command=self.SupplierTable.yview)
        self.SupplierTable.heading("счет-фактура", text="счет-фактура")
        self.SupplierTable.heading("ФИО", text="ФИО")
        self.SupplierTable.heading("Телефон", text="Телефон")
        self.SupplierTable.heading("Описание", text="Описание")

        self.SupplierTable["show"] = "headings"

        self.SupplierTable.column("счет-фактура", width=150)
        self.SupplierTable.column("ФИО", width=350)
        self.SupplierTable.column("Телефон", width=200)
        self.SupplierTable.column("Описание", width=250)

        self.SupplierTable.pack(fill=BOTH, expand=1)
        self.SupplierTable.bind("<ButtonRelease-1>", self.get_data)
        self.show()

#=================functions=========================================

    def add(self):
        con = sqlite3.connect(database=r"diplom_project.db")
        cur = con.cursor()
        try:
            if self.var_sup_invoice.get() == "":
                messagebox.showerror("Error", "Номер счет-фактуры должен быть заполнен", parent=self.root)
            else:
                cur.execute("SELECT * FROM supplier WHERE invoice=?", (self.var_sup_invoice.get(),))
                row=cur.fetchone()
                if row != None:
                    messagebox.showerror("Error", "Ошибка. Счет-фактура с таким номером уже существует. Назначьте другой номер", parent=self.root)
                else:
                    cur.execute("Insert into supplier (invoice,name,contact,desc) values (?,?,?,?)",

                                    (
                                    self.var_sup_invoice.get(),
                                    self.var_name.get(),
                                    self.var_contact.get(),
                                    self.txt_desc.get('1.0', END),
                                ))
                    con.commit()
                    messagebox.showinfo("Успешно", "Запись была успешно добавлена в базу",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Ошибка с {str(ex)}", parent=self.root)


    def show(self):
        con = sqlite3.connect(database=r"diplom_project.db")
        cur = con.cursor()
        try:
            cur.execute("select * from supplier")
            rows=cur.fetchall()
            self.SupplierTable.delete(*self.SupplierTable.get_children())
            for row in rows:
                self.SupplierTable.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Error", f"Ошибка с {str(ex)}", parent=self.root)

    def get_data(self,ev):
        f= self.SupplierTable.focus()
        content=(self.SupplierTable.item(f))
        row=content['values']
        #print(row)
        self.var_sup_invoice.set(row[0])
        self.var_name.set(row[1])
        self.var_contact.set(row[2])
        self.txt_desc.delete('1.0', END)
        self.txt_desc.insert(END, row[3])

    def update(self):
        con = sqlite3.connect(database=r"diplom_project.db")
        cur = con.cursor()
        try:
            if self.var_sup_invoice.get() == "":
                messagebox.showerror("Error", "Номер счет-фактуры должен быть заполнен", parent=self.root)
            else:
                cur.execute("SELECT * FROM supplier WHERE invoice=?", (self.var_sup_invoice.get(),))
                row=cur.fetchone()
                if row == None:
                    messagebox.showerror("Error", "Неккоректный номер счета-фактуры", parent=self.root)
                else:
                    #cur.execute("Insert into employee (ID,Пол,Телефон,ФИО,Отдел,Должность,Email,Пароль,Тип пользователя,Адрес,Зп) values (?,?,?,?,?,?,?,?,?,?,?)",
                    cur.execute("Update supplier set name=?,contact=?,desc=? where invoice=?",(
                        self.var_name.get(),
                        self.var_contact.get(),
                        self.txt_desc.get('1.0', END),
                        self.var_sup_invoice.get(),
                    ))
                    con.commit()
                    messagebox.showinfo("Успешно", "Данные успешно обновлены", parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Ошибка с {str(ex)}", parent=self.root)

    def delete(self):
        con = sqlite3.connect(database=r"diplom_project.db")
        cur = con.cursor()
        try:
            if self.var_sup_invoice.get() == "":
                messagebox.showerror("Error", "Номер счет-фактуры должен быть заполнен", parent=self.root)
            else:
                cur.execute("SELECT * FROM supplier WHERE invoice=?", (self.var_sup_invoice.get(),))
                row=cur.fetchone()
                if row == None:
                    messagebox.showerror("Error", "Неккоректный номер счет-фактуры", parent=self.root)
                else:
                    op=messagebox.askyesno("Подтверждение", "Вы действительно хотите удалить запись?", parent=self.root)
                    if op==True:
                        cur.execute("delete from supplier where invoice=?",(self.var_sup_invoice.get(),))
                        con.commit()
                        messagebox.showinfo("Удалить", "Запись успешно удалена", parent=self.root)
                        self.clear()
        except Exception as ex:
            messagebox.showerror("Error", f"Ошибка с {str(ex)}", parent=self.root)


    def clear(self):
        self.var_sup_invoice.set("")
        self.var_name.set("")
        self.var_contact.set("")
        self.txt_desc.delete('1.0', END)
        self.var_searchtxt.set("")
        self.show()

    def search(self):
        con = sqlite3.connect(database=r"diplom_project.db")
        cur = con.cursor()
        try:
            if self.var_searchtxt.get()=="":
                messagebox.showerror("Ошибка", "Задана пустая строка, введите значение",  parent=self.root)
            else:
                cur.execute("select * from supplier where invoice=?", (self.var_searchtxt.get(),))
                row=cur.fetchone()
                if row!=None:
                    self.SupplierTable.delete(*self.SupplierTable.get_children())
                    self.SupplierTable.insert('',END,values=row)
                else:
                    messagebox.showerror("Ошибка", "Ничего не найдено",  parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error", f"Ошибка с {str(ex)}", parent=self.root)
            print(str(self.var_searchby.get()))

if __name__=="__main__":
    root = Tk()
    obj = supplierClass(root)
    root.mainloop()