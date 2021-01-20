##importing modules

from tkinter import *
import base64

#initialize window
root = Tk()
root.geometry('500x300')
root.resizable(0,0)
#title of the window
root.title("DataFlair - Message Encode and Decode")

#label

Label(root, text ='ENCODE DECODE', font = 'arial 20 bold').pack()
Label(root, text ='DataFlair', font = 'arial 20 bold').pack(side =BOTTOM)
