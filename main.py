# harri
# Main UI for Cable Management system
# 25.7.23 - __.__.23

import customtkinter
import fileDatabase

db = fileDatabase()

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title('Duffinator_CableManager7014')
        self.geometry('960x540')

        db.removeCables()


# class 


app = App()
app.mainloop()