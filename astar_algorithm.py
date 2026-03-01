# astar_algorithm.py
import time
from queue import PriorityQueue

class AStar:
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
        """Perform A* Search"""
        start_time = time.time()
        
        # Priority queue for frontier (f_value, position, path, g_cost)
        frontier = PriorityQueue()
        frontier.put((0, start, [start], 0))
        
        # Track visited nodes and their g costs
        g_costs = {start: 0}
        
        self.nodes_visited = 0
        self.frontier = [start]
        self.visited = []
        self.path = []
        
        while not frontier.empty():
            # Get node with lowest f = g + h
            f_value, current, path, g_cost = frontier.get()
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
                self.path_cost = g_cost
                self.execution_time = (time.time() - start_time) * 1000
                return path
            
            # Explore neighbors (8-directional for euclidean, 4-directional for manhattan)
            use_diagonal = (self.heuristic == 'euclidean')
            for neighbor in self.grid.get_neighbors(current[0], current[1], diagonal=use_diagonal):
                # Calculate movement cost (√2 for diagonal, 1 for cardinal)
                dr = abs(neighbor[0] - current[0])
                dc = abs(neighbor[1] - current[1])
                step_cost = 1.414 if (dr + dc == 2) else 1
                new_g_cost = g_cost + step_cost
                
                if neighbor not in g_costs or new_g_cost < g_costs[neighbor]:
                    g_costs[neighbor] = new_g_cost
                    
                    # Calculate heuristic
                    if self.heuristic == 'manhattan':
                        h_value = self.grid.manhattan_distance(neighbor, goal)
                    else:  # euclidean
                        h_value = self.grid.euclidean_distance(neighbor, goal)
                    
                    # Calculate f = g + h
                    f_value = new_g_cost + h_value
                    
                    # Add to frontier
                    new_path = path + [neighbor]
                    frontier.put((f_value, neighbor, new_path, new_g_cost))
                    
                    if neighbor not in self.frontier and neighbor not in self.visited:
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