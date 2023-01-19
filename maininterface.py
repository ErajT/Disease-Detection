from tkinter import *
from PIL import Image
import danyaproject
import project


def back_pn():
        w.destroy()
        project.main()


def back_tb():
    w.destroy()
    danyaproject.main()


w = Tk()
f1 = Frame(w,  bd=5,bg="grey")
f1.place(x=10,y=10)
w.title('                                                                                                                                                                                    Disease Detection')
w.state("zoomed")

im = Image.open("C:\\Users\\hp\\Documents\\NED semester1\\PL Project\\accessories\\bgformain.png")
width, height = im.size
image = PhotoImage(file="C:\\Users\\hp\\Documents\\NED semester1\\PL Project\\accessories\\bgformain.png")
image = image.subsample(1,1)

# Create a label to display the image
label = Label(f1, image=image)
label.config(width=1250, height=625)
label.image = image
label.grid(row=0, column=0)

f3 = Frame(f1)
f3.place(anchor=N, relx=0.28, rely=0.2)

button3 = Label(f3, text="Hello! I am your virtual radiologist.\n Please select the disease you want to detect below", font=("Times New Roman Bold", 24), bg='azure'
                    , fg='dark BLUE')
button3.pack()

f2 = Frame(f1)
f2.place(anchor=N, relx=0.265, rely=0.69)

button2 = Button(f2, text="PNEUMONIA", font=("Times New Roman Bold", 25), bg='azure'
                    , fg='dark BLUE', command=back_pn)
button2.pack()


f4 = Frame(f1)
f4.place(anchor=N, relx=0.265, rely=0.49)

button4 = Button(f4, text="TUBERCULOSIS", font=("Times New Roman Bold", 25), bg='azure'
                    , fg='dark BLUE', command=back_tb)
button4.pack()

w.mainloop()