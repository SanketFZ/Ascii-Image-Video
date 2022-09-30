from PIL import Image, ImageDraw, ImageFont
import glob
import numpy as np
import math
import cv2,sys,os
chars = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1{}[]?-_+~<>i!lI;:,\"^`'. "[::-1]
# chars = "#Wo- "[::-1]
charArray = list(chars)
charLength = len(charArray)
interval = charLength/256

scaleFactor = 0.2

oneCharWidth = 10
oneCharHeight = 18

def getChar(inputInt):
    return charArray[math.floor(inputInt*interval)]

text_file = open("Output.txt", "w")

#im = Image.open('D:\IMAGES\Naruto Shippuden  Wallpapers\874582.jpg')
def main(image):
    global width,height,outputImage
    fnt = ImageFont.truetype('C:\\Windows\\Fonts\\lucon.ttf', 15)

    width, height = image.size
    image = image.resize((int(scaleFactor*width), int(scaleFactor*height*(oneCharWidth/oneCharHeight))), Image.NEAREST)
    width, height = image.size
    pix = image.load()

    outputImage = Image.new('RGB', (oneCharWidth * width, oneCharHeight * height), color = (0, 0, 0))
    d = ImageDraw.Draw(outputImage)
    
   
    

    for i in range(height):
        for j in range(width):
            r, g, b= pix[j, i]
            h = int(r/3 + g/3 + b/3)
            pix[j, i] = (h, h, h)
            text_file.write(getChar(h))
            d.text((j*oneCharWidth, i*oneCharHeight), getChar(h), font = fnt, fill = (r, g, b))

    text_file.write('\n')
    
   # sys.stdout.write()
   # os.system("cls")
#outputImage.save('output2.png')
Outputvideo=cv2.VideoCapture("video_2021-04-27_18-22-09.mp4")
current_frame=0

try:
    if not os.path.exists('Project images'):
        os.makedirs('Project images')
except OSError:
    print('Error: Failed to create a directory"Project images"')

while True:
    ret,frame=Outputvideo.read()
    if ret:
        name="./Project images/frame"+str(current_frame)+'.png'
        print('Creating...'+name)
        cv2.WINDOW_NORMAL 
        cv2.imshow("frame",frame)
        #main(Image.fromarray(cv2.cvtColor(frame,cv2.COLOR_RGB2BGR)))
        ##outputImage=Image.fromarray()
        cv2.imwrite(name,frame)     
        cv2.waitKey(31)    
        current_frame += 1
        
    else:
        break
    
Outputvideo.release()
Outputvideo.destroyAllWindows()


#image_array=[]
#for filename in glob.glob(format('Project images/sav'+ str(o) +'.png')):
#    img=cv2.imread(filename)
#    height,width,layers=img.shape
#    size=(width,height)
#    image_array.append(img)


#    out=cv2.VideoWriter('project2.avi',cv2.VideoWriter_fourcc(*'DIVX'),15,size)


#    for i in range(len(image_array)):
#        out.write(image_array[i])
#    out.release()

  