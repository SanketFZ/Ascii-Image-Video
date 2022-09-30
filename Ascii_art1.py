
from PIL import Image, ImageDraw, ImageFont, ImageOps
import  math

ASCII_CHARS= "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1{}[]?-_+~<>i!lI;:,\"^`'. "[::-1]
char_array=list(ASCII_CHARS)
Char_length=len(char_array)
scale_factor=0.02
def get_chars(inputInt):
    return char_array[math.floor(inputInt*scale_factor)]

text_file=open('Output.txt','w')
im=Image.open('Screenshot (8).png')
width,height=im.size
pixel=im.load()
im=im.resize((int(scale_factor*width),int(scale_factor*height)), Image.NEAREST)

print(width,height)
# convert image to gray_scale


for i in range(height):
    for j in range(width):
        r,g,b,a=pixel[j,i]
        h=int(r/3 + g/3 + b/3)
        pixel[j,i]=(h,h,h)
        text_file.write(get_chars(h))
    text_file.write('\n')

im.save('gray_scale.png')
print(pixel)