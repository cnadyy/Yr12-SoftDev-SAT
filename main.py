# harri
# Main UI for Cable Management system
# 25.7.23 - 15.8.23

import customtkinter
import fileDatabase

db = fileDatabase.SQLDatabase()


class ScrollingCables(customtkinter.CTkScrollableFrame):
    def __init__(self, master, height, title):
        super().__init__(master, label_text=title, height=height)
        self.grid_columnconfigure(0, weight=1)
        
        # using information in file system, creates an enumerated list displaying all information from SQLite system
        def cableUpdate(self):
            cables = db.getCables()
            self.update = 0
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
                
                self.update += 1
        cableUpdate(self)
        
    def updateUI(self):
        rows = self.winfo_children()

        frameAdd = AddCableFrame()
        
        frameAdd.destroy()
        # iterates through existing rows generated and destroys each label, then calls cableUpdate() and recreates display. .destroy() as of current does not work, resulting in no update to UI upon adding a cable
        for row in rows:
            # self.row.destroy()
            self.cableName.destroy()
            self.cableLength.destroy()
            self.cableDesc.destroy()
            self.cableQuant.destroy()
            self.cableLoc.destroy()
        # cableUpdate(self) - does not call function

# new frame for the 'header' / top bar of main UI
class HeaderFrame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)

        # self.lblTitle = customtkinter.CTkLabel(self, text='Duffinator_CableManager7014')
        # self.lblTitle.grid(row=0, column=0, padx=(10, 0), sticky='w')

        # opens AddCable Frame to allow user to add information
        def addCallBack():
            AddCableFrame()    
        def editCallBack():
            self.btnEditCable.configure(text='Unavailable', fg_color='red')
        def deleteCallBack():
            self.btnDeleteCable.configure(text='Unavailable', fg_color='red')

        self.lblTitle = customtkinter.CTkLabel(self, text='Really Cool Logo')
        self.lblTitle.grid(row=0, column=0, padx=(10, 0), sticky='w')
            
        self.btnAddCable = customtkinter.CTkButton(self, text='Add Cable', command=addCallBack)
        self.btnAddCable.grid(row=1, column=0, padx=(10, 0), pady=(10, 10), sticky='w')

        self.btnEditCable = customtkinter.CTkButton(self, text='Edit Cable', command=editCallBack)
        self.btnEditCable.grid(row=1, column=1, padx=(10, 0), pady=(10, 10), sticky='w')

        self.btnDeleteCable = customtkinter.CTkButton(self, text='Delete Cable', command=deleteCallBack)
        self.btnDeleteCable.grid(row=1, column=2, padx=(10, 0), pady=(10, 10), sticky='w')

        self.userSearch = customtkinter.CTkEntry(self, placeholder_text='search')
        self.userSearch.grid(row=0, column=1, padx=(10,0))

        self.lblSort = customtkinter.CTkLabel(self, text='sort:')
        self.lblSort.grid(row=0, column=2, padx=(10, 0))

        self.optionSort = customtkinter.CTkOptionMenu(self, values=['option', 'date ^', 'date v', 'length ^', 'length v'])
        self.optionSort.grid(row=0, column=5, padx=(10,0))

# new pop-up frame, allows user input of information into file system through entry
class AddCableFrame(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title('Add Cable')
        self.geometry('300x300')
        self.grid_columnconfigure(0, weight=1)

        self.lblTitle = customtkinter.CTkLabel(self, text='Add Cable?')
        self.lblTitle.grid(row=0, column=0, columnspan=100, padx=(10,10), pady=(10,10), sticky='we')

        self.lblName = customtkinter.CTkLabel(self, text='name:')
        self.lblName.grid(row=1, column=0, padx=(10,0), pady=(5,5))

        self.inputName = customtkinter.CTkEntry(self, width=200, placeholder_text='i.e. Type C')
        self.inputName.grid(row=1, column=1, padx=(10,5), pady=(5,5))

        self.lblLength = customtkinter.CTkLabel(self, text='length:')
        self.lblLength.grid(row=2, column=0, padx=(10,0), pady=(5,5))

        self.inputLength = customtkinter.CTkEntry(self, width=200, placeholder_text='i.e. 1.2')
        self.inputLength.grid(row=2, column=1, padx=(10,0), pady=(5,5))

        self.lblQuant = customtkinter.CTkLabel(self, text='quantity:')
        self.lblQuant.grid(row=3, column=0, padx=(10,0), pady=(5,5))

        self.inputQuant = customtkinter.CTkEntry(self, width=200, placeholder_text='i.e. 3')
        self.inputQuant.grid(row=3, column=1, padx=(10,0), pady=(5,5))

        self.lblDesc = customtkinter.CTkLabel(self, text='description:')
        self.lblDesc.grid(row=4, column=0, padx=(10,0), pady=(5,5))

        self.inputDesc = customtkinter.CTkEntry(self, width=200, placeholder_text='i.e. Black Type C Cable')
        self.inputDesc.grid(row=4, column=1, padx=(10,0), pady=(5,5))

        self.lblLocate = customtkinter.CTkLabel(self, text='location:')
        self.lblLocate.grid(row=5, column=0, padx=(10,0), pady=(5,5))

        self.inputLocate = customtkinter.CTkEntry(self, width=200, placeholder_text='i.e. Server Room, Black Box')
        self.inputLocate.grid(row=5, column=1, padx=(10,0), pady=(5,5))

        self.addBtn = customtkinter.CTkButton(self, text='Add Cable', command=self.cableAdd)
        self.addBtn.grid(row=6, column=0, columnspan=100, padx=(5,5))
    
    # adds all information entered above, converts to appropriate data type & adds to the file system
    def cableAdd(self):
            usrName = self.inputName.get()
            usrDesc = self.inputDesc.get()
            usrLength = self.inputLength.get()
            usrQuant = self.inputQuant.get()
            usrLocate = self.inputLocate.get()

            #### TYPE VALIDATION & UPDATE ?
            try:
                db.addCable({'name': f"{usrName}", 'description': f"{usrDesc}", 'length': float(usrLength), 'quantity': int(usrQuant), 'location': f"{usrLocate}"})
                self.addBtn.configure(fg_color='green', text='Cable Added | Please Refresh Program')
            except:
                self.addBtn.configure(fg_color='red', text='Length / Quant Entry Error')

# base app, including all 'home' frames to be displayed
class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title('Duffinator_CableManager7014')
        self.geometry('960x540')
        self.grid_columnconfigure(0, weight=1)
        # self.grid_rowconfigure(0, weight=1)

        self.appHeader = HeaderFrame(self)
        self.appHeader.grid(row=0, column=0, padx=(10, 10), pady=(10, 0), sticky='nsew')

        self.scrollingCables = ScrollingCables(self, height=400, title='Name | Length | Description | Quantity | Location')
        self.scrollingCables.grid(row=1, column=0, padx=(10, 10), pady=(10, 0), sticky='nsew')

        db.sortCable()

app = App()
app.mainloop()