import pandas as pd
import cv2
import pytesseract
import cv2
import numpy as np
import matplotlib.pyplot as plt
import os
import shutil
from craft_text_detector import Craft
import os
from PIL import Image




def move_of_the_end_process(image_filename,folder_path):
    txt=image_filename.split(("."))[0]+".txt"
    to_path="./Done/"
    create_folder_if_not_exists(to_path)
    shutil.move(folder_path+image_filename,to_path+image_filename)
    shutil.move(folder_path+txt,to_path+txt)
    # print(f"Image {image_filename.split(("."))[0]} is finished")    python 3.12
    print("Image {} is finished".format(image_filename.split(".")[0]))   #python 3.8
def create_folder_if_not_exists(folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)        
def sorting_alg(boxes_arr):
    """
    Sorts a numpy array of boxes based on their vertical and horizontal positions.

    Args:
    boxes_arr: numpy array of boxes, where each box is represented by an array of four points.
               The shape of the array is (n_boxes, 4, 2), where n_boxes is the number of boxes, 
               4 represents the four points of each box, and 2 represents the x and y coordinates 
               of each point.

    Returns:
    sorted_boxes_arr: a flattened numpy array of sorted boxes, where each box is represented by an
                      array of four points. The shape of the array is (n_boxes, 4, 2), where n_boxes 
                      is the number of boxes, 4 represents the four points of each box, and 2 
                      represents the x and y coordinates of each point. The boxes are sorted first 
                      based on their vertical position (y-coordinate), and then based on their 
                      horizontal position (x-coordinate) in descending order.

    """
    # check if the passed argument is empty
    if len(boxes_arr)==0:
        return boxes_arr


    # group boxes according to their position
    def group_boxes(boxes_arr, d):
        """
        Groups boxes based on their vertical position, where boxes whose vertical distance is less
        than or equal to d are grouped together.

        Args:
        boxes_arr: numpy array of boxes, where each box is represented by an array of four points.
                   The shape of the array is (n_boxes, 4, 2), where n_boxes is the number of boxes, 
                   4 represents the four points of each box, and 2 represents the x and y coordinates 
                   of each point.
        d: maximum vertical distance between boxes that should be grouped together which is determined by the max. veryical edge

        Returns:
        groups: list of numpy arrays, where each numpy array represents a group of boxes.

        """
        
        # Get center y-value of each box
        centers = np.mean(boxes_arr, axis=1)[:, 1]

        # Sort boxes by their center y-value
        sorted_indices = np.argsort(centers)
        sorted_boxes = boxes_arr[sorted_indices]
        # centers = np.sort(centers)
        centers= centers[sorted_indices]

        # Initialize list to hold position-similar boxes in groups
        groups = []

        # initialize the first with the first box
        current_group = [sorted_boxes[0]]

        # Loop over boxes and group them together
        for i in range(1, len(sorted_boxes)):
            # Calculate distance between centers of current box and the dominant 
            # box of the current group
            dist = abs(np.mean(current_group, axis=1)[0, 1] - centers[i])

            # If distance is less than d, add box to current group
            if dist <= d:
                current_group.append(sorted_boxes[i])

            # If distance is greater than d, start a new group
            else:
                groups.append(np.array(current_group))
                current_group = [sorted_boxes[i]]

        # Add last group to list
        groups.append(np.array(current_group))

        # Return groups
        return groups
    
    # sort groups
    def sort_groups(groups):
        """
        Sorts boxes in each group based on their position.

        Args:
            groups (list): A list of groups, where each group is a numpy.ndarray of boxes.

        Returns:
            numpy.ndarray: A sorted array of boxes, where each box is represented by an array of 4 points.

        """
        # For each group, sort the boxes based on their center 
        # x-coordinate
        sorted_boxes = []
        for group in groups:
            centers_x = np.mean(group, axis=1)[:, 0]
            sorted_idxs = np.argsort(centers_x)[::-1]
            sorted_boxes.append(group[sorted_idxs])
        
        # Combine the sorted boxes from all groups into a 
        # 3D numpy array
        sorted_boxes_arr = np.concatenate(sorted_boxes)
        
        return sorted_boxes_arr
    
    # calculate the dominant vertical distance of eaxh box
    verticals= abs(boxes_arr[:,0,1]- boxes_arr[:,3,1])

    # group boxes
    grouped_boxes= group_boxes(boxes_arr, max(verticals)/2)

    # spread sorted boxes into the result
    sorted_boxes= sort_groups(grouped_boxes)
    
    return sorted_boxes
def draw_boxes(boxes):
    fig, ax = plt.subplots()
    max_x = 0
    max_y = 0
    for i, points in enumerate(boxes):
        x = [point[0] for point in points]
        y = [point[1] for point in points]
        max_x = max(max_x, max(x))
        max_y = max(max_y, max(y))
        ax.plot(x, y)
        ax.plot([x[3], x[0]], [y[3], y[0]])

        ax.scatter(x[1], y[1])
        center_x = sum(x) / 4
        center_y = sum(y) / 4
        ax.text(
            center_x,
            center_y,
            str(i),
            horizontalalignment="center",
            verticalalignment="center",
        )
    ax.set_xlim(0, max_x)
    ax.set_ylim(0, max_y)
    plt.show()
def extract_word(img,boxes,image_filename):
    i=0
    # kernel = np.ones((2,2),np.uint8)
    # # print("Image shape before conversion:", img.shape)
    # grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # # grey = cv2.GaussianBlur(grey,(3,3),0)
    # # ret3,img = cv2.threshold(grey,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    # img = cv2.morphologyEx(grey, cv2.MORPH_OPEN, kernel)
    doc=[]
    print(image_filename)
    recimg=Image.open(image_filename)
    recimg = np.array(recimg)
    qqq=boxes[::-1]
    for box in boxes:
        # print(box)
        x_box_arr=[]
        y_box_arr=[]
        for b in box:
            x_box_arr.append(b[0])
            y_box_arr.append(b[1])
        x_box_max=max(x_box_arr)
        y_box_max=max(y_box_arr)
        x_box_min=min(x_box_arr)
        y_box_min=min(y_box_arr)
        imgb=img[y_box_min:y_box_max,x_box_min:x_box_max]
        cv2.rectangle(recimg, (x_box_min, y_box_min), (x_box_max, y_box_max), (0, 255, 0), 2)
        # print(imgb)
        doc.append(imgb)
        # f=f"./out/{image_filename.split(("/"))[-1].split(".")[0]}/" #python 3.12
        f = os.path.join("./out", image_filename.split("/")[-1].split(".")[0], "") #python 3.8
        create_folder_if_not_exists(f)
        cv2.imwrite(f"{f}{i}.jpg",imgb)
        cv2.imwrite(f"{f}Original.jpg",img)
        
        i=i+1
    cv2.imwrite(f"{f}Detected_words.jpg",recimg)
    # print(boxes[0])
    # cv2.imwrite("output_image.jpg", img)
    return doc
def ocr(doc,image_name):
    # image=cv2.imread("aaa.jpeg")
# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    text=[]
    custom_config = r'--oem 1 --psm 8 -l ara-Amiri'  # Arabic   ara-Amiri language configuration = ara , amiri=ara-Amiri ,ara-Amiri-layer,ara-Amiri-layer
    # d = pytesseract.image_to_string(gray, config=custom_config)
    create_folder_if_not_exists("result/Out/")
    file_path = f"result/Out/{image_name}_OCR.txt"

    # Open the file in write mode ('w')


    for d in doc:
        t = pytesseract.image_to_string(d, config=custom_config)
        t=t.replace('\n\x0c', ' ')
        t=t.replace('\u200f', ' ')
        t=t.replace('\u200e', ' ')
        t=t.replace('\x0c', ' ')
        text.append(t)
        
    print(text)
    # x=text.replace('\n', '$')

    with open(file_path, 'w+',encoding='utf-8') as f:
        # Write the string to the file
        for t in text:
            
            f.write(t)
    print("String written to file successfully.")
    return text
def extract_text_craft(image,output_dir):
    craft = Craft(output_dir=output_dir, crop_type="box", cuda=False, weight_path_craft_net=r'weights\craft_mlt_25k.pth', weight_path_refine_net=r'weights\craft_refiner_CTW1500.pth')

    # apply craft text detection and export detected regions to output directory
    prediction_result = craft.detect_text(image)
    # print(prediction_result["text_crop_paths"])











