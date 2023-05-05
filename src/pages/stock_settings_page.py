from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

from src.user import User
from src.stock import Stock
from src.ownership import Ownership
from src.stock import Stock

from tkinter.font import Font

class StockSettingsPage(ttk.Frame):
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
        from src.pages.home_page import HomePage
        self.home_sidebar_btn = ttk.Button(self, text="Dashboard", style='sidebar_btn.TButton', padding=(120, 10, 131, 10), command=lambda: controller.update_page(HomePage))
        from src.pages.notification_page import NotificationPage
        self.notification_sidebar_btn = ttk.Button(self, text="Notification", style='sidebar_btn.TButton', padding=(120, 10, 127, 10), command=lambda: controller.update_page(NotificationPage))
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

        #Stock Settings page
        #Stock Settings page title
        self.pageTitle = ttk.Label(self, text="Stock Settings", foreground="#4D5D69", font=("Livvic Bold", int(SCR_HEIGHT/30)))
        #set widgets position
        self.pageTitle.place(relx=0.23, rely=0.08, anchor="w")
        
        #Stock Settings page Subtitle
        #stock name
        self.stock_id = controller.get_stock_id()
        print(self.stock_id)
        stock = Stock.get_stock(self.stock_id)
        stock_name = stock.get_name()
        self.pageSubtitle = ttk.Label(self, text=stock_name, foreground="#4D5D69", font=("Livvic Medium", int(SCR_HEIGHT/40)))
        #set widgets position
        self.pageSubtitle.place(relx=0.23, rely=0.14, anchor="w")
        #Hi,user 
        username = controller.get_username()
        user = User.get_information(username)
        firstname = user.get_firstname()
        self.user = ttk.Label(self, text="Hi, "+firstname, foreground="#4D5D69", font=("Livvic Regular", int(SCR_HEIGHT/38)))
        self.user.place(relx=0.92, rely=0.08, anchor="e")
        #user icon
        user_img = Image.open("assets/logo/profile.png")
        user_img = user_img.resize((75, 75), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(user_img)
        self.userIcon = Label(self, image=photo, bd=0)
        self.userIcon.image = photo
        self.userIcon.place(relx=0.95, rely=0.08, anchor="center")
        #BODY
        #get stock data
        stock_description = stock.get_description()
        #stockname section
        self.stocknameLabel = ttk.Label(self, text="name", foreground="#4D5D69", font=("Livvic Regular", int(SCR_HEIGHT/60)))
        self.stocknameLabel.place(relx=0.25, rely=0.2, anchor="w")
        self.stockname_entry = ttk.Entry(self, font=('Livvic Regular', int(SCR_HEIGHT/58)), width=64)
        self.stockname_entry.insert(0, stock_name)
        self.stockname_entry.place(relx=0.25, rely=0.25, anchor="w")
        #description section
        self.descriptionLabel = ttk.Label(self, text="description", foreground="#4D5D69", font=("Livvic Regular", int(SCR_HEIGHT/60)))
        self.descriptionLabel.place(relx=0.25, rely=0.3, anchor="w")
        self.description_entry = ttk.Entry(self, font=('Livvic Regular', int(SCR_HEIGHT/58)), width=64)
        self.description_entry.insert(0, stock_description)
        self.description_entry.place(relx=0.25, rely=0.35, anchor="w")
        #Button save
        s = ttk.Style()
        s.configure('stock_settings_btn.TButton', font=('Livvic Medium', int(SCR_HEIGHT/64)), padding=(10,10), width=20, background='#4D5D69', foreground='#FFFFFF', borderwidth=0)
        self.save_btn= ttk.Button(self, text="save", style='stock_settings_btn.TButton', bootstyle=PRIMARY)
        self.save_btn.place(relx=0.75, rely= 0.35, anchor="w")
        #username section
        self.usernameLabel = ttk.Label(self, text="username", foreground="#4D5D69", font=("Livvic Regular", int(SCR_HEIGHT/60)))
        self.usernameLabel.place(relx=0.25, rely=0.4, anchor="w")
        self.username_entry = ttk.Entry(self, font=('Livvic Regular', int(SCR_HEIGHT/58)), width=30)
        self.username_entry.place(relx=0.25, rely=0.45, anchor="w")
        #role
        self.roleLabel = ttk.Label(self, text="role", foreground="#4D5D69", font=("Livvic Regular", int(SCR_HEIGHT/60)))
        self.roleLabel.place(relx=0.49, rely=0.4, anchor="w")

        s = ttk.Style()
        s.configure('role.TCombobox',  background='#BDC3C6')
        font = Font(family = "Livvic Regular", size = int(SCR_HEIGHT/72))
        self.option_add("*TCombobox*Listbox*Font", font)
        s.map('role.TCombobox', selectforeground=[('readonly', '#38393B')], selectbackground=[('readonly', '#BDC3C6')], fieldbackground=[('readonly', '#BDC3C6')], background=[('readonly', '#BDC3C6')])
        self.role = ttk.Combobox(self, state="readonly", style='role.TCombobox', values=["edit","view"], font=('Livvic Regular', int(SCR_HEIGHT/60)), width=30)
        self.role.set("edit")
        self.role.place(relx=0.49, rely=0.45, anchor="w")
        # add user button function
        def add():
            user=Ownership
            user.add_stock_user
        #Button add user
        self.add_user_btn= ttk.Button(self, text="add user", style='stock_settings_btn.TButton', bootstyle=PRIMARY)
        self.add_user_btn.place(relx=0.75, rely= 0.45, anchor="w")
        #users list section
        self.list= ttk.Label(self, text="users list", foreground="#4D5D69", font=("Livvic SemiBold", int(SCR_HEIGHT/60)))
        self.list.place(relx=0.25, rely=0.53, anchor="w")

        # create a Treeview widget including all user's stocks
        style = ttk.Style()
        style.configure('userslist.Treeview', rowheight=30, padding=5, font=("Livvic Regular", 12))
        # configure the Treeview heading style
        style.configure("userslist.Treeview.Heading", font=("Livvic Medium", 14), stretch=False)
        # Create treeview
        self.tree = ttk.Treeview(self, columns=("Username", "Email", "Role", "Action", ""), show='headings', style='userslist.Treeview')
        self.tree.heading("Username", text="Username", anchor="w")
        self.tree.heading("Email", text="Email", anchor="w")
        self.tree.heading("Role", text="Role", anchor="w")
        self.tree.heading("Action", text="Action", anchor="w")
        self.tree.heading("", text="")

        self.tree.column("Username", width=250)
        self.tree.column("Email", width=400)
        self.tree.column("Role", width=395)
        self.tree.column("Action", width=98)
        self.tree.column("", width=95)

        #display all user's stocks
        users = Stock.get_stock_users(self.stock_id)
        for user in users:
            self.add_row(user[0], user[1], user[2])

        self.tree.bind("<Button-1>", self.on_click)

        self.tree.place(relx=0.25, rely=0.67, anchor="w")
        self.controller = controller

    def add_row(self, username, email, role):
        item_id = self.tree.insert("", "end", values=(username, email, role, "Edit", "Delete"))

    def on_click(self, event):
        item_id = self.tree.identify_row(event.y)
        if item_id:
            column = self.tree.identify_column(event.x)
            username = self.tree.item(item_id, "values")[0]
            ownership = Ownership.get_ownership(username, self.stock_id)
           
            if column == "#4":
                print("edit: "+username)
                if ownership.get_role() == 'edit':
                    pass
                else:
                    messagebox.showerror("Error", "Unable to edit ownership. Your account does not have the necessary permissions to perform this action. Please contact your stock administrator for assistance")
            elif column == "#5":
                if ownership.get_role() == 'edit':
                    Ownership.remove_stock_user(username, self.stock_id)
                    self.controller.update_page(StockSettingsPage)
                else:
                    messagebox.showerror("Error", "Unable to delete ownership. Your account does not have the necessary permissions to perform this action. Please contact your stock administrator for assistance")

    def clear_form(self):
        self.stockname_entry.delete(0, 'end')
        self.description_entry.delete(0, 'end')
        self.username_entry.delete(0, 'end')
