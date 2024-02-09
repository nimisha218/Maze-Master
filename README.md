# Maze Master Game

Maze Master is a maze-solving game implemented using Python and Pygame library. In this game, you can create your own maze by placing start and end points, along with barriers, and then watch as the A* algorithm finds the shortest path between the start and end points.

## Installation

1. Make sure you have Python installed on your system. You can download it from [python.org](https://www.python.org/).

2. Install Pygame library by running the following command:
    ```
    pip install pygame
    ```

3. Clone or download this repository to your local machine.

4. Navigate to the directory containing the `maze_master.py` file.

## Usage

Run the maze_master.py script using the following command:
    ```
    python maze_master.py
    ```

Once the game window appears, follow these instructions:

- First left click will set the starting point.
- The next left click will set the ending point.
- Subsequent left clicks will set barriers.
- Right-clicking on any clicked spot will reset the spot.
- Press the SPACE key to start the A* algorithm and find the shortest path between the start and end points.
- Press the 'C' key to clear the window and start a new search.

## Screenshots

### Initial Grid
![Initial Grid](https://github.com/nimisha218/Maze-Master/blob/main/Images/InitialGrid.png)

*Description*: This screenshot shows the initial grid where the user has set the starting point (light green block), the ending point (dark green block), and added barriers (grey blocks).

### Shortest Path
![Shortest Path](https://github.com/nimisha218/Maze-Master/blob/main/Images/FinalGrid.png)

*Description*: This screenshot displays the final grid with the generated shortest path (sequence of blue blocks) using the A* algorithm. The red blocks represent closed spots, indicating areas that have been explored but deemed unsuitable for the current path. The yellow blocks represent open spots, marking areas that are still being evaluated for potential inclusion in the path.

## Contributors

- Nimisha Bhagat - https://github.com/nimisha218

