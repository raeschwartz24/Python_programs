# imageEdit.py
# provides user with image edititing functionality (horizontal flip, horizontal scroll, image negative, zoom, posterize, 180 degree rotation).
# Rachael Schwartz
#
import picture2

def main():
    def copyImage(pF):
        w = pF.getWidth()
        h = pF.getHeight()
        picCopy = picture2.Picture(w,h)
        for y in range(0,h):
            for x in range(0,w):
                (r,g,b) = pF.getPixelColor(x,y)
                picCopy.setPixelColor(x,y,r,g,b)
        return picCopy
        
    def getImage():
        inputImage = raw_input("Wow, an image editor! So cool. Amaze. Please enter the name of the image file you'd like to edit: ")
        image = inputImage
        i = 1
        while (i == 1):
            try:
                image = picture2.Picture(image)
                print"Joy! Now make it weird."
                i = i+1
            except:
                errorImage = raw_input("Oops! Either you entered the wrong kind of file, or something else went wrong. Try again: ")
                image = errorImage
        return image
    
    def editOption(picEdit):
        editInput = raw_input("Okay, so you can make the image: \nFlip, Mirror, Scroll, Negative, Grayscale, Cycle Color Channels, Zoom, \nPosterize, Change Brightness, Contrast, Blur, Rotate, or Neon. \nIf you're done editing, you can Exit. \nPick one: ")    
        editTry = editInput
        if (editTry == "Flip"):
            edit = Flip(picEdit)
            return edit
        elif (editTry == "Mirror"):
            edit = Mirror(picEdit)
            return edit
        elif (editTry == "Scroll"):
            return Scroll(picEdit)
        elif (editTry == "Negative"):
            edit = Negative(picEdit)
            return edit
        elif (editTry == "Grayscale"):
            edit = Grayscale(picEdit)
            return edit
        elif (editTry == "Cycle Color Channels"):
            edit = CycleColorChannels(picEdit)
            return edit
        elif (editTry == "Zoom"):
            edit = Zoom(picEdit)
            return edit
        elif (editTry == "Posterize"):
            edit = Posterize(picEdit)
            return edit
        elif (editTry == "Change Brightness"):
            edit = Brightness(picEdit)
            return edit
        elif (editTry == "Contrast"):
            edit = Contrast(picEdit)
            return edit
        elif (editTry == "Blur"):
            edit = Blur(picEdit)
            return edit
        elif (editTry == "Rotate"):
            edit = Rotate(picEdit)
            return edit
        elif (editTry == "Neon"):
            edit = Neon(picEdit)
            return edit        
        elif (editTry == "Exit"):
            edit = 0
            return edit
        else:
            editGenError = raw_input("Sorry, something went wrong! Please try again: ")
            editTry = editGenError
                
    def Flip(picEdit):
        pic = picEdit
        w = pic.getWidth()
        h = pic.getHeight()
        picNew = picture2.Picture(w,h)
        for i in range(0,h):
            for j in range(0,w):
                x = j
                y = i
                (r,g,b) = pic.getPixelColor(x,y)
                f = ((w-1) - x)
                picNew.setPixelColor(f,y,r,g,b)
        return picNew
    
    def Mirror(picEdit):
        pic = picEdit
        w = pic.getWidth()
        h = pic.getHeight()
        picNew = picture2.Picture(w,h)
        for i in range(0,h):
            for j in range(0,(w//2)):
                x = j
                y = i
                (r,g,b) = pic.getPixelColor(x,y)
                m = ((w-1) - x)
                picNew.setPixelColor(x,y,r,g,b)
                picNew.setPixelColor(m,y,r,g,b)
        return picNew
                
    def Scroll(picEdit):
        pic = picEdit
        uI = eval(raw_input("Please enter a number of pixels: "))
        userInput = uI
        i = 1
        while (i == 1):
            try:
                n = userInput
                w = pic.getWidth()
                h = pic.getHeight()
                picNew = picture2.Picture(w,h)
                for i in range(0,h):
                    for j in range(0,w):
                        x = j
                        y = i
                        (r,g,b) = pic.getPixelColor(x,y)
                        s = (x + n)
                        if (s < w):
                            picNew.setPixelColor(s,y,r,g,b)
                        else:
                            picNew.setPixelColor((s - w),y,r,g,b)
                return picNew        
            except IndexError:
                errInd = eval(raw_input("You entered too high a number! Try again: "))
                userInput = errInd
            except:
                errGen = eval(raw_input("Sorry, something went wrong! Try again: "))
                userInput = errGen
            
    def Negative(picEdit):
        pic = picEdit
        w = pic.getWidth()
        h = pic.getHeight()
        picNew = picture2.Picture(w,h)
        for i in range(0,h):
            for j in range(0,w):
                x = j
                y = i
                [r,g,b] = pic.getPixelColor(x,y)
                P = [r,g,b]
                C = []
                for e in P:
                    C = C + [255 - e]
                rNeg = C[0]
                gNeg = C[1]
                bNeg = C[2]
                picNew.setPixelColor(x, y, rNeg, gNeg, bNeg)
        return picNew
    
    def Grayscale(picEdit):
        pic = picEdit
        w = pic.getWidth()
        h = pic.getHeight()
        picNew = picture2.Picture(w,h)
        for i in range(0,h):
            for j in range(0,w):
                x = j
                y = i
                [r,g,b] = pic.getPixelColor(x,y)
                g = ((r+g+b)//3)
                picNew.setPixelColor(x,y,g,g,g)
        return picNew
        
    def CycleColorChannels(picEdit):
        pic = picEdit
        w = pic.getWidth()
        h = pic.getHeight()
        picNew = picture2.Picture(w,h)
        for i in range(0,h):
            for j in range(0,w):
                x = j
                y = i
                [r,g,b] = pic.getPixelColor(x,y)
                rC = b
                gC = r
                bC = g
                picNew.setPixelColor(x,y,rC,gC,bC)
        return picNew
    
    def Zoom(picEdit):
        pic = picEdit
        w = pic.getWidth()
        h = pic.getHeight()
        wZoom = w//2
        hZoom = h//2
        picZoom = picture2.Picture(wZoom,hZoom)
        picNew = picture2.Picture(w,h)
        for i in range(0,hZoom):
            for j in range(0,wZoom):
                xZoom = j
                yZoom = i
                xEdit = (xZoom + (w//4))
                yEdit = (yZoom + (h//4))
                (r,g,b) = pic.getPixelColor(xEdit,yEdit)
                picZoom.setPixelColor(xZoom, yZoom, r, g, b)
                xNew = ((xEdit - (w//4)) + xZoom)
                yNew = ((yEdit - (h//4)) + yZoom)
                picNew.setPixelColor(xNew,yNew,r,g,b)
                picNew.setPixelColor((xNew+1),yNew,r,g,b)
                picNew.setPixelColor(xNew,(yNew+1),r,g,b)
                picNew.setPixelColor((xNew+1),(yNew+1),r,g,b)
        return picNew
    
    def Posterize(picEdit):
        pic = picEdit
        w = pic.getWidth()
        h = pic.getHeight()
        picNew = picture2.Picture(w,h)
        for i in range(0,h):
            for j in range(0,w):
                x = j
                y = i
                [r,g,b] = pic.getPixelColor(x,y)
                P = [r,g,b]
                C = []
                for e in P:
                    p = e//32
                    multLess = p*32
                    multGreat = (multLess + 32)
                    mLdist = (e - multLess)
                    mGdist = (multGreat - e)
                    if (mLdist < mGdist):
                        C = C + [multLess]
                    else:
                        C = C + [multGreat]
                rPost = C[0]
                gPost = C[1]
                bPost = C[2]
                picNew.setPixelColor(x, y, rPost, gPost, bPost)
        return picNew                
    
    def Brightness(picEdit):
        pic = picEdit
        w = pic.getWidth()
        h = pic.getHeight()
        picNew = picture2.Picture(w,h)
        n = eval(raw_input("Please enter a positive or negative number: "))
        for i in range(0,h):
            for j in range(0,w):
                x = j
                y = i
                [r,g,b] = pic.getPixelColor(x,y)
                P = [r,g,b]
                C = []
                for e in P:
                    c = e + n
                    if (c < 0):
                        C = C + [0]
                    if (c > 255):
                        C = C + [255]
                    else:
                        C = C + [e + n]
                rBright = C[0]
                gBright = C[1]
                bBright = C[2]
                picNew.setPixelColor(x, y, rBright, gBright, bBright)
        return picNew
    
    def Contrast(picEdit):
        pic = picEdit
        w = pic.getWidth()
        h = pic.getHeight()
        picNew = picture2.Picture(w,h)
        for i in range(0,h):
            for j in range(0,w):
                x = j
                y = i
                [r,g,b] = pic.getPixelColor(x,y)
                P = [r,g,b]
                C = []
                for e in P:
                    v = e
                    if (v > 128):
                        d = v-128
                        c = (v + d)
                        C = C + [c]
                    elif (v <= 128):
                        d = 128-v
                        c = (v - d)
                        C = C + [c]    
                rCont = C[0]
                gCont = C[1]
                bCont = C[2]
                picNew.setPixelColor(x, y, rCont, gCont, bCont)
        return picNew            
    
    def Rotate(picEdit):
        pic = picEdit
        w = pic.getWidth()
        h = pic.getHeight()
        picNew = picture2.Picture(w,h)
        for i in range(0,h):
            for j in range(0,w):
                x = j
                y = i
                (r,g,b) = pic.getPixelColor(x,y)
                fW = ((w-1) - x)
                fH = ((h-1) - y)
                picNew.setPixelColor(fW,fH,r,g,b)
        return picNew
    
    def Neon(picEdit):
        pic = picEdit
        w = pic.getWidth()
        h = pic.getHeight()
        picNew = picture2.Picture(w,h)
        for i in range(0,h):
            for j in range(0,w):
                x = j
                y = i
                [r,g,b] = pic.getPixelColor(x,y)
                P = [r,g,b]
                C = []
                for e in P:
                    v = e
                    if (v < 128): 
                        p = (128-v)
                        C = C + [e - p]
                    if (v > 128):
                        p = (v-128)
                        C = C + [e - p]
                    else:
                        C = C + [e]
                rNeon = C[0]
                gNeon = C[1]
                bNeon = C[2]
                picNew.setPixelColor(x, y, rNeon, gNeon, bNeon)
        return picNew
    
    picFile = getImage()
    picFile.display()
    raw_input()
    picCopy = copyImage(picFile)
    pic = picCopy
    i = 1
    while (i > 0):
        picEdit = pic
        picNew = editOption(picEdit)
        if (picNew == 0):
            i = 0
        else:
            picNew.display()
            raw_input()
            pic = picNew
            i = i+1
    print"Wow, such edit. Go you. Thanks!"
    
    main()
