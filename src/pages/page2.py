from tkinter import messagebox
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

class Page2(ttk.Frame):
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        self.label = ttk.Label(self, text="Page 2")
        self.label.pack(padx=10, pady=10)

        from pages.page1 import Page1
        self.btn = ttk.Button(self, text="Go to Page 1", command=lambda: controller.show_page(Page1))
        self.btn.pack(padx=10, pady=10)

        self.controller = controller
