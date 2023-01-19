from tkinter import *
from PIL import Image, ImageTk
from tkinter import filedialog
import os
import cv2
import numpy as np
from keras.models import load_model

def main():

    os.chdir('C:\\Users\\hp\\Documents\\NED semester1\\PL Project\\archive')


    model_path = "..erajproject.h5"
    vgg_conv=load_model(model_path)



    m=Tk()
    root = Frame(m, width=300, height=300, bd=5, bg="grey")
    root.place(x=10, y=10)
    m.title( '                                                                                                                                                                                    Disease Detection')
    m.state("zoomed")

    img = PhotoImage(file='C:\\Users\\hp\\Documents\\NED semester1\\PL Project\\accessories\\bg.png')
    bg_image = img.subsample(1,1)
    bg_label = Label(root, image=bg_image)
    bg_label.config()
    bg_label.pack(fill=BOTH, expand=True,padx=100)

    frame1= Frame(m, highlightbackground='DarkBlue',highlightthickness=7)
    frame1.place(relx=0.32, rely=0.05, anchor=N)
    label1 = Label(frame1, text="Disease Detection using Chest X-ray", font=("MS Sans Serif", 25), bg='light blue',
                      highlightthickness=0, fg='dark blue')
    label1.pack()


    def open_file():
        # Open a file dialog and get the selected file's path

        image_frame=Frame(m)
        image_frame.place(x=200,y=110)

        f_types = [('Jpeg Files', '.jpeg'), ('Png Files', '.png')]
        file_path = filedialog.askopenfilename(filetypes=f_types)
        im = Image.open(file_path)
        im_1 = im.resize((300,300))
        image = ImageTk.PhotoImage(im_1)
        label = Label(image_frame, image=image)
        label.config(width=300,height=300)
        label.image = image
        label.grid(row=0, column=0)
        pred = predict(file_path)

        frame3= Frame(m)
        frame3.place(relx=0.25, rely=0.85, anchor=N)
        label3 = Label(frame3, text=pred, font=("Times New Roman Bold", 20), bg="light blue"
        ,fg='dark blue')
        label3.pack()

    def predict(file_path1):
        # os.chdir('c:\\Users\hp\Downloads\\archive')

        def prepare(img):
            img = cv2.imread(str(img))
            img = np.array(img)
            img = cv2.resize(img, (224, 224))
            if img.shape[2] == 1:
                img = np.dstack([img, img, img])
            # img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            img = img.astype(np.float32) / 255.
            return img


        test_data = prepare(file_path1)
        arr = np.array(test_data)
        test_data = np.reshape(arr, (1, 224, 224, 3))

        pred = vgg_conv.predict(test_data, batch_size=1)

        if pred[0][0] > pred[0][1]:
            prediction = "NORMAL"
        else:
            prediction = "PNEUMONIC"

        return prediction


    frame2 = Frame(m)
    frame2.place(anchor=N,relx=0.265, rely=0.69 )
    button2 = Button(frame2, text="Upload Chest X-Ray", font=("Times New Roman Bold", 20),bg='azure'
                      ,fg='dark blue',command=open_file)
    button2.pack()

    m.mainloop()

