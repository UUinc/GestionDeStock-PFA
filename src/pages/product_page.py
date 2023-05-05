from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

from src.user import User
from src.stock import Stock
from src.ownership import Ownership
from src.product import Product

from src.utils import *

class ProductPage(ttk.Frame):
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)

        SCR_HEIGHT = self.winfo_screenheight()

        #Background left side
        # Load background image file
        img = Image.open("assets/background/sidebar.png")
        img = img.resize((int(SCR_HEIGHT/3.01), SCR_HEIGHT), Image.Resampling.LANCZOS)
        self.img = ImageTk.PhotoImage(img)

        # Load logo file
        logo_img = Image.open("assets/icon/logo.png")
        logo_img = logo_img.resize((int(SCR_HEIGHT*0.08), int(SCR_HEIGHT*0.08)), Image.Resampling.LANCZOS)
        self.logo_img = ImageTk.PhotoImage(logo_img)

        self.canvas = Canvas(self, width=self.winfo_screenwidth(), height=SCR_HEIGHT, highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)
        # Set canvas height to window height
        self.canvas.config(height=SCR_HEIGHT)
        # Place image at bottom-left corner with canvas width and image height
        self.canvas.create_image(0, SCR_HEIGHT, image=self.img, anchor="sw", tags="bg")
        # Add logo image on top of background image
        self.canvas.create_image(int(SCR_HEIGHT*0.04), int(SCR_HEIGHT*0.05), image=self.logo_img, anchor="nw")
        # Add text on top of the image
        self.canvas.create_text(int(SCR_HEIGHT*0.21), int(SCR_HEIGHT*0.09), text="STOCK.ME", font=("Livvic Bold", int(SCR_HEIGHT/52)), fill="#313f4a", tags="text")

        #Sidebar buttons
        s = ttk.Style()
        s.configure('sidebar_btn.TButton', font=('Livvic Medium', int(SCR_HEIGHT/64)), background='#BDC3C6', foreground='#38393B', borderwidth=0)
        s.map('sidebar_btn.TButton', background=[('active', '!disabled', '#A7AEB1')], foreground=[('active', '!disabled', '#38393B')])
        #create buttons
        from src.pages.home_page import HomePage
        self.home_sidebar_btn = ttk.Button(self, text="Dashboard", style='sidebar_btn.TButton', padding=(120, 10, 132, 10), command=lambda: controller.update_page(HomePage))
        from src.pages.notification_page import NotificationPage
        self.notification_sidebar_btn = ttk.Button(self, text="Notification", style='sidebar_btn.TButton', padding=(120, 10, 127, 10), command=lambda: controller.update_page(NotificationPage))
        from src.pages.settings_page import SettingsPage
        self.settings_sidebar_btn = ttk.Button(self, text="Settings", style='sidebar_btn.TButton', padding=(120, 10, 160, 10), command=lambda: controller.update_page(SettingsPage))
        from src.pages.login_page import LoginPage
        self.logout_sidebar_btn = ttk.Button(self, text="Logout", style='sidebar_btn.TButton', padding=(120, 10, 172, 10), command=lambda: controller.show_page(LoginPage))
        #Sidebar logos
        #Dashboard icon
        home_img = Image.open("assets/logo/home.png")
        home_img = home_img.resize((25, 25), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(home_img)
        self.homeIcon = Label(self, image=photo, bd=0)
        self.homeIcon.image = photo
        #Notification icon
        notification_img = Image.open("assets/logo/notification.png")
        notification_img = notification_img.resize((25, 25), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(notification_img)
        self.notificationIcon = Label(self, image=photo, bd=0)
        self.notificationIcon.image = photo
        #Settings icon
        settings_img = Image.open("assets/logo/settings.png")
        settings_img = settings_img.resize((25, 25), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(settings_img)
        self.settingsIcon = Label(self, image=photo, bd=0)
        self.settingsIcon.image = photo
        #Logout icon
        logout_img = Image.open("assets/logo/logout.png")
        logout_img = logout_img.resize((25, 25), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(logout_img)
        self.logoutIcon = Label(self, image=photo, bd=0)
        self.logoutIcon.image = photo

        #set sidebar buttons position
        self.home_sidebar_btn.place(relx=0, rely=0.2, anchor="w")
        self.homeIcon.place(relx=0.038, rely=0.2, anchor="w")
        self.notification_sidebar_btn.place(relx=0, rely=0.25, anchor="w")
        self.notificationIcon.place(relx=0.038, rely=0.25, anchor="w")
        self.settings_sidebar_btn.place(relx=0, rely=0.3, anchor="w")
        self.settingsIcon.place(relx=0.038, rely=0.3, anchor="w")
        self.logout_sidebar_btn.place(relx=0, rely=0.35, anchor="w")
        self.logoutIcon.place(relx=0.038, rely=0.35, anchor="w")

        #Dashboard page
        #Dashborad page title
        self.pageTitle = ttk.Label(self, text="Product", foreground="#4D5D69", font=("Livvic Bold", int(SCR_HEIGHT/30)))
        #User information
        #user greeting
        self.username = controller.get_username()
        user = User.get_information(self.username)
        fullname = user.get_firstname()
        self.usergreetingTitle = ttk.Label(self, text="Hi, "+fullname, foreground="#4D5D69", font=("Livvic Regular", int(SCR_HEIGHT/38)))
        #user image
        profile_img = Image.open("assets/logo/profile.png")
        profile_img = profile_img.resize((75, 75), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(profile_img)
        self.profileIcon = Label(self, image=photo, bd=0)
        self.profileIcon.image = photo

        #stock name
        self.stock_id = controller.get_stock_id()
        stock = Stock.get_stock(self.stock_id)
        stock_name = stock.get_name()
        self.stocknameTitle = ttk.Label(self, text=stock_name, foreground="#4D5D69", font=("Livvic Medium", int(SCR_HEIGHT/40)))
        
        #product name
        self.product_id = controller.get_product_id()
        self.state = "Add"
        if self.product_id != -1:
            self.state = "Edit"
            product = Product.get_product(self.product_id)
        
        product_name = self.state + " product"
        self.productStateTitle = ttk.Label(self, text=product_name, foreground="#4D5D69", font=("Livvic Medium", int(SCR_HEIGHT/62)))

        #body 
        self.nameLabel = ttk.Label(self, text="name", foreground="#4D5D69", font=("Livvic Regular", int(SCR_HEIGHT/60)))
        self.nameEntry = ttk.Entry(self, font=('Livvic Regular', int(SCR_HEIGHT/50)), width=67)
        self.descriptionLabel = ttk.Label(self, text="description", foreground="#4D5D69", font=("Livvic Regular", int(SCR_HEIGHT/60)))
        self.descriptionEntry = ttk.Entry(self, font=('Livvic Regular', int(SCR_HEIGHT/50)), width=67)
        self.unitpriceLabel = ttk.Label(self, text="unit price", foreground="#4D5D69", font=("Livvic Regular", int(SCR_HEIGHT/60)))
        self.unitpriceEntry = ttk.Entry(self, font=('Livvic Regular', int(SCR_HEIGHT/50)), width=67)
        self.quantityLabel = ttk.Label(self, text="quantity", foreground="#4D5D69", font=("Livvic Regular", int(SCR_HEIGHT/60)))
        self.quantityEntry = ttk.Entry(self, font=('Livvic Regular', int(SCR_HEIGHT/50)), width=67)
        self.thresholdLabel = ttk.Label(self, text="alert threshold", foreground="#4D5D69", font=("Livvic Regular", int(SCR_HEIGHT/60)))
        self.thresholdEntry = ttk.Entry(self, font=('Livvic Regular', int(SCR_HEIGHT/50)), width=67)
        
        if self.product_id != -1:
            self.nameEntry.insert(0, product.get_name())
            self.descriptionEntry.insert(0, product.get_description())
            self.unitpriceEntry.insert(0, product.get_unit_price())
            self.quantityEntry.insert(0, product.get_quantity())
            self.thresholdEntry.insert(0, product.get_alert_threshold())

        #save button
        s = ttk.Style()
        s.configure('save_btn.TButton', font=('Livvic Medium', int(SCR_HEIGHT/50)), padding=(100, 9), background='#4D5D69', foreground='#FFFFFF', borderwidth=0)
        self.save_btn= ttk.Button(self, text=self.state, style='save_btn.TButton', bootstyle=PRIMARY, command=self.save)

        #set widgets position
        self.pageTitle.place(relx=0.23, rely=0.08, anchor="w")
        self.usergreetingTitle.place(relx=0.92, rely=0.08, anchor="e")
        self.profileIcon.place(relx=0.95, rely=0.08, anchor="center")
        self.stocknameTitle.place(relx=0.23, rely=0.14, anchor="w")
        self.productStateTitle.place(relx=0.231, rely=0.18, anchor="w")

        self.nameLabel.place(relx=0.28, rely=0.25, anchor="w")
        self.nameEntry.place(relx=0.28, rely=0.3, anchor="w")
        self.descriptionLabel.place(relx=0.28, rely=0.35, anchor="w")
        self.descriptionEntry.place(relx=0.28, rely=0.4, anchor="w")
        self.unitpriceLabel.place(relx=0.28, rely=0.45, anchor="w")
        self.unitpriceEntry.place(relx=0.28, rely=0.5, anchor="w")
        self.quantityLabel.place(relx=0.28, rely=0.55, anchor="w")
        self.quantityEntry.place(relx=0.28, rely=0.6, anchor="w")
        self.thresholdLabel.place(relx=0.28, rely=0.65, anchor="w")
        self.thresholdEntry.place(relx=0.28, rely=0.7, anchor="w")
        
        self.save_btn.place(relx=0.51, rely= 0.84, anchor="w")
        
        self.controller = controller

    def clear_form(self):
        self.nameEntry.delete(0, 'end')
        self.descriptionEntry.delete(0, 'end')
        self.unitpriceEntry.delete(0, 'end')
        self.quantityEntry.delete(0, 'end')
        self.thresholdEntry.delete(0, 'end')

    def save(self):
        name = self.nameEntry.get()
        description = self.descriptionEntry.get()
        unitprice = self.unitpriceEntry.get()
        quantity = self.quantityEntry.get()
        threshold = self.thresholdEntry.get()

        if self.state == 'Add':
            product = Product(name, description, unitprice, quantity, threshold)
            product.add_product(self.stock_id)
            self.clear_form()
        else:
            product = Product(name, description, unitprice, quantity, threshold)
            oldProduct = Product.get_product(self.product_id)

            product.set_last_entry_date(oldProduct.get_last_entry_date())
            product.set_last_release_date(oldProduct.get_last_release_date())

            if oldProduct.get_quantity() < int(quantity):
                product.set_last_entry_date(current_timestamp())
            elif oldProduct.get_quantity() > int(quantity):
                product.set_last_release_date(current_timestamp())

            product.update_product(self.stock_id, self.product_id)
        
        from src.pages.stock_page import StockPage
        self.controller.update_page(StockPage)