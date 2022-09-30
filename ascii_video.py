
from PIL import Image
import sys,os,cv2

# ascii characters used to build the output text
#ASCII_CHARS = ["@", "#", "S", '$', '&', "%", '=', "?", "*", '^', "+", ";", ":", ",", "."]
ASCII_CHARS="$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1{}[]?-_+~<>i!lI;:,\"^`'. "[::-1]
ASCII_CHARS=list(ASCII_CHARS)
# resize image according to a new width
def resize_image(image, new_width=100):
    width, height = image.size
    ratio = height/width
    new_height = int(new_width * ratio)
    resized_image = image.resize((new_width, new_height))
    return(resized_image)

# convert each pixel to grayscale
def grayify(image):
    grayscale_image = image.convert("L")
    return(grayscale_image)
    
# convert pixels to a string of ascii characters
def pixels_to_ascii(image):
    pixels = image.getdata()
    characters = "".join([ASCII_CHARS[pixel//25] for pixel in pixels])
    return(characters)    

def main(image,new_width=100):
    global ascii_image
    # attempt to open image from user-input
    #path=input('Enter a valid pathname to image:\n')
    
    #try:
    #    image = Image.open(path)
    #except:
    #    print(path, " is not a valid pathname to an image.")
    #    return
  
    # convert image to ascii    
    new_image_data = pixels_to_ascii(grayify(resize_image(image)))
    
    # format
    pixel_count = len(new_image_data)  
    ascii_image = "\n".join([new_image_data[index:(index+new_width)] for index in range(0, pixel_count, new_width)])
    
    # print result
    sys.stdout.write(ascii_image)
    os.system("cls")
    
#Outputvideo=cv2.VideoCapture("final.mp4")   
#while True:
#    ret,frame=Outputvideo.read()
#    cv2.imshow("frame",frame)
#    main(Image.fromarray(frame))
#    cv2.waitKey(2)
#    print("frame:"+str(frame))
#    print(ascii_image)
    
