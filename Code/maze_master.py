import pygame
from queue import PriorityQueue

# Set the width of the window
WINDOW_WIDTH = 600

# Initialize the display
DISPLAY = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_WIDTH))

# Set the caption for the game window
pygame.display.set_caption("Welcome to Maze Master")

# Define color codes for the game theme
START = (0, 255, 0)  # Light Green
END = (0, 100, 0)  # Dark Green
PASTEL_RED = (255, 128, 128)
PASTEL_YELLOW = (255, 255, 153)
PASTEL_BLUE = (173, 216, 230)
PASTEL_WHITE = (255, 255, 255)
PASTEL_BLACK = (96, 96, 96)
BLUE = (0, 0, 255)
PASTEL_GREY = (192, 192, 192)

class Spot:
    def __init__(self, row, col, width, total_rows):

        self.row = row
        self.col = col
        self.x = row * width
        self.y = col * width 
        self.color = PASTEL_WHITE
        self.neighbours = []
        self.width = width
        self.total_rows = total_rows
    
    # Get the position of the current spot
    def get_position(self):
        return self.row, self.col
    
    # Check if the spot is closed
    def is_closed(self):
        return self.color == PASTEL_RED
    
    # Check if the spot is open
    def is_open(self):
        return self.color == PASTEL_YELLOW
    
    # Check if the spot is a barrier
    def is_barrier(self):
        return self.color == PASTEL_BLACK

    # Check if the spot is the start
    def is_start(self):
        return self.color == START  
    
    # Check if the spot is the end
    def is_end(self):
        return self.color == END  
    
    # Reset the spot
    def reset(self):
        self.color = PASTEL_WHITE

    # Make the spot the start
    def make_start(self):
        self.color = START  
    
    # Make the spot closed (PASTEL_RED)
    def make_closed(self):
        self.color = PASTEL_RED

    # Make the spot open (PASTEL_YELLOW)
    def make_open(self):
        self.color = PASTEL_YELLOW

    # Make the spot a barrier (PASTEL_BLACK)
    def make_barrier(self):
        self.color = PASTEL_BLACK
    
    # Make the spot the end 
    def make_end(self):
        self.color = END  
    
    # Mark the spot as part of the path (BLUE)
    def make_path(self):
        self.color = BLUE
    
    # Draw a rectangle representing the spot on the screen
    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.width))

    # Update the neighbors of the spot on the grid
    def update_neighbors(self, grid):

        self.neighbours = []

        # Move down
        if self.row < self.total_rows - 1 and not grid[self.row + 1][self.col].is_barrier():
            self.neighbours.append(grid[self.row + 1][self.col])
        
        # Move up
        if self.row > 0 and not grid[self.row - 1][self.col].is_barrier():
            self.neighbours.append(grid[self.row - 1][self.col])

        # Move right
        if self.col < self.total_rows - 1 and not grid[self.row][self.col + 1].is_barrier():
            self.neighbours.append(grid[self.row][self.col + 1])
        
        # Move left
        if self.col > 0 and not grid[self.row][self.col - 1].is_barrier():
            self.neighbours.append(grid[self.row][self.col - 1])
    

# Heuristic function (Manhattan distance)
def heuristic(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return abs(x1-x2) + abs(y1-y2)

# Reconstruct the path from start to end
def reconstruct_path(came_from, current, draw):
    while current in came_from:
        current = came_from[current]
        current.make_path()
        draw()

# A* algorithm for pathfinding
def algorithm(draw, grid, start, end):
    
    count = 0
    open_set = PriorityQueue()
    open_set.put((0, count, start))
    # came_from will be used for path reconstruction
    came_from = {}
    # All the g_scores and f_scores will be infinity initially
    g_score = {spot: float("inf") for row in grid for spot in row}
    g_score[start] = 0
    f_score = {spot: float("inf") for row in grid for spot in row}
    f_score[start] = heuristic(start.get_position(), end.get_position())

    # Add the starting node to the open set
    open_set_hash = {start}

    while not open_set.empty():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        current = open_set.get()[2]
        open_set_hash.remove(current)

        if current == end:
            # Search complete -> recontruct the path now
            reconstruct_path(came_from, end, draw)
            end.make_end()
            return True
        
        for neighbor in current.neighbours:

            # Assuming 2 squares are "1" distance apart
            temp_g_score = g_score[current] + 1

            # Found a better g_score -> update the g_score
            if temp_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = temp_g_score
                f_score[neighbor] = temp_g_score + heuristic(neighbor.get_position(), end.get_position())

                if neighbor not in open_set_hash:
                    count += 1
                    open_set.put((f_score[neighbor], count, neighbor))
                    open_set_hash.add(neighbor)
                    neighbor.make_open()

        draw()

        if current != start:
            current.make_closed()

    return False 

# Create the main grid
def create_grid(rows, width):
    grid = []
    gap = width // rows
    for i in range(rows):
        grid.append([])
        for j in range(rows):
            spot = Spot(i, j, gap, rows)
            grid[i].append(spot)
    return grid

# Draw the grid lines on the main display
def draw_grid_lines(win, rows, width):
    gap = width // rows
    for i in range(rows):
        # Draw horizontal lines on the grid
        pygame.draw.line(win, PASTEL_GREY, (0, i * gap), (width, i * gap))
        for j in range(rows):
            # Draw vertical lines on the grid
            pygame.draw.line(win, PASTEL_GREY, (j * gap, 0), (j * gap, width))

# Draw the main grid
def draw_main_grid(win, grid, rows, width):
    win.fill(PASTEL_WHITE)
    for row in grid:
        for spot in row:
            spot.draw(win)

    draw_grid_lines(win, rows, width)
    pygame.display.update()

# Get the coordinates of the spot clicked on the grid
def get_clicked_position(pos, rows, width):
    gap = width // rows
    y, x = pos
    row = y // gap
    col = x // gap
    return row, col

# Main function to run the game
def main_game(win, width):
    ROWS = 30
    grid = create_grid(ROWS, width)

    start = None
    end = None

    run = True

    while run:

        draw_main_grid(win, grid, ROWS, width)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                run = False
            
            # [0] represents left mouse click
            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_position(pos, ROWS, width)
                spot = grid[row][col]

                if not start and spot != end:
                    start = spot
                    start.make_start()
                
                elif not end and spot != start:
                    end = spot
                    end.make_end()
                
                elif spot != end and spot != start:
                    spot.make_barrier()

            # [2] represents right mouse click 
            if pygame.mouse.get_pressed()[2]:
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_position(pos, ROWS, width)
                spot = grid[row][col]
                spot.reset()

                if spot == start:
                    start = None

                elif spot == end:
                    end = None

            if event.type == pygame.KEYDOWN:

                # Start pathfinding algorithm on pressing "space"
                if event.key == pygame.K_SPACE and start and end:
                    for row in grid:
                        for spot in row:
                            spot.update_neighbors(grid)
                    algorithm(lambda: draw_main_grid(win, grid, ROWS, width), grid, start, end)
                    start.make_start()

                # Reset the window on pressing "c"
                if event.key == pygame.K_c:
                    start = None
                    end = None
                    grid = create_grid(ROWS, width)

    pygame.quit()

if __name__ == "__main__":
    main_game(DISPLAY, WINDOW_WIDTH)
