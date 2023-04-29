from tkinter import messagebox
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

class SignupPage(ttk.Frame):
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        self.label = ttk.Label(self, text="SIGN UP")
        self.label.pack(padx=10, pady=10)

        from pages.home_page import HomePage
        self.btn = ttk.Button(self, text="Go to DASHBOARD", command=lambda: controller.show_page(HomePage))
        self.btn.pack(padx=10, pady=10)

        self.controller = controller
