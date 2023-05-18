from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
import sqlite3
class employeeClass:
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

        self.var_emp_id = StringVar()
        self.var_gender = StringVar()
        self.var_contact = StringVar()
        self.var_name = StringVar()
        self.var_dob = StringVar()
        self.var_doj = StringVar()
        self.var_email = StringVar()
        self.var_pass = StringVar()
        self.var_utype = StringVar()
        self.var_address = StringVar()
        self.var_salary = StringVar()

        #===search_frame===
        SearchFrame=LabelFrame(self.root,text="Поиск по сотрудникам", bg="white")
        SearchFrame.place(x=250,y=20,width=600,height=70)

        #===options===
        cmb_search=ttk.Combobox(SearchFrame,textvariable=self.var_searchby,values=("Выбрать", "ФИО", "Email", "Телефон"),state='readonly',justify=CENTER)
        cmb_search.place(x=10,y=10,width=180)
        cmb_search.current(0)

        txt_search = Entry(SearchFrame, textvariable=self.var_searchtxt,font=("Verdana",15),bg="#fae6b4").place(x=200,y=8, width=200)
        btn_search = Button(SearchFrame, text = "Поиск", bg="#4caf50",cursor="hand2").place(x=410, y=7, width=150, height=30)

        #===title===
        title = Label(self.root,text="Данные о сотруднике",bg="grey",fg="white").place(x=50, y=100, width=1000)

        #===content===
        #===row1===
        lbl_empid = Label(self.root, text="ID сотрудника", bg="white").place(x=50, y=150)
        lbl_gender = Label(self.root, text="Пол", bg="white").place(x=460, y=150)
        lbl_contact = Label(self.root, text="Телефон", bg="white").place(x=750, y=150)

        txt_empid = Entry(self.root, textvariable=self.var_emp_id, bg="white").place(x=150, y=150, width=180)
        cmb_gender = ttk.Combobox(self.root, textvariable=self.var_gender,
                                  values=("Выбрать", "М", "Ж"), state='readonly', justify=CENTER)
        cmb_gender.place(x=500, y=150, width=180)
        cmb_gender.current(0)
        txt_contact = Entry(self.root, textvariable=self.var_contact, bg="white").place(x=850, y=150, width=180)

        #===row2===
        lbl_name = Label(self.root, text="ФИО", bg="white").place(x=50, y=190)
        lbl_dob = Label(self.root, text="Отдел", bg="white").place(x=450, y=190)
        lbl_doj = Label(self.root, text="Должность", bg="white").place(x=750, y=190)

        txt_name = Entry(self.root, textvariable=self.var_name, bg="white").place(x=150, y=190, width=180)
        cmb_dob = ttk.Combobox(self.root, textvariable=self.var_dob,
                               values=("Выбрать", "Руководство", "Бухгалтерия и финансы",
                                       "Отдел снабжения и закупок", "Рабочие", "Ремонтный отдел",
                                       "Транспортный отдел", "Инженерный отдел", "Отдел энергообеспечения"), state='readonly', justify=CENTER)
        cmb_dob.place(x=500, y=190, width=180)
        cmb_dob.current(0)
        txt_doj = Entry(self.root, textvariable=self.var_doj, bg="white").place(x=850, y=190, width=180)

        #===row3===
        lbl_email = Label(self.root, text="Email", bg="white").place(x=50, y=230)
        lbl_pass = Label(self.root, text="Пароль", bg="white").place(x=440, y=230)
        lbl_utp = Label(self.root, text="Тип пользователя", bg="white").place(x=750, y=230)

        txt_email = Entry(self.root, textvariable=self.var_email, bg="white").place(x=150, y=230, width=180)
        txt_pass = Entry(self.root, textvariable=self.var_pass, bg="white").place(x=500, y=230, width=180)
        cmb_utp = ttk.Combobox(self.root, textvariable=self.var_utype,
                               values=("Выбрать","Администратор", "Сотрудник"), state='readonly', justify=CENTER)
        cmb_utp.place(x=900, y=230, width=127)
        cmb_utp.current(0)

        #===row4===
        lbl_address = Label(self.root, text="Адрес", bg="white").place(x=50, y=270)
        lbl_salary = Label(self.root, text="Заработок", bg="white").place(x=420, y=270)

        self.txt_address = Text(self.root, bg="white")
        self.txt_address.place(x=150, y=270, width=240, height=60)
        txt_salary = Entry(self.root, textvariable=self.var_salary, bg="white").place(x=500, y=270, width=180)

        #===button===
        btn_add = Button(self.root, text="Сохранить", command=self.add, bg="#2196f3", fg= "white", cursor="hand2").place(x=500, y=305, width=90, height=28)
        btn_update = Button(self.root, text="Обновить", command=self.update, bg="#4caf50", fg= "white", cursor="hand2").place(x=610, y=305, width=90, height=28)
        btn_delete = Button(self.root, text="Удалить все", bg="#f44336", fg= "white", cursor="hand2").place(x=720, y=305, width=90, height=28)
        btn_clear = Button(self.root, text="Очистить", bg="#607d8b", fg= "white", cursor="hand2").place(x=830, y=305, width=90, height=28)

        #===employee details===

        emp_frames=Frame(self.root,bd=3)
        emp_frames.place(x=0,y=350,relwidth=1, height=150)
        scrolly = Scrollbar(emp_frames,orient=VERTICAL)
        scrollx = Scrollbar(emp_frames, orient=HORIZONTAL)

        self.EmployeeTable = ttk.Treeview(emp_frames, columns=(
            "ID", "Пол", "Телефон", "ФИО", "Отдел",
            "Должность",  "Email", "Пароль", "Тип пользователя", "Адрес", "Зп"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)

        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.EmployeeTable.xview)
        scrolly.config(command=self.EmployeeTable.yview)
        self.EmployeeTable.heading("ID", text="ID")
        self.EmployeeTable.heading("Пол", text="Пол")
        self.EmployeeTable.heading("Телефон", text="Телефон")
        self.EmployeeTable.heading("ФИО", text="ФИО")
        self.EmployeeTable.heading("Отдел", text="Отдел")
        self.EmployeeTable.heading("Должность", text="Должность")
        self.EmployeeTable.heading("Email", text="Email")
        self.EmployeeTable.heading("Пароль", text="Пароль")
        self.EmployeeTable.heading("Тип пользователя", text="Тип пользователя")
        self.EmployeeTable.heading("Адрес", text="Адрес")
        self.EmployeeTable.heading("Зп", text="З/п")

        self.EmployeeTable["show"] = "headings"

        self.EmployeeTable.column("ID", width=50)
        self.EmployeeTable.column("Пол", width=50)
        self.EmployeeTable.column("Телефон", width=100)
        self.EmployeeTable.column("ФИО", width=250)
        self.EmployeeTable.column("Отдел", width=200)
        self.EmployeeTable.column("Должность", width=150)
        self.EmployeeTable.column("Email", width=150)
        self.EmployeeTable.column("Пароль", width=150)
        self.EmployeeTable.column("Тип пользователя", width=100)
        self.EmployeeTable.column("Адрес", width=300)
        self.EmployeeTable.column("Зп", width=130)

        self.EmployeeTable.pack(fill=BOTH, expand=1)
        self.EmployeeTable.bind("<ButtonRelease-1>", self.get_data)
        self.show()

#==========================================================

    def add(self):
        con = sqlite3.connect(database=r"diplom_project.db")
        cur = con.cursor()
        try:
            if self.var_emp_id.get() == "":
                messagebox.showerror("Error", "ID сотрудника должно быть заполнено", parent=self.root)
            else:
                cur.execute("SELECT * FROM employee WHERE ID=?", (self.var_emp_id.get(),))
                row=cur.fetchone()
                if row != None:
                    messagebox.showerror("Error", "Ошибка. Пользователь с таким ID уже создан. Назначьте другой ID", parent=self.root)
                else:
                    #cur.execute("Insert into employee (ID,Пол,Телефон,ФИО,Отдел,Должность,Email,Пароль,Тип пользователя,Адрес,Зп) values (?,?,?,?,?,?,?,?,?,?,?)",
                    cur.execute("Insert into employee (ID,gender,phone,fio,dob,doj,email,pass,utype,address,salary) values (?,?,?,?,?,?,?,?,?,?,?)",

                                    (
                                    self.var_emp_id.get(),
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
                                ))
                    con.commit()
                    messagebox.showinfo("Успешно", "Сотрудник был успешно добавлен в базу",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Ошибка с {str(ex)}", parent=self.root)


    def show(self):
        con = sqlite3.connect(database=r"diplom_project.db")
        cur = con.cursor()
        try:
            cur.execute("select * from employee")
            rows=cur.fetchall()
            self.EmployeeTable.delete(*self.EmployeeTable.get_children())
            for row in rows:
                self.EmployeeTable.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Error", f"Ошибка с {str(ex)}", parent=self.root)

    def get_data(self,ev):
        f= self.EmployeeTable.focus()
        content=(self.EmployeeTable.item(f))
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


if __name__=="__main__":
    root=Tk()
    obj=employeeClass(root)
    root.mainloop()