from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

from src.user import User

class SignupPage(ttk.Frame):
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)

        SCR_HEIGHT = self.winfo_screenheight()

        #Background left side
        # Load background image file
        img = Image.open("assets/background/background.png")
        img = img.resize((SCR_HEIGHT, SCR_HEIGHT), Image.Resampling.LANCZOS)
        self.img = ImageTk.PhotoImage(img)

        # Load logo file
        logo_img = Image.open("assets/icon/logo.png")
        logo_img = logo_img.resize((int(SCR_HEIGHT*0.42), int(SCR_HEIGHT*0.42)), Image.Resampling.LANCZOS)
        self.logo_img = ImageTk.PhotoImage(logo_img)

        self.canvas = Canvas(self, width=self.winfo_screenwidth(), height=SCR_HEIGHT, highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)
        # Set canvas height to window height
        self.canvas.config(height=SCR_HEIGHT)
        # Place image at bottom-left corner with canvas width and image height
        self.canvas.create_image(0, SCR_HEIGHT, image=self.img, anchor="sw", tags="bg")
        # Add logo image on top of background image
        self.canvas.create_image(int(SCR_HEIGHT*0.15), int(SCR_HEIGHT*0.35), image=self.logo_img, anchor="nw")
        # Add text on top of the image
        self.canvas.create_text(int(SCR_HEIGHT/2.63), int(SCR_HEIGHT/1.2), text="STOCK.ME", font=("Livvic Bold", int(SCR_HEIGHT/15)), fill="white", tags="text")
        self.canvas.create_text(int(SCR_HEIGHT/2.63), int(SCR_HEIGHT/1.08), text="Power Up Your Inventory Management: Our App's Got You Covered!", font=("Livvic Medium", int(SCR_HEIGHT/68)), fill="white", tags="text")

        #Form login
        #signup page title
        self.pageTitle = ttk.Label(self, text="SIGN UP", foreground="#4D5D69", font=("Livvic Bold", int(SCR_HEIGHT/13)))
        #entries labels
        self.usernameLabel = ttk.Label(self, text="username", foreground="#4D5D69", font=("Livvic Regular", int(SCR_HEIGHT/60)))
        self.firstnameLabel = ttk.Label(self, text="first name", foreground="#4D5D69", font=("Livvic Regular", int(SCR_HEIGHT/60)))
        self.lastnameLabel = ttk.Label(self, text="last name", foreground="#4D5D69", font=("Livvic Regular", int(SCR_HEIGHT/60)))
        self.emailLabel = ttk.Label(self, text="email", foreground="#4D5D69", font=("Livvic Regular", int(SCR_HEIGHT/60)))
        self.passwordLabel = ttk.Label(self, text="password", foreground="#4D5D69", font=("Livvic Regular", int(SCR_HEIGHT/60)))
        #entries logos
        #Load logo files
        #user icon
        username_img = Image.open("assets/logo/user.png")
        username_img = username_img.resize((25, 25), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(username_img)
        self.usernameIcon = Label(self, image=photo, bd=0)
        self.usernameIcon.image = photo
        #email icon
        email_img = Image.open("assets/logo/email.png")
        email_img = email_img.resize((25, 25), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(email_img)
        self.emailIcon = Label(self, image=photo, bd=0)
        self.emailIcon.image = photo
        #padlock icon
        password_img = Image.open("assets/logo/padlock.png")
        password_img = password_img.resize((25, 25), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(password_img)
        self.passwordIcon = Label(self, image=photo, bd=0)
        self.passwordIcon.image = photo
        #entries
        self.usernameEntry = ttk.Entry(self, font=('Livvic Regular', int(SCR_HEIGHT/58)), width=36)
        self.firstnameEntry = ttk.Entry(self, font=('Livvic Regular', int(SCR_HEIGHT/58)), width=17)
        self.lastnameEntry = ttk.Entry(self, font=('Livvic Regular', int(SCR_HEIGHT/58)), width=17)
        self.emailEntry = ttk.Entry(self, font=('Livvic Regular', int(SCR_HEIGHT/58)), width=36)
        self.passwordEntry = ttk.Entry(self, font=('Livvic Regular', int(SCR_HEIGHT/58)), width=36, show="•")

        #login button
        #style button
        s = ttk.Style()
        s.configure('primary_btn.TButton', font=('Livvic Medium', int(SCR_HEIGHT/48)), padding=(int(SCR_HEIGHT/9), 10), background='#4D5D69', foreground='#FFFFFF', borderwidth=0)
        #create button
        self.signupBTN = ttk.Button(self, text="sign up", style='primary_btn.TButton', bootstyle=PRIMARY, command=self.signup)
        #login message text
        self.loginMessage = ttk.Label(self, text="Already have an account?", foreground="#4D5D69", font=("Livvic Medium", int(SCR_HEIGHT/64)))
        #login button
        #style button
        s = ttk.Style()
        s.configure('secondary_btn.TButton', font=('Livvic Bold', int(SCR_HEIGHT/64)), background='#FFFFFF', foreground='#4D5D69', borderwidth=0)
        s.map('secondary_btn.TButton', background=[('active', '!disabled', '#FFFFFF')], foreground=[('active', '!disabled', '#4D5D69')])
        #create button
        self.loginBTN = ttk.Button(self, text="LOGIN", style='secondary_btn.TButton', command=self.login)

        #set widgets position
        self.pageTitle.place(relx=0.72, rely=0.10, anchor="center")
        #username
        self.usernameLabel.place(relx=0.615, rely=0.25, anchor="center")
        self.usernameIcon.place(relx=0.84, rely=0.30, anchor="center")
        self.usernameIcon.lift()
        self.usernameEntry.place(relx=0.72, rely=0.30, anchor="center")
        #first name
        self.firstnameLabel.place(relx=0.615, rely=0.37, anchor="center")
        self.firstnameEntry.place(relx=0.65, rely=0.42, anchor="center")
        #last name
        self.lastnameLabel.place(relx=0.754, rely=0.37, anchor="center")
        self.lastnameEntry.place(relx=0.789, rely=0.42, anchor="center")
        #email
        self.emailLabel.place(relx=0.602, rely=0.49, anchor="center")
        self.emailIcon.place(relx=0.84, rely=0.54, anchor="center")
        self.emailIcon.lift()
        self.emailEntry.place(relx=0.72, rely=0.54, anchor="center")
        #password
        self.passwordLabel.place(relx=0.615, rely=0.61, anchor="center")
        self.passwordIcon.place(relx=0.84, rely=0.66, anchor="center")
        self.passwordIcon.lift()
        self.passwordEntry.place(relx=0.72, rely=0.66, anchor="center")
        #login btn
        self.signupBTN.place(relx=0.72, rely=0.8, anchor="center")
        #sign up
        self.loginMessage.place(relx=0.692, rely=0.86, anchor="center")
        self.loginBTN.place(relx=0.78, rely=0.86, anchor="center")

        self.controller = controller

    def clear_form(self):
        self.usernameEntry.delete(0, 'end')
        self.firstnameEntry.delete(0, 'end')
        self.lastnameEntry.delete(0, 'end')
        self.emailEntry.delete(0, 'end')
        self.passwordEntry.delete(0, 'end')

    def signup(self):
        username = self.usernameEntry.get()
        firstname = self.firstnameEntry.get().strip()
        lastname = self.lastnameEntry.get().strip()
        email = self.emailEntry.get().strip()
        password = self.passwordEntry.get()

        u = User(username, firstname, lastname, email, password)

        try:
            u.signup()
            self.clear_form()
            self.controller.set_username(username)
            from src.pages.home_page import HomePage
            self.controller.update_page(HomePage)
        except Exception as e:
            errorMessage = e.args[1]
            match e.args[1].split()[5].strip('\''):
                case 'PRIMARY':
                    errorMessage = "Username already exist"
                case 'UC_email':
                    errorMessage = "Email already exist"
            messagebox.showerror("Error", errorMessage)

    def login(self):
        self.clear_form()
        from src.pages.login_page import LoginPage
        self.controller.show_page(LoginPage)
