# recpic.py
# prints fractal images
# Rachael Schwartz
import picture

def main():
    
    def MakePattern(p):
        s = eval(input("Please enter a size: "))
        d = eval(input("Please enter a depth: "))
        pic = picture.Picture(s,s)
        x1 = 0
        y1 = 0
        x2 = s
        y2 = s
        if (p == "Bubbles"):
            r = s//4
            Bubbles(pic,x1,y1,x2,y2,r,d)
        elif (p == "Carpet"):
            h = s//3
            Carpet(pic,x1,y1,x2,y2,h,d)
        elif (p == "Gasket"):
            (aX,aY) = (0,s)
            (bX,bY) = (s,s)
            (cX,cY) = ((s//2),0)
            pic.setFillColor(100,200,255)
            pic.setOutlineColor(30,200,255)
            pic.drawPolygonFill(((aX,aY), (bX,bY), (cX,cY)))
            Gasket(pic,aX,aY,bX,bY,cX,cY,d)
        elif (p == "Snowflake"):
            (aX,aY) = ((s//6),((s//3)*2))
            (bX,bY) = (((s//6)*5),((s//3)*2))
            (cX,cY) = ((s//2),(s//6))
            Snowflake(pic,aX,aY,bX,bY,d)
        else:
            print("Sorry! The pattern you entered is invalid.")
        pic.display()
        input()
            
    def Bubbles(pic,x1,y1,x2,y2,r,d):
        if (d > 0):
            (cX,cY) = (((x1 + x2)//2), ((y1 + y2)//2))
            pic.setOutlineColor(0,225,225)
            pic.setFillColor(0,225,225)
            pic.drawCircleFill(cX,cY,r)
            Bubbles(pic,x1,y1,cX,cY,(r//2),(d-1))
            Bubbles(pic,cX,y1,x2,cY,(r//2),(d-1))
            Bubbles(pic,x1,cY,cX,y2,(r//2),(d-1))
            Bubbles(pic,cX,cY,x2,y2,(r//2),(d-1))
            
    def Carpet(pic,x1,y1,x2,y2,h,d):
        if (d > 0):
            (pX,pY) = ((((x2 - x1)//3) + x1), (((y2 - y1)//3) + y1))
            pic.setOutlineColor(0,0,0)
            pic.setFillColor(0,0,0)
            pic.drawRectFill(pX,pY,h,h)
            Carpet(pic,x1,y1,pX,pY,(h//3),(d-1))
            Carpet(pic,pX,y1,(pX + h),pY,(h//3),(d-1))
            Carpet(pic,(pX + h),y1,x2,pY,(h//3),(d-1))
            Carpet(pic,x1,pY,pX,(pY + h),(h//3),(d-1))
            Carpet(pic,(pX + h),pY,x2,(pY + h),(h//3),(d-1))
            Carpet(pic,x1,(pY + h),pX,y2,(h//3),(d-1))
            Carpet(pic,pX,(pY + h),(pX + h),y2,(h//3),(d-1))
            Carpet(pic,(pX + h),(pY + h),x2,y2,(h//3),(d-1))
            
    def Gasket(pic,aX,aY,bX,bY,cX,cY,d):
        if (d > 0):
            (acX,acY) = (((aX + cX)//2), ((aY + cY)//2))
            (abX,abY) = (((aX + bX)//2), ((aY + bY)//2))
            (bcX,bcY) = (((bX + cX)//2), ((bY + cY)//2))
            pic.setOutlineColor(255,0,50)
            pic.setFillColor(255,0,50)
            pic.drawPolygonFill(((acX,acY), (abX,abY), (bcX,bcY)))
            Gasket(pic,cX,cY,acX,acY,bcX,bcY,(d-1))
            Gasket(pic,aX,aY,acX,acY,abX,abY,(d-1))
            Gasket(pic,bX,bY,bcX,bcY,abX,abY,(d-1))
            
    def Snowflake():
        
    p = input("Please choose a pattern (Bubbles, Carpet, Gasket, Snowflake): ")
    MakePattern(p)

    
main()
