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
# db.addCable({'name': f"{usrName}", 'description': f"{usrDesc}", 'length': f"{float(usrLength)}", 'quantity': f"{int(usrQuant)}", 'location': f"{usrLocate}"})


class ScrollingCables(customtkinter.CTkScrollableFrame):
    def __init__(self, master, title):
        super().__init__(master, label_text=title)
        self.grid_columnconfigure(0, weight=1)

        cables = db.getCables()

        i = 0
        for cable in cables:
            print(cable[0])



        

        #print(db.getCables())
        #print('where is this maent to be')



class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title('Duffinator_CableManager7014')
        self.geometry('960x540')

        self.scrollingCables = ScrollingCables(self, title='test')
        self.scrollingCables.grid(row=1, column=0, padx=(10, 0), pady=(10, 0), sticky="nsew")

        db.sortCable()


# class 


app = App()
app.mainloop()