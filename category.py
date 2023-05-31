from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
import sqlite3
class categoryClass:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1130x500+220+130")
        self.root.title("Система управления для компании ООО Тесла | Разработчик: Разумова Е.В.")
        self.root.config(bg="white")
        self.root.focus_force()

        #====variables====
        self.var_cat_id = StringVar()
        self.var_name = StringVar()

        #===title===

        lbl_title = Label(self.root, text="Управление категориями товаров",bg="#184a45",fg="white",font=("Verdana",20)).pack(side=TOP,fill=X, padx=20, pady=20)

        lbl_name = Label(self.root, text="Введите название категории:",bg="white",font=("Verdana", 14)).place(x=50, y=100)

        lbl_name = Entry(self.root, textvariable=self.var_name, bg="lightyellow",font=("Verdana", 12)).place(x=50, y=150, width=300)
        btn_add = Button(self.root, text="Добавить", command=self.add,bg="#4caf50",fg="white",cursor="hand2").place(x=360, y=150, height=30,width=150)
        btn_delete = Button(self.root, text="Удалить", command=self.delete,bg="red",fg="white",cursor="hand2").place(x=520, y=150, height=30,width=150)

        # ===employee details===

        cat_frame = Frame(self.root, bd=3)
        cat_frame.place(x=700, y=100, width=380, height=250)
        scrolly = Scrollbar(cat_frame, orient=VERTICAL)
        scrollx = Scrollbar(cat_frame, orient=HORIZONTAL)

        self.CategoryTable = ttk.Treeview(cat_frame, columns=("cid", "название"), yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)

        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.CategoryTable.xview)
        scrolly.config(command=self.CategoryTable.yview)

        self.CategoryTable.heading("cid", text="C ID")
        self.CategoryTable.heading("название", text="Название")
        self.CategoryTable["show"] = "headings"
        self.CategoryTable.column("cid", width=30)
        self.CategoryTable.column("название", width=250)
        self.CategoryTable.pack(fill=BOTH, expand=1)
        self.CategoryTable.bind("<ButtonRelease-1>", self.get_data)

        self.show()
#===================functions===========================

    def add(self):
        con = sqlite3.connect(database=r"diplom_project.db")
        cur = con.cursor()
        try:
            if self.var_name.get() == "":
                messagebox.showerror("Error", "Название категории должно быть заполнено", parent=self.root)
            else:
                cur.execute("SELECT * FROM category WHERE name=?", (self.var_name.get(),))
                row=cur.fetchone()
                if row != None:
                    messagebox.showerror("Error", "Ошибка. Данная категория уже существует, выберите другое название", parent=self.root)
                else:
                    cur.execute("Insert into category (name) values (?)",(self.var_name.get(),))
                    con.commit()
                    messagebox.showinfo("Успешно", "Категория успешно добавлена в базу",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Ошибка с {str(ex)}", parent=self.root)

    def show(self):
        con = sqlite3.connect(database=r"diplom_project.db")
        cur = con.cursor()
        try:
            cur.execute("select * from category")
            rows = cur.fetchall()
            self.CategoryTable.delete(*self.CategoryTable.get_children())
            for row in rows:
                self.CategoryTable.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Error", f"Ошибка с {str(ex)}", parent=self.root)

    def get_data(self, ev):
        f = self.CategoryTable.focus()
        content = (self.CategoryTable.item(f))
        row = content['values']
        self.var_cat_id.set(row[0])
        self.var_name.set(row[1])

    def delete(self):
        con = sqlite3.connect(database=r"diplom_project.db")
        cur = con.cursor()
        try:
            if self.var_cat_id.get() == "":
                messagebox.showerror("Error", "Выберите или введите категорию", parent=self.root)
            else:
                cur.execute("SELECT * FROM category WHERE cid=?", (self.var_cat_id.get(),))
                row=cur.fetchone()
                if row == None:
                    messagebox.showerror("Error", "Ошибка, попробуйте снова", parent=self.root)
                else:
                    op=messagebox.askyesno("Подтверждение", "Вы действительно хотите удалить запись?", parent=self.root)
                    if op==True:
                        cur.execute("delete from category where cid=?",(self.var_cat_id.get(),))
                        con.commit()
                        messagebox.showinfo("Удалить", "Данная категория успешно удалена", parent=self.root)
                        self.show()
                        self.var_cat_id.set("")
                        self.var_name.set("")
        except Exception as ex:
            messagebox.showerror("Error", f"Ошибка с {str(ex)}", parent=self.root)


if __name__=="__main__":
    root = Tk()
    obj = categoryClass(root)
    root.mainloop()