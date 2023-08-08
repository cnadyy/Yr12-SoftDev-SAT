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
    def __init__(self, master, title):
        super().__init__(master, label_text=title)
        self.grid_columnconfigure(0, weight=1)

        cables = db.getCables()
        
        print(cables)
        
        for i, cable in enumerate(cables):
            print(cable)
            cableName = customtkinter.CTkLabel(self, text=cable[0])
            cableName.grid(row=i, column=0, sticky='w')

            cableLength = customtkinter.CTkLabel(self, text=cable[1])
            cableLength.grid(row=i, column=1, sticky='w')

            cableDesc = customtkinter.CTkLabel(self, text=cable[2])
            cableDesc.grid(row=i, column=2, sticky='w') 

            cableQuant = customtkinter.CTkLabel(self, text=cable[3])
            cableQuant.grid(row=i, column=3, sticky='w')

            cableLoc = customtkinter.CTkLabel(self, text=cable[4])
            cableLoc.grid(row=i, column=4, sticky='w')

        #print(db.getCables())
        #print('where is this maent to be')

class HeaderFrame(customtkinter.CTkFrame):
    def __init__(self, master, bg_color):
        super().__init__(master)
        self.grid_columnconfigure(0, weight=1)

        self.lblTitle = customtkinter.CTkLabel(self, text='Duffinator_CableManager7014')
        self.lblTitle.grid(row=0, column=0, padx=(10, 0), sticky='w')

        def btnCallBack(cableVerify):
            AddCableFrame()    
            
        self.btnAddCable = customtkinter.CTkButton(self, text='Add Cable', command=btnCallBack)
        self.btnAddCable.grid(row=1, column=0, padx=(10, 0))

        self.userSearch = customtkinter.CTkEntry(self)
        self.userSearch.grid(row=0, column=1, padx=(10,0))

        self.lblSort = customtkinter.CTkLabel(self, text='sort:')
        self.lblSort.grid(row=0, column=2, padx=(10, 0))

        self.optionSort = customtkinter.CTkOptionMenu(self, values=['option', 'date ^', 'date v', 'length ^', 'length v'])
        self.optionSort.grid(row=0, column=3, padx=(10,0))

class AddCableFrame(customtkinter.CTk):
    def __init__(self, cableVerify):
        super().__init__()
        self.title('Add Cable')
        self.geometry('300x540')


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title('Duffinator_CableManager7014')
        self.geometry('960x540')
        self.grid_columnconfigure(0, weight=1)

        self.appHeader = HeaderFrame(self, bg_color='green')
        self.appHeader.grid(row=0, column=0, padx=(10, 0), pady=(10, 0), sticky='nsew')

        self.scrollingCables = ScrollingCables(self, title='test')
        self.scrollingCables.grid(row=1, column=0, padx=(10, 0), pady=(10, 0), sticky='nsew')

        db.sortCable()


# class 


app = App()
app.mainloop()