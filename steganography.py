# steganography.py
# decrypts image according to prespecified code to reveal message
# Rachael Schwartz
import picture2

def main():
    
    pic = picture2.Picture("fruit.bmp")
    w = pic.getWidth()
    h = pic.getHeight()
    for y in range(0,h):
        for x in range(0,w):
            (r,g,b) = pic.getPixelColor(x,y)
            pic.setPixelColor(x, y, ((r%4)*64), ((g%4)*64), ((b%4)*64))
    pic.display()
    input()
    
main()
