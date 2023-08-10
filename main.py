# harri
# Main UI for Cable Management system
# 25.7.23 - __.__.23
 
import customtkinter
import fileDatabase

# usrName = input('what is a name ?? ')
# usrDesc = input('descption ?!?! ' )
# usrLength = input('pick a length plss ')
# usrQuant = input('how many !?! ')
# usrLocate = input('where is it ?! ')

db = fileDatabase.SQLDatabase()
# db.addCable({'name': f"{usrName}", 'description': f"{usrDesc}", 'length': float(usrLength), 'quantity': int(usrQuant), 'location': f"{usrLocate}"})


class ScrollingCables(customtkinter.CTkScrollableFrame):
    def __init__(self, master, title, height):
        super().__init__(master, label_text=title, height=height)
        self.grid_columnconfigure(0, weight=1)

        cables = db.getCables()

        def cableUpdate():
            for i, cable in enumerate(cables):
                self.cableName = customtkinter.CTkLabel(self, text=cable[0], width=20)
                self.cableName.grid(row=i, column=0, sticky='w')

                self.cableLength = customtkinter.CTkLabel(self, text=cable[1])
                self.cableLength.grid(row=i, column=1, sticky='w')

                self.cableDesc = customtkinter.CTkLabel(self, text=cable[2])
                self.cableDesc.grid(row=i, column=2, sticky='w') 

                self.cableQuant = customtkinter.CTkLabel(self, text=cable[3])
                self.cableQuant.grid(row=i, column=3, sticky='w')

                self.cableLoc = customtkinter.CTkLabel(self, text=cable[4])
                self.cableLoc.grid(row=i, column=4, sticky='w')
        cableUpdate()

        #print(db.getCables())
        #print('where is this maent to be')

class HeaderFrame(customtkinter.CTkFrame):
    def __init__(self, master, bg_color):
        super().__init__(master)
        self.grid_columnconfigure(0, weight=1)

        self.lblTitle = customtkinter.CTkLabel(self, text='Duffinator_CableManager7014')
        self.lblTitle.grid(row=0, column=0, padx=(10, 0), sticky='w')

        def btnCallBack():
            AddCableFrame()    
            
        self.btnAddCable = customtkinter.CTkButton(self, text='Add Cable', command=btnCallBack)
        self.btnAddCable.grid(row=1, column=0, padx=(10, 0))

        self.userSearch = customtkinter.CTkEntry(self, placeholder_text='search')
        self.userSearch.grid(row=0, column=1, padx=(10,0))

        self.lblSort = customtkinter.CTkLabel(self, text='sort:')
        self.lblSort.grid(row=0, column=2, padx=(10, 0))

        self.optionSort = customtkinter.CTkOptionMenu(self, values=['option', 'date ^', 'date v', 'length ^', 'length v'])
        self.optionSort.grid(row=0, column=3, padx=(10,0))

class AddCableFrame(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title('Add Cable')
        self.geometry('300x540')
        self.grid_columnconfigure(0, weight=1)

        self.lblTitle = customtkinter.CTkLabel(self, text='Add Cable?')
        self.lblTitle.grid(row=0, column=0, columnspan=100, padx=(10,10), pady=(10,10), sticky='we')

        self.lblName = customtkinter.CTkLabel(self, text='name:')
        self.lblName.grid(row=1, column=0, padx=(10,0), pady=(5,5))

        self.inputName = customtkinter.CTkEntry(self, width=200, placeholder_text='i.e. Type C')
        self.inputName.grid(row=1, column=1, padx=(10,5), pady=(5,5))

        self.lblLength = customtkinter.CTkLabel(self, text='length:')
        self.lblLength.grid(row=2, column=0, padx=(10,0), pady=(5,5))

        self.inputLength = customtkinter.CTkEntry(self)
        self.inputLength.grid(row=2, column=1, padx=(10,0), pady=(5,5))

        self.lblQuant = customtkinter.CTkLabel(self, text='quantity:')
        self.lblQuant.grid(row=3, column=0, padx=(10,0), pady=(5,5))

        self.inputQuant = customtkinter.CTkEntry(self)
        self.inputQuant.grid(row=3, column=1, padx=(10,0), pady=(5,5))

        self.lblDesc = customtkinter.CTkLabel(self, text='description:')
        self.lblDesc.grid(row=4, column=0, padx=(10,0), pady=(5,5))

        self.inputDesc = customtkinter.CTkEntry(self)
        self.inputDesc.grid(row=4, column=1, padx=(10,0), pady=(5,5))

        self.lblLocate = customtkinter.CTkLabel(self, text='location:')
        self.lblLocate.grid(row=5, column=0, padx=(10,0), pady=(5,5))

        self.inputLocate = customtkinter.CTkEntry(self)
        self.inputLocate.grid(row=5, column=1, padx=(10,0), pady=(5,5))

        self.addBtn = customtkinter.CTkButton(self, text='Add Cable', command=self.cableAdd)
        self.addBtn.grid(row=6, column=0, columnspan=100, padx=(5,5))
    
def cableAdd(self):
        usrName = self.inputName.get()
        usrDesc = self.inputDesc.get()
        usrLength = self.inputLength.get()
        usrQuant = self.inputQuant.get()
        usrLocate = self.inputLocate.get()
        
        db.addCable({'name': f"{usrName}", 'description': f"{usrDesc}", 'length': float(usrLength), 'quantity': int(usrQuant), 'location': f"{usrLocate}"})
        
        test = ScrollingCables()
        test.cableUpdate()

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title('Duffinator_CableManager7014')
        self.geometry('960x540')
        self.grid_columnconfigure(0, weight=1)
        # self.grid_rowconfigure(0, weight=1)

        self.appHeader = HeaderFrame(self, bg_color='green')
        self.appHeader.grid(row=0, column=0, padx=(10, 10), pady=(10, 0), sticky='nsew')

        self.scrollingCables = ScrollingCables(self, title='test', height=400)
        self.scrollingCables.grid(row=1, column=0, padx=(10, 10), pady=(10, 0), sticky='nsew')

        db.sortCable()


# class 


app = App()
app.mainloop()