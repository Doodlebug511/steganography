# OK...I tried using multiple windows in tkinter
# it is possible, but I cannot achieve the complexity
# for the windows appearance that I hoped for.
# will be using a single window here, but if I find
# a way within tkinter, will revise this code
# also, I tried to make a row of radio buttons appear
# like the 'success' label during execution, but I
# could not get any variables to register...next time

from PIL import Image
import tkinter as tk
import stepic
from stegano import lsb
from stegano import exifHeader
from stegano import lsbset
from stegano.lsbset import generators
import bleach
import os
import sys


# one of four encoding techniques
def stepic_A(filename, imagename, direct_input):

    # Open image file in which you want to hide your data
    if os.path.exists(imagename):
        im = Image.open(imagename)

    # to encode text directly, use this...
    if direct_input:
        # convert user input into bytes type first
        filename = bytes(filename, 'utf-8')
        im1 = stepic.encode(im, filename)
        im1.save('stepic_output.png', 'PNG')
    else:
        # to encode file into image and save as .png file
        # open and read the file to be encoded in binary mode...
        if os.path.exists(filename):
            with open(filename, 'rb') as f:
                fc = f.read()

        # if 'too much data' error, use larger .png file
        im1 = stepic.encode(im, fc)
        im1.save('stepic_ouput.png', 'PNG')

    success()


# two of four encoding techniques
def stegano_lsb(filename, imagename, direct_input):

    # to encode text directly, use this...
    if direct_input:
        # encode text directly into image and save
        if os.path.exists(imagename):
            steggy = lsb.hide(imagename, filename)
            steggy.save("stegano_output.png")
    else:
        # to encode file into image and save as .png file
        open_file(filename)

        # encode via lsb in image file and save
        if os.path.exists(imagename):
            steggy = lsb.hide(imagename, fc)
            steggy.save('stegano_output.png')

    success()

# three of four encoding techniques        
def stegano_gen(filename, imagename, direct_input):
    # there are several generators than can be used, 
    # note to user which one
    print('Use triangular_numbers generator to decode...')

    # to encode text directly, use this...
    if direct_input:
        if os.path.exists(imagename):
            secret_image = lsbset.hide(imagename, filename,
                                       generators.triangular_numbers())
            secret_image.save("stegano_tri_numbers_output.png")
    else:
        # to encode file into image and save as .png file
        open_file(filename)

        # encode via generator in image file and save
        if os.path.exists(imagename):
            si = lsbset.hide(imagename, fc, generators.triangular_numbers())
            si.save('stegano_tri_numbers_output.png')

    success()

# four of four encoding techniques
def stegano_exif(filename, imagename, direct_input):
    # to encode text directly...
    if direct_input:
        if os.path.exists(imagename):
            exifHeader.hide(imagename, 'stegano_exif_output.jpg',
                            secret_message=filename)
    
    else:
        # to encode a text file...
        open_file(filename)
    
        # encode in image file and save
        if os.path.exists(imagename):
            exifHeader.hide(imagename, 'stegano_exif_output.jpg', sm)
    
    success()


def open_file(filename):
    # open and read the file to be encoded... 
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            sm = f.read()


# success indicator, appears once encoding and saving finishes
def success():
    label5 = tk.Label(master=frame5, text='Success!!!',bg='blue',
                  fg='white', font=('New Times Roman', 20))

    label5.place(x=430, y=2)


# takes in input from GUI
def selection():
    # set direct user input to false
    direct_input = False

    # get image file name and text file name or user message
    # ...sanitize user input
    if user_text.get() == '' and file_name.get() == '':
        print('No input...')
        sys.exit('No input')

    elif user_text.get() == '':
        filename = bleach.clean(file_name.get()[0:30])
    elif file_name.get() == '':
        filename = bleach.clean(user_text.get()[0:30])
        # if file name entry is blank, assume direct user input
        direct_input = True
    else:
        print('One or the other, please!!')
        sys.exit()

    if image_name.get() == '':
        print('No image file name given!!!')
        sys.exit()
    else:
        imagename = bleach.clean(image_name.get()[0:30])

    # get choice of encoding technique
    choice = var.get()

    if choice == 1:
        stepic_A(filename, imagename, direct_input)
    elif choice == 2:
        stegano_lsb(filename, imagename, direct_input)
    elif choice == 3:
        stegano_gen(filename, imagename, direct_input)
    elif choice == 4:
        stegano_exif(filename, imagename, direct_input)


window = tk.Tk()
window.title('Encoder...')

# GUI...
# main header
frame1 = tk.Frame(master=window, width=600, height=80, borderwidth=1,
                  bg='blue')
frame1.pack()

label1 = tk.Label(master=frame1, text='Encoder...',
                  bg='blue', fg='white', font=('New Times Roman', 20))
label1.place(x=250, y=20)

# user entry for file name or direct user input
frame2 = tk.Frame(master=window, width=600, height=150, borderwidth=1,
                  bg='blue')
frame2.pack()

label2 = tk.Label(master=frame2, text='Name of Text File',bg='blue',
                  fg='white', font=('New Times Roman', 20))
label2.place(x=10, y=5)
label2a = tk.Label(master=frame2, text='or',bg='blue',
                  fg='white', font=('New Times Roman', 20))
label2a.place(x=100, y=33)
label2b = tk.Label(master=frame2, text='Text To Be Encoded',bg='blue',
                  fg='white', font=('New Times Roman', 20))
label2b.place(x=10, y=65)

file_name = tk.Entry(master=frame2, font=('New Times Roman', 15),
                          width=25, bd=0)
file_name.place(x=300, y=12)
user_text = tk.Entry(master=frame2, font=('New Times Roman', 15),
                          width=25, bd=0)
user_text.place(x=300, y=72)

# user entry for image file name
frame3 = tk.Frame(master=window, width=600, height=50, borderwidth=1,
                  bg='blue')
frame3.pack()

label3 = tk.Label(master=frame3, text='Name of Image File',bg='blue',
                  fg='white', font=('New Times Roman', 20))
label3.place(x=10, y=8)

image_name = tk.Entry(master=frame3, font=('New Times Roman', 15),
                          width=25, bd=0)
image_name.place(x=300, y=12)

# radio buttons for encoding methods and note to user
frame4 = tk.Frame(master=window, width=600, height=250, borderwidth=1,
                  bg='blue')
frame4.pack()

label4 = tk.Label(master=frame4, text='Encoding Technique',bg='blue',
                  fg='white', font=('New Times Roman', 20))
label4.place(x=170, y=25)

var = tk.IntVar()

rbox1 = tk.Radiobutton(master=frame4, text='Stepic', variable=var, value=1,
                       height=2, width=10, bg='alice blue',
                       activebackground='alice blue')
rbox1.place(x=65, y=80)

rbox2 = tk.Radiobutton(master=frame4, text='Stegano_LSB', variable=var, 
                       value=2, height=2, width=12, bg='alice blue',
                       activebackground='alice blue')
rbox2.place(x=175, y=80)

rbox3 = tk.Radiobutton(master=frame4, text='Stegano_Gen', variable=var,
                       value=3, height=2, width=13,
                       bg='alice blue', activebackground='alice blue')
rbox3.place(x=297, y=80)

rbox4 = tk.Radiobutton(master=frame4, text='Stegano_exif', variable=var,
                       value=4, height=2, width=13,
                       bg='alice blue', activebackground='alice blue')
rbox4.place(x=425, y=80)

r1 = 'First 3 choices good for .png image files...'
r2 = 'choice 4 for .jpg and .tiff image files.'

label4a = tk.Label(master=frame4, text=r1+r2, bg='blue',
                  fg='white', font=('New Times Roman', 12))
label4a.place(x=30, y=135)

# start button and space for success indicator
frame5 = tk.Frame(master=window, width=600, height=100, borderwidth=1,
                  bg='blue')
frame5.pack()

button1 = tk.Button(master=frame5, text='Start', bg='blue',
                    fg='white', font=('New Times Roman', 20), bd=2,
                    activebackground='alice blue', width=8, height=1,
                    command=selection)
button1.place(x=230, y=1)

window.mainloop()
