from tkinter import *

import tkinter.messagebox
from tkinter import messagebox as ms
import sqlite3

with sqlite3.connect('quit.db') as db:
    c = db.cursor()

c.execute('CREATE TABLE IF NOT EXISTS user (username TEXT NOT NULL PRIMARY KEY,password TEX NOT NULL);')
db.commit()
db.close()


#main Class
class main:
    def __init__(self,master):
    	# Window 
        self.master = master
        self.master.title("Login page")
        # Some Usefull variables
        self.username = StringVar()
        self.password = StringVar()
        self.n_username = StringVar()
        self.n_password = StringVar()
        #Create Widgets
        self.widgets()

    #Login Function
    def login(self):
    	#Establish Connection
        with sqlite3.connect('quit.db') as db:
            c = db.cursor()

        #Find user If there is any take proper action
        find_user = ('SELECT * FROM user WHERE username = ? and password = ?')
        c.execute(find_user,[(self.username.get()),(self.password.get())])
        result = c.fetchall()
        if result:
            croot = Tk()
            crimify = Crime(croot)
            croot.mainloop()
            
        else:
            ms.showerror('Oops!','Username Not Found.')
            
    def new_user(self):
    	#Establish Connection
        with sqlite3.connect('quit.db') as db:
            c = db.cursor()

        #Find Existing username if any take proper action
        find_user = ('SELECT username FROM user WHERE username = ?')
        c.execute(find_user,[(self.n_username.get())])        
        if c.fetchall():
            ms.showerror('Error!','Username Taken Try a Diffrent One.')
        else:
            ms.showinfo('Success!','Account Created!')
            self.log()
        #Create New Account 
        insert = 'INSERT INTO user(username,password) VALUES(?,?)'
        c.execute(insert,[(self.n_username.get()),(self.n_password.get())])
        db.commit()

        #Frame Packing Methords
    def log(self):
        self.username.set('')
        self.password.set('')
        self.crf.pack_forget()
        self.head['text'] = 'LOGIN'
        self.logf.pack()
    def cr(self):
        self.n_username.set('')
        self.n_password.set('')
        self.logf.pack_forget()
        self.head['text'] = 'Create Account'
        self.crf.pack()
        
    #Draw Widgets
    def widgets(self):
        self.head = Label(self.master,text = 'LOGIN',font = ('',35),pady = 10)
        self.head.pack()
        self.logf = Frame(self.master,padx =10,pady = 10)
        Label(self.logf,text = 'Username: ',font = ('',20),pady=5,padx=5).grid(sticky = W)
        Entry(self.logf,textvariable = self.username,bd = 5,font = ('',15)).grid(row=0,column=1)
        Label(self.logf,text = 'Password: ',font = ('',20),pady=5,padx=5).grid(sticky = W)
        Entry(self.logf,textvariable = self.password,bd = 5,font = ('',15),show = '*').grid(row=1,column=1)
        Button(self.logf,text = ' Login ',bd = 3 ,font = ('',15),padx=5,pady=5,command=self.login).grid()
        Button(self.logf,text = ' Create Account ',bd = 3 ,font = ('',15),padx=5,pady=5,command=self.cr).grid(row=2,column=1)
        self.logf.pack()
        
        self.crf = Frame(self.master,padx =10,pady = 10)
        Label(self.crf,text = 'Username: ',font = ('',20),pady=5,padx=5).grid(sticky = W)
        Entry(self.crf,textvariable = self.n_username,bd = 5,font = ('',15)).grid(row=0,column=1)
        Label(self.crf,text = 'Password: ',font = ('',20),pady=5,padx=5).grid(sticky = W)
        Entry(self.crf,textvariable = self.n_password,bd = 5,font = ('',15),show = '*').grid(row=1,column=1)
        Button(self.crf,text = 'Create Account',bd = 3 ,font = ('',15),padx=5,pady=5,command=self.new_user).grid()
        Button(self.crf,text = 'Go to Login',bd = 3 ,font = ('',15),padx=5,pady=5,command=self.log).grid(row=2,column=1)
        







        
        
        
        
        
        


class Crime:
    def __init__(self,root):
        
        
        p = Database()
        p.conn()
        
        self.root = root
        self.root.title("CRIME RECORD MANAGEMENT SYSTEM")
        self.root.geometry("1325x690")
        self.root.config(bg="yellow")

        cId = StringVar()
        cName = StringVar()
        cStname = StringVar()
        cCrime = StringVar()
        cPlace=StringVar()
        cCitname=StringVar()
        
        
        
        def close():
            close =  tkinter.messagebox.askyesno("CRIME RECORD MANAGEMENT SYSTEM", "Are you sure?")
            if close>0:
                root.destroy()
                return 
                
                
                
        def clear():
            self.txtcID.delete(0,END)
            self.txtcName.delete(0,END)
            self.txtcStname.delete(0,END)
            self.txtcCrime.delete(0,END)
            self.txtcPlace.delete(0,END)
            self.txtcCitname.delete(0,END)
            
            
            
        def insert():
            if(len(cId.get())!=0):
                p.insert(cId.get(),cName.get(), cStname.get(), cCrime.get(), cPlace.get(), cCitname.get())
                
                crimeList.delete(0,END)
                crimeList.insert(END,cId.get(),cName.get(), cStname.get(), cCrime.get(), cPlace.get(), cCitname.get())
                showlist()
                
            else:
                tkinter.messagebox.askyesno("CRIME RECORD MANAGEMENT SYSTEM", "Enter Crime ID atleast")
                
                
                
                
                
        def showlist():
            crimeList.delete(0,END)
            for row in p.show():
                crimeList.insert(END,row,str(""))
                
                
                
        def crimerec(event):
            global cd
            
            searchPd = crimeList.curselection()[0]
            cd = crimeList.get(searchPd)
            
            self.txtcID.delete(0,END)
            self.txtcID.insert(END,cd[0])
            
            self.txtcName.delete(0,END)
            self.txtcName.insert(END,cd[1])
            
            self.txtcStname.delete(0,END)
            self.txtcStname.insert(END,cd[2])
            
            self.txtcCrime.delete(0,END)
            self.txtcCrime.insert(END,cd[3])
            
            self.txtcPlace.delete(0,END)
            self.txtcPlace.insert(END,cd[4])
            
            self.txtcCitname.delete(0,END)
            self.txtcCitname.insert(END,cd[5])
            
            
            
        def delete():
            if(len(cId.get())!=0):
                p.delete(cd[0])
                clear()
                showlist()
            
            
            
        def search():
            crimeList.delete(0,END)
            for row in p.search(cId.get(),cName.get(), cStname.get(), cCrime.get(), cPlace.get(), cCitname.get()):
                crimeList.insert(END,row,str(""))
                
                
                
        def update():
            if(len(cId.get())!=0):
                p.delete(pd[0])
            if(len(cId.get())!=0):
                p.insert(cId.get(),cName.get(), cStname.get(), cCrime.get(), cPlace.get(), cCitname.get())
                crimeList.delete(0,END)
            crimeList.insert(END,(cId.get(),cName.get(), cStname.get(), cCrime.get(), cPlace.get(), cCitname.get()))
            
            
            
            
            

        
        MainFrame=Frame(self.root,bg="red")
        MainFrame.grid()
        
        HeadFrame = Frame(MainFrame, bd=1,padx=1, pady=1, bg="white",relief=RIDGE)
        
        HeadFrame.pack(side=TOP)
        
        self.ITitle = Label(HeadFrame, font = ('arial',50 ,'bold'), fg = 'blue', text = "CRIME RECORD MANAGEMENT SYSTEM", bg="white")
        
        self.ITitle.grid()
        
        
        OperationFrame = Frame(MainFrame,bd=2,width=1300,height=60,padx=50,pady=20, bg="white",relief=RIDGE)
        
        OperationFrame.pack(side=BOTTOM)

        BodyFrame = Frame(MainFrame,bd=2,width=1290,height=400,padx=30,pady=20, bg="white",relief=RIDGE)
        
        BodyFrame.pack(side=BOTTOM)
        
        LeftBodyFrame = LabelFrame(BodyFrame,bd=2,width=600,height=380,padx=20,pady=10, bg="yellow",relief=RIDGE, font=('arial', 15, 'bold'),
       text = 'CRIME DETAIL:')

        LeftBodyFrame.pack(side=LEFT)
        
        RightBodyFrame = LabelFrame(BodyFrame,bd=2,width=400,height=380,padx=20,pady=10, bg="yellow",relief=RIDGE, font=('arial', 15, 'bold'),
         text = 'Crime Information:')

        RightBodyFrame.pack(side=RIGHT)




        self.labelcID=Label(LeftBodyFrame, font=('arial', 15, 'bold'), text="Crime ID",padx=2, pady=2, bg="white", fg="blue")

        self.labelcID.grid(row=0,column=0,sticky=W)

        self.txtcID = Entry(LeftBodyFrame, font=('arial', 20, 'bold'), textvariable=cId, width=35)

        self.txtcID.grid(row=0, column=1, sticky=W)





        self.labelcName=Label(LeftBodyFrame, font=('arial', 15, 'bold'), text="Criminal Name",padx=2, pady=2, bg="white", fg="blue")

        self.labelcName.grid(row=1,column=0,sticky=W)

        self.txtcName = Entry(LeftBodyFrame, font=('arial', 20, 'bold'), textvariable=cName, width=35)

        self.txtcName.grid(row=1, column=1, sticky=W)





        self.labelcStname=Label(LeftBodyFrame, font=('arial', 15, 'bold'), text="Station Name",padx=2, pady=2, bg="white", fg="blue")

        self.labelcStname.grid(row=2,column=0,sticky=W)

        self.txtcStname = Entry(LeftBodyFrame, font=('arial', 20, 'bold'), textvariable=cStname, width=35)

        self.txtcStname.grid(row=2, column=1, sticky=W)




        self.labelcCrime=Label(LeftBodyFrame, font=('arial', 15, 'bold'), text="Crime",padx=2, pady=2, bg="white", fg="blue")

        self.labelcCrime.grid(row=3,column=0,sticky=W)

        self.txtcCrime = Entry(LeftBodyFrame, font=('arial', 20, 'bold'), textvariable=cCrime, width=35)

        self.txtcCrime.grid(row=3, column=1, sticky=W)



        self.labelcPlace=Label(LeftBodyFrame, font=('arial', 15, 'bold'), text="Crime Place",padx=2, pady=2, bg="white", fg="blue")

        self.labelcPlace.grid(row=4,column=0,sticky=W)

        self.txtcPlace = Entry(LeftBodyFrame, font=('arial', 20, 'bold'), textvariable=cPlace, width=35)

        self.txtcPlace.grid(row=4, column=1, sticky=W)



        self.labelcCitname=Label(LeftBodyFrame, font=('arial', 15, 'bold'), text="Citizen Name",padx=2, pady=2, bg="white", fg="blue")

        self.labelcCitname.grid(row=5,column=0,sticky=W)

        self.txtcCitname = Entry(LeftBodyFrame, font=('arial', 20, 'bold'), textvariable=cCitname, width=35)

        self.txtcCitname.grid(row=5, column=1, sticky=W)
        
        
        self.labelcCitnameC1=Label(LeftBodyFrame, padx=2, pady=2)

        self.labelcCitnameC1.grid(row=6,column=0,sticky=W)
        
        self.labelcCitnameC2=Label(LeftBodyFrame, padx=2, pady=2)

        self.labelcCitnameC2.grid(row=7,column=0,sticky=W)
        
        self.labelcCitnameC3=Label(LeftBodyFrame, padx=2, pady=2)

        self.labelcCitnameC3.grid(row=8,column=0,sticky=W)
        
        self.labelcCitnameC4=Label(LeftBodyFrame, padx=2, pady=2)

        self.labelcCitnameC4.grid(row=9,column=0,sticky=W)
        
        
        scroll = Scrollbar(RightBodyFrame)
        scroll.grid(row=0, column=1, sticky='ns')
        
        
        
        
        crimeList = Listbox(RightBodyFrame, width=40, height=16, font=('arial', 12, 'bold'), yscrollcommand = scroll.set)
        
        crimeList.bind('<<ListboxSelect>>', crimerec)
        
        crimeList.grid(row=0, column=0,padx=8)
        
        scroll.config(command=crimeList.yview)
        
        
        
        
        self.buttonSaveData =  Button(OperationFrame, text = "Save", font=('arial', 18, 'bold'), height = 1, width=10,bd=4,command=insert)
        self.buttonSaveData.grid(row=0,column=0)
        
        self.buttonShowData =  Button(OperationFrame, text = "Show", font=('arial', 18, 'bold'), height = 1, width=10,bd=4, command=showlist)
        self.buttonShowData.grid(row=0,column=1)
        
        self.buttonClear =  Button(OperationFrame, text = "Clear", font=('arial', 18, 'bold'), height = 1, width=10,bd=4, command=clear)
        self.buttonClear.grid(row=0,column=4)
        
        self.buttonDelete =  Button(OperationFrame, text = "Delete", font=('arial', 18, 'bold'), height = 1, width=10,bd=4,command=delete)
        self.buttonDelete.grid(row=0,column=5)
        
        self.buttonSearch =  Button(OperationFrame, text = "Search", font=('arial', 18, 'bold'), height = 1, width=10,bd=4,command=search)
        self.buttonSearch.grid(row=0,column=2)
        
        self.buttonUpdate =  Button(OperationFrame, text = "Update", font=('arial', 18, 'bold'), height = 1, width=10,bd=4)
        self.buttonUpdate.grid(row=0,column=3)
        
        self.buttonClose =  Button(OperationFrame, text = "Close", font=('arial', 18, 'bold'), height = 1, width=10,bd=4,command=close)
        self.buttonClose.grid(row=0,column=6)
        
        
        
        
        

        
        
        
        
class Database:
    def conn(self):
        print("Database: Connection method called")
        con = sqlite3.connect("inventory.db")
        cur = con.cursor()
        query = "create table if not exists crime(cId integer primary key,cName text, cStname text, cCrime text, cPlace text, cCitname text)"
        cur.execute(query)
        con.commit()
        con.close()
        print("Database: Connection method finished\n")
        
        
    def insert(self, cId, cName, cStname, cCrime, cPlace, cCitname):
        print("Database: Insert method called")
        con = sqlite3.connect("inventory.db")
        cur = con.cursor()
        query =  "insert into crime values(?,?,?,?,?,?)"
        cur.execute(query, (cId,cName,cStname,cCrime,cPlace,cCitname))
        con.commit()
        con.close()
        print("Database: Insert method finished\n")
        
        
    def show(self):
        print("Database: Show method called")
        con = sqlite3.connect("inventory.db")
        cur = con.cursor()
        query = "select * from crime"
        cur.execute(query)
        rows = cur.fetchall()
        con.close()
        print("Database: Show method finished\n")
        return rows
    
    
    
    
    def delete(self,cId):
        print("Database: Delete method called", cId)
        con = sqlite3.connect("inventory.db")
        cur = con.cursor()
        cur.execute("delete from crime where cId =?", (cId,))
        con.commit()
        con.close()
        print(cId, "Database: Delete method finished\n")
        
        
    def search(self,cId="", cName="", cStname="", cCrime="", cPlace="", cCitname=""):
        print("Database: Search method called")
        con = sqlite3.connect("inventory.db")
        cur = con.cursor()
        cur.execute("select * from crime where cId=? or cName=? or cStname=? or cCrime=? or cCitname=? or cPlace=?",(cId,cName,cStname,cCrime,cPlace,cCitname))
        row = cur.fetchall()
        con.close()
        print("Database: Search method finished")
        return row
    
    
    
    
    def update(self,cId="", cName="", cStname="", cCrime="", cPlace="", cCitname=""):
        print("Database: Update method called")
        con = sqlite3.connect("inventory.db")
        cur = con.cursor()
        cur.execute("update crime set cId=? or cName=? or cStname=? or cCrime=? or cPlace=? or cCitname=? where cId=?",(cId, cName, cStname, cCrime, cPlace, cCitname,cId))
        con.commit()
        con.close()
        print(cId, "Database: Update method finished\n")
        
        

        
        
        
            
        
        
        
        
        
        
        
        
        
          
 
if __name__== '__main__':
    root = Tk()
    application = main(root)
    root.mainloop()
    
    
    
