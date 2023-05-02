from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from src.connect import *
from src.user import *

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


        #Stock Settings page
        #Stock Settings page title
        self.pageTitle = ttk.Label(self, text="Stock Settings", foreground="#4D5D69", font=("Livvic Bold", int(SCR_HEIGHT/30)))
        #set widgets position
        self.pageTitle.place(relx=0.23, rely=0.08, anchor="w")
        
        #Stock Settings page Subtitle
        self.pageSubtitle= ttk.Label(self, text="Stock name", foreground="#4D5D69", font=("Livvic SemiBold", int(SCR_HEIGHT/50)))
        #set widgets position
        self.pageSubtitle.place(relx=0.23, rely=0.15, anchor="w")
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
        #user information widgets position
        self.usergreetingTitle.place(relx=0.92, rely=0.08, anchor="e")
        self.profileIcon.place(relx=0.95, rely=0.08, anchor="center")
        #BODY
        #stockname section
        self.stocknameLabel = ttk.Label(self, text="Stock name", foreground="#4D5D69", font=("Livvic Regular", int(SCR_HEIGHT/60)))
        self.stocknameLabel.place(relx=0.25, rely=0.25, anchor="w")
        self.stockname_entry = ttk.Entry(self, font=('Livvic Regular', int(SCR_HEIGHT/58)), width=61)
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
        self.roleLabel.place(relx=0.5, rely=0.35, anchor="w")
        self.role= ttk.Combobox(self,width=60)
        self.role.place(relx=0.5, rely=0.4, anchor="w")
        #Button add user
        self.add_user_btn= ttk.Button(self, text="add user", style='sidebar_btn.TButton', padding=(10,10),width=20)
        self.add_user_btn.place(relx=0.75, rely= 0.4, anchor="w")
        #users list section
        self.list= ttk.Label(self, text="users list", foreground="#4D5D69", font=("Livvic SemiBold", int(SCR_HEIGHT/60)))
        self.list.place(relx=0.25, rely=0.50, anchor="w")
        #list items
        #username
        self.list_username= ttk.Label(self, text="Username", foreground="#4D5D69", font=("Livvic Medium", int(SCR_HEIGHT/70)))
        self.list_username.place(relx=0.28, rely=0.55, anchor="w")
        #email
        self.list_email= ttk.Label(self, text="Email", foreground="#4D5D69", font=("Livvic Medium", int(SCR_HEIGHT/70)))
        self.list_email.place(relx=0.42, rely=0.55, anchor="w")
        #role
        self.list_role= ttk.Label(self, text="Role", foreground="#4D5D69", font=("Livvic Medium", int(SCR_HEIGHT/70)))
        self.list_role.place(relx=0.65, rely=0.55, anchor="w")
        #actions
        self.list_actions= ttk.Label(self, text="Actions", foreground="#4D5D69", font=("Livvic Medium", int(SCR_HEIGHT/70)))
        self.list_actions.place(relx=0.80, rely=0.55, anchor="w")


        
    
        def get_email(self):
            conn = mysqlconnect()
            cur = conn.cursor()
            username = self.username_entry.get()
            # if username exists
            cur.execute('SELECT * FROM user WHERE username = %s', username)
            result = cur.fetchone()
            email = User(result[3])
            conn.close()
            return email
        
        






        self.controller = controller
