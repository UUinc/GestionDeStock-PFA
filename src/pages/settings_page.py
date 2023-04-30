from tkinter import messagebox
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

class SettingsPage(ttk.Frame):
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        self.label = ttk.Label(self, text="Settings")
        self.label.pack(padx=10, pady=10)

        from src.pages.stock_page import StockPage
        self.btn = ttk.Button(self, text="Go to STOCK", command=lambda: controller.show_page(StockPage))
        self.btn.pack(padx=10, pady=10)

        self.controller = controller
