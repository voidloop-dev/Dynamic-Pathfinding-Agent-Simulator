# 🧠 Dynamic Pathfinding Agent

An interactive visualization tool demonstrating real-time pathfinding algorithms with dynamic obstacle handling. Watch as AI agents navigate through mazes that change in real-time!

![Python](https://img.shields.io/badge/Python-3.6%2B-blue)
![Pygame](https://img.shields.io/badge/Pygame-2.5.2-green)
![License](https://img.shields.io/badge/License-MIT-yellow)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)

## 📋 Table of Contents
- [Features](#-features)
- [Color Legend](#-color-legend)
- [Algorithms Implemented](#-algorithms-implemented)
- [Installation](#-installation)
- [How to Run](#-how-to-run)
- [Usage Guide](#-usage-guide)
- [Button Controls](#-button-controls)
- [Project Structure](#-project-structure)
- [How It Works](#-how-it-works)
- [Development Process](#-development-process)
- [Troubleshooting](#-troubleshooting)
- [License](#-license)

## ✨ Features

### Core Functionality
- **Multiple Algorithms**: Compare A* and Greedy Best-First Search (GBFS)
- **Dual Heuristics**: Manhattan and Euclidean distance calculations
- **Dynamic Environment**: Random obstacles spawn while agent moves (20% chance per step)
- **Real-time Replanning**: Instant path recalculation when obstacles appear
- **Interactive Editor**: Click to add/remove obstacles manually

### User Controls
- **Custom Start/Goal**: Set your own start and goal positions
- **Algorithm Selection**: Toggle between algorithms before searching
- **Grid Resizing**: Adjust grid dimensions (5-20 rows, 8-30 columns)
- **Density Control**: Set obstacle density from 10% to 90%
- **Dynamic Mode Toggle**: Turn dynamic obstacles on/off

## 🎨 Color Legend

| Color | Representation | Description |
|-------|---------------|-------------|
| 🟩 **Green Square** | Start Node | Initial position of the agent |
| 🟥 **Red Square** | Goal Node | Target destination |
| 🟨 **Yellow Square** | Frontier Nodes | Nodes currently in the priority queue (waiting to be explored) |
| 🟦 **Light Blue Square** | Visited Nodes | Nodes that have been expanded/explored |
| 🟩 **Green Line** | Final Path | The calculated optimal path connecting cell centers |
| ⬛ **Black Square** | Static Obstacles | Original obstacles from maze generation |
| 🟧 **Orange Square** | Dynamic Obstacles | New obstacles that appear during movement (20% spawn chance) |
| 🟠 **Orange Circle** | Current Agent Position | Real-time location of the agent |


### Status Bar Messages
- `Status: Ready` - Waiting for input
- `Status: Moving` - Agent following path
- `Status: Replanning...` - Obstacle detected, calculating new path
- `Status: Goal reached` - Successfully arrived at destination
- `Status: No path found` - Cannot reach goal with current obstacles
- `Status: New obstacle appeared!` - Dynamic obstacle spawned

## 🧮 Algorithms Implemented

### 1. A* Search
- **Evaluation Function**: `f(n) = g(n) + h(n)`
- **g(n)**: Actual cost from start to node n
- **h(n)**: Heuristic estimate to goal
- **Properties**: Optimal and complete, finds shortest path

### 2. Greedy Best-First Search (GBFS)
- **Evaluation Function**: `f(n) = h(n)`
- **h(n)**: Heuristic estimate to goal only
- **Properties**: Faster but may not find optimal path

### 3. Heuristic Functions
- **Manhattan Distance**: `|x1 - x2| + |y1 - y2|` (for 4-directional movement)
- **Euclidean Distance**: `√[(x1 - x2)² + (y1 - y2)²]` (for diagonal movement)

## 💻 Installation

### Prerequisites
- Python 3.6 or higher
- pip (Python package installer)

### Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/dynamic-pathfinding-agent.git
   cd dynamic-pathfinding-agent
2.  Install dependencies

   pip install -r requirements.txt
   (This installs pygame - the only external dependency)

Run the application

bash
python main_pygame.py
## 🎮 How to Run
bash
# Navigate to project directory
cd dynamic-pathfinding-agent

  # Run the main program
    python main_pygame.py

##📖 Usage Guide
 # Basic Workflow
    **Generate a Maze
    Click "GENERATE" for random obstacles
    Or click individual cells to place/remove obstacles manually

# Select Algorithm :

      Click "A MAN"* (A* with Manhattan heuristic)
      
      Click "A EUC"* (A* with Euclidean heuristic)
      
      Click "GBFS MAN" (GBFS with Manhattan heuristic)
      
      Click "GBFS EUC" (GBFS with Euclidean heuristic)
   
      Selected algorithm will be highlighted in cyan

# Set Start/Goal (Optional) :

      Click "SET START" then click any empty cell to place new start
      
      Click "SET GOAL" then click any empty cell to place new goal
      
      Click "RESET POS" to return to default positions

# Find Path :

      Click "FIND PATH" to calculate the route
      
      Watch as yellow frontier nodes expand and turn blue when visited
      
      Green path line appears when route is found

# Navigate :

      Click "START" to begin agent movement
      
      Click "STOP" to pause

      Watch the orange circle agent follow the green path

# Dynamic Mode (Optional)

      Click "DYNAMIC ON" to enable dynamic obstacles
      
      Orange squares will appear randomly (20% chance per step)
      
      Agent automatically replans when path is blocked
      
      Watch the path recalculate in real-time

# Clear Dynamic Obstacles

  Click "CLEAR DYN" to remove all orange dynamic obstacles

## 🎯 Button Controls
  # Row 1 - Grid Controls :
      Button	Function
     GENERATE	Create random maze with current density setting
     CLEAR	   Remove all obstacles from the grid
     GRID RxC	Change grid dimensions (click, then enter rows/cols)
    DENSITY X%	Adjust obstacle percentage (10-90%)
 # Row 2 - Algorithm Selection :
      Button	Function
      A MAN*	Select A* algorithm with Manhattan heuristic
      A EUC*	Select A* algorithm with Euclidean heuristic
      GBFS MAN	Select GBFS algorithm with Manhattan heuristic
     GBFS EUC	Select GBFS algorithm with Euclidean heuristic
 # Row 3 - Start/Goal Editing :
      Button	Function
    SET START	Enter start placement mode (click grid to set)
    SET GOAL	Enter goal placement mode (click grid to set)
    RESET POS	Reset start and goal to default positions
 # Row 4 - Actions :
      Button	Function
    FIND PATH	Calculate path using selected algorithm
     START	   Begin agent movement along path
     STOP	   Pause agent movement
    DYNAMIC	   Toggle dynamic obstacle spawning
    CLEAR DYN	Remove all dynamically spawned obstacles
## 📁 Project Structure :
dynamic-pathfinding-agent/
│
├── main_pygame.py          # Main GUI application with Pygame (entry point)
├── grid_environment.py     # Grid management and heuristic calculations
├── gbfs_algorithm.py       # Greedy Best-First Search implementation
├── astar_algorithm.py      # A* Search implementation
├── dynamic_pathfinding.py  # Dynamic obstacle handling and replanning logic
├── button.py               # Custom button class for Pygame interface
├── requirements.txt        # Project dependencies (pygame only)
└── README.md               # Project documentation (this file)

## ⚙️ Configuration

| Parameter          | Default | Min | Max | Description                    |
|--------------------|---------|-----|-----|--------------------------------|
| Rows               | 12      | 5   | 20  | Number of grid rows            |
| Columns            | 18      | 8   | 30  | Number of grid columns         |
| Obstacle Density   | 40%     | 10% | 90% | Percentage of cells as walls   |
| Spawn Probability  | 20%     | —   | —   | Chance of new obstacle per step|

---

## 🔍 How It Works

1. **Grid Generation** — A random grid is generated with obstacles based on the configured density, ensuring the start `(0,0)` and goal `(rows-1, cols-1)` remain clear.

2. **Path Search** — The selected algorithm (A\* or GBFS) with the chosen heuristic finds a path from start to goal using 4-directional movement (up, down, left, right).

3. **Agent Movement** — The agent moves step-by-step along the computed path. If **dynamic mode** is enabled, new obstacles may randomly appear on the grid.

4. **Adaptive Replanning** — At each step, the system checks whether the remaining path is still clear. If an obstacle blocks the path, the agent **automatically replans** from its current position using the same algorithm.

## Search Visualization :
   Frontier (Yellow): Nodes currently in the priority queue waiting to be explored

   Visited (Light Blue): Nodes that have already been expanded

   Path (Green Line): Final optimal path from start to goal

## Development Process :
   This project was developed iteratively in three phases:

**Commit 1: Core Grid and Basic Structure
   Grid environment with obstacle density control

   Manhattan and Euclidean distance heuristics

   Basic data structures for pathfinding

**Commit 2: Algorithm Implementation
   A* search algorithm with g(n) + h(n) evaluation

  Greedy Best-First Search with pure heuristic evaluation

  Path cost calculation and node visitation tracking

**Commit 3: GUI and Dynamic Features
  Full Pygame interface with all control buttons

  Dynamic obstacle spawning (20% chance per step)

  Real-time replanning when path is blocked

  Start/Goal editing functionality

  Visual feedback with color-coded cells

  Live metrics display

## ❗ Troubleshooting :
   **Common Issues and Solutions
  **Issue | Solution
     => "Module not found: pygame" |	Run pip install pygame
     => No path found | Reduce obstacle density or clear some obstacles
     => Agent gets stuck	| Click "STOP" then "FIND PATH" again
     => Grid too small/large |	Use "GRID" button to adjust dimensions
     => Too many obstacles |	Reduce density percentage or click "CLEAR"
     => Dynamic obstacles not appearing |	Make sure "DYNAMIC ON" is displayed
     => Can't set start/goal |	Cannot place on existing obstacles
     => Performance Tips | Keep grid size under 20x30 for smooth performance

         Density above 70% may make paths impossible Dynamic mode works best with density 30-50%

## 📝 requirements.txt :
text
pygame==2.5.2

## 📄 License :
This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments :
Thanks to the Pygame community for the excellent library

Inspired by classic pathfinding algorithm visualizations

Built for educational purposes to demonstrate AI search strategies

## 📧 Contact :
hasnainbwp765@gmail.com

Project Link: https://github.com/yourusername/dynamic-pathfinding-agent

⭐ Star this repository if you find it useful!

Happy Pathfinding! 🚀
