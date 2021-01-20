####importing modules####

from tkinter import * #####  Libraries added  ######
import base64

#initialize window
root = Tk()                
root.geometry('600x400')     ### Scaling Window #####
root.resizable(0,0)

#title of the window
root.title("AI_Python - Message Encode and Decode")

#label

Label(root, text ='ENCODE DECODE', font = 'Verdana 20 bold').pack()
Label(root, text ='AI-Python', font = 'Verdana 20 bold').pack(side =BOTTOM)

#define variables

Text = StringVar()
private_key = StringVar()
mode = StringVar()
Result = StringVar()

###define functions#####

#function to encode
def Encode(key,message):
    enc=[]
    for i in range(len(message)):
        key_c = key[i % len(key)]
        enc.append(chr((ord(message[i]) + ord(key_c)) % 256))
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()

######function to decode######

def Decode(key,message):
    dec=[]
    message = base64.urlsafe_b64decode(message).decode()
    for i in range(len(message)):
        key_c = key[i % len(key)]
        dec.append(chr((256 + ord(message[i])- ord(key_c)) % 256))       
    return "".join(dec)

###function to set mode###
def Mode():
    if(mode.get() == 'e'):
        Result.set(Encode(private_key.get(), Text.get()))
    elif(mode.get() == 'd'):
        Result.set(Decode(private_key.get(), Text.get()))
    else:
        Result.set('Mode Invalid')


###Function to exit window###    
def Exit():
    root.destroy()

####Reset Function####
def Reset():
    Text.set("")
    private_key.set("")
    mode.set("")
    Result.set("")
######## Label and Button #######

##Message##

Label(root, font= 'Verdana 12 bold', text='Message').place(x= 60,y=60)
Entry(root, font = 'Verdana 10', textvariable = Text, bg = 'ghost white').place(x=350, y = 60)

###key###
Label(root, font = 'Verdana 12 bold', text ='Key').place(x=60, y = 90)
Entry(root, font = 'Verdana 10', textvariable = private_key , bg ='ghost white').place(x=350, y = 90)

###mode##
Label(root, font = 'Verdana 12 bold', text ='Mode((e)-encode, (d)-decode)').place(x=60, y = 120)
Entry(root, font = 'Verdana 10', textvariable = mode , bg= 'ghost white').place(x=350, y = 120)

##result##
Entry(root, font = 'Verdana 10 bold', textvariable = Result, bg ='ghost white').place(x=350, y = 150)

###result button###
Button(root, font = 'Verdana 10 bold', text = 'Result'  ,padx =5 , pady = 5,bg ='LightGray' ,command = Mode).place(x=260, y = 150)

###reset button###
Button(root, font = 'Verdana 10 bold' ,text ='Reset' ,width =10, command = Reset,bg = 'yellow', padx=8, pady=8).place(x=160, y = 190)

####exit button####
Button(root, font = 'Verdana 10 bold',text= 'Exit' , width = 10, command = Exit,bg = 'red', padx=8, pady=8).place(x=290, y = 190)
root.mainloop()