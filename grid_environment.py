# grid_environment.py
import random

class GridEnvironment:
    def __init__(self, rows, cols, obstacle_density=0.3):
        self.rows = rows
        self.cols = cols
        self.obstacle_density = obstacle_density
        self.grid = [[0 for _ in range(cols)] for _ in range(rows)]  # 0: empty, 1: obstacle
        self.start = (0, 0)
        self.goal = (rows-1, cols-1)
        self.current_pos = self.start
        
    def generate_random_maze(self):
        """Generate random obstacles with given density"""
        for i in range(self.rows):
            for j in range(self.cols):
                if random.random() < self.obstacle_density:
                    self.grid[i][j] = 1
                else:
                    self.grid[i][j] = 0
        
        # Ensure start and goal are not obstacles
        self.grid[self.start[0]][self.start[1]] = 0
        self.grid[self.goal[0]][self.goal[1]] = 0
        
    def set_obstacle(self, row, col, value):
        """Manually set obstacle at position"""
        if (row, col) != self.start and (row, col) != self.goal:
            self.grid[row][col] = value
            
    def is_valid(self, row, col):
        """Check if position is within grid and not obstacle"""
        if row < 0 or row >= self.rows or col < 0 or col >= self.cols:
            return False
        return self.grid[row][col] == 0
    
    def get_neighbors(self, row, col, diagonal=False):
        """Get valid neighboring positions (4 or 8-directional movement)"""
        neighbors = []
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # right, down, left, up
        if diagonal:
            directions += [(1, 1), (1, -1), (-1, 1), (-1, -1)]  # diagonals
        
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            if self.is_valid(new_row, new_col):
                neighbors.append((new_row, new_col))
        
        return neighbors
    
    def manhattan_distance(self, pos1, pos2):
        """Calculate Manhattan distance between two positions"""
        return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])
    
    def euclidean_distance(self, pos1, pos2):
        """Calculate Euclidean distance between two positions"""
        return ((pos1[0] - pos2[0])**2 + (pos1[1] - pos2[1])**2) ** 0.5
    
    def resize(self, new_rows, new_cols):
        """Resize the grid"""
        self.rows = new_rows
        self.cols = new_cols
        self.grid = [[0 for _ in range(new_cols)] for _ in range(new_rows)]
        self.start = (0, 0)
        self.goal = (new_rows-1, new_cols-1)
        self.current_pos = self.start