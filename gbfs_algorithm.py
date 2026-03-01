# gbfs_algorithm.py
import time
from queue import PriorityQueue

class GBFS:
    def __init__(self, grid_env, heuristic='manhattan'):
        self.grid = grid_env
        self.heuristic = heuristic
        self.nodes_visited = 0
        self.path = []
        self.frontier = []
        self.visited = []
        self.execution_time = 0
        self.path_cost = 0
        
    def search(self, start, goal):
        """Perform Greedy Best-First Search"""
        start_time = time.time()
        
        # Priority queue for frontier (priority, position, path)
        frontier = PriorityQueue()
        frontier.put((0, start, [start]))
        
        # Track visited nodes
        visited_set = set()
        visited_set.add(start)
        
        self.nodes_visited = 0
        self.frontier = [start]
        self.visited = []
        self.path = []
        
        while not frontier.empty():
            # Get node with lowest heuristic value
            priority, current, path = frontier.get()
            self.nodes_visited += 1
            if current not in self.visited:
                self.visited.append(current)
            
            # Update frontier visualization
            self.frontier = []
            for item in list(frontier.queue):
                if item[1] not in self.visited:
                    self.frontier.append(item[1])
            
            # Check if we reached the goal
            if current == goal:
                self.path = path
                self.path_cost = len(path) - 1  # Number of steps
                self.execution_time = (time.time() - start_time) * 1000
                return path
            
            # Explore neighbors (8-directional for euclidean, 4-directional for manhattan)
            use_diagonal = (self.heuristic == 'euclidean')
            for neighbor in self.grid.get_neighbors(current[0], current[1], diagonal=use_diagonal):
                if neighbor not in visited_set:
                    visited_set.add(neighbor)
                    
                    # Calculate heuristic
                    if self.heuristic == 'manhattan':
                        h_value = self.grid.manhattan_distance(neighbor, goal)
                    else:  # euclidean
                        h_value = self.grid.euclidean_distance(neighbor, goal)
                    
                    # Add to frontier with heuristic as priority
                    new_path = path + [neighbor]
                    frontier.put((h_value, neighbor, new_path))
                    if neighbor not in self.frontier:
                        self.frontier.append(neighbor)
        
        self.execution_time = (time.time() - start_time) * 1000
        return None  # No path found
    
    def get_stats(self):
        """Return search statistics"""
        return {
            'nodes_visited': len(self.visited),
            'path_cost': self.path_cost,
            'execution_time': self.execution_time
        }