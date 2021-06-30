import sys
sys.path.append("..")
from src.solver import *
import numpy as np
import cv2
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

thickness =3
width = 106
height = 106
top_left_x = 48
top_left_y = 385

selector_centering = 50
selector_top_left_x = 120
selector_top_left_y = 1503

selector_width = 192
selector_height = 108

#crop the image at the corresponding coordinates in the grid

def read_number(array,x,y):
    result = []
    for i in range (top_left_y + (thickness * y)+(height*(y-1)), top_left_y + (thickness *y )+(height*(y-1))+height):
        result.append([])
        for j in range (top_left_x+ (thickness * x) +(width * (x-1)), top_left_x+(width * (x-1))+ (thickness * x)+width):
            result[-1].append (array[i][j])
    return np.array(result)



#read the number in the cropped image and transform it into an int

def from_pic_to_number(pic):
    result = pytesseract.image_to_string(pic, config='--psm 10')
    result = result[0]
    if result == 'A':
        result = 4
    elif result == '_':
        result  = 0
    else:
        result = int(result)
    return result



#transform screenshot into a 2d array

def from_img_to_array(img):
    result = []
    print("Transforming image into array...")
    progress_num = 0
    progress ="[_____________________________________________________________________________________________________]"
    for y in range (1,10):
        result.append([])
        for x in range(1,10):
            pic = read_number(img,x,y)
            result[-1].append(from_pic_to_number(pic))

        progress_num = int(y / 9 * 100)
        list_progress = list(progress)
        for i in range(progress_num + 1):
            list_progress[1 + i] = '#'
        progress = "".join(list_progress)
        final_string = str(progress_num) + "% " + progress
        print(final_string, end='\r')
    print("\nTransformation finalized")
    return result



#reads an image and transforms it into black and white image (0=black, 255=white)

def read_img_bw(path):
    img = cv2.imread(path, 0)
    print ("Processing image")
    progress_num = 0
    progress ="[_____________________________________________________________________________________________________]"
    for i in range (len(img)):
        for j in range( len (img[0])):
            if (img[i][j] < 150):
                img[i][j] = 0
            else:
                img[i][j] = 255
        progress_num = int(i/(len(img)-1) * 100)
        list_progress = list(progress)
        for i in range (progress_num+1):
            list_progress[1+i] = '#'
        progress = "".join(list_progress)
        final_string = str(progress_num) + "% "+progress
        print(final_string, end = '\r')
    print ("\nImage processed")
    return img



def main():
    pass

if __name__ == '__main__':
    main()
