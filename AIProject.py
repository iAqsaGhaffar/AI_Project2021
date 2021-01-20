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

#define variables

Text = StringVar()
private_key = StringVar()
mode = StringVar()
Result = StringVar()

###define function#####
#function to encode

def Encode(key,message):
    enc=[]
    for i in range(len(message)):
        key_c = key[i % len(key)]
        enc.append(chr((ord(message[i]) + ord(key_c)) % 256))
        
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()