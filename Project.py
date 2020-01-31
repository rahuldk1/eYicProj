import Tkinter as tk
import RPi.GPIO as GPIO
import time



GPIO.setmode(GPIO.BCM)
GPIO.setup(14,GPIO.IN)
GPIO.setup(15,GPIO.IN)
GPIO.setup(13,GPIO.IN)
GPIO.setup(12,GPIO.IN)


window = tk.Tk()
window.title("Growth Box")
window.geometry("600x800")



def UPDATE():
    Val_Huminity = GPIO.input(14)
    Val_Temp =GPIO.input(15)
    tbox1.delete(1.0,tk.END)
    tbox2.delete(1.0,tk.END)
    tbox1.insert(tk.END,Val_Huminity)
    tbox2.insert(tk.END,float(Val_Temp*0.488))
    verified = tk.Label(text = "Values Verified ! Status OK ",anchor = "center",font = ("Times new Roman",8))
    verified.place(x=150,y=350,anchor="center")
    window.update()
    time.sleep(5)
    verified.destroy()
    window.update()
    
title = tk.Label(text = "GROWTH BOX",bd = 10,anchor = "center",font = ("Times new roman",15))
title.place(x=300,y=30,anchor="center")


title2 = tk.Label(text = "Currently Monitoring 2 sensors...",anchor = "center",font = ("Times ew roman",10))
title2.place(x=100,y=100,anchor="center")


humid = tk.Label(text = "Humidity Sensor : ",anchor = "center",font = ("Times new Roman",8))
humid.place(x=100,y=200,anchor="center")

temp = tk.Label(text = "Tempreture Sensor : ",anchor = "center",font = ("Times new Roman",8))
temp.place(x=100,y=250,anchor="center")


start = tk.Button(text = "UPDATE",command = UPDATE)
start.place(x=300,y= 350,anchor="center")



tbox1 = tk.Text(master = window,height = 1,width = 25)
tbox1.place(x=400,y=200,anchor="center")

tbox2 = tk.Text(master = window,height = 1,width = 25)
tbox2.place(x=400,y=250,anchor="center")


window.mainloop()


