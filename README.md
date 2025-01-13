# Mazing

This project is a maze generation and solving application using Python. It creates a maze, displays it graphically, and attempts to solve it.

## Features

- Generates a maze with specified dimensions.
- Displays the maze graphically.
- Solves the maze and indicates whether it is solvable.

## Requirements

- Python 3.x
- `graphics` library (or any other library you are using for graphical display)

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/mdelgadonyc/mazing.git
    cd mazing
    ```

2. Install the required libraries:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

Run the main script to generate and solve a maze:
```sh
python main.py
```

## Project Structure

- `main.py`: The main script to run the application.
- `maze.py`: Contains the `Maze` class which handles maze generation and solving.
- `cell.py`: Contains the `Cell` class used by the `Maze` class.
- `graphics.py`: Contains the `Window` class for graphical display.

## Example

When you run the application, it will create a maze with the specified dimensions, display it, and attempt to solve it. The output will indicate whether the maze is solvable.

```sh
maze created
Maze is solved
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.