from tkinter import messagebox
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

from src.pages.login_page import LoginPage
from src.pages.signup_page import SignupPage
from src.pages.home_page import HomePage
from src.pages.settings_page import SettingsPage
from src.pages.stock_page import StockPage
from src.pages.stock_settings_page import StockSettingsPage

class GUI:
    def __init__(self):
        self.root = ttk.Window(themename="gestionstock")
        self.root.title("STOCK.ME")
        self.root.iconbitmap("assets/icon/stockme.ico")
        self.root.state('zoomed')
        self.root.resizable(False, False)

        self.container = ttk.Frame(self.root)
        self.container.pack(fill="both", expand=True)

        self.pages = {}
        for page_name in (LoginPage, SignupPage, HomePage, SettingsPage, StockPage, StockSettingsPage):
            page = page_name(self.container, self)
            self.pages[page_name] = page
            page.grid(row=0, column=0, sticky="nsew")
        self.show_page(LoginPage)

        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.root.mainloop()

    def show_page(self, page_name):
        page = self.pages[page_name]
        page.tkraise()

    def on_closing(self):
        if messagebox.askyesno(title="Quit?", message="Do you really want to quit?"):
            self.root.destroy()
