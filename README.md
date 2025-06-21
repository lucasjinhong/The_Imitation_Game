# The Imitation Game

"The Imitation Game" is an interactive, story-driven educational game built with Python and PyQt5. It takes players on a thrilling adventure through the world of computer science, teaching fundamental concepts like number systems and digital logic through engaging puzzles and a compelling narrative. Inspired by the pioneers of computing, the game challenges you to think like a machine to unravel its mysteries.

## Features

- **Interactive Narrative:** A multi-level story that unfolds as you solve challenges.
- **Educational Puzzles:** Learn and apply concepts of binary, hexadecimal, and logic gates (NOT, AND, OR, XOR, NAND, NOR, XNOR).
- **Progressive Difficulty:** Three distinct story levels that build upon each other, introducing more complex topics.
- **Graphical User Interface:** A user-friendly desktop application powered by PyQt5.
- **Dynamic Question Generation:** Puzzles are generated dynamically, offering replayability.

## Story Synopsis

The game is divided into three parts, each with its own unique story and set of challenges:

- **Story 1: The Escape Room**
  You awaken in a mysterious room with two doors: "Real" and "Unreal". To escape, you must master the basics of binary and hexadecimal number systems, making choices that will lead you to a final, combined puzzle.

- **Story 2: The Binaropolis Heroes**
  In the digital city of Binaropolis, a mysterious hacker threatens to plunge the world into chaos. Team up with the four heroes—Not, And, Or, and Xor—to decipher the hacker's obfuscated code and save the city, learning the function of each logic gate along the way.

- **Story 3: The Puppet Master**
  The threat evolves. A new hacker emerges, turning the heroes against each other by manipulating their core logic. You must delve deeper into advanced logic, including NAND, NOR, and XNOR gates, and understand concepts like logic simplification and signal buffering to free your friends and unmask the true enemy.

## Requirements

- Python 3.x
- PyQt5

## Installation & Usage

1.  **Clone the repository:**
    ```sh
    git clone https://github.com/lucasjinhong/The_Imitation_Game.git
    cd The_Imitation_Game
    ```

2.  **Install the required package:**
    ```sh
    pip install -r requirements.txt
    ```

3.  **Run the game:**
    ```sh
    python main.py
    ```

## Project Structure

- `main.py`: The main entry point for the application.
- `View/`: Contains all PyQt5 UI components and the presentation logic for the story.
- `Controller/`: Holds the core game logic, including puzzle generation (`Codec`) and story flow.
- `Model/`: Stores all the narrative text files (`.txt`) for the different story levels and scenes.
- `requirements.txt`: Lists the project dependencies.

## Credits

- **Story & Puzzle Design:** 凱勛 (28598519a 劃破黑夜)
- **Programming:** 峻灃 (lucasjinhong), 凱勛 (28598519a 劃破黑夜)
- **PyQt5 Interface:** 景霖 (TaylorNTUT), 凱勛 (28598519a 劃破黑夜)
