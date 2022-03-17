# OK...I tried using multiple windows in tkinter
# it is possible, but I cannot achieve the complexity
# for the windows appearance that I hoped for.
# will be using a single window here, but if I find
# a way within tkinter, will revise this code
# also, I tried to make a row of radio buttons appear
# like the 'success' label during execution, but I
# could not get any variables to register...next time

# this is the decoder for the encoder

from PIL import Image
import tkinter as tk
from tkinter import scrolledtext
import stepic
from stegano import lsb
from stegano import exifHeader
from stegano import lsbset
from stegano.lsbset import generators
import bleach
import os


# one of four decoding techniques
def stepic_Decoder(imagename, direct_output):
    # Decode the image so as to extract the hidden data from the image
    # Open image file which has the data to exteact
    if os.path.exists(imagename):
        im2 = Image.open(imagename)
        message = stepic.decode(im2)
        
    # display text...    
    if direct_output:
        #output to display
        display_output(message)
     
    else:
        #save as file...
        save_to_file(message)  
       
    success()
 
 
# two of four decoding techniques    
def stegano_lsb_Decoder(imagename, direct_output):
    # Decode the image so as to extract the hidden data from the image
    if os.path.exists(imagename):
        message = lsb.reveal(imagename)
        
    # display text...
    if direct_output:
        display_output(message)
     
    else:
        #save as file...
        save_to_file(message)  
        
    success()
   
# three of four decoding techniques        
def stegano_gen_Decoder(imagename, direct_output):
    # there are several generators than can be used, note to user which one
    print('Using triangular_numbers generator to decode...')
    
    # Decode the image so as to extract the hidden data from the image
    if os.path.exists(imagename):
        message = lsbset.reveal(imagename, generators.triangular_numbers())
    
    # display text...
    if direct_output:
        display_output(message)
     
    else:
        #save as file...
        save_to_file(message)  
            
    success()     
        
# four of four decoding techniques
def stegano_exif_Decoder(imagename, direct_output):
    # Decode the image so as to extract the hidden data from the image
    if os.path.exists(imagename):
        message = exifHeader.reveal(imagename)
 
        # output in bytes class, convert into str...
        message = message.decode()
       
   # display text...
    if direct_output:
        display_output(message)
     
    else:
        #save as file...
        save_to_file(message)    
          
    success()
    
    
def display_output(message):
    message_field.insert(tk.END, message)
   
   
def save_to_file(message):
    with open('encoded_message.txt', 'w') as fw:
        fw.write(message)     
 

# success indicator, appears once encoding and saving finishes
def success():
    label5 = tk.Label(master=frame5, text='Success!!!',bg='blue',
                  fg='white', font=('New Times Roman', 20))

    label5.place(x=430, y=2)
    

# takes in input from GUI
def selection():
    # set direct output to false
    direct_output = False
    
    # get image file name of encoded image
    # ...sanitize user input
    if image_name.get() == '':
        print('No image file name given!!!')
        sys.exit()
    else:
        imagename = bleach.clean(image_name.get()[0:30])
          
     
    # get output choice
    choice1 = var1.get()
    
    if choice1 == 2:
        direct_output = True
    elif choice1 == 1:
        pass
    else:
        print('Please choose output')
        
    # get choice of decoding technique
    choice = var.get()

    if choice == 1:
        stepic_Decoder(imagename, direct_output)
    elif choice == 2:
        stegano_lsb_Decoder(imagename, direct_output)
    elif choice == 3:
        stegano_gen_Decoder(imagename, direct_output)
    elif choice == 4:
        stegano_exif_Decoder(imagename, direct_output)
      

window = tk.Tk()
window.title('Decoder...')

# GUI...
# main header
frame1 = tk.Frame(master=window, width=600, height=70, borderwidth=1,
                  bg='blue')
frame1.pack()

label1 = tk.Label(master=frame1, text='Decoder...',
                  bg='blue', fg='white', font=('New Times Roman', 20))
label1.place(x=250, y=20)

# user entry for image file name 
frame2 = tk.Frame(master=window, width=600, height=50, borderwidth=1,
                  bg='blue')
frame2.pack()

label2 = tk.Label(master=frame2, text='Name of Image File',bg='blue',
                  fg='white', font=('New Times Roman', 20))
label2.place(x=10, y=5)

image_name = tk.Entry(master=frame2, font=('New Times Roman', 15),
                          width=25, bd=0)
image_name.place(x=280, y=12)


# radio buttons for decoding methods and note to user
frame3 = tk.Frame(master=window, width=600, height=160, borderwidth=1,
                  bg='blue')
frame3.pack()

label3 = tk.Label(master=frame3, text='Decoding Technique',bg='blue',
                  fg='white', font=('New Times Roman', 20))
label3.place(x=170, y=25)

var = tk.IntVar()

rbox1 = tk.Radiobutton(master=frame3, text='Stepic', variable=var, value=1,
                       height=2, width=10, bg='alice blue',
                       activebackground='alice blue')
rbox1.place(x=65, y=80)

rbox2 = tk.Radiobutton(master=frame3, text='Stegano_LSB', variable=var, value=2,
                       height=2, width=12, bg='alice blue',
                       activebackground='alice blue')
rbox2.place(x=175, y=80)

rbox3 = tk.Radiobutton(master=frame3, text='Stegano_Gen', variable=var, value=3,
                       height=2, width=13, bg='alice blue',
                       activebackground='alice blue')
rbox3.place(x=297, y=80)

rbox4 = tk.Radiobutton(master=frame3, text='Stegano_exif', variable=var, value=4,
                       height=2, width=13, bg='alice blue',
                       activebackground='alice blue')
rbox4.place(x=425, y=80)
 
r1 = 'First 3 choices good for .png image files...'
r2 = 'choice 4 for .jpg and .tiff image files.'

label3a = tk.Label(master=frame3, text=r1+r2, bg='blue',
                  fg='white', font=('New Times Roman', 12))
label3a.place(x=30, y=135)


# radio buttons for output location (file or display)
frame4 = tk.Frame(master=window, width=600, height=140, borderwidth=1,
                  bg='blue')
frame4.pack()

label4 = tk.Label(master=frame4, text='Output Location',bg='blue',
                  fg='white', font=('New Times Roman', 20))
label4.place(x=180, y=25)

var1 = tk.IntVar()

rbox1 = tk.Radiobutton(master=frame4, text='To File...', variable=var1, value=1,
                       height=2, width=10, bg='alice blue',
                       activebackground='alice blue')
rbox1.place(x=165, y=80)

rbox2 = tk.Radiobutton(master=frame4, text='Displayed', variable=var1, value=2,
                       height=2, width=12, bg='alice blue',
                       activebackground='alice blue')
rbox2.place(x=290, y=80)


# start button and space for success indicator
frame5 = tk.Frame(master=window, width=600, height=70, borderwidth=1,
                  bg='blue')
frame5.pack()

button1 = tk.Button(master=frame5, text='Start', bg='blue',
                    fg='white', font=('New Times Roman', 20), bd=2,
                    activebackground='alice blue', width=8, height=1,
                    command=selection)
button1.place(x=220, y=1)

frame6 = tk.Frame(master=window, width=600, height=150, borderwidth=1,
                  bg='blue')
frame6.pack()

# text box for direct output
message_field = scrolledtext.ScrolledText(master=frame6,
                                              font=('New Times Roman', 15),
                                              width=45, height=4, bd=0,
                                              wrap=tk.WORD)
message_field.place(x=45, y=20)

window.mainloop()

