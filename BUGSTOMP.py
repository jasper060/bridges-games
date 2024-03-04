import random
#You should install bridges
from bridges import *

#Think about an object like a bankaccount...a bankaccount has a balance (at a minimum)
#A bankaccount has specific behaviors: deposit, withdraw, print balance
#Instead of having lots of code that is randomly distributed around a file, we can organize it in a class


class BugStomp(NonBlockingGame):
    #Initial player location
    loc = [2, 2]
    previous_loc = loc
    #Board size - can change to 10x10, 20x20
    boardSize = [30, 30]
    
    #Bug's original location
    bug = [5, 5]
    
    #Bug's lifetime - needed to make the game more challenging
    buglife = 100
    
    #TODO: initialize a variable called score to 0
    #Player's score
    score = 0
    #Bug's color - you can choose another color just keep the NamedColor.
    bugColor = NamedColor.green
    
    #Random number
    randomNumber = random.randrange(1, 10, 1)
    
    #Game variable
    my_game = 10
    
    #Boolean to track if the game is won
    won = False

    #Anything below that starts with def is a function. We can write functions to organize our code.
    #Think of a chapter in a book. We can write the chapter and then move it around as we need to.
    #That's the same idea as a function, which we will cover next week.
    #The initialize method runs first, and it only runs once
    #The purpose is to initialize the board

    def initialize(self):
        #Gets a random number between 0 and the first dimension of the size of the board (30)
        #The self is referring to that variable up on line 32 and is clarifying that fact
        self.randomNumber = random.randrange(0, self.boardSize[0]-1, 1)
        
        #TODO: if you don't want the bug to change color, you can comment out the following line
        self.bugColor = random.choice(list(NamedColor))

        #TODO: Color in the board, loop through the rows and columns of the board
        for row in range(0,self.boardSize[0],1):
            for column in range(0,self.boardSize[1],1):
                self.set_bg_color(column, row, NamedColor.blue)

        #TODO: Remove any symbols on the board
        #TIP: self.set_bg_color(column, row, NamedColor.white) will set the color at column, row to white
        #TIP: self.draw_symbol(column, row, NamedSymbol.none, NamedColor.white) will remove a symbol
        for i in range(self.boardSize[0]):
            for j in range(self.boardSize[1]):
                self.set_bg_color(j,i,NamedColor.white)
                self.draw_symbol(j, i, NamedSymbol.none, NamedColor.white)


        #TODO: set the bug's location using that variable on line 20 (hint: what goes before the variable name?)
        #Use randrange like on line 46, but the bug's location is a list, which requires two values
        self.bug[0] = random.randrange(0, self.boardSize[0]-1, 1)
        self.bug[1] = random.randrange(0, self.boardSize[1]-1, 1)

    #Controls the movement of the player (human)
    def handle_input(self):
        #If left key pressed, decrease column because the player is moving to the left
        #Remember, the upper, lefthand corner of the screen is 0,0
        self.previous_loc[0] = self.loc[0]
        self.previous_loc[1] = self.loc[1]

        if self.key_left():
                self.loc[1] = self.loc[1] - 1
        #TODO: Complete for self.key_right(), self.key_up(), and self.key_down()
        if self.key_right():
                self.loc[1] = self.loc[1] + 1
        if self.key_down():
                self.loc[0] = self.loc[0] + 1
        if self.key_up():
                self.loc[0] = self.loc[0] - 1
        #Check the top row, did we go past 0? If so, reset to 0
        if self.loc[0] < 0:
            self.loc[0] = 0
        #TODO: Check rightmost column
        if self.loc[0] > (self.boardSize[0]-1):
            self.loc[0] -= 1
        #TODO: Check top row
        if self.loc[1] < 0:
            self.loc[1] = 0
        #TODO: Check bottom row
        if self.loc[1] > (self.boardSize[1]-1):
            self.loc[1] -= 1

        
    #Check for overlap between player and bug
    def overlap(self):
        # return abs(self.bug[0] - self.loc[0]) == 0 and abs(self.bug[1] - self.loc[1]) == 0
        return abs(self.bug[0] - self.loc[0]) < 2 and abs(self.bug[1] - self.loc[1]) < 2

    #Update bug lifetime, score, check edge cases
    def handle_bug(self):
        #The bug is winning
        if self.buglife < 1:
            #TODO: Get a new random location for the bug (you did this before!)
            self.bug[0] = random.randrange(0, self.boardSize[0]-1, 1)
            self.bug[1] = random.randrange(0, self.boardSize[1]-1, 1)
            #Set the bug's life to a random value
            self.buglife = random.randrange(100, 200)
            #Set the bug's color
            self.bugColor = random.choice(list(NamedColor))
            #TODO: Decrease the score by 1 (what goes before score?)
            self.score -= 1
        #We want you to have a little help
        if self.score < 0:
            #TODO: Set the score to 0
            self.score = 0
        else:
            #TODO: Decrease the bug's life by 1
            self.buglife -= 1
        if self.overlap():
            #TODO: Get a new bug's location
            self.bug[0] = random.randrange(0, self.boardSize[0]-1, 1)
            self.bug[1] = random.randrange(0, self.boardSize[1]-1, 1)
            #Get a new bug color
            self.bugColor = random.choice(list(NamedColor))
            
            #TODO: Increase the score by 1, you squashed the bug!!!
            self.score += 1

    #TODO: Write a winning message on teh board. Below is an example...customize it
    def win(self):
        self.draw_symbol(0, 0, NamedSymbol.man, NamedColor.white)
        self.draw_symbol(0, 1, NamedSymbol.W, NamedColor.white)
        self.draw_symbol(0, 2, NamedSymbol.i, NamedColor.white)
        self.draw_symbol(0, 3, NamedSymbol.n, NamedColor.white)
        self.draw_symbol(0, 4, NamedSymbol.n, NamedColor.white)
        self.draw_symbol(0, 5, NamedSymbol.e, NamedColor.white)
        self.draw_symbol(0, 6, NamedSymbol.r, NamedColor.white)

        #Set the boolean to True for the win
        self.won = True

    #Print the score
    def print_score(self):
        self.draw_symbol(0, 0, NamedSymbol.S, NamedColor.white)
        self.draw_symbol(0, 1, NamedSymbol.c, NamedColor.white)
        self.draw_symbol(0, 2, NamedSymbol.o, NamedColor.white)
        self.draw_symbol(0, 3, NamedSymbol.r, NamedColor.white)
        self.draw_symbol(0, 4, NamedSymbol.e, NamedColor.white)
        self.draw_symbol(0, 6, list(NamedSymbol)[self.score + 53], NamedColor.white)

    #Redraw method - draws the board throughout the game
    def print_screen(self):
        
        #TODO: Loop through the rows and columns and color the board
        #Hint: You did this in the initialize method
        for row in range(0,self.boardSize[0],1):
            for column in range(0,self.boardSize[1],1):
                self.set_bg_color(column, row, NamedColor.black)
                self.draw_symbol(column, row, NamedSymbol.none, NamedColor.white)
        
        #NOTE: if you want to hurt somebody eyes RUN it
        # colorList = ["blue","yellow","ivory","indigo","mistyrose","springgreen","navy","gold","burlywood","khaki"]
        # for col in colorList:
        #     i = 0
        #     while i < 500:
        #         row = random.randint(0,self.boardSize[0]-1)
        #         column = random.randint(0,self.boardSize[1]-1)
        #         self.set_bg_color(column, row, col)
        #         i += 1
                
        #TODO: Draw the bug (remember, self.bug is a list with the column in position 0 and
        #the row in position 1. NamedSymbol.bug3 is a nifty pic, and you already have a color selected
        #in a variable...which one?
        # self.draw_symbol(self.previous_loc[0], self.previous_loc[1], NamedSymbol.none, NamedColor.white)
        self.draw_symbol(self.bug[0], self.bug[1], NamedSymbol.bug3, self.bugColor)
        self.draw_symbol(self.loc[0], self.loc[1], NamedSymbol.man, NamedColor.white)
       

    #This is called every frame
    def game_loop(self):
        #Check if the game has been won
        if not self.won:
            #Call handle_input()
            self.handle_input()
            #Call handle_bug()
            self.handle_bug()
            #Call print_screen()
            self.print_screen()
            #Call print_score()
            self.print_score()

            #TODO: Check if the player's score is 10 or more
            #If so, call self.win()
            if self.score >= 10:
                self.win()

    def __init__(self, assid, login, apikey, cols, rows):
        super(BugStomp, self).__init__(assid, login, apikey, cols, rows)
        self.boardSize[0] = cols
        self.boardSize[1] = rows

#Driver of the game
def main():
    # create game class with bridges credentials
    my_game = BugStomp(219, "User Name", "API Key", 30, 30)
    my_game.start()


if __name__ == '__main__':
    main()
