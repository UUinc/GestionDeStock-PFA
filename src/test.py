from tkinter import *
from PIL import ImageTk, Image

class ExampleFrame(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)

        # Load image file
        img = Image.open("../assets/background/background.png")
        img = img.resize((self.winfo_screenheight(), self.winfo_screenheight()), Image.Resampling.LANCZOS)
        self.img = ImageTk.PhotoImage(img)

        # Load logo file
        logo_img = Image.open("../assets/icon/logo.png")
        logo_img = logo_img.resize((510, 460), Image.Resampling.LANCZOS)
        self.logo_img = ImageTk.PhotoImage(logo_img)

        self.canvas = Canvas(self, width=400, height=400, highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)
        # Set canvas height to window height
        self.canvas.config(height=self.winfo_screenheight())
        # Place image at bottom-left corner with canvas width and image height
        self.canvas.create_image(0, self.winfo_screenheight(), image=self.img, anchor="sw", tags="bg")
        # Add secondary image on top of main image
        self.canvas.create_image(120, 350, image=self.logo_img, anchor="nw")
        # Add text on top of the image
        self.canvas.create_text(self.winfo_screenheight()/2 - 130, self.winfo_screenheight() - 190, text="STOCK.ME", font=("Livvic Bold", 72), fill="white", tags="text")
        self.canvas.create_text(self.winfo_screenheight()/2 - 130, self.winfo_screenheight() - 80, text="Power Up Your Inventory Management: Our App's Got You Covered!", font=("Livvic Medium", 16), fill="white", tags="text")

root = Tk()
frame = ExampleFrame(root)
frame.pack(fill="both", expand=True)
root.state("zoomed")
root.mainloop()
