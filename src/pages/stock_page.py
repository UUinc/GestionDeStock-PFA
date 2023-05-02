from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

class StockPage(ttk.Frame):
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        self.label = ttk.Label(self, text="Stock")
        self.label.pack(padx=10, pady=10)

        from src.pages.stock_settings_page import StockSettingsPage
        self.btn = ttk.Button(self, text="Go to STOCK SETTINGS", command=lambda: controller.update_page(StockSettingsPage))
        self.btn.pack(padx=10, pady=10)

        self.controller = controller
