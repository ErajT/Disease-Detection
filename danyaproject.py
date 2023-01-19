from tkinter import *
import tkinter as tk
import cv2
from PIL import Image, ImageTk
from tkinter import filedialog
import numpy as np
from keras import Sequential
from tkinter import ttk

def main():
    m = Tk()
    root = Frame(m, width=300, height=300, bd=5, bg="grey")
    root.place(x=10, y=10)
    m.title(
        '                                                                                                                                                                                    Disease Detection')
    m.state("zoomed")

    img = PhotoImage(file='C:\\Users\\hp\\Documents\\NED semester1\\PL Project\\accessories\\bg.png')
    bg_image = img.subsample(1, 1)
    bg_label = Label(root, image=bg_image)
    bg_label.config()
    bg_label.pack(fill=BOTH, expand=True, padx=100)

    frame1 = Frame(m, highlightbackground='DarkBlue', highlightthickness=7)
    frame1.place(relx=0.32, rely=0.05, anchor=N)
    label1 = Label(frame1, text="Disease Detection using Chest X-ray", font=("MS Sans Serif", 25), bg='light blue',
                   highlightthickness=0, fg='dark blue')
    label1.pack()




    def open_file():
        f_types=[('Jpg Files','.jpg'),('Png Files','.png'),('Jpeg Files','*.jpeg')]
        filename=filedialog.askopenfilename(filetypes=f_types)
        image_frame=tk.Frame(m)
        image_frame.place(x=200,y=110)
        img=Image.open(filename)
        img_resized=img.resize((300,300))
        img = ImageTk.PhotoImage(img_resized)
        label = tk.Label(image_frame, image=img)
        label.configure(image=img)
        label.image=img
        label.pack()
        var1 = predict(filename)
        frame3 = tk.Frame(m)
        frame3.place(relx=0.25, rely=0.85, anchor=tk.N)
        label3 = tk.Label(frame3, text=var1, font=("Times New Roman Bold", 20), bg="light blue"
                        , fg='dark blue')
        label3.pack()
    def predict(filename):
        import os
        from keras.models import load_model
        os.chdir('C:\\Users\\hp\\Documents\\NED semester1\\PL Project')
        checkpoint_path='C:\\Users\\hp\\Documents\\NED semester1\\PL Project\\archive\\model (1).h5'
        model = load_model(checkpoint_path)
        model.load_weights(checkpoint_path)
        def prepare(filename):
            img=cv2.imread(filename=str(filename))
            img=np.array(img)
            img=cv2.resize(img,(500,500))
            if img.shape[2]==1:
               img = np.dstack([img,img,img])
            # img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
            return img
        test_data=prepare(filename)
        arr=np.array(test_data)
        test_data=np.reshape(arr,(-1,500,500,1))

        pred = model.predict(test_data, batch_size=1)
        index = np.argmax(pred)
        if index == 0:
            var1 = 'TUBERCULOSIS'
        else:
            var1 = 'NORMAL'
        return var1
    frame2=tk.Frame(m)
    frame2.place(anchor=tk.N,relx=0.265,rely=0.69)
    button2=tk.Button(frame2,text="Upload Chest X-Ray",font=('Time New Roman',20),bg='azure',
                      fg='dark blue',command=open_file)
    button2.pack()
    m.mainloop()
