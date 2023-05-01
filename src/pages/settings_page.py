from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

class SettingsPage(ttk.Frame):
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
        s.configure('sidebar_btn.TButton', font=('Livvic Medium', int(SCR_HEIGHT/64)), background='#9DAAAF', foreground='#38393B', borderwidth=0)
        s.map('sidebar_btn.TButton', background=[('active', '!disabled', '#7d9198')], foreground=[('active', '!disabled', '#38393B')])
        s = ttk.Style()
        s.configure('sidebar_disabled_btn.TButton', font=('Livvic Bold', int(SCR_HEIGHT/64)), background='#9DAAAF', foreground='#38393B', borderwidth=0)
        s.map('sidebar_disabled_btn.TButton', background=[('active', '!disabled', '#7d9198')], foreground=[('active', '!disabled', '#38393B')])
        #create buttons
        from src.pages.home_page import HomePage
        self.home_sidebar_btn = ttk.Button(self, text="Dashboard", style='sidebar_btn.TButton', padding=(120, 10, 131, 10), command=lambda: controller.show_page(HomePage))
        from src.pages.stock_settings_page import StockSettingsPage
        self.userslist_sidebar_btn = ttk.Button(self, text="Users list", style='sidebar_btn.TButton', padding=(120, 10, 150, 10), command=lambda: controller.show_page(StockSettingsPage))
        from src.pages.home_page import HomePage
        self.notification_sidebar_btn = ttk.Button(self, text="Notification", style='sidebar_btn.TButton', padding=(120, 10, 127, 10), command=lambda: controller.show_page(HomePage))
        self.settings_sidebar_btn = ttk.Button(self, text="Settings", style='sidebar_disabled_btn.TButton', padding=(120, 10, 153, 10))
        
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


        #Settings page
        #Settings page title
        self.pageTitle = ttk.Label(self, text="Settings", foreground="#4D5D69", font=("Livvic Bold", int(SCR_HEIGHT/13)))

        #set widgets position
        self.pageTitle.place(relx=0.72, rely=0.19, anchor="center")


        self.controller = controller
