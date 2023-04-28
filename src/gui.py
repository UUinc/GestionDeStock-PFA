from tkinter import messagebox
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

from pages.page1 import Page1
from pages.page2 import Page2

class GUI:
    def __init__(self):
        self.root = ttk.Window()
        self.root.title("STOCK.ME")
        self.root.iconbitmap("../assets/stockme.ico")
        self.root.state('zoomed')

        self.container = ttk.Frame(self.root)
        self.container.pack(fill="both", expand=True)

        self.pages = {}
        for page_name in (Page1, Page2):
            page = page_name(self.container, self)
            self.pages[page_name] = page
            page.grid(row=0, column=0, sticky="nsew")
        self.show_page(Page1)

        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.root.mainloop()

    def show_page(self, page_name):
        page = self.pages[page_name]
        page.tkraise()

    def on_closing(self):
        if messagebox.askyesno(title="Quit?", message="Do you really want to quit?"):
            self.root.destroy()


if __name__ == "__main__":
    GUI()
