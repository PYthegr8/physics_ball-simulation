'''Papa Yaw Owusu Nti
    CS 152B
    Project 7
    November 8th 2023
    This program consists of both my extensions and the interactive demo
'''

import graphicsPlus as gr
import physics_objects_demo as pho
import random
import time

def create_blocks(win, num_blocks, block_width, block_height):
    # Function to create blocks in a grid pattern
    blocks = []
    blocks_per_row = 5
    for i in range(num_blocks):
        row = i // blocks_per_row
        col = i % blocks_per_row

        x_position = 5 + col * (block_width + 2)
        y_position = 5 + row * (block_height + 2)

        block = pho.Block(win, dx=block_width, dy=block_height)
        block.setPosition(x_position, y_position)
        block.setFill("White")
        block.draw()
        blocks.append(block)
    return blocks

def main():
    # Main function to run the interactive demo
    win = gr.GraphWin("Falling", 500, 500, False)
    win.setBackground("purple")

    # Create and initialize the first ball
    ball = pho.Ball(win)
    ball.setFill("Yellow")
    ball.draw()
    ball.setPosition(25, 25)
    ball.setVelocity(random.randint(-10, 30), random.randint(-10, 30))
    ball.setAcceleration(0, -20)
    
    # Create and initialize the second ball
    ball2 = pho.Ball(win)
    ball2.setFill("White")  # Different color for the second ball
    ball2.draw()
    ball2.setPosition(25, 25)
    ball2.setVelocity(random.randint(-10, 30), random.randint(-10, 30))
    ball2.setAcceleration(0, -20)

    # User input for the number of blocks
    num_blocks = int(input("Enter the number of blocks: "))
    block_width = 6
    block_height = 3
    blocks = create_blocks(win, num_blocks, block_width, block_height)

    # Store the original position and color of the first ball
    original_position = ball.getPosition()
    original_color = "Yellow"

    while True:
        # Update both balls and wait for a short time
        ball.update(0.033)
        ball2.update(0.033)
        time.sleep(0.033)

        # Check for collisions with blocks for the first ball
        for block in blocks:
            if block.collision(ball):
                original_position = ball.getPosition()
                original_color = "red"
                block.undraw()
            else:
                ball.setFill(original_color)
                ball.setFill("Yellow")

        # Check collision between the two balls
        if ball.ball_collision(ball, ball2):
            ball.setFill("red")
            ball2.setFill("red")
        else:
            ball.setFill(original_color)
            ball2.setFill("white")  # Change color back for the second ball

        # Reset the first ball if it goes outside the window
        if (ball.getPosition()[0] < 0 or ball.getPosition()[0] > win.getWidth() or
                ball.getPosition()[1] < 0 or ball.getPosition()[1] > win.getHeight()):
            ball.setPosition(25, 25)
            ball.setVelocity(random.randint(-10, 10), random.randint(-10, 10))
            original_color = "Yellow"
        
        # Reset the second ball if it goes outside the window
        if (ball2.getPosition()[0] < 0 or ball2.getPosition()[0] > win.getWidth() or
                ball2.getPosition()[1] < 0 or ball2.getPosition()[1] > win.getHeight()):
            ball2.setPosition(25, 60)
            ball2.setVelocity(random.randint(-10, 10), random.randint(-10, 10))

        # Check if the first ball is back to its starting position
        if ball.getPosition() == original_position:
            ball.setFill(original_color)

        # Check for user input to exit the program
        if win.checkMouse() or win.checkKey() == 'q':
            break

        win.update()

if __name__ == "__main__":
    main()
