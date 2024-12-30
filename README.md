# Flappy Bird
#### Video Demo:  <URL HERE>https://youtu.be/54EFTiQMbvQ
#### Description:
Welcome to the **Flappy Bird Game**, a Python-powered recreation of the beloved arcade classic. This project uses the Pygame library to bring the essence of Flappy Bird to your computer, offering a rich, interactive gaming experience. Designed with object-oriented principles, the game incorporates smooth animations, customizable parameters, and intuitive controls, making it both fun to play and a great learning tool for aspiring developers.

The game simulates the original mechanics: controlling a bird to pass through pipes without colliding. With added features like score tracking, high score persistence, and dynamic visual effects, this version elevates the charm of the original game.

---

## File Structure and Descriptions

This project is modular, with each file handling a specific responsibility. Here’s a breakdown of the files:

### 1. `game.py`
This is the main script that initializes and runs the game. It serves as the entry point and orchestrates interactions between different game components.

- **Responsibilities:**
  - Initializes Pygame modules, sets up the display, and configures the game loop.
  - Manages the current game state (menu, gameplay, or game over screens).
  - Acts as the mediator between game logic and visuals.

---

### 2. `classes.py`
This file defines the core game objects and their behaviors, including the bird, ground, pipes, and score colliders.

- **Bird**:
  - Represents the player’s avatar.
  - Handles movement mechanics, including jumping and responding to gravity.
  - Animates the bird’s flapping motion.

- **Ground**:
  - Simulates the scrolling ground beneath the bird.
  - Detects collisions with the bird, ending the game when they occur.

- **Pipes**:
  - Creates obstacles that move from right to left.
  - Resets their position and gap when they move off-screen.
  - Detects collisions with the bird and awards points when successfully passed.

- **ScoreCollider**:
  - Invisible object placed between pipes to detect when the bird scores a point.

---

### 3. `globals.py`
This file centralizes global variables and constants for easy access and modification. It includes resources such as images, sounds, and gameplay parameters.

- **Key Constants**:
  - `GAME_RES`, `FPS`: Define screen resolution and frame rate.
  - `GRAVITY`, `SPEED`: Control game physics.
  - `HIT_BOXES`: Enables debugging by displaying hitboxes.

- **Resources**:
  - Paths to images, fonts, and audio files are specified here.
  - Pygame `Sound` and `Surface` objects are preloaded for efficiency.

---

### 4. `pages.py`
This module manages different screens in the game: the main menu, gameplay, and game over screen.

- **MainMenu**:
  - Displays the title screen with animated prompts.
  - Starts the game when the player presses the spacebar.

- **Gameplay**:
  - Runs the main game loop, handling bird movement, collision detection, and scoring.
  - Tracks whether the game can be restarted or exited to the main menu.

- **Game Over**:
  - Displays the final score and high score.
  - Allows the player to retry or return to the main menu.

---

### 5. `scores.py`
Handles the storage and retrieval of high scores using Python’s `pickle` module.

- **HighScore**:
  - Maintains the highest score achieved by the player.
  - Saves the high score to a file (`score.pkl`) and retrieves it when the game starts.

---

## Installation

### Prerequisites
- Python 3.8 or above
- Clone the repository:
    ```bash
    git clone https://github.com/Mohammad-Ali-Haider/flappy-bird.git
    cd flappy-bird-game
    ```

---

## Setting Up the Environment

To ensure a clean and organized setup for running the game, we recommend creating a Python virtual environment. Follow these steps:

### 1. Create a Virtual Environment
1. Open a terminal and navigate to the project directory.
2. Run the following command to create a virtual environment:
    ```bash
    python -m venv venv
    ```

### 2. Activate the Virtual Environment

- #### On Windows:
    ```bash
    venv\Scripts\activate
    ```
- #### On macOS/Linux:
    ```bash
    venv\Scripts\activate
    ```

Once activated, your terminal prompt will indicate that the virtual environment is active.

### 3. Install Pygame

With the virtual environment activated, install the Pygame library:
```bash
pip install pygame
```
You can verify the installation by running:
```bash
pip show pygame
```

---

## Running the Game
After setting up the environment, follow these steps to play the game:

1. Ensure the virtual environment is activated.
2. Navigate to the project directory.
3. Run the main script:
    ```bash
    python game.py
    ```

Enjoy the game! Use the spacebar to control the bird and try to achieve the highest score.

---

## Design Choices and Justifications
### 1. Modular Design
The project is divided into multiple files, each focusing on a specific aspect of the game. \
This modularity:
- Improves code readability and maintainability.
- Facilitates debugging and future enhancements.

### 2. Object-Oriented Approach
Game elements like the bird, pipes, and ground are represented as classes.\
This approach:
- Encapsulates behaviors and attributes for each object.
- Promotes code reuse and scalability.

### 3. Resource Preloading
Images and sounds are preloaded in globals.py to optimize performance. This avoids delays during gameplay caused by loading resources dynamically.

### 4. Collision Debugging
The HIT_BOXES flag allows developers to visualize hitboxes, simplifying the debugging of collision-related issues.

### 5. High Score Persistence
Using a file-based system for high score storage ensures players’ progress is not lost between sessions, enhancing user satisfaction.

---

## Future Enhancements
- Multiplayer Mode: Allow two players to compete on the same screen.
- Custom Skins: Provide options for players to change bird sprites or backgrounds.
- Dynamic Difficulty: Gradually increase speed or decrease pipe gaps as the score increases.

---

## Acknowledgments
This project was inspired by the original Flappy Bird game by Dong Nguyen. It was developed using Pygame, a powerful library for game development in Python.

Thank you for exploring this project! Feedback and contributions are welcome.