from tkinter import *
from PIL import Image, ImageTk
from employee import employeeClass
from supplier import  supplierClass
from category import  categoryClass
from product import productClass
class IMS:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1680x800+0+0")
        self.root.title("Система управления для компании ООО Тесла")
        self.root.config(bg="white")

        #===title===
        title = Label(self.root,text="Система управления для компании ООО Тесла", 
                    font=("Verdana", 30, "bold"), bg="#694717", fg="white").place(x=0, y=0, relwidth=1, height=70)
        btn_logout = Button(self.root, text="Выйти", font=("Verdana", 13, "bold"), bg="white", fg="#694717").place(x=1400, y=10, height=30, width=150)
        
        #===left-menu===
        self.MenuLogo = Image.open("logo.png")
        self.MenuLogo = self.MenuLogo.resize((200,200), Image.ANTIALIAS)
        self.MenuLogo=ImageTk.PhotoImage(self.MenuLogo)

        LeftMenu = Frame(self.root, bd = 2, relief=RIDGE,bg="white")
        LeftMenu.place(x=0, y=70, width=300, height=730)

        lbl_menuLogo = Label(LeftMenu,image=self.MenuLogo)
        lbl_menuLogo.pack(side=TOP,fill=X)

        lbl_menu = Label(LeftMenu, text="Меню", font=("Verdana", 13, "bold"), bg="#fae6b4", fg="#694717").pack(side=TOP,fill=X)
        btn_emoloyee = Button(LeftMenu, text="Сотрудники", command=self.employee,font=("Verdana", 13), bg="white", fg="#694717",bd=3, cursor="hand2", height=4).pack(side=TOP,fill=X)
        btn_supplier = Button(LeftMenu, text="Поставщики", command=self.supplier, font=("Verdana", 13), bg="white", fg="#694717", bd=3, cursor="hand2", height=4).pack(side=TOP, fill=X)
        #projects instead of suplieers
        btn_category = Button(LeftMenu, text="Категории", command=self.category, font=("Verdana", 13), bg="white", fg="#694717",bd=3,cursor="hand2", height=4).pack(side=TOP,fill=X)
        btn_product = Button(LeftMenu, text="Товары", command=self.product, font=("Verdana", 13), bg="white", fg="#694717",bd=3,cursor="hand2", height=4).pack(side=TOP,fill=X)
        btn_sales = Button(LeftMenu, text="Продажи", font=("Verdana", 13), bg="white", fg="#694717",bd=3,cursor="hand2", height=4).pack(side=TOP,fill=X)

        #===content===
        self.lbl_employee = Label(self.root, text="Все сотрудники\n[ 0 ]", bd=5, bg="#694717",fg="white", font=("Lineyka Regular", 20))
        self.lbl_employee.place(x=500, y=120, height=150, width=300)

        self.lbl_projects = Label(self.root, text="Все проекты\n[ 0 ]", bd=5, bg="#694717", fg="white",
                                  font=("Lineyka Regular", 20))
        self.lbl_projects.place(x=850, y=120, height=150, width=300)

        self.lbl_category = Label(self.root, text="Все категории\n[ 0 ]", bd=5, bg="#694717", fg="white",
                                  font=("Lineyka Regular", 20))
        self.lbl_category.place(x=500, y=300, height=150, width=300)

        self.lbl_sales = Label(self.root, text="Все скидки\n[ 0 ]", bd=5, bg="#694717", fg="white",
                                  font=("Lineyka Regular", 20))
        self.lbl_sales.place(x=850, y=300, height=150, width=300)


        #===footer===
        lbl_footer = Label(self.root,text="Система управления бизнес-процессами предприятия ООО ТЕСТА | Разработчик: Разумова Е.В.",
                           font=("Verdana", 13), bg="white", fg="grey").pack(side=BOTTOM, fill=X)
#===============================================

    def employee(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = employeeClass(self.new_win)

    def supplier(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = supplierClass(self.new_win)
    def category(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = categoryClass(self.new_win)

    def product(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = productClass(self.new_win)

if __name__=="__main__":
    root=Tk()
    obj=IMS(root)
    root.mainloop()