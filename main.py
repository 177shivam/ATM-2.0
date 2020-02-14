from tkinter import *
import threading as t
from time import sleep
import pyqrcode 
from pyqrcode import QRCode
from reportlab.graphics import renderPDF
from svglib.svglib import svg2rlg
import random
import time
import string
import tkinter as tk
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
GPIO.cleanup()
import os

flag=False

reader = SimpleMFRC522()
import pyrebase as pyrebase
config = {
  "apiKey": "AIzaSyDGitbXcZNZrjvLyFAbcMNAAcDT_SDRx6o",
  "authDomain": "agshack-a80f1.firebaseapp.com",
  "databaseURL": "https://agshack-a80f1.firebaseio.com/",
  "storageBucket": "",
  "serviceAccount": "agshack-a80f1-firebase-adminsdk-baydy-c53fa0f114.json"
}
firebase = pyrebase.initialize_app(config)
db = firebase.database()
tk = tk.Tk()
tk.title("Welcome to bank") 
tk.geometry("700x500")
#tk.attributes("-fullscreen", True)
frame= Frame(tk, borderwidth=2)
frame.pack(expand=1, fill=BOTH)
amount=""
pin=""
cid="12345"
def clearFrame():
    list = frame.winfo_children()
    for l in list:
         l.destroy()
def displayMenu():
	clearFrame()
	button1 = Button(frame, text="Balance", font='Times 20 bold', bg='gray', fg='white', height=2, width=14)
	button1.grid(row=0, column=0, padx=(35, 35),pady=(35, 35))
	button2 = Button(frame, text='Cash Withdraw', font='Times 20 bold', bg='gray', fg='white', height=2, width=14)
	button2.grid(row=0, column=1,padx=(85, 35),pady=(35, 35))
	button3 = Button(frame, text='Mini Satement',font='Times 20 bold', bg='gray', fg='white', height=2, width=14)
	button3.grid(row=1, column=0,padx=(35, 35),pady=(35, 35))
	button4 = Button(frame, text='Change PIN',font='Times 20 bold', bg='gray', fg='white', height=2, width=14)
	button4.grid(row=1, column=1,padx=(85, 35),pady=(35, 35))
	button5 = Button(frame, text='QR print',font='Times 20 bold', bg='gray', fg='white', height=2, width=14, command=lambda: qrPage())
	button5.grid(row=2, column=0,padx=(35, 35),pady=(35, 35))
	button6 = Button(frame, text='Transfer',font='Times 20 bold', bg='gray', fg='white', height=2, width=14)
	button6.grid(row=2, column=1,padx=(85, 35),pady=(35, 35))
    
def qrPage():
	clearFrame()
	label = Label( frame, text="Please enter amount", font='Times 20 bold', fg='black')
	label.place(relx=0.5, rely=0.2, anchor=CENTER)
	showAmount=Text(frame, font='Times 30 bold', height=1, width=10,  wrap=WORD)
	showAmount.grid(row= 1, column=4)
	num1 = Button(frame, text="1", font='Times 20 bold', bg='gray', fg='white', height=2, width=2,  command=lambda: numTapAmount("1", showAmount))
	num1.grid(row=0, column=0, padx=(20, 20),pady=(120, 20))
	num2 = Button(frame, text="2", font='Times 20 bold', bg='gray', fg='white', height=2, width=2,  command=lambda: numTapAmount("2", showAmount))
	num2.grid(row=0, column=1, padx=(20, 20),pady=(120, 20))
	num3 = Button(frame, text="3", font='Times 20 bold', bg='gray', fg='white', height=2, width=2,  command=lambda: numTapAmount("3", showAmount))
	num3.grid(row=0, column=2, padx=(20, 20),pady=(120, 20))
	num4 = Button(frame, text="4", font='Times 20 bold', bg='gray', fg='white', height=2, width=2,  command=lambda: numTapAmount("4", showAmount))
	num4.grid(row=1, column=0, padx=(20, 20),pady=(20, 20))
	num5 = Button(frame, text="5", font='Times 20 bold', bg='gray', fg='white', height=2, width=2,  command=lambda: numTapAmount("5", showAmount))
	num5.grid(row=1, column=1, padx=(20, 20),pady=(20, 20))
	num6 = Button(frame, text="6", font='Times 20 bold', bg='gray', fg='white', height=2, width=2,  command=lambda: numTapAmount("6", showAmount))
	num6.grid(row=1, column=2, padx=(20, 20),pady=(20, 20))
	num7 = Button(frame, text="7", font='Times 20 bold', bg='gray', fg='white', height=2, width=2,  command=lambda: numTapAmount("7", showAmount))
	num7.grid(row=2, column=0, padx=(20, 20),pady=(20, 20))
	num8 = Button(frame, text="8", font='Times 20 bold', bg='gray', fg='white', height=2, width=2,  command=lambda: numTapAmount("8", showAmount))
	num8.grid(row=2, column=1, padx=(20, 20),pady=(20, 20))
	num9 = Button(frame, text="9", font='Times 20 bold', bg='gray', fg='white', height=2, width=2,  command=lambda: numTapAmount("9", showAmount))
	num9.grid(row=2, column=2, padx=(20, 20),pady=(20, 20))
	num0 = Button(frame, text="0", font='Times 20 bold', bg='gray', fg='white', height=2, width=2,  command=lambda: numTapAmount("0", showAmount))
	num0.grid(row=3, column=1, padx=(20, 20),pady=(20, 20))
	confirm = Button(frame, text="CONFIRM", font='Times 20 bold', bg='gray', fg='white', height=2, width=9, command=lambda: pinPage())
	confirm.grid(row=3, column=6, padx=(20, 20),pady=(20, 20))

def numTapAmount(input, showAmount):
	global amount
	amount=amount+input
	showAmount.delete(1.0,END)
	showAmount.insert(INSERT, "Rs: "+amount)
	#print(amount)
def pinPage():
	clearFrame()
	label = Label( frame, text="Please enter PIN", font='Times 20 bold', fg='black')
	label.place(relx=0.5, rely=0.2, anchor=CENTER)
	showPIN=Text(frame, font='Times 30 bold', height=1, width=10,  wrap=WORD)
	showPIN.grid(row= 1, column=4)
	num1 = Button(frame, text="1", font='Times 20 bold', bg='gray', fg='white', height=2, width=2,  command=lambda: numTapPIN("1", showPIN))
	num1.grid(row=0, column=0, padx=(20, 20),pady=(120, 20))
	num2 = Button(frame, text="2", font='Times 20 bold', bg='gray', fg='white', height=2, width=2,  command=lambda: numTapPIN("2", showPIN))
	num2.grid(row=0, column=1, padx=(20, 20),pady=(120, 20))
	num3 = Button(frame, text="3", font='Times 20 bold', bg='gray', fg='white', height=2, width=2,  command=lambda: numTapPIN("3", showPIN))
	num3.grid(row=0, column=2, padx=(20, 20),pady=(120, 20))
	num4 = Button(frame, text="4", font='Times 20 bold', bg='gray', fg='white', height=2, width=2,  command=lambda: numTapPIN("4", showPIN))
	num4.grid(row=1, column=0, padx=(20, 20),pady=(20, 20))
	num5 = Button(frame, text="5", font='Times 20 bold', bg='gray', fg='white', height=2, width=2,  command=lambda: numTapPIN("5", showPIN))
	num5.grid(row=1, column=1, padx=(20, 20),pady=(20, 20))
	num6 = Button(frame, text="6", font='Times 20 bold', bg='gray', fg='white', height=2, width=2,  command=lambda: numTapPIN("6", showPIN))
	num6.grid(row=1, column=2, padx=(20, 20),pady=(20, 20))
	num7 = Button(frame, text="7", font='Times 20 bold', bg='gray', fg='white', height=2, width=2,  command=lambda: numTapPIN("7", showPIN))
	num7.grid(row=2, column=0, padx=(20, 20),pady=(20, 20))
	num8 = Button(frame, text="8", font='Times 20 bold', bg='gray', fg='white', height=2, width=2,  command=lambda: numTapPIN("8", showPIN))
	num8.grid(row=2, column=1, padx=(20, 20),pady=(20, 20))
	num9 = Button(frame, text="9", font='Times 20 bold', bg='gray', fg='white', height=2, width=2,  command=lambda: numTapPIN("9", showPIN))
	num9.grid(row=2, column=2, padx=(20, 20),pady=(20, 20))
	num0 = Button(frame, text="0", font='Times 20 bold', bg='gray', fg='white', height=2, width=2,  command=lambda: numTapPIN("0", showPIN))
	num0.grid(row=3, column=1, padx=(20, 20),pady=(20, 20))
	confirm = Button(frame, text="CONFIRM", font='Times 20 bold', bg='gray', fg='white', height=2, width=9, command=lambda: pinCheckPage())
	confirm.grid(row=3, column=6, padx=(20, 20),pady=(20, 20))

def numTapPIN(input,showPIN):
	global pin
	pin+=input
	showPIN.insert(INSERT,"*" )
	#print(pin)
def pinCheckPage():
	clearFrame()
	label = Label( frame, text="Please wait", font='Times 20 bold', fg='black')
	label.place(relx=0.5, rely=0.5, anchor=CENTER)
	if(validatePIN()):
	   qrGenerateUser()
	else:
	   global pin
	   global amount
	   pin=""
	   amount=""
	   displayWelcome()
def qrGenerateUser():
	qrid=string_generator()
	data ={"cid": cid, "timeStamp": time.time(), "amount":int(amount)}
	db.child("generatedQR").child(qrid).set(data)
	s = qrid
	
	url = pyqrcode.create(s)
	url.svg(qrid+".svg", scale = 8)
	drawing = svg2rlg(str(qrid)+".svg")
	renderPDF.drawToFile(drawing, str(qrid)+".pdf", autoSize=0)
	os.system("scp "+str(qrid)+".pdf"+" satinder@10.42.0.1:/home/satinder/Desktop/qr")
def validatePIN():
	global pin
	dbPin=db.child("pin").child(cid).get().val()
	return pin==str(dbPin)

def displayWelcome():
        ourMessage ='Welcome to ATM 2.0'
        messageVar = Message(master=frame, text = ourMessage, font='Times 30 bold', justify=CENTER, width="300")
        messageVar.config(bg='lightgreen')
        messageVar.place(relx=0.5, rely=0.5, anchor=CENTER)
        label = Label( frame, text="Please enter your card", font='Times 20 bold', fg='black')
        label.place(relx=0.5, rely=0.6, anchor=CENTER)
        print(flag)
        
            
        
def key():
    global flag
    try:
        id,text=reader.read()
        displayMenu()
    except:
        pass
    finally:
        GPIO.cleanup()
def string_generator(size=12, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))
    
def man():
    displayWelcome()
    tk.mainloop() 
 
   
t1=t.Thread(target=key)
t1.start()
man()

