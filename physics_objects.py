'''Papa Yaw Owusu Nti
    CS 152B
    Project 7
    November 7th 2023
    
    The program includes defines classes for simulating the motion of a balls and a block in a graphics window 
    using principles of physics. 
    The Block class is a subclass of the Ball class, representing rectangular blocks in the graphics window. 
    The program has collision_test function between the falling ball and the blocks. 
'''

import graphicsPlus as gr

class Ball:
    def __init__(self,win):
        '''initializes fields for vis, position, velocity, acceleration, force, mass, and radius.
        The field vis is a list that contains one element: a Zelle graphics Circle.  '''
        self.mass = 1
        self.radius = 1
        self.position = [0,0]
        self.velocity = [0,0] 
        self.acceleration = [0,0]
        self.win = win
        self.scale = 10.0
        self.vis = [ gr.Circle( gr.Point(self.position[0]*self.scale, win.getHeight()-self.position[1]*self.scale),self.radius * self.scale ) ]

    def draw(self):
        '''Draws the ball on the graphics window by iterating over self.vis'''
        for circle in self.vis:
            circle.draw(self.win)
            
    def getPosition(self): 
        '''returns a 2-element list with the x, y position'''
        return self.position[:]
    def setPosition(self, px, py): 
        ''' returns an updated ball's position to new coordinates [px, py]'''
        x_old = self.position[0]
        y_old = self.position[1]
        self.position = [px, py]

        dx = (px - x_old) * self.scale
        dy = (py - y_old) * (-self.scale)

        for item in self.vis:
            item.move(dx, dy)
        
    def getVelocity(self): 
        ''' returns a 2-element list with the x and y velocities'''
        return self.velocity[:]
    
    def setVelocity(self, vx, vy): 
        ''' returns an updated ball's velocity to new values [vx, vy]'''
        # vx and vy are the new x and y velocities
        self.velocity= [vx,vy]
        
    def getAcceleration(self): 
        '''returns a 2-element list with the x and y acceleration values.'''
        return self.acceleration[:]
    
    def setAcceleration(self, ax, ay): 
        ''' returns an updated ball's acceleration to new values [ax, ay]'''
        # ax and ay are new x and y accelerations.
        self.acceleration= [ax,ay]
        
    def getMass(self): 
        '''Returns the mass of the object as a scalar value'''
        return self.mass
    
    def setMass(self, m): 
        '''Updates the mass of the ball to a new value m'''
        # m is the new mass of the object
        self.mass = m
    def getRadius(self): 
        '''Returns the radius of the Ball as a scalar value'''
        return self.radius

    def setRadius(self, r):
       self.radius = r 
        # (**Optional** You might implement this later when you are making your ball class fancier) r is the new radius of the Ball object. 


    def update(self, dt):
        '''simulates the Ball's projectile motion using Newtonian mechanics over a time step dt. 
        Both its physics coordinates and visualization coordinates are updated appropriately'''
        
        # assign to x_old the current x position
        # assign to y_old the current y position
        x_old = self.position[0]
        y_old = self.position[1]
        x_velocity = self.velocity[0]
        y_velocity = self.velocity[1]
        x_acceleration = self.acceleration[0]
        y_acceleration = self.acceleration[1]

        # update the x position to be x_old + x_vel*dt + 0.5*x_acc * dt*dt
        # update the y position to be y_old + y_vel*dt + 0.5*y_acc * dt*dt 
        self.position[0] = x_old + self.velocity[0] * dt + 0.5 * self.acceleration[0] * dt * dt
        self.position[1] = y_old + self.velocity[1] * dt + 0.5 * self.acceleration[1] * dt * dt

        # assign to dx the change in the x position times the scale factor (self.scale)
        # assign to dy the negative of the change in the y position times the scale factor (self.scale)
        dx = (self.position[0] - x_old) * self.scale
        dy = (self.position[1] - y_old) * self.scale * (-1)

        # for each item in self.vis
        # call the move method of the graphics object with dx and dy as arguments
        for item in self.vis:
            item.move(dx, dy)

        # update the x velocity by adding the acceleration times dt to its old value
        # update the y velocity by adding the acceleration times dt to its old value
        x_velocity += x_acceleration * dt
        y_velocity += y_acceleration * dt
        self.setVelocity(x_velocity,y_velocity)

 
 
class Block(Ball):
    def __init__(self, win, dx=1, dy=1):
        """
        Initializes a Block object with a given window, width (dx), and height (dy)
        """
        super().__init__(win) 
        self.dx = dx
        self.dy = dy
        self.win = win
        self.scale = 10  
        point1 = gr.Point((self.position[0] - self.dx/2) * self.scale,
                      win.getHeight() - (self.position[1] + self.dy/2) * self.scale)
        point2 = gr.Point((self.position[0] + self.dx/2) * self.scale,
                      win.getHeight() - (self.position[1] - self.dy/2) * self.scale)
        self.vis = [gr.Rectangle(point1, point2)]

    def draw(self):
        """
        Draws the block on the graphics window
        """
        for block in self.vis:
            block.draw(self.win)

    def undraw(self):
        """
        Undraws the block from the graphics window
        """
        for block in self.vis:
            block.undraw()
            
    def setPosition(self, px, py):
        """
        Moves the block to a new position (px, py) and updates its visuals
        """
        dx = (px - self.position[0]) * self.scale
        dy = (py - self.position[1]) * self.scale
        for visual in self.vis:
            visual.move(dx, -dy)
        self.position = [px, py]

    def getWidth(self):
        """
        Returns the width of the block
        """
        return self.dx

    def setWidth(self, new_xchange):
        """
        Sets a new width for the block and updates its visuals
        """
        self.undraw()
        self.dx = new_xchange
        self.draw()

    def getHeight(self):
        """
        Returns the height of the block
        """
        return self.dy

    def setHeight(self, new_ychange):
        """
        Sets a new height for the block and updates its visuals
        """
        self.undraw()
        self.dy = new_ychange
        self.draw()

    def collision(self, ball):
        """
        Checks for collision between the block and a given ball
        Returns True if a collision occurs, False otherwise
        """
        ball_position = ball.getPosition()
        ball_radius = ball.getRadius()
        block_height = self.getHeight()
        block_width = self.getWidth()
        block_position = self.getPosition()

        dx = abs(ball_position[0] - block_position[0])
        dy = abs(ball_position[1] - block_position[1])
            
        # Minimum distances for collision
        min_dx = ball_radius + block_width/2
        min_dy = ball_radius + block_height/2

        return dx <= min_dx and dy <= min_dy
