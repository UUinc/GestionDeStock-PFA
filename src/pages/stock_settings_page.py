from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from src.user import User
from src.ownership import Ownership

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
        from src.pages.stock_settings_page import StockSettingsPage
        self.userslist_sidebar_btn = ttk.Button(self, text="Users list", style='sidebar_disabled_btn.TButton', padding=(120, 10, 145, 10), command=lambda: controller.update_page(StockSettingsPage))
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
        #Logout icon
        logout_img = Image.open("assets/logo/logout.png")
        logout_img = logout_img.resize((25, 25), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(logout_img)
        self.logoutIcon = Label(self, image=photo, bd=0)
        self.logoutIcon.image = photo

        #set sidebar buttons position
        self.home_sidebar_btn.place(relx=0, rely=0.2, anchor="w")
        self.homeIcon.place(relx=0.038, rely=0.2, anchor="w")
        self.userslist_sidebar_btn.place(relx=0, rely=0.25, anchor="w")
        self.userslistIcon.place(relx=0.038, rely=0.25, anchor="w")
        self.notification_sidebar_btn.place(relx=0, rely=0.3, anchor="w")
        self.notificationIcon.place(relx=0.038, rely=0.3, anchor="w")
        self.settings_sidebar_btn.place(relx=0, rely=0.35, anchor="w")
        self.settingsIcon.place(relx=0.038, rely=0.35, anchor="w")
        self.logout_sidebar_btn.place(relx=0, rely=0.4, anchor="w")
        self.logoutIcon.place(relx=0.038, rely=0.4, anchor="w")


        #Stock Settings page
        #Stock Settings page title
        self.pageTitle = ttk.Label(self, text="Stock Settings", foreground="#4D5D69", font=("Livvic Bold", int(SCR_HEIGHT/30)))
        #set widgets position
        self.pageTitle.place(relx=0.23, rely=0.08, anchor="w")
        
        #Stock Settings page Subtitle
        self.pageSubtitle= ttk.Label(self, text="Stock name", foreground="#4D5D69", font=("Livvic SemiBold", int(SCR_HEIGHT/50)))
        #set widgets position
        self.pageSubtitle.place(relx=0.23, rely=0.15, anchor="w")
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
        #stockname section
        self.stocknameLabel = ttk.Label(self, text="Stock name", foreground="#4D5D69", font=("Livvic Regular", int(SCR_HEIGHT/60)))
        self.stocknameLabel.place(relx=0.25, rely=0.25, anchor="w")
        self.stockname_entry = ttk.Entry(self, font=('Livvic Regular', int(SCR_HEIGHT/58)), width=62)
        self.stockname_entry.place(relx=0.25, rely=0.3, anchor="w")
        #Button save
        self.save_btn= ttk.Button(self, text="save", style='sidebar_btn.TButton', padding=(10,10),width=20)
        self.save_btn.place(relx=0.75, rely= 0.3, anchor="w")
        #username section
        self.usernameLabel = ttk.Label(self, text="Username", foreground="#4D5D69", font=("Livvic Regular", int(SCR_HEIGHT/60)))
        self.usernameLabel.place(relx=0.25, rely=0.35, anchor="w")
        self.username_entry = ttk.Entry(self, font=('Livvic Regular', int(SCR_HEIGHT/58)), width=30)
        self.username_entry.place(relx=0.25, rely=0.4, anchor="w")
        #role
        self.roleLabel = ttk.Label(self, text="Role", foreground="#4D5D69", font=("Livvic Regular", int(SCR_HEIGHT/60)))
        self.roleLabel.place(relx=0.49, rely=0.35, anchor="w")
        self.role= ttk.Combobox(self,width=28,values=["edit","view"],height=50,font=("Livvic Regular", int(SCR_HEIGHT/60)))
        self.role.place(relx=0.49, rely=0.4, anchor="w",height=50)
        self.role.set("choose a role")
        #Button add user
        self.add_user_btn= ttk.Button(self, text="add user", style='sidebar_btn.TButton', padding=(10,10),width=20)
        self.add_user_btn.place(relx=0.75, rely= 0.4, anchor="w")
        #users list section
        self.list= ttk.Label(self, text="users list", foreground="#4D5D69", font=("Livvic SemiBold", int(SCR_HEIGHT/60)))
        self.list.place(relx=0.25, rely=0.50, anchor="w")


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

        self.tree.place(relx=0.25, rely=0.70, anchor="w")
        self.controller = controller

    
       



        # #list items
        # style = ttk.Style()
        # style.configure('userslist.Treeview', rowheight=30, padding=5, font=("Livvic Regular", 12))
        # # configure the Treeview heading style
        # style.configure("userslist.Treeview.Heading", font=("Livvic Medium", 14), stretch=False)
        # #items
        # self.tree = ttk.Treeview(self, columns=("Username", "Email", "Role", "Action"), show='headings', style='userslist.Treeview')
        # self.tree.heading("Username", text="Username", anchor="w")
        # self.tree.heading("Email", text="Email", anchor="w")
        # self.tree.heading("Role", text="Role", anchor="w")
        # self.tree.heading("Action", text="Action", anchor="w")
        # self.tree.column('Username', width=300)
        # self.tree.column('Email', width=400)
        # self.tree.column('Role', width=400)
        # self.tree.column('Action', width=120)
        # self.tree.place(relx=0.25, rely=0.70, anchor="w")



        
    
        
    
        
