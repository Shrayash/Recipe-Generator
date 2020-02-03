import sys

sys.path.append('/users/shrayash/pycharmprojects/venv/lib/site-packages')
import time
import cv2
import pandas as pd
import numpy as np
import csv
from tkinter import *
import tkinter.ttk as ttk
import tkinter as tk
from tkinter.filedialog import askopenfilename
import requests
from PIL import Image, ImageTk


# LOADYOLO
net = cv2.dnn.readNet("yolov3.weights", "yolov3.cfg")
classes = []
confidences = []
class_ids = []
boxes = []
labels = []
with open("coco.names", "r") as f:
    classes = [line.strip() for line in f.readlines()]
layer_names = net.getLayerNames()
outputLayers = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]

def upload_image():
    img = cv2.imread("test1.jpg");
    img = cv2.resize(img, None, fx=0.4, fy=0.4)
    height, width, channels = img.shape
    blob = cv2.dnn.blobFromImage(img, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
    for b in blob:
        net.setInput(blob)
        outs = net.forward(outputLayers)
        # print(outs)


    for out in outs:
        for detection in out:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            if confidence > 0.5:
                # detectobject
                center_x = int(detection[0] * width)
                center_y = int(detection[1] * height)
                w = int(detection[2] * width)
                h = int(detection[3] * height)

                # rectangle
                # Rectangle coordinates
                x = int(center_x - w / 2)
                y = int(center_y - h / 2)
                boxes.append([x, y, w, h])
                confidences.append(float(confidence))
                class_ids.append(class_id)
                number_object_detected = len(boxes)
                indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)

                font = cv2.FONT_HERSHEY_PLAIN
                for i in range(len(boxes)):
                    x, y, w, h = boxes[i]
                    label = classes[class_ids[i]]
                    labels.append(classes[class_ids[i]])
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
                    cv2.putText(img, label, (x, y + 30), font, 1, (0, 0, 0), 3)
                cv2.imshow("image",img)
                cv2.waitKey(0)
                cv2.destroyAllWindows()

def generate():
    ingre = []
    serial = []
    collect_data = []
    collect_index = []
    collect_serial = []
    labs = []
    title = []
    title2 = []
    ingredients = []
    ingredients2 = []
    instructions = []
    list_value=[]
    list_value2 = []
    a = 0
    with open("ingredients_cleaned.csv", "r") as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            ingre.append(row[4])

    for i in labels:
        for idx, j in enumerate(ingre):
            if i == j:
                collect_index.append(idx)
                collect_data.append(i)



    with open("ingredients_cleaned.csv", "r") as f:
        df = csv.reader(f, delimiter=',')
        for row in df:
            serial.append(row[0])
    for i in collect_index:
        for idx, val in enumerate(serial):
            if i == idx:
                collect_serial.append(val)


        df=pd.read_csv('ingredients_cleaned.csv')
        df_data=df[df.serial.isin(collect_serial)]
        df_column=df_data[['title','ingredients','instructions']]
        df_column.to_csv("filtered2.csv")

        with open('filtered2.csv') as f, open('filtered_ingredients.csv', 'w') as csvfile:
        # with open('filtered2.csv') as f:
            reader = csv.DictReader(f, delimiter=',')
            writer = csv.writer(csvfile)
            writer.writerow(['instruction'])
            for row in reader:
                title = row['title']
                title2.append(title)

                ingredients = row['ingredients']
                ingredients2.append(ingredients)

                instructions = row['instructions']
                inst = instructions.split('.')
                for x in inst:
                    if x != '':
                        # list_value=[x]
                        # list_value2.append(list_value)
                        writer.writerow([x])
        instrct=[]
        instrct2=[]
        with open('filtered_ingredients.csv') as f:
            reader = csv.DictReader(f, delimiter=',')
            for row in reader:
                instrct = row['instruction']
                instrct2.append(instrct)


            label['text'] =  tree.insert("", 'end', text="list_value" + str(a), values="Food Name:")
            for ttl in title2:
                if ttl != '':
                    label['text'] = tree.insert("", 'end', text="title" + str(a), values=[ttl])
                    a = a + 1
            label['text'] = tree.insert("", 'end', text="list_value" + str(a), values="                   ")
            label['text'] =  tree.insert("", 'end', text="list_value" + str(a), values="Ingredients:")
            for ing in ingredients2:
                if ing != '':
                    label['text'] = tree.insert("", 'end', text="ingredients" + str(a), values=[ing])
                    a = a + 1
                    label['text'] = tree.insert("", 'end', text="list_value" + str(a), values="                   ")
            label['text'] =  tree.insert("", 'end', text="list_value" + str(a), values="Instructions:")
            label['text'] = tree.insert("", 'end', text="list_value" + str(a), values=[instrct2])
            a = a + 1
            label['text'] =  tree.insert("", 'end', text="list_value" + str(a), values="-------------------end------------------------")


HEIGHT = 600
WIDTH =600
root = tk.Tk()
root.title('Recipe Generator')
canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

image = Image.open("bg2.jpg")
photo = ImageTk.PhotoImage(image)
background_label = tk.Label(root, image=photo)
background_label.place(width=WIDTH,height=HEIGHT)


frame = tk.Frame(root, bg='#80c1ff', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

button = tk.Button(frame, text="Detect Image", font=40, command=upload_image)
button.place(relwidth=0.5, relheight=1)

button = tk.Button(frame, text="Generate Recipe", font=40, command=generate)
button.place(relx=0.5, relheight=1, relwidth=0.5)

lower_frame = tk.Frame(root, bg='#80c1ff', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = tk.Label(lower_frame)
label.place(relwidth=1, relheight=1)



#
width = 500
height =400
screen_width = lower_frame.winfo_screenwidth()
screen_height = lower_frame.winfo_screenheight()
x = (screen_width / 2) - (width / 2)
y = (screen_height / 2) - (height / 2)
root.geometry("%dx%d+%d+%d" % (width, height, x, y))
root.resizable(0, 0)
#
TableMargin = Frame(lower_frame, width=1500)
TableMargin.pack(side=TOP)
scrollbarx = Scrollbar(TableMargin, orient=HORIZONTAL)
scrollbary = Scrollbar(TableMargin, orient=VERTICAL)
tree = ttk.Treeview(TableMargin, columns=("Generated Recipe:"), height=800, selectmode="extended", yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
scrollbary.config(command=tree.yview)
scrollbary.pack(side=RIGHT, fill=Y)
scrollbarx.config(command=tree.xview)
scrollbarx.pack(side=BOTTOM, fill=X)
tree.column('#0', stretch=NO, minwidth=0, width=0)
tree.column('#1', stretch=NO, minwidth=0, width=500)
tree.pack()

# with open('filtered2.csv') as f:
#     reader = csv.DictReader(f, delimiter=',')
#     for row in reader:
#         title = row['title']
#         ingredients = row['ingredients']
#         instructions = row['instructions']
#
#     # label['text'] = title
if __name__ == '__main__':
    root.mainloop()