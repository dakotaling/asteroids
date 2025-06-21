# Asteroids Game

A classic arcade-style asteroids game built with Python and Pygame, demonstrating comprehensive Object-Oriented Programming principles.

## Game Features

- **Classic Asteroids Gameplay**: Navigate your spaceship through an asteroid field
- **Dynamic Asteroid Splitting**: Large asteroids break into smaller pieces when shot
- **Collision Detection**: Player-asteroid and bullet-asteroid collision systems
- **Pause Functionality**: Press P or SPACEBAR to pause/resume the game
- **Continuous Asteroid Spawning**: New asteroids spawn from screen edges at regular intervals
- **Smooth 60 FPS Gameplay**: Consistent frame rate with delta time-based movement

## Installation

### Prerequisites
- Python 3.7 or higher
- Git
- pip (Python package installer)

### Setup Instructions

As a best practice, each Python project on your machine should have its own virtual environment to keep them isolated from each other.

1. **Create a new directory and Git repository for this project**:
   ```bash
   mkdir asteroids-game
   cd asteroids-game
   git clone https://github.com/dakotaling/asteroids.git
   ```

2. **Create a virtual environment at the top level of your project directory**:
   ```bash
   python3 -m venv venv
   ```

3. **Activate the virtual environment**:
   ```bash
   source venv/bin/activate
   ```
   You should see `(venv)` at the beginning of your terminal prompt.

4. **Create a file called `requirements.txt` in the top level of your project directory**:
   ```
   pygame==2.6.1
   ```
   This tells Python that this project requires pygame version 2.6.1.

5. **Install the requirements**:
   ```bash
   pip install -r requirements.txt
   ```
   pip is Python's package manager. It will install the pygame module into the virtual environment you created.

6. **Verify pygame is installed**:
   ```bash
   python3 -m pygame
   ```
   This will result in an error (expected), but the output will show that pygame is installed.

7. **Run the game**:
   ```bash
   python main.py
   ```

Make sure that your virtual environment is activated when running the game.

## Controls
- **Arrow Keys**: Move your spaceship
- **Spacebar**: Shoot bullets
- **P or Spacebar**: Pause/Resume game
- **ESC or Close Window**: Quit game

## Object-Oriented Programming Concepts

This project demonstrates advanced OOP principles and design patterns:

### 1. **Inheritance Hierarchy**
- **Base Class**: `CircleShape` serves as the foundation for all circular game objects
- **Derived Classes**: `Player`, `Asteroid`, and `Shot` all inherit from `CircleShape`
- **Method Inheritance**: All classes inherit collision detection and basic positioning logic

```python
class CircleShape(pygame.sprite.Sprite):  # Base class
    def collides_with(self, other):       # Shared method

class Player(CircleShape):                # Inherits collision detection
class Asteroid(CircleShape):              # Inherits collision detection  
class Shot(CircleShape):                  # Inherits collision detection
```

### 2. **Polymorphism**
- **Method Overriding**: Each class implements its own `draw()` and `update()` methods
- **Uniform Interface**: All game objects can be treated uniformly through the base class interface
- **Dynamic Method Resolution**: The correct method is called based on the actual object type

```python
# Same method call works for all object types
for obj in drawable:
    obj.draw(screen)  # Calls Player.draw(), Asteroid.draw(), or Shot.draw()
```

### 3. **Encapsulation**
- **Data Hiding**: Object properties (position, velocity, radius) are encapsulated within classes
- **Controlled Access**: Public methods provide controlled access to internal state
- **Method Cohesion**: Related functionality is grouped within appropriate classes

### 4. **Composition and Aggregation**
- **Sprite Groups**: Uses Pygame's sprite groups to manage collections of objects
- **Container System**: Objects automatically add themselves to appropriate groups via `containers` attribute
- **Loose Coupling**: Objects interact through well-defined interfaces rather than direct manipulation

```python
# Objects automatically join appropriate groups
Player.containers = (updatable, drawable)
Asteroid.containers = (asteroids, updatable, drawable)
```

### 5. **Factory Pattern**
- **AsteroidField Class**: Acts as a factory for creating new asteroids
- **Parameterized Creation**: Creates asteroids with varying sizes, positions, and velocities
- **Centralized Creation Logic**: All asteroid spawning logic is contained in one place

### 6. **Strategy Pattern**
- **Edge Spawning**: Different spawning strategies for each screen edge
- **Configurable Behavior**: Asteroid spawning behavior can be easily modified
- **Data-Driven Design**: Spawn locations and directions defined in data structures

### 7. **Template Method Pattern**
- **Base Update Cycle**: `CircleShape` provides template for position updates
- **Specialized Behavior**: Subclasses add their own specific update logic
- **Consistent Interface**: All objects follow the same update pattern

### 8. **Single Responsibility Principle**
- **Player Class**: Handles only player-specific logic (movement, shooting)
- **Asteroid Class**: Manages only asteroid behavior (movement, splitting)
- **AsteroidField Class**: Responsible only for spawning new asteroids
- **Shot Class**: Handles only projectile behavior

### 9. **Open/Closed Principle**
- **Extensible Design**: New object types can be added by inheriting from `CircleShape`
- **Modification Safe**: Core game loop doesn't need changes for new object types
- **Plugin Architecture**: New behaviors can be added without modifying existing code

## Project Structure

```
asteroids-game/
├── main.py           # Game loop and main logic
├── player.py         # Player class definition
├── asteroid.py       # Asteroid class definition
├── shot.py          # Shot/bullet class definition
├── asteroidfield.py # Asteroid spawning system
├── circleshape.py   # Base class for circular objects
├── constants.py     # Game configuration constants
└── README.md        # This file
```

## Configuration

Game parameters can be modified in `constants.py`:
- Screen dimensions
- Player movement speeds
- Asteroid properties
- Shooting mechanics
- Spawn rates

## Learning Outcomes

This project demonstrates:
- **Class Design**: Creating meaningful class hierarchies
- **Code Reusability**: Sharing common functionality through inheritance
- **Maintainable Architecture**: Organizing code for easy modification and extension
- **Game Development Patterns**: Common patterns used in game programming
- **Python OOP Best Practices**: Proper use of Python's object-oriented features

## Future Enhancements

Potential improvements that would demonstrate additional OOP concepts:
- **Observer Pattern**: Score tracking and event notifications
- **State Machine**: Different game states (menu, playing, game over)
- **Command Pattern**: Input handling and replay systems
- **Decorator Pattern**: Power-ups and temporary abilities
- **Singleton Pattern**: Game configuration management

---

*This project showcases practical application of Object-Oriented Programming principles in game development, demonstrating how proper OOP design leads to maintainable, extensible, and well-organized code.*
