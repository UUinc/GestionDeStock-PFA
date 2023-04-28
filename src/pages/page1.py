from tkinter import messagebox
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

class Page1(ttk.Frame):
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        self.label = ttk.Label(self, text="Page 1")
        self.label.pack(padx=10, pady=10)

        from pages.page2 import Page2
        self.btn = ttk.Button(self, text="Go to Page 2", command=lambda: controller.show_page(Page2))
        self.btn.pack(padx=10, pady=10)

        self.label = ttk.Label(self, text="Your message")
        self.label.pack(padx=10, pady=10)

        self.textbox = ttk.Text(self, height=5)
        self.textbox.pack(padx=10, pady=10)

        self.check_state = ttk.IntVar()

        self.check = ttk.Checkbutton(self, text="Show Messagebox", variable=self.check_state)
        self.check.pack(padx=10, pady=10)
        
        self.button = ttk.Button(self, text="Show Message", command=self.show_message)
        self.button.pack(padx=10, pady=10)

        self.controller = controller

    def show_message(self):
        print(self.check_state.get())
