from tkinter import *
import winsound

root = Tk()#create window
winsound.PlaySound('bee_forest.wav',winsound.SND_ASYNC)#byte_like_object
#winsound.PlaySound('bee_audio.wav',winsound.SND_ASYNC)
# Define a function to create a new window.
def new_window():
    new_root = Toplevel()
    # Add widgets to the new window as desired
    # ...

# Define a function to quit the application
def quit_app():
    root.destroy()

# Load the background image
bg_img = PhotoImage(file="page_1_bg.png")

# Create a label to display the background image
bg_label = Label(root, image=bg_img)
bg_label.pack()

# Load the image for the button
#button_img = PhotoImage(file="C:\\Users\\saisi\\OneDrive\\Desktop\\wise project\\bee3_image.png")
button_img1 = PhotoImage(file="abc.png")
#button_img2 = PhotoImage(file="exit.jpeg")

# Create the button with the image
#button = Button(root, image=button_img)
#button2 = Button(root, image=button_img2, command=new_window)  # Call the new_window function when this button is clicked
button1 = Button(root, image=button_img1, command=quit_app)  # Call the quit_app function when this button is clicked

# Place the button on the background image
#button.place(x=1015, y=600)
button1.place(x=550, y=290)
#button2.place(x=750, y=450)

root.mainloop()


import part2