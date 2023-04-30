from tkinter import messagebox
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

class StockSettingsPage(ttk.Frame):
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        self.label = ttk.Label(self, text="Stock Settings")
        self.label.pack(padx=10, pady=10)

        from src.pages.login_page import LoginPage
        self.btn = ttk.Button(self, text="Go to LOGIN", command=lambda: controller.show_page(LoginPage))
        self.btn.pack(padx=10, pady=10)

        self.controller = controller
