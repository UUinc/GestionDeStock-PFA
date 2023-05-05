from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

from src.user import User
from src.stock import Stock
from src.ownership import Ownership
from src.product import Product

from datetime import date

class StockPage(ttk.Frame):
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
        self.home_sidebar_btn = ttk.Button(self, text="Dashboard", style='sidebar_btn.TButton', padding=(120, 10, 125, 10), command=lambda: controller.update_page(HomePage))
        from src.pages.settings_page import SettingsPage
        self.notification_sidebar_btn = ttk.Button(self, text="Notification", style='sidebar_btn.TButton', padding=(120, 10, 127, 10), command=lambda: controller.update_page(SettingsPage))
        from src.pages.settings_page import SettingsPage
        self.settings_sidebar_btn = ttk.Button(self, text="Settings", style='sidebar_btn.TButton', padding=(120, 10, 160, 10), command=lambda: controller.update_page(SettingsPage))
        from src.pages.login_page import LoginPage
        self.logout_sidebar_btn = ttk.Button(self, text="Logout", style='sidebar_btn.TButton', padding=(120, 10, 160, 10), command=lambda: controller.show_page(LoginPage))
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
        self.pageTitle = ttk.Label(self, text="Stock", foreground="#4D5D69", font=("Livvic Bold", int(SCR_HEIGHT/30)))
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
        print(self.stock_id)
        stock = Stock.get_stock(self.stock_id)
        stock_name = stock.get_name()
        self.stocknameTitle = ttk.Label(self, text=stock_name, foreground="#4D5D69", font=("Livvic Medium", int(SCR_HEIGHT/40)))
        #date
        today = date.today()
        formatted_date = today.strftime("%d %b %Y")
        self.dateTitle = ttk.Label(self, text=formatted_date, foreground="#4D5D69", font=("Livvic Regular", int(SCR_HEIGHT/54)))
        #products list title
        self.productlistTitle = ttk.Label(self, text="Products", foreground="#4D5D69", font=("Livvic Bold", int(SCR_HEIGHT/60)))
        #searchbar
        #search icon
        search_img = Image.open("assets/logo/search.png")
        search_img = search_img.resize((25, 25), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(search_img)
        self.searchIcon = Label(self, image=photo, bd=0)
        self.searchIcon.image = photo
        #filter button
        s = ttk.Style()
        s.configure('filter_btn.TButton', font=('Livvic Medium', int(SCR_HEIGHT/64)), padding=(30, 9), background='#4D5D69', foreground='#FFFFFF', borderwidth=0)
        self.filterBTN = ttk.Button(self, text="Filter", style='filter_btn.TButton', bootstyle=PRIMARY, command=self.filter)
        #entry
        self.searchbarEntry = ttk.Entry(self, font=('Livvic Regular', int(SCR_HEIGHT/58)), width=46)
        
        #Add stock button
        s = ttk.Style()
        s.configure('addproduct_btn.TButton', font=('Livvic Medium', int(SCR_HEIGHT/64)), padding=(18, 9), background='#4D5D69', foreground='#FFFFFF', borderwidth=0)
        #create button
        self.addProductBTN = ttk.Button(self, text="Add product", style='addproduct_btn.TButton', bootstyle=PRIMARY, command=self.add_product)

        # create a Treeview widget including all user's stocks
        style = ttk.Style()
        style.configure('product.Treeview', rowheight=30, padding=5, font=("Livvic Regular", 12))
        # configure the Treeview heading style
        style.configure("product.Treeview.Heading", font=("Livvic Medium", 14), stretch=False)
        # Create treeview
        self.tree = ttk.Treeview(self, columns=("ID", "Name", "Description", "Unit Price", "Quantity", "Status", "Entry Date", "Release Date", "Action", ""), show='headings', style='product.Treeview', height=21)
        self.tree.heading("ID", text="ID", anchor="w")
        self.tree.heading("Name", text="Name", anchor="w")
        self.tree.heading("Description", text="Description", anchor="w")
        self.tree.heading("Unit Price", text="Unit Price", anchor="w")
        self.tree.heading("Quantity", text="Quantity", anchor="w")
        self.tree.heading("Status", text="Status", anchor="w")
        self.tree.heading("Entry Date", text="Entry Date", anchor="w")
        self.tree.heading("Release Date", text="Release Date", anchor="w")
        self.tree.heading("Action", text="Action", anchor="w")
        self.tree.heading("", text="")

        #max size = 1370
        self.tree.column("ID", width=50)
        self.tree.column("Name", width=180)
        self.tree.column("Description", width=290)
        self.tree.column("Unit Price", width=110)
        self.tree.column("Quantity", width=110)
        self.tree.column("Status", width=130)
        self.tree.column("Entry Date", width=180)
        self.tree.column("Release Date", width=180)
        self.tree.column("Action", width=70)
        self.tree.column("", width=70)

        #display all user's stocks
        products = Product.get_products(self.stock_id)
        for product in products:
            self.add_row(product[0], product[1], product[2], product[3], product[4], product[5], product[6], product[7])

        self.tree.bind("<Button-1>", self.on_click)

        #set widgets position
        self.pageTitle.place(relx=0.23, rely=0.08, anchor="w")
        self.usergreetingTitle.place(relx=0.92, rely=0.08, anchor="e")
        self.profileIcon.place(relx=0.95, rely=0.08, anchor="center")
        self.stocknameTitle.place(relx=0.23, rely=0.14, anchor="w")
        self.dateTitle.place(relx=0.23, rely=0.19, anchor="w")
        self.productlistTitle.place(relx=0.229, rely=0.26, anchor="w")
        self.searchIcon.place(relx=0.803, rely=0.26, anchor="e")
        self.searchIcon.lift()
        self.searchbarEntry.place(relx=0.808, rely=0.26, anchor="e")
        self.filterBTN.place(relx=0.867, rely=0.26, anchor="e")
        #add product
        self.addProductBTN.place(relx=0.95, rely=0.26, anchor="e")
        #place the Treeview widget into the tkinter window
        self.tree.place(relx=0.23, rely=0.31, anchor="nw")

        self.controller = controller

    def get_status(self, quantity, threshold):
        if quantity == 0:
            return "Out Of Stock"
        if quantity <= threshold:
            return "Low Stock"
        return "In Stock"

    def add_row(self, id, name, description, unit_price, quantity, threshold, entry_date, release_date):
        item_id = self.tree.insert("", "end", values=(id, name, description, unit_price, quantity, self.get_status(quantity, threshold), entry_date, release_date, "Edit", "Delete"))

    def on_click(self, event):
        item_id = self.tree.identify_row(event.y)
        if item_id:
            column = self.tree.identify_column(event.x)
            id_value = self.tree.item(item_id, "values")[0]
            ownership = Ownership.get_ownership(self.username, self.stock_id)
     
            if column == "#9":
                print("edit: "+id_value)
                if ownership.get_role() == 'edit':
                    self.controller.set_product_id(id_value)
                    from src.pages.product_page import ProductPage
                    self.controller.update_page(ProductPage)
                else:
                    messagebox.showerror("Error", "Unable to edit product. Your account does not have the necessary permissions to perform this action. Please contact your stock administrator for assistance")
            elif column == "#10":
                if ownership.get_role() == 'edit':
                    Product.delete_product(id_value)
                    self.controller.update_page(StockPage)
                else:
                    messagebox.showerror("Error", "Unable to delete product. Your account does not have the necessary permissions to perform this action. Please contact your stock administrator for assistance")

    def clear_form(self):
        self.searchbarEntry.delete(0, 'end')
    
    def filter(self):
        self.tree.delete(*self.tree.get_children())
        products = Product.get_products_filter(self.stock_id, self.searchbarEntry.get())
        for product in products:
            self.add_row(product[0], product[1], product[2], product[3], product[4], product[5], product[6], product[7])
        self.clear_form()

    def add_product(self):
        ownership = Ownership.get_ownership(self.username, self.stock_id)
        if ownership.get_role() == 'edit':
            self.controller.set_product_id(-1)
            from src.pages.product_page import ProductPage
            self.controller.update_page(ProductPage)
        else:
            messagebox.showerror("Error", "Unable to edit product. Your account does not have the necessary permissions to perform this action. Please contact your stock administrator for assistance")
        pass