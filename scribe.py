#importing modules
import os
import time
import math


#creating a class for canvas
class Canvas:
    def __init__(self,width,height):
        self._x=width
        self._y=height
        self._canvas=[[' ' for x in range(self._y)] for y in range(self._x)]
        
    def setpos(self,pos,mark):
        self._canvas[pos[0]][pos[1]]=mark
        
        
    def clear(self):
        os.system('cls' if os.name=='nt' else 'clear')
        
    def print(self):
        self.clear()
        for y in range(self._y):
            print(' '.join([col[y] for col in self._canvas]))
        time.sleep(0.1)
        

class TerminalScribe:
    def __init__(self,canvas):
        self.canvas=canvas
        self.pos=[0,0]
        
        self.mark= '*'
        self.trail= '.'
        
    def draw(self,pos):
        self.canvas.setpos(self.pos,self.trail)
        self.pos=pos
        self.canvas.setpos(self.pos,self.trail)
        self.canvas.print()
        
    def draw_down(self):
        self.canvas.setpos(self.pos,self.trail)
        self.pos=[self.pos[0],self.pos[1]+1]
        self.canvas.setpos(self.pos,self.trail)
        self.canvas.print()
        
    def draw_right(self):
        self.canvas.setpos(self.pos,self.trail)
        self.pos=[self.pos[0]+1,self.pos[1]]
        self.canvas.setpos(self.pos,self.trail)
        self.canvas.print()
    
    def draw_left(self):
        self.canvas.setpos(self.pos,self.trail)
        self.pos=[self.pos[0]-1,self.pos[1]]
        self.canvas.setpos(self.pos,self.trail)
        self.canvas.print()
        
    def draw_up(self):
        self.canvas.setpos(self.pos,self.trail)
        self.pos=[self.pos[0],self.pos[1]-1]
        self.canvas.setpos(self.pos,self.trail)
        self.canvas.print()
        
    def draw_square(self,length):
        for i in range(length):
            self.draw_down()
        for i in range(length):
            self.draw_right()
        for i in range(length):
            self.draw_up()
        for i in range(length):
            self.draw_left()
        
        
                    
canvas = Canvas(30,30)
scribe = TerminalScribe(canvas)

scribe.draw_square(5)








        