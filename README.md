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
![Initial Grid](https://private-user-images.githubusercontent.com/51924838/303491847-77ffef19-3a7c-4f51-a15d-3191c4075465.jpg?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MDc0MjkwNTgsIm5iZiI6MTcwNzQyODc1OCwicGF0aCI6Ii81MTkyNDgzOC8zMDM0OTE4NDctNzdmZmVmMTktM2E3Yy00ZjUxLWExNWQtMzE5MWM0MDc1NDY1LmpwZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNDAyMDglMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjQwMjA4VDIxNDU1OFomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPWZkZjAzYjNkZjUwODc2YTQwMmFkNTk5OGM4MTkxZDFmOGE4NTM2OTIyODhiNGZiMjdhMGY3ZDRmMzAxMGFlYjYmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JmFjdG9yX2lkPTAma2V5X2lkPTAmcmVwb19pZD0wIn0.wSx8TKbbbKCcj46V2MgB4ALfAJBhySJ2OUQ0EYuo_wI)

*Description*: This screenshot shows the initial grid where the user has set the starting point (light green block), the ending point (dark green block), and added barriers (grey blocks).

### Shortest Path
![Shortest Path](https://private-user-images.githubusercontent.com/51924838/303491845-097bba49-30db-46b8-8efc-1aef5543d195.jpg?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MDc0MjkwNTgsIm5iZiI6MTcwNzQyODc1OCwicGF0aCI6Ii81MTkyNDgzOC8zMDM0OTE4NDUtMDk3YmJhNDktMzBkYi00NmI4LThlZmMtMWFlZjU1NDNkMTk1LmpwZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNDAyMDglMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjQwMjA4VDIxNDU1OFomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTdiNDVmYTE4NTUyMmUwZWEyZmMzNjAwZmE5OGNjZjBhMjM5MDcxNmFmMmExNzg5YjczMWU5NWU4ZmFhMmI1NDkmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JmFjdG9yX2lkPTAma2V5X2lkPTAmcmVwb19pZD0wIn0.zFwk99_Me7lfo1mrGvHy-f_30dGCZ4mpwL00XwIiDg0)

*Description*: This screenshot displays the final grid with the generated shortest path (sequence of blue blocks) using the A* algorithm. The red blocks represent closed spots, indicating areas that have been explored but deemed unsuitable for the current path. The yellow blocks represent open spots, marking areas that are still being evaluated for potential inclusion in the path.

## Contributors

- Nimisha Bhagat - https://github.com/nimisha218

