# Harri :3
# practice toward dynamically generated frames !!
# 14.7.23

import customtkinter

class CheckboxFrame(customtkinter.CTkFrame):
    def __init__(self, master, values):
        super().__init__(master)
        self.values = values
        self.checkboxes = []

    # generates buttons through list of values from for loop
        for i, value in enumerate(self.values):
            checkboxOne = customtkinter.CTkCheckBox(self, text=value)
            checkboxOne.grid(row=i, column=0, padx=10, pady=(10, 0), sticky="w")
            self.checkboxes.append(checkboxOne)

    def get(self):
        checkedBoxes = []
        for checkboxOne in self.checkboxes:
            if checkboxOne.get() == 1:
                checkedBoxes.append(checkboxOne.cget("text"))
        return checkedBoxes

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title('name test')
        self.geometry('400x180')
        self.grid_columnconfigure((0, 1), weight=1)
        self.grid_rowconfigure(0, weight=1)

        values = ['item 1', 'item 2', 'item 3']

        self.checkboxFrame = CheckboxFrame(self, values)
        self.checkboxFrame.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="nsew")

        self.checkboxFrameTwo = CheckboxFrame(self, values=['option one', 'option two'])
        self.checkboxFrameTwo.grid(row=0, column=1, padx=10, pady=(10, 0), sticky="nsew")

        self.button = customtkinter.CTkButton(self, text="my button", command=self.button_callback)
        self.button.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky="ew")
    
    
    def button_callback(self):
        print("checked checkboxes:", self.checkboxFrame.get())
        print("checked checkboxes:", self.checkboxFrameTwo.get())


app = App()
app.mainloop()


# place !!! important for updating existing frame with new items
# i.e. confirmAdd.place(x=50, y=50) -> will add atop the existing frame without worry of previous collumns and frames