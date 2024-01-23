import graphicsPlus as gr
import random
import time 



def test():
    win = gr.GraphWin('Window title!', 500 , 500 )
    while True:
        point = gr.Point(250,250)
        circle =gr.Circle(point,100)
        circle.draw(win)
        print(win.getMouse())
        win.close()
        
if __name__ == "__main__":
    test()
    
    
def test2():
    win = gr.GraphWin('Window title!', 500 , 500 )
    shapes =[]
    while True:
        
        pos = win.checkMouse()
        if pos!= None:
            circle =gr.Circle(pos,10)
            circle.setFill('blue') 
            shapes.append(circle)
            circle.draw(win)
            
        
        # print(shapes)
            
        user_key= win.checkKey() 
        if user_key== 'q':
            break
        
        for circle in shapes:
            x_change = random.randint(-10,10)
            y_change = random.randint(-10,10)
            print (x_change)
            print (y_change)
            circle.move(x_change,y_change)   
            

        time.sleep(0.033)
        # win.close()
        
                
if __name__ == "__main__":
    test2()       
        


