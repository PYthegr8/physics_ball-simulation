''' 
    by Papa Yaw Owusu Nti
    November 7th 2023
    This program tests the functionality of physics_objects.py.
'''

import graphicsPlus as gr
import physics_objects as pho
import random
import time


def main():
    '''main function for implementing the test code'''
    # create a graphics window
    win = gr.GraphWin("Falling", 500, 500, False)
    # create a ball
    ball = pho.Ball(win)
    ball.draw()
    # move it to the center of the screen and draw it
    ball.setPosition(25, 25)
    # give it a random velocity
    ball.setVelocity(random.randint(-10,30), random.randint(-10,30))
    # set the acceleration to (0, -20)
    ball.setAcceleration(0, -20)
    
    
    blocks = []
    number_of_blocks = 6
    block_width = 6
    block_height = 3

    # Position the blocks along the bottom of the screen
    for i in range(number_of_blocks):
        block = pho.Block(win, dx=block_width, dy=block_height)
        x_position = 5 + i * (block_width + 2)  # Adjust spacing
        y_position = 5  # Position at the bottom of the screen
        block.setPosition(x_position, y_position)
        block.draw()
        blocks.append(block)
    

    
    textbox = gr.Text( gr.Point( 250, 50 ), "Clear" )
    textbox.draw(win)
    # print(block.collision( ball ))
    
    if block.collision( ball ):
        textbox.setText( 'Collision' )
    

    while True:
        # call the ball's update method with a dt of 0.033
        ball.update(0.033)
        time.sleep( 0.033 ) # have the animation go at the same speed


        if win.checkMouse(): # did the user click the mouse?
            break
        
        # Check for collisions
        collision_detected = False
        for block in blocks:
            if block.collision(ball):
                collision_detected = True
                textbox.setText('Collision')
                block.undraw()
                
            if collision_detected == False:
                textbox.setText('Clear')
        

        # if the ball is outside the window   
        if (ball.getPosition()[0] < 0 or ball.getPosition()[0] > win.getWidth() or ball.getPosition()[1] < 0 or ball.getPosition()[1] > win.getHeight()):
           # reposition the ball to the center of the window
           ball.setPosition(25, 25)
           # give it a random velocity
           ball.setVelocity(random.randint(-10,10), random.randint(-10,10))
           
        win.update()


    win.close()

if __name__ == "__main__":
    main()