from graphics import*
from Button import*

def main():
    win = GraphWin("Image Editor", 800, 600)
    B = Button(win, Point(600, 100), Point(700, 175), "tomato", "Darken")
    M = Button(win, Point(600, 200), Point(700, 275), "tomato", "Lighten")
    Q = Button(win, Point(600, 300), Point(700, 375), "tomato", "Quit")
    G = Button(win, Point(600, 400), Point(700, 475), "tomato", "Grayscale")
    C = Button(win, Point(600, 500), Point(700, 575), "tomato", "Contrast")
    I = Image(Point(300, 300), "pngegg.png")
    I.draw(win)


    while True:
        
        m = win.getMouse()

        if M.isClicked(m):
            lighten(I)
            

        if B.isClicked(m):
            darken(I)

        if G.isClicked(m):
            grayscale(I)

        if C.isClicked(m):
            contrast(I)
                        

        if Q.isClicked(m):
            win.close()
            break
    
def lighten(img):
    x = img.getWidth()
    y = img.getHeight()


    for i in range(x):
        for j in range(y):
            pix = img.getPixel(i, j)
            red = pix[0]
            green = pix[1]
            blue = pix[2]
            red = red +40
            green = green + 40
            blue = blue + 40

            if red > 255:
                red = 255

            if blue > 255:
                blue = 255
                
            if green > 255:
                green = 255

            
            c = color_rgb(red, green, blue)
            img.setPixel(i, j, c)


def darken(img):
    x = img.getWidth()
    y = img.getHeight()


    for i in range(x):
        for j in range(y):
            pix = img.getPixel(i, j)
            red = pix[0]
            green = pix[1]
            blue = pix[2]
            red = red - 40
            green = green - 40
            blue = blue - 40

            if red < 0:
                red = 0

            if blue < 0:
                blue = 0
                
            if green < 0:
                green = 0
                
            c = color_rgb(red, green, blue)
            img.setPixel(i, j, c)
            
           
            


def grayscale(img):
    x = img.getWidth()
    y = img.getHeight()


    for i in range(x):
        for j in range(y):
            pix = img.getPixel(i, j)
            red = pix[0]
            green = pix[1]
            blue = pix[2]
            color = red + blue + green
            gray = int(color / 3)

            

            if gray < 0:
                gray = 0
                
            elif gray > 255:
                gray = 255

            c = color_rgb(gray, gray, gray)
            img.setPixel(i, j, c)
            
def contrast(img):
    x = img.getWidth()
    y = img.getHeight()


    for i in range(x):
        for j in range(y):
            pix = img.getPixel(i, j)
            red = pix[0]
            green = pix[1]
            blue = pix[2]
            if (red + green + blue) > 382:
                red = red + 35
                green = green + 35
                blue = blue + 35
                
                
            if (red + green + blue) <= 382:
                red = red - 30
                green = green - 30
                blue = blue - 30
                
            if red < 0:
                red = 0

            if blue < 0:
                blue = 0
                
            if green < 0:
                green = 0

            if red > 255:
                red = 255

            if blue > 255:
                blue = 255
                
            if green > 255:
                green = 255

            c = color_rgb(red, green, blue)
            img.setPixel(i, j, c)
    
    


    
if __name__ == "__main__":
     main()
