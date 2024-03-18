from bridges import *

import random
from datetime import datetime
import time

start = time.time()
class RaceCar(NonBlockingGame):
    car_position = [0, 0]
    frame = 0
    # List of positions of the left wall, the right wall will just add road_width
    left_wall = []
    road_width = 0

    # This will be the next position of the incoming road
    road_position = 0

    # The goal of the road position to reach
    road_goal = 0

    # How many frames to wait to set a new goal
    turn_frames = 30
    
    game_over = False
    def __init__(self, assid, login, apikey):
        #The screen will be 30x30
        super(RaceCar, self).__init__(assid, login, apikey, 30, 30)
    
    #This method will be called once
    def initialize(self):
        #Set the title of the game
        self.set_title("Race Car")

        self.car_position = [15, 28]#column row
        # Left wall list
        #TODO: set to an empty list
        self.left_wall = []
        # The position of the next left wall as the road moves down
        self.road_position = 8
        # The goal that road_position moves towards each frame
        self.road_goal = self.road_position

        self.road_width = 13

        #This loop iterates from 0 to the size of the first dimension of the board
        for i in range(self.grid.grid_size[0]):
            #Appends the current road_position to the left_wall
            self.left_wall.append(self.road_position)

    #This will be called every time period in the game
    def draw(self):
        # Draw the background
        #TODO: Iterate through the rows
        for row in range(self.grid.grid_size[0]):
        #TODO: Iterate through the columns
            for column in range(self.grid.grid_size[1]):
        #TODO: use self.set_bg_color to set the row, column color to NamedColor.green (or whatever color you like just not black)
                self.set_bg_color(row, column, NamedColor.green)
        #TODO: use self.draw_symbol to set the row, column to NamedSymbol.none and NamedColor.floralwhite
                self.draw_symbol(row, column, NamedSymbol.none, NamedColor.floralwhite)
        # Draw the road walls alternating colors - in the sample image, this is the dark gray/light gray part
        #TODO: Loop through the columns
        for i in range(self.grid.grid_size[1]):
        #TODO: if self.frame is even (how do you compute that if self.frame is a number)
            if self.frame % 2 == 0:
                self.set_bg_color(i, self.left_wall[i], NamedColor.darkgray if i % 2 == 0 else NamedColor.gray)
                self.set_bg_color(i, self.left_wall[i] + self.road_width, NamedColor.darkgray if i % 2 == 0 else NamedColor.gray)
        #TODO: otherwise
            else:
                self.set_bg_color(i, self.left_wall[i], NamedColor.darkgray if i % 2 != 0 else NamedColor.gray)
                self.set_bg_color(i, self.left_wall[i] + self.road_width, NamedColor.darkgray if i % 2 != 0 else NamedColor.gray)

        # Draw the road core itself
        for y in range(self.grid.grid_size[0]):
            for x in range(1, self.road_width):
                if x == self.road_width // 2 and y % 2 == (0 if self.frame % 2 == 0 else 1):
                    self.set_bg_color(y, self.left_wall[y] + x, NamedColor.greenyellow)
                else:
                    self.set_bg_color(y, self.left_wall[y] + x, NamedColor.black)

        #Draws the car
        self.draw_symbol(self.car_position[1], self.car_position[0], NamedSymbol.triangle_up, NamedColor.floralwhite)
        self.set_bg_color(self.car_position[1], self.car_position[0], NamedColor.black)

    def handle_input(self):
        #TODO: Only take input every other frame...only even frame numbers (self.frame)
        if self.frame % 2 == 0:        
        #TODO: Add the if statement for the above line
            #TODO: if the user presses left
            if self.key_left():
                self.car_position[0] = max(0, self.car_position[0] - 1)
            #TODO: if the user presses right
            if self.key_right():
                self.car_position[0] = min(self.grid.grid_size[1] - 1, self.car_position[0] + 1)

    def check_collision(self):
        # Return true if the car collides with either road wall
        if self.left_wall[28] == self.car_position[0] or (self.left_wall[28] + self.road_width) == self.car_position[0]:
            exit()
            
    def move_road(self):
        # Move the road towards the goal
        if self.frame % 10 == 0 and self.road_position != self.road_goal:
            self.road_position += 1 if (self.road_goal - self.road_position) > 0 else - 1
    
        # Set a new goal to move towards
        if self.frame % self.turn_frames == 0:
            self.road_goal = random.randrange(0, self.grid.grid_size[1] - self.road_width)

        # Move the road down
        self.left_wall[0] = self.road_position
        for i in range(self.grid.grid_size[0] - 1, 0, -1):
            self.left_wall[i] = self.left_wall[i - 1]

    def print_score(self):
        end = time.time()
        score= str(int(end-start))
        self.draw_symbol(0, 0, NamedSymbol.S, NamedColor.white)
        self.draw_symbol(0, 1, NamedSymbol.c, NamedColor.white)
        self.draw_symbol(0, 2, NamedSymbol.o, NamedColor.white)
        self.draw_symbol(0, 3, NamedSymbol.r, NamedColor.white)
        self.draw_symbol(0, 4, NamedSymbol.e, NamedColor.white)
        for i in range(len(score)):
            self.draw_symbol(0, i + 6 ,list(NamedSymbol)[int(score[i]) + 53] , NamedColor.white)

    def game_loop(self):
        #TODO: increment self.frame by 1
        self.frame += 1
        #TODO: call the method to move the road (don't forget self.)
        self.move_road()
        #TODO: call the method to handle the input (don't forget self.)
        self.handle_input()
        #TODO: call check collision (don't forget self.)
        self.check_collision()
        #TODO: call draw (don't forget self.)
        self.draw()
        self.print_score()


def main():
    game = RaceCar(221, "User Name",  "API Key")  
    # Start the game
    game.start()



if __name__ == '__main__':
    main()
