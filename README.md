# Asteroids

This is a classic Asteroids arcade game clone built using **Python** and the **Pygame** library. This project was developed as part of the backend development curriculum on [Boot.dev](https://www.boot.dev) by Jerome Tremblay.

## Description

In this game, you control a spaceship in a field of asteroids. The goal is to survive as long as possible by maneuvering and blasting asteroids into smaller fragments. This project demonstrates core programming concepts such as:

*   **Object-Oriented Programming (OOP)**: Using classes and inheritance for game entities.
*   **Game Loops**: Managing updates and rendering at a consistent frame rate.
*   **Vector Math**: Using `pygame.Vector2` for movement, rotation, and velocity.
*   **Collision Detection**: Implementing circular hitboxes to detect interactions between objects.

## Installation

1.  Ensure you have [Python 3](https://www.python.org/) installed on your system.
2.  Install the Pygame library:
    ```bash
    pip install pygame
    ```
3.  Clone this repository:
    ```bash
    git clone https://[https://github.com/Jerome-Tremblay/Asteroids]
    ```

## How to Play

Run the game using Python in the terminal:

```bash
uv run main.py
```

## Controls

*   **W / S**: Move forward and backward
*   **A / D**: Rotate the ship left and right
*   **Space**: Fire lasers

## Development Process

This project was built step-by-step, starting from a basic game loop to a fully functional game with multiple classes:

*   **Player**: Handles movement and shooting.
*   **Asteroid**: Handles splitting logic and random movement.
*   **Shot**: Manages projectiles.
*   **AsteroidField**: A management class that spawns asteroids at intervals.

## Custom Features

While the core concepts of the project were established through Boot.dev's backend curriculum, additional custom features were added by Jerome Tremblay.

*    **Score**: A score system was added (1 asteroids destroyed = 1 point).
*   **UI**: A simple UI was added to the right of the screen, superposed on top of the game.
*    **Signature**: A simple signature was added to the bottom of the UI.
*    **Game State**: A Game State to the game was added with a Starting menu, a Playing interface (the original) and a Game Over screen.
*    **High Score**: A High Score system carrying through games was added. This High Score disappears if the user quits the program.

## Credits

Boot.dev Team
Etienne Rayes
