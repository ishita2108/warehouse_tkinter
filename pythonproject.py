#import modules
from tkinter import *
from tkinter import font
import tkinter.messagebox
import sqlite3
from PIL import Image, ImageTk

#Class for Front End UI (user interface)
class Product:
    def __init__(self,root):

        #create object reference/ instance of database class as p
        p = Database()
        p.conn()

        self.root = root
        self.root.title("WAREHOUSE INVENTORY SALES PURCHASE MANAGEMENT SYSTEM")
        self.root.geometry("1530x790")

        pId = StringVar()
        pName = StringVar()
        pPrice = StringVar()
        pQty = StringVar()
        pCompany = StringVar()
        pContact = StringVar()
        pDate = StringVar()

        '''Lets call the database method to perform database operations'''
        def close():
            print("Product : close method called")
            close = tkinter.messagebox.askyesno("WAREHOUSE INVENTORY SALES PURCHASE MANAGEMENT SYSTEM", "Are you sure you want to quit?")
            if close > 0:
                root.destroy()
                print("Product : close method finished")
                return

        def clear():
            print("Product : clear method called")
            self.txtpId.delete(0,END)
            self.txtpName.delete(0,END)
            self.txtpPrice.delete(0,END)
            self.txtpQty.delete(0,END)
            self.txtpCompany.delete(0,END)
            self.txtpContact.delete(0,END)
            self.txtpDate.delete(0,END)
            print("Product : clear method finished\n")

        def insert():
            print("Product : insert method called")
            if (len(pId.get()) != 0):
                p.insert(pId.get(), pName.get(), pPrice.get(), pQty.get(), pCompany.get(), pContact.get(), pDate.get())
                pList.delete(0,END)
                pList.insert(END,pId.get(), pName.get(), pPrice.get(), pQty.get(), pCompany.get(), pContact.get(), pDate.get())
                show()
            else:
                tkinter.messagebox.askyesno("WAREHOUSE INVENTORY SALES PURCHASE MANAGEMENT SYSTEM", "Enter all the fields")
            print("Product : inser method finished\n")

        def show():
            print("Product : show method called")
            pList.delete(0,END)
            for row in p.show():
                pList.insert(END,row,str(" "))
            print("Product : show method finished\n")

        #add to scroll bar
        def productRec(event):  #function to be called from scrollbar pList
            print("Product : productRec method called\n")
            global pd

            searchPd = pList.curselection()[0]
            pd = pList.get(searchPd)

            self.txtpId.delete(0,END)
            self.txtpId.insert(END, pd[0])

            self.txtpName.delete(0,END)
            self.txtpName.insert(END, pd[1])

            self.txtpPrice.delete(0,END)
            self.txtpPrice.insert(END, pd[2])

            self.txtpQty.delete(0,END)
            self.txtpQty.insert(END, pd[3])
            
            self.txtpCompany.delete(0,END)
            self.txtpCompany.insert(END, pd[4])

            self.txtpContact.delete(0,END)
            self.txtpContact.insert(END, pd[5])

            self.txtpDate.delete(0,END)
            self.txtpDate.insert(END, pd[6])

            print("Product : productRec method finished")

        def delete ():
            print("Product : delete method called")
            if (len(pId.get()) != 0):
                p.delete(pd[0])
                clear()
                show()
            print("Product : delete method finished\n")

        def search ():
            print("Product : search method called")
            pList.delete(0,END)
            for row in p.search(pId.get(), pName.get(), pPrice.get(), pQty.get(), pCompany.get(), pContact.get(), pDate.get()):
                pList.insert(END,row,str(" "))
            print("Product : search method finished")

        def update():
            print("Product : update method called")
            if (len(pId.get()) != 0):
                # print("pd[0]", pd[p])
                p.delete(pd[0])
                if(len(pId.get()) != 0):
                    p.insert(pId.get(), pName.get(), pPrice.get(), pQty.get(), pCompany.get(), pContact.get(), pDate.get())
                    pList.delete(0,END)
                pList.insert(END,(pId.get(), pName.get(), pPrice.get(), pQty.get(), pCompany.get(), pContact.get(), pDate.get()))
            print("Product : update method finished")

        # img = Image.open("images/background.jpg")
        # img = img.resize((1530,790),Image.ANTIALIAS)
        # self.photoimg = ImageTk.PhotoImage(img)

        # f_lbl = Label(self.root, image=self.photoimg)
        # f_lbl.place(x=0, y=0, width=1530, height=790)
    
        '''Create the frame'''
        MainFrame = Frame(self.root,bg="white")
        MainFrame.grid()

        #Title Frame
        HeadFrame = Frame(MainFrame, bd=1, padx=480, pady=10, bg="#281e5d", relief = RIDGE)
        HeadFrame.pack(side=TOP)
        self.ITitle = Label(HeadFrame, font=('Helvetica', 25,'bold'),fg='white', text='Warehouse Inventory Sales Purchase', bg='#281e5d')
        self.ITitle.grid()

        #Operation Frame
        OperationFrame = Frame(MainFrame, bd=2, width=1535, height=60, padx=50, pady=20,bg='white', relief=RIDGE)
        OperationFrame.pack(side=BOTTOM)

        #Body Frame
        BodyFrame = Frame(MainFrame, bd=2, width=1535, height=700, padx=50, pady=20,bg='#fff', relief=RIDGE)
        BodyFrame.pack(side=BOTTOM)

        #LeftBody
        LeftBodyFrame = LabelFrame(BodyFrame, bd=2, width=700, height=400, padx=20, pady=10,bg='white', font=('Helvetica', 15,'bold') ,relief=RIDGE, text='Products Detail')
        LeftBodyFrame.pack(side=LEFT)

        #Right
        RightBodyFrame = LabelFrame(BodyFrame, bd=2, width=400, height=400, padx=20, pady=10,bg='white', font=('Helvetica', 15,'bold') ,relief=RIDGE, text='Products Info')
        RightBodyFrame.pack(side=RIGHT)

        '''Add the widgets to the LeftBodyFrame'''
        self.labelpId = Label(LeftBodyFrame, bd=2, font=('Helvetica', 15,'bold'),text="Product Id",pady=5, padx=2, fg="black", bg="white")
        self.labelpId.grid(row=0, column=0,sticky=W)
        self.txtpId = Entry(LeftBodyFrame,font=('Helvetica', 20,'bold'), textvariable=pId, width=35 )
        self.txtpId.grid(row=0, column=1,sticky=W)

        self.labelpName = Label(LeftBodyFrame, bd=2, font=('Helvetica', 15,'bold'),text="Product Name", padx=2, pady=6, fg="black",bg="white")
        self.labelpName.grid(row=1, column=0,sticky=W)
        self.txtpName = Entry(LeftBodyFrame,font=('Helvetica', 20,'bold'), textvariable=pName, width=35 )
        self.txtpName.grid(row=1, column=1,sticky=W)

        self.labelpPrice = Label(LeftBodyFrame, bd=2, font=('Helvetica', 15,'bold'),text="Product Price", padx=2,pady=5, fg="black",bg="white")
        self.labelpPrice.grid(row=2, column=0,sticky=W)
        self.txtpPrice = Entry(LeftBodyFrame,font=('Helvetica', 20,'bold'), textvariable=pPrice, width=35 )
        self.txtpPrice.grid(row=2, column=1,sticky=W)

        self.labelpQty = Label(LeftBodyFrame, bd=2, font=('Helvetica', 15,'bold'),text="Product Qty", padx=2,pady=5, fg="black",bg="white")
        self.labelpQty.grid(row=3, column=0,sticky=W)
        self.txtpQty = Entry(LeftBodyFrame,font=('Helvetica', 20,'bold'), textvariable= pQty, width=35 )
        self.txtpQty.grid(row=3, column=1,sticky=W)

        self.labelpCompany = Label(LeftBodyFrame, bd=2, font=('Helvetica', 15,'bold'),text="Mfg Comp", padx=2,pady=5, fg="black",bg="white")
        self.labelpCompany.grid(row=4, column=0,sticky=W)
        self.txtpCompany = Entry(LeftBodyFrame,font=('Helvetica', 20,'bold'), textvariable=pCompany, width=35 )
        self.txtpCompany.grid(row=4, column=1,sticky=W)

        self.labelpContact = Label(LeftBodyFrame, bd=2, font=('Helvetica', 15,'bold'),text="Contact", padx=2, pady=5,fg="black",bg="white")
        self.labelpContact.grid(row=5, column=0,sticky=W)
        self.txtpContact = Entry(LeftBodyFrame,font=('Helvetica', 20,'bold'), textvariable=pContact, width=35 )
        self.txtpContact.grid(row=5, column=1,sticky=W)

        self.labelpDate = Label(LeftBodyFrame, bd=2, font=('Helvetica', 15,'bold'),text="Date", padx=2, pady=5,fg="black",bg="white")
        self.labelpDate.grid(row=6, column=0,sticky=W)
        self.txtpDate = Entry(LeftBodyFrame,font=('Helvetica', 20,'bold'), textvariable=pDate, width=35 )
        self.txtpDate.grid(row=6, column=1,sticky=W)

        self.labelpC1 = Label(LeftBodyFrame,padx=2, pady=5)
        self.labelpC1.grid(row=7, column=1,sticky=W)

        self.labelpC2 = Label(LeftBodyFrame,padx=2, pady=5)
        self.labelpC2.grid(row=8, column=1,sticky=W)

        self.labelpC3 = Label(LeftBodyFrame,padx=2, pady=5)
        self.labelpC3.grid(row=9, column=1,sticky=W)

        '''Scroll Bar'''
        scroll = Scrollbar(RightBodyFrame)
        scroll.grid(row=0,column=1, sticky='ns')

        #List Box
        pList = Listbox(RightBodyFrame, width=40, height=16, font=('Helvetica',12, 'bold'), yscrollcommand=scroll.set)

        #Call above created productRec function
        pList.bind('<<ListboxSelect>>', productRec)
        pList.grid(row=0, column=0, padx=8)
        scroll.config(command=pList.yview)

        '''Buttons to operation frame'''
        self.buttonSave = Button(OperationFrame, bg='#281e5d', fg="white", text="Save", font=('Helvetica',15, 'bold'), height= 1, width=13, bd=4, command=insert)
        self.buttonSave.grid(row=0,column=0)

        self.buttonShow = Button(OperationFrame, bg='#281e5d', fg="white", text="Show", font=('Helvetica',15, 'bold'), height= 1, width=13, bd=4, command=show)
        self.buttonShow.grid(row=0,column=1)

        self.buttonClear = Button(OperationFrame, bg='#281e5d', fg="white", text="Clear", font=('Helvetica',15, 'bold'), height= 1, width=13, bd=4, command=clear)
        self.buttonClear.grid(row=0,column=2)

        self.buttonDelete = Button(OperationFrame, bg='#281e5d', fg="white", text="Delete", font=('Helvetica',15, 'bold'), height= 1, width=13, bd=4, command=delete)
        self.buttonDelete.grid(row=0,column=3)

        self.buttonSearch = Button(OperationFrame, bg='#281e5d', fg="white", text="Search", font=('Helvetica',15, 'bold'), height= 1, width=13, bd=4, command=search)
        self.buttonSearch.grid(row=0,column=4)

        self.buttonUpdate = Button(OperationFrame, bg='#281e5d', fg="white", text="Update", font=('Helvetica',15, 'bold'), height= 1, width=13, bd=4, command=update)
        self.buttonUpdate.grid(row=0,column=5)

        self.buttonClose = Button(OperationFrame, bg='#281e5d', fg="white", text="Close", font=('Helvetica',15, 'bold'), height= 1, width=13, bd=4, command=close)
        self.buttonClose.grid(row=0,column=6)
        
#Backend Database Operations
class Database:
    def conn(self):
        print("Database: Connection Method called")
        con = sqlite3.connect("warehouse.db")
        cur = con.cursor()
        query = "create table if not exists product(pid integer primary key, pname text, price text, qty text, company text, contact text, date text)"
        cur.execute(query)
        con.commit()
        con.close()
        print("Database: Connection Method finished\n")

    def insert(self, pid,name,price,qty,company,contact,date):
        print("Database: Insert Method called")
        con = sqlite3.connect("warehouse.db")
        cur = con.cursor()
        query = "insert into product values(?,?,?,?,?,?,?)"
        cur.execute(query,(pid,name,price,qty,company,contact,date))
        con.commit()
        con.close()
        print("Database: Insert Method finished\n")

    def show(self):
        print("Database: Show Method called")
        con = sqlite3.connect("warehouse.db")
        cur = con.cursor()
        query = "select * from product"
        cur.execute(query)
        rows = cur.fetchall()
        con.close()
        print("Database: Show Method finished\n")
        return rows

    def delete(self,pid):
        print("Database: Delete Method called", pid)
        con = sqlite3.connect("warehouse.db")
        cur = con.cursor()
        cur.execute("delete from product where pid=?" , (pid,))
        con.commit()
        con.close()
        print(pid, "Database: Delete Method finished\n")

    def search(self, pid="", name="", price="", qty="", company="", contact="", date=""):
        print("Database: Search Method called", pid)
        con = sqlite3.connect("warehouse.db")
        cur = con.cursor()
        cur.execute("select * from product where pid =? or pname=? or price=? or qty=? or company=? or contact=? or date=?",(pid,name,price,qty,company,contact,date))
        row = cur.fetchall()
        con.close()
        print(pid, "Database: Search Method finished\n")
        return row

    def update(self, pid='',name='',price='',qty='',company='',contact='',date=''):
        print("Database: Update Method called", pid)
        con = sqlite3.connect("warehouse.db")
        cur = con.cursor()
        query = "update product set pid=? or pname=? or  price=? or qty=? or company=? contact=? or date=? where pid=?" ,(pid,name,price,qty,company,contact,date,pid)
        cur.execute(query)
        con.commit()
        con.close()
        print(pid, "Database: Update Method finished\n")




if __name__ =='__main__':
    root = Tk()
    application = Product(root)
    root.mainloop()