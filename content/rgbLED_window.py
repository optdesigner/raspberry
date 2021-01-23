from tkinter import *
import RPi.GPIO as GPIO
from YourBox import Linebox


def on_closing():
    print("close")    
    window.destroy()
    GPIO.cleanup()

if __name__ == "__main__":
    window = Tk()
    rgbLed = Linebox(window)
    window.protocol("WM_DELETE_WINDOW",on_closing)
    window.mainloop()