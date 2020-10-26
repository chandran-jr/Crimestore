class Product:
    def __init__(self,root):
        
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
        
        
        
        

        

        
        
 
if __name__== '__main__':
    root = Tk()
    application = Product(root)
    root.mainloop()
