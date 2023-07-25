# Harrison
# the 'base' or home UI for the cable management system.
# 10.7.23 - __.__.__

import customtkinter

class CheckboxFrame(customtkinter.CTkFrame):
    def __init__(self, master, title, values):
        super().__init__(master)
        self.grid_columnconfigure(0, weight=1)
        self.values = values
        self.title = title
        self.checkboxes = []

        self.title = customtkinter.CTkLabel(self, text=self.title, fg_color="gray30", corner_radius=6)
        self.title.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="ew")

    # generates buttons through list of values from for loop
        for i, value in enumerate(self.values):
            checkboxOne = customtkinter.CTkCheckBox(self, text=value)
            checkboxOne.grid(row=i+1, column=0, padx=10, pady=(10, 0), sticky="w")
            self.checkboxes.append(checkboxOne)

    def get(self):
        checkedBoxes = []
        for checkboxOne in self.checkboxes:
            if checkboxOne.get() == 1:
                checkedBoxes.append(checkboxOne.cget("text"))
        return checkedBoxes

class ScrollableCheckboxFrame(customtkinter.CTkScrollableFrame):
    def __init__(self, master, title, values):
        super().__init__(master, label_text=title)
        self.grid_columnconfigure(0, weight=1)
        self.values = values
        self.checkboxes = []

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



class RadiobuttonFrame(customtkinter.CTkFrame):
    def __init__(self, master, title, values):
        super().__init__(master)
        self.grid_columnconfigure(0, weight=1)
        self.values = values
        self.title = title
        self.radiobuttons = []
        self.variable = customtkinter.StringVar(value="")

        self.title = customtkinter.CTkLabel(self, text=self.title, fg_color='gray30', corner_radius=6)
        self.title.grid(row=0, column=0, padx=10, pady=(10,0), sticky='ew')

        for i, value in enumerate(self.values):
            radiobuttonOne = customtkinter.CTkRadioButton(self, text=value, value=value, variable=self.variable)
            radiobuttonOne.grid(row=i+1, column=0, padx=10, pady=(10, 0), sticky='w')
            self.radiobuttons.append(radiobuttonOne)

    def get(self):
        return self.variable.get()

    def set(self, value):
        self.variable.set(value)


class App(customtkinter.CTk): 
    def __init__(self):
        super().__init__()
        self.title('Duffinator_CableManager7014')
        self.geometry('960x540')
        self.grid_columnconfigure((0, 1), weight=1)
        self.grid_rowconfigure(0, weight=1)
        
        values = ['item 1', 'item 2', 'item 3', 'item 4', 'item 5', 'item 6', 'item 7', 'item 8', 'boom', 'pow']
        self.scrollCheckboxFrame = ScrollableCheckboxFrame(self, title='values', values=values)
        self.scrollCheckboxFrame.grid(row=0, column=0, padx=(10, 0), pady=(10, 0), sticky="nsew")

        options = ['optoin 1', 'option 2', 'option3']
        self.checkboxFrameTwo = CheckboxFrame(self, 'options', values=options)
        self.checkboxFrameTwo.grid(row=0, column=1, padx=5, pady=(10, 0), sticky='nsew')
        self.checkboxFrameTwo.configure(fg_color='transparent')

        self.radiobuttonFrame = RadiobuttonFrame(self, "button", values=["option 1", "option 2"])
        self.radiobuttonFrame.grid(row=0, column=2, padx=(0, 10), pady=(10, 0), sticky="nsew")

        valuesTwo = ['item 1', 'item 2', 'VALUE 3', 'item four']
        self.checkboxFrameThree = ScrollableCheckboxFrame(self, title='Values !! Again !!', values=valuesTwo)
        self.checkboxFrameThree.grid(row=0, column=3, padx=(10, 0), pady=(10, 0), sticky='nsew')

        self.button = customtkinter.CTkButton(self, text="my button", command=self.button_callback)
        self.button.grid(row=1, column=0, columnspan=3, padx=10, pady=10, sticky="ew")

        def segmented_button_callback(value):
            print("segmented button clicked:", value)

        segemented_button_var = customtkinter.StringVar(value="Value 1")
        
        segemented_button = customtkinter.CTkSegmentedButton(self, values=["Value 1", "Value 2", "Value 3"],
                                                     command=segmented_button_callback,
                                                     variable=segemented_button_var)
        segemented_button.grid(row=2, column=0, columnspan=3, padx=10, pady=10, sticky="ew")
    
    def button_callback(self):
        print("checked checkboxes:", self.scrollCheckboxFrame.get())
        print("checked checkboxes:", self.checkboxFrameTwo.get())
        print("checked checkboxes:", self.radiobuttonFrame.get())
        print("checked checkboxes:", self.checkboxFrameThree.get())


app = App()
app.mainloop()