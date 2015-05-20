from Tkinter import *
from ucasts import ID12LA
import RPi.GPIO as GPIO
import os
import sys

GPIO.setmode(GPIO.BCM)
GPIO.setup(10, GPIO.OUT)
GPIO.output(10,GPIO.LOW)

def toggle():
	if GPIO.input(10):
		GPIO.output(10,GPIO.LOW)
		toggleButton["text"]="Direction"
		photo = PhotoImage(file="Capture.gif")
		label = Label(root, image=photo)
		label.photo = photo
		label.pack()
		
	else:
		GPIO.output(10, GPIO.HIGH)
		toggleButton["text"] = "Information"
	
def numtest():
	reader = ID12LA()
	tag = reader.wait_for_scan()
	print("Scan: %s") % (tag)
	
switch(tag)
{ 
	case string.hexdigits(6F005CA30A9A:
		print("Welcome Hafiy");
		break;
	case 6F005C86AF1A:
		print("Welcome Haziq");
		break;
	case 6F005CB7BC38:
		print("Welcome Druggie");
		break;
	default:
		print("Tag error");
	break;
}

clear = lambda : os.system('clear')
clear()

root = Tk()
root.title("RP Clinic")
print("Scan tag")

toggleButton = Button(root, text="Direction", command=toggle)
toggleButton.pack(side=RIGHT)

quitButton = Button(root, text="Scan new", command=exit)
quitButton.pack(side=LEFT)

numtest()
root.mainloop()