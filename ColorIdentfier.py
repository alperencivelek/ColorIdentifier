import os
import cv2
import numpy as np
import pandas as pd
import tkinter as tk
from tkinter import filedialog
root = tk.Tk()
root.withdraw()
img_path=filedialog.askopenfilename(initialdir=os.getcwd())
img=cv2.imread(img_path)

clicked=False
red=green=blue=xposition=yposition=0

index=["color","color_name","hex","Red","Green","Blue"]
csv=pd.read_csv("colors.csv",names=index, header=None)

def getColorName(Red,Green,Blue):
    min=10000
    for i in range (len(csv)):
        distance=abs(Red-int(csv.loc[i,"Red"]))+abs(Green-int(csv.loc[i,"Green"]))+abs(Blue-int(csv.loc[i,"Blue"]))
        if(distance<=min):
            min=distance
            color_name=csv.loc[i,"color_name"]
    return color_name

def pick_color_from_image(event,x,y,flags,param):
    if event==cv2.EVENT_LBUTTONDBLCLK:
        global red,green,blue,xposition,yposition,clicked
        clicked=True
        xposition=x
        yposition=y
        blue,green,red=img[y,x]
        red=int(red)
        green=int(green)
        blue=int(blue)

cv2.namedWindow("Image")
cv2.setMouseCallback("Image",pick_color_from_image)

while True:
    cv2.imshow("Image",img)
    if(clicked):
        cv2.rectangle(img,(20,20),(750,60),(blue,green,red), -1)
        text=getColorName(red,green,blue) + " R=" + str(red) + " G=" + str(green) + " B=" + str(blue)
        cv2.putText(img,text,(50,50),2,0.8,(255,255,255),2,cv2.LINE_AA)
        if(red+blue+green>=600):
            cv2.putText(img, text, (50, 50), 2, 0.8, (0, 0, 0), 2, cv2.LINE_AA)
        clicked=False

    if cv2.waitKey(20) & 0xFF==27:
        break
cv2.destroyAllWindows()




