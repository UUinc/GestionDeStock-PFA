from tkinter import messagebox
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

class LoginPage(ttk.Frame):
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        self.label = ttk.Label(self, text="LOGIN")
        self.label.pack(padx=10, pady=10)

        from pages.signup_page import SignupPage
        self.btn = ttk.Button(self, text="Go to SIGN UP", command=lambda: controller.show_page(SignupPage))
        self.btn.pack(padx=10, pady=10)

        # #example of label, textbox, checkbox and button in ttk bootsrap
        # self.label = ttk.Label(self, text="Your message")
        # self.label.pack(padx=10, pady=10)

        # self.textbox = ttk.Text(self, height=5)
        # self.textbox.pack(padx=10, pady=10)

        # self.check_state = ttk.IntVar()

        # self.check = ttk.Checkbutton(self, text="Show Messagebox", variable=self.check_state)
        # self.check.pack(padx=10, pady=10)
        
        # self.button = ttk.Button(self, text="Show Message", command=self.show_message)
        # self.button.pack(padx=10, pady=10)

        self.controller = controller

    def show_message(self):
        print(self.check_state.get())
