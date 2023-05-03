from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

from src.user import User

class HomePage(ttk.Frame):
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
        s = ttk.Style()
        s.configure('sidebar_disabled_btn.TButton', font=('Livvic Bold', int(SCR_HEIGHT/64)), background='#BDC3C6', foreground='#38393B', borderwidth=0)
        s.map('sidebar_disabled_btn.TButton', background=[('active', '!disabled', '#A7AEB1')], foreground=[('active', '!disabled', '#38393B')])
        #create buttons
        self.home_sidebar_btn = ttk.Button(self, text="Dashboard", style='sidebar_disabled_btn.TButton', padding=(120, 10, 125, 10))
        from src.pages.stock_settings_page import StockSettingsPage
        self.userslist_sidebar_btn = ttk.Button(self, text="Users list", style='sidebar_btn.TButton', padding=(120, 10, 150, 10), command=lambda: controller.update_page(StockSettingsPage))
        from src.pages.settings_page import SettingsPage
        self.notification_sidebar_btn = ttk.Button(self, text="Notification", style='sidebar_btn.TButton', padding=(120, 10, 127, 10), command=lambda: controller.update_page(SettingsPage))
        from src.pages.settings_page import SettingsPage
        self.settings_sidebar_btn = ttk.Button(self, text="Settings", style='sidebar_btn.TButton', padding=(120, 10, 160, 10), command=lambda: controller.update_page(SettingsPage))
        
        #Sidebar logos
        #Dashboard icon
        home_img = Image.open("assets/logo/home.png")
        home_img = home_img.resize((25, 25), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(home_img)
        self.homeIcon = Label(self, image=photo, bd=0)
        self.homeIcon.image = photo
        #Users list icon
        userslist_img = Image.open("assets/logo/users_list.png")
        userslist_img = userslist_img.resize((25, 25), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(userslist_img)
        self.userslistIcon = Label(self, image=photo, bd=0)
        self.userslistIcon.image = photo
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

        #set sidebar buttons position
        self.home_sidebar_btn.place(relx=0, rely=0.2, anchor="w")
        self.homeIcon.place(relx=0.038, rely=0.2, anchor="w")
        self.userslist_sidebar_btn.place(relx=0, rely=0.25, anchor="w")
        self.userslistIcon.place(relx=0.038, rely=0.25, anchor="w")
        self.notification_sidebar_btn.place(relx=0, rely=0.3, anchor="w")
        self.notificationIcon.place(relx=0.038, rely=0.3, anchor="w")
        self.settings_sidebar_btn.place(relx=0, rely=0.35, anchor="w")
        self.settingsIcon.place(relx=0.038, rely=0.35, anchor="w")

        #Dashboard page
        #Dashborad page title
        self.pageTitle = ttk.Label(self, text="Dashboard", foreground="#4D5D69", font=("Livvic Bold", int(SCR_HEIGHT/30)))
        #User information
        #user greeting
        username = controller.get_username()
        user = User.get_information(username)
        fullname = user.get_firstname()
        self.usergreetingTitle = ttk.Label(self, text="Hi, "+fullname, foreground="#4D5D69", font=("Livvic Regular", int(SCR_HEIGHT/38)))
        #user image
        profile_img = Image.open("assets/logo/profile.png")
        profile_img = profile_img.resize((75, 75), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(profile_img)
        self.profileIcon = Label(self, image=photo, bd=0)
        self.profileIcon.image = photo
        #searchbar
        #search icon
        search_img = Image.open("assets/logo/search.png")
        search_img = search_img.resize((25, 25), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(search_img)
        self.searchIcon = Label(self, image=photo, bd=0)
        self.searchIcon.image = photo
        #entry
        self.searchbarEntry = ttk.Entry(self, font=('Livvic Regular', int(SCR_HEIGHT/58)), width=46)
        #Add stock button
        s = ttk.Style()
        s.configure('addstock_btn.TButton', font=('Livvic Medium', int(SCR_HEIGHT/64)), padding=(18, 9), background='#4D5D69', foreground='#FFFFFF', borderwidth=0)
        #create button
        self.addStockBTN = ttk.Button(self, text="Add stock", style='addstock_btn.TButton', bootstyle=PRIMARY, command=self.add_stock)
        #stocks list title
        self.stocklistTitle = ttk.Label(self, text="Stocks", foreground="#4D5D69", font=("Livvic Bold", int(SCR_HEIGHT/60)))

        # create a Treeview widget including all user's stocks
        style = ttk.Style()
        style.configure('stock.Treeview', rowheight=30, padding=5, font=("Livvic Regular", 12))
        # configure the Treeview heading style
        style.configure("stock.Treeview.Heading", font=("Livvic Medium", 14), stretch=False)
         # Create treeview
        self.tree = ttk.Treeview(self, columns=("ID", "Stock Name", "Description", "Creation Date", "Date Modified", "Action", ""), show='headings', style='stock.Treeview')
        self.tree.heading("ID", text="ID", anchor="w")
        self.tree.heading("Stock Name", text="Stock Name", anchor="w")
        self.tree.heading("Description", text="Description", anchor="w")
        self.tree.heading("Creation Date", text="Creation Date", anchor="w")
        self.tree.heading("Date Modified", text="Date Modified", anchor="w")
        self.tree.heading("Action", text="Action", anchor="w")
        self.tree.heading("", text="")

        # Add sample rows
        self.add_row(1, "IT", "all IT accessories", "16-04-2023 10:30:55", "11-04-2023 10:30:55")
        self.add_row(2, "IT2", "all IT 2", "17-04-2023 10:30:55", "15-04-2023 10:30:55")
        self.add_row(3, "IT3", "all IT 3", "18-04-2023 10:30:55", "14-04-2023 10:30:55")
        self.add_row(4, "IT4", "all IT 4", "19-04-2023 10:30:55", "13-04-2023 10:30:55")
        self.add_row(5, "IT5", "all IT 5", "20-04-2023 10:30:55", "12-04-2023 10:30:55")

        self.tree.bind("<Button-1>", self.on_click)

        #set widgets position
        self.pageTitle.place(relx=0.23, rely=0.08, anchor="w")
        self.usergreetingTitle.place(relx=0.92, rely=0.08, anchor="e")
        self.profileIcon.place(relx=0.95, rely=0.08, anchor="center")
        self.searchIcon.place(relx=0.56, rely=0.19, anchor="center")
        self.searchIcon.lift()
        self.searchbarEntry.place(relx=0.405, rely=0.19, anchor="center")
        self.addStockBTN.place(relx=0.615, rely=0.19, anchor="center")
        self.stocklistTitle.place(relx=0.25, rely=0.26, anchor="center")
        # place the Treeview widget into the tkinter window
        self.tree.place(relx=0.25, rely=0.5, anchor="w")

        self.controller = controller

    def add_row(self, id, stockname, description, creation_date, modified_date):
        item_id = self.tree.insert("", "end", values=(id, stockname, description, creation_date, modified_date, "Edit", "Delete"))
        self.tree.column("ID", width=60)
        self.tree.column("Stock Name", width=200)
        self.tree.column("Description", width=400)
        self.tree.column("Creation Date", width=250)
        self.tree.column("Date Modified", width=250)
        self.tree.column("Action", width=80)
        self.tree.column("", width=90)

    def on_click(self, event):
        item_id = self.tree.identify_row(event.y)
        if item_id:
            column = self.tree.identify_column(event.x)
            if column == "#3":
                id_value = self.tree.item(item_id, "values")[0]
                print("edit: "+id_value)
            if column == "#4":
                id_value = self.tree.item(item_id, "values")[0]
                print("delete: "+id_value)

    def add_stock():
        pass
