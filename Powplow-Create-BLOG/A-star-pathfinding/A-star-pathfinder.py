 #python path finder

##########################################################

#imports

import pygame
import math
from queue import PriorityQueue

##########################################################

#CODE

#set up display

WIDTH = 800
WIN = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("a star path finder")

#colors

white = ((255,255,255))
blue = ((0,0,255))
green = ((0,255,0))
red = ((255,0,0))
black = ((0,0,0))
orange = ((255,100,10))
yellow = ((255,255,0))
blue_green = ((0,255,170))
marroon = ((115,0,0))
lime = ((180,255,100))
pink = ((255,100,180))
purple = ((240,0,255))
gray = ((127,127,127))
magenta = ((255,0,230))
brown = ((100,40,0))
forest_green = ((0,50,0))
navy_blue = ((0,0,100))
rust = ((210,150,75))
dandilion_yellow = ((255,200,0))
highlighter = ((255,255,100))
sky_blue = ((0,255,255))
light_gray = ((200,200,200))
dark_gray = ((50,50,50))
tan = ((230,220,170))
coffee_brown =((200,190,140))
moon_glow = ((235,245,255))


##########################################################

#CLASS'S AND DEF'S

class Spot:
    def __init__(self, row, col ,width, total_rows):
        self.row = row
        self.col = col
        self.x = row * width
        self.y = col * width
        self.color = white
        self.neighbors = []
        self.width = width
        self.total_rows = total_rows


    def get_pos(self):
        return self.row, self.col

    def is_closed(self):
        return self.color == red
    
    def is_open(self):
        return self.color == green

    def is_barrier(self):
        return self.color == black

    def is_start(self):
        return self.color == orange

    def is_end(self):
        return self.color == purple

    def reset(self):
        self.color = white
      
    def make_closed(self):
         self.color = red
    
    def make_open(self):
         self.color = green

    def make_barrier(self):
        self.color = black

    def make_start(self):
        self.color = orange

    def make_end(self):
        self.color = purple

    def make_path(self):
        self.color = navy_blue

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.width))

    def update_neighbors(self, grid):
        self.neighbors = []

        if self.row < self.total_rows - 1 and not grid[self.row + 1][self.col].is_barrier():
          self.neighbors.append(grid[self.row + 1][self.col])        
        
        if self.row > 0 and not grid[self.row - 1][self.col].is_barrier():
          self.neighbors.append(grid[self.row - 1][self.col])        
        
        if self.col < self.total_rows - 1 and not grid[self.row][self.col + 1].is_barrier():
          self.neighbors.append(grid[self.row][self.col + 1])        
        
        if self.col > 0 and not grid[self.row][self.col - 1].is_barrier():
          self.neighbors.append(grid[self.row][self.col - 1])
        

    def __lt__(self, other):
        return False


#GET OUR h(n)in the function f(n) = g(n) + h(n)

def h(p1, p2):
    x1, y1 = p1
    x2, y2 = p2

    return abs (x1 - x2) + abs(y1 - y2)

#make the path
def rec_path(came_from, end, draw):
  while end in came_from:
    end = came_from[end]
    end.make_path()
    draw()

#THE algorithm

def algorithm(draw, grid, start, end):
  draw()
  count = 0
  open_set = PriorityQueue()
  open_set.put((0, count, start))
  came_from = {}
  g_score = {spot: float("inf") for row in grid for spot in row}
  g_score[start] = 0
  f_score = {spot: float("inf") for row in grid for spot in row}
  f_score[start] = h(start.get_pos(), end.get_pos())

  open_set_hash = {start} 

  while not open_set.empty():
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
    
    current = open_set.get()[2]
    open_set_hash.remove(current)

    if current == end:
      end.make_end()

      rec_path(came_from, end, draw)
      
      return True

    for neighbor in current.neighbors:
      temp_g_scroe = g_score[current] + 1

      if temp_g_scroe < g_score[neighbor]:
        came_from[neighbor] = current
        g_score[neighbor] = temp_g_scroe
        f_score[neighbor] = temp_g_scroe + h(neighbor.get_pos(), end.get_pos())
      
        if neighbor not in open_set_hash:
          count += 1
          open_set.put((f_score[neighbor], count, neighbor))
          open_set_hash.add(neighbor)
          neighbor.make_open()
    draw()

    if current != start:
      current.make_closed()

  return None




       
#MAKEING OUR GRID

def make_grid(rows, width):
    grid = []
    gap = width // rows

    
    #MAKE GRID

    for i in range(rows):
        grid.append([])
        for j in range(rows):
            spot = Spot(i, j, gap, rows)
            grid[i].append(spot)

    return grid

#NOW WE NEED TO DRAW OUT GIRD

def draw_grid(win, rows, width):
    gap = width // rows
    for i in range(rows):
        #we make gird lines here
        pygame.draw.line(win, gray, (0, i * gap), (width ,  i * gap))
        for j in range(rows):
            pygame.draw.line(win, gray, (j * gap, 0), (j * gap, width))

#NOW A FUNCTION TO DRAW

def draw(win, grid, rows, width):
    win.fill(white)

    for row in grid:
        for spot in row:
            spot.draw(win)

    draw_grid(win, rows, width)
    pygame.display.update()

#NOW SOME MORE FUNCTIONS


def get_click_pos(pos, rows, width):
    gap = width // rows
    y, x = pos

    row = y // gap
    col = x // gap

    return row, col


#OUR MAIN LOOP

def main(win, width):
  ROWS = 50
  grid = make_grid(ROWS, width)
  
  start = None
  end = None
  
  run = True
  started = False
  
  while run:
    draw(win, grid, ROWS, width)
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        run = False
        
      if started:
        continue
      
      if pygame.mouse.get_pressed()[0]:
        pos = pygame.mouse.get_pos()
        row, col = get_click_pos(pos, ROWS, width)
        spot = grid[row][col]
        
        if not start and spot != end:
          start = spot
          start.make_start()
          
        elif not end and spot != start:
          end = spot
          end.make_end()
          
        elif spot != end and spot != start:
          spot.make_barrier()
        
      elif pygame.mouse.get_pressed()[2]:
        pos = pygame.mouse.get_pos()
        row, col = get_click_pos(pos, ROWS, width)
        spot = grid[row][col]
        spot.reset()
        if spot == start:
          start = None
        elif spot == end:
          end = None
      
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_SPACE and start and end:
          for row in grid:
            for spot in row:
              spot.update_neighbors(grid)
          
          algorithm(lambda: draw(win, grid, ROWS, width), grid, start, end)

     
        
  pygame.quit()
  
  


main(WIN, WIDTH)










        
    
    












