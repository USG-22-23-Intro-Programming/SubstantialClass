from graphics import*
from Button import*


def main():

    win = GraphWin("Palindrome", 800, 600)

    Q = Button(win, Point(600, 500), Point(700, 575), "tomato", "QUIT")
    Check = Button(win, Point(350, 350), Point(450, 425), "SteelBlue1", "Check!")

    E = Entry(Point(400, 300), 30)
    E.draw(win)
    E.setSize(16)

    T = Text(Point(400, 250), "Write a potential Palindrome below!")
    T.draw(win)
    
    

    while True:

        m = win.getMouse()

        if Q.isClicked(m):
            break


        if Check.isClicked(m):
            pal = E.getText()

        length = len(pal)
        palindrome = True 
            
        for i in range(length):
            if pal[i]!= pal[length-1-i]:
                palindrome = False

        if palindrome:
            T.setText("It is a palindrome")
        else:
            T.setText("Not a Palindrome")
                
        
            


        

        

            

    win.close()


if __name__ == "__main__":
    main()
