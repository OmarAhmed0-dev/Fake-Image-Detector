#GUI Imports
import tkinter as tk
import customtkinter  as ctk

#Predict and evaluate imports
from PIL import Image , ImageTk
import matplotlib
import pandas as pd
import numpy as np
import seaborn as sns 
from keras.models import load_model
import re
from PIL import Image, ImageChops, ImageEnhance
np.random.seed(2)
import cv2
import tensorflow as tf


#Load Model
model = load_model('GRADUATION PRJECT.h5')

#Setup GUI Window
ctk.set_appearance_mode("light")

ctk.set_default_color_theme("green.json")

app = ctk.CTk()
app.geometry("1000x800")
app.title("Fack Image Detector")
app.iconbitmap("artificial-intelligence.ico")

#Setup GUI Background
backgroundImage = tk.PhotoImage(file="greenBackground.png")
labelBackground = tk.Label(app , image=backgroundImage)
labelBackground.place(x=0 , y=0 , relwidth=1 , relheight= 1)

#Text
label1 = ctk.CTkLabel(master= app , text="Welcome to our Fake Image Detector Project" ,width=190 ,font=("Arial" ,24 ,"bold") ,bg_color="#c5fbc9")
label1.grid(row = 0  , column = 0 , pady = 10)

label2 = ctk.CTkLabel(master = app, text="Upload a photo to check if it is FAKE or REAL" , width=190 ,font=("Arial" ,18 ,"bold"),bg_color="#c5fbc9")
label2.grid(row = 1  , column = 0 , pady = 5)

#Add Image Button
add_photo_img =ImageTk.PhotoImage(Image.open("add-image.png").resize((20,20) , Image.ANTIALIAS))
button = ctk.CTkButton(master = app , image=add_photo_img  , text="Open Photo" , width=220 , height=50 , compound="left"  ,  font=("Helvetica" ,14 ,"bold"),command=lambda:upload_file())
button.grid(row=2 , column=0 , padx=20 , pady=20 )
app.grid_columnconfigure(0, weight=1)


#Global variable for the file path of the uploaded image
filePath=""


#Uploads image
def upload_file():
    f_types = [("all files","*.*"),
               ('PNG Files','*.png'),
               ('Jpg Files', '*.jpg'),
               ('Jpeg Files','*.jpeg')]   # type of files to select 
    filename = ctk.filedialog.askopenfilename(filetypes=f_types)
    col=0 # start from column 1
    row=8 # start from row 3 
   
    img=Image.open(filename) # read the image file
    img=img.resize((400,400)) # new width & height
    img=ImageTk.PhotoImage(img)
    e1 =tk.Label(master = app )
    e1.grid(row=row,column=col)
    e1.image = img # keep a reference! by attaching it to a widget attribute
    e1['image']=img # Show Image  
    filePath=filename


    #Image Prediction checking Button
    button_fake = ctk.CTkButton(app ,  text= "Check" ,  width=220 , height=50 , compound="left"  ,  font=("Helvetica" ,14 ,"bold") ,command= lambda:predict(filePath))
    button_fake.grid(row = 9 , column = 0 , pady =12)

    image_size = (128,128)
    

    #from Predict and evaluate
    def ela_image(filePath, quality=98):
        temp_filename = 'temp_file_name.jpg'
        ela_filename = 'temp_ela.png' 
        image = Image.open(filePath).convert('RGB')
        image.save(temp_filename, 'JPEG', quality = quality)
        temp_image = Image.open(temp_filename)
        ela_image = ImageChops.difference(image, temp_image)
        extrema = ela_image.getextrema()
        max_diff = max([ex[1] for ex in extrema])
        if max_diff == 0:
            max_diff = 1
        scale = 255.0 / max_diff 
        ela_image = ImageEnhance.Brightness(ela_image).enhance(scale)  
        return ela_image
    def preprocessing(image_path):
        return np.array(ela_image(image_path).resize(image_size)).flatten()/255

    def predict(filePath):
        img = preprocessing(filePath).reshape(-1,128,128,3)
        prediction = model.predict(img)
        if prediction[0][1] > prediction[0][0] :
            show_prediction_result("Real")
        else:
            show_prediction_result("Fake")



#Image Prediction result window
def show_prediction_result(x1):
    if(x1 == "Real"):
        newFrame = ctk.CTkFrame(master=app , width=300 , height=200 , fg_color="#c5fbc9" )
        newFrame.place(relx=0.5 , rely = 0.5 , anchor="center")
        labelX = tk.Label(newFrame , text="Real Image" ,font=("Arial" ,18 ,"bold") ,bg="#c5fbc9")
        labelX.place(relx=0.5 , rely = 0.2 , anchor="center" )
        button = ctk.CTkButton(master = newFrame , image=add_photo_img  , text="Try Again" , width=220 , height=50 , compound="left"  ,  font=("Helvetica" ,14 ,"bold"),command=lambda:upload_file())
        button.place(relx=0.5 , rely = 0.5 , anchor="center" )
    else:
        newFrame = ctk.CTkFrame(master=app , width=300 , height=200 , fg_color="#c5fbc9" )
        newFrame.place(relx=0.5 , rely = 0.5 , anchor="center")
        labelX = tk.Label(newFrame , text="Fake Image" ,font=("Arial" ,18 ,"bold") , bg="#c5fbc9")
        labelX.place(relx=0.5 , rely = 0.2 , anchor="center" )
        button = ctk.CTkButton(master = newFrame , image=add_photo_img  , text="Try Again" , width=220 , height=50 , compound="left"  ,  font=("Helvetica" ,14 ,"bold"),command=lambda:upload_file())
        button.place(relx=0.5 , rely = 0.5 , anchor="center" )


fake_real = tk.StringVar()
fake_real_lable = tk.Label(app,textvariable=fake_real,fg='red' ,font=("Arial" ,18 ,"bold"))

fake_real.set("")
fake_real_lable



app.mainloop()