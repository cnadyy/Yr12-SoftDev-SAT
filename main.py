# harri
# Main UI for Cable Management system
# 25.7.23 - __.__.23

import customtkinter
import fileDatabase

usrName = 'name      test JACK EDITION'
usrDesc = 'can you quickly press comand z'

db = fileDatabase.SQLDatabase()
db.addCable({'name': f"{usrName}", 'description': f"{usrDesc}", 'length': 1.2, 'quantity': 4, 'location': "there"})


class ScrollingCables(customtkinter.CTkScrollableFrame):
    def __init__(self, master, title):
        super().__init__(master, label_text=title)
        self.grid_columnconfigure(0, weight=1)



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