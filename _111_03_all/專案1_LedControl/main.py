import tkinter as tk
from PIL import Image,ImageTk
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("private/raspberry1-58efc-firebase-adminsdk-tzk5o-2743aa1e4a.json")
firebase_admin.initialize_app(cred,{
    'databaseURL': 'https://raspberry1-58efc-default-rtdb.firebaseio.com/'
})

led = db.reference('ledControl')

class LightButton(tk.Button):
    def __init__(self,parent,**kwargs):
        super().__init__(parent,**kwargs)
        #建立圖片
        ##建立close的圖片
        close_image = Image.open('light_close.png')
        self.close_photo = ImageTk.PhotoImage(close_image)
        ##建立open的圖片
        open_image = Image.open('light_open.png')
        self.open_photo = ImageTk.PhotoImage(open_image)

    def open(self):
        self.config(image=self.open_photo)

    def close(self):
        self.config(image=self.close_photo);   

class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        #建立title
        self.title("LED Controller")

        #建立按鈕

        self.btn = LightButton(self,padx=50,pady=30,font=('arial',18),command=self.userClick)
        self.btn.pack(padx=50,pady=30)
        currentState = led.get()['led']
        if currentState:
           self.btn.close()
        else:
           self.btn.open()
    
    def userClick(self):
        currentState = led.get()['led']
        led.update({'led':not currentState})
        if currentState:
           self.btn.open()
        else:
           self.btn.close()


def main():
    window = Window()
    window.mainloop()

if __name__ == "__main__":
    main()