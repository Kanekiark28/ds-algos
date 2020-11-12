"""
Given an m x n 2d grid map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

"""

class Problems:

    def num_of_islands(self,grid):
        
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    #explore all neighboring islands
                    res += 1
                    self.dfs(grid,i,j,res)
        return res

    def dfs(self,grid,i,j,res):
        
        if i < 0 or i > len(grid)-1 or j < 0 or j > len(grid[0])-1 or grid[i][j] == "0":
            return 0
        #mark as visited
        grid[i][j] = "0"
        self.dfs(grid,i+1,j,res)
        self.dfs(grid,i-1,j,res)
        self.dfs(grid,i,j+1,res)
        self.dfs(grid,i,j-1,res)
        
    """
    Given an undirected graph, return true if and only if it is bipartite.

    Recall that a graph is bipartite if we can split its set of nodes into two independent subsets A and B, such that every edge in the graph has one node in A and another node in B.

    The graph is given in the following form: graph[i] is a list of indexes j for which the edge between nodes i and j exists.  Each node is an integer between 0 and graph.length - 1.  There are no self edges or parallel edges: graph[i] does not contain i, and it doesn't contain any element twice.
                      0     1     2     3
    Input: graph = [[1,3],[0,2],[1,3],[0,2]]
    Output: true
    Explanation: We can divide the vertices into two groups: {0, 2} and {1, 3}.
    
    Input: graph = [[1,2,3],[0,2],[0,1,3],[0,2]]
    Output: false
    Explanation: We cannot find a way to divide the set of nodes into two independent subsets.
    """
    def is_graph_bipartite(self,graph):
        # number of nodes in graph
        num_of_nodes = len(graph)
        
        # color the nodes -> 0 not visited, 1 visiting, -1 visited
        colors = [0 for x in range(num_of_nodes)]
        
        for node in range(len(graph)):
            #if current node has not been visited and color_dfs is false -> false
            if colors[node] == 0 and not (self.color_dfs(graph,node,colors,1)):
                return False
        return True
    
    def color_dfs(self,graph,node,colors,color):
        #if colors[node] is visiting or visited, check if it's the same color
        if colors[node] != 0:
            return colors[node] == color
        else:
            #otherwise color the node with the given color
            colors[node] = color
            #check all neighbors of the current node for same colors
            for nei in graph[node]:
                if not (self.color_dfs(graph,nei,colors,-color)):
                    return False
            return True
        
        
    """
    There are a total of numCourses courses you have to take, labeled from 0 to numCourses-1.

    Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

    Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?
    
    Example 1:

    Input: numCourses = 2, prerequisites = [[1,0]]
    Output: true
    Explanation: There are a total of 2 courses to take. 
    To take course 1 you should have finished course 0. So it is possible.
    
    Example 2:

    Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
    Output: false
    Explanation: There are a total of 2 courses to take. 
    To take course 1 you should have finished course 0, and to take course 0 you should
    also have finished course 1. So it is impossible.
    
    """
    
    def can_courses(self,prerequisites,num_courses):
        
       
        self.adjacency_list = [None]*num_courses
        
        #build adjacency list
        for i in range(num_courses):
            self.adjacency_list[i] = []
        
        #[[1,0],[0,1]]
        #[[1],[0]]   
        for x,y in prerequisites:
            self.adjacency_list[x].append(y)
        
        #build visited list: 0 -> not visited, 1 -> currently visiting, 2 -> explored
        visited = [0 for j in range(num_courses)]
        
        for i in range(num_courses):
            #if node is not visited and the result of exploration is False -> return False
            if visited[i] == 0 and not self.explore(visited,i):
                return False
            
        return True
    
    def explore(self,visited, adj):
        #if node is currently visiting, means there is a back edge so return False
        if visited[adj] == 1:
            return False
        
        #otherwise mark as visited
        visited[adj] = 1
        
        #check if there is a back edge in neighbors
        for a in self.adjacency_list[adj]:
            if not self.explore(visited,a):
                return False
            
        visited[adj] = 2
        return True
    
    
    """
    There are N rooms and you start in room 0.  Each room has a distinct number in 0, 1, 2, ..., N-1, and each room may have some keys to access the next room. 

    Formally, each room i has a list of keys rooms[i], and each key rooms[i][j] is an integer in [0, 1, ..., N-1] where N = rooms.length.  A key rooms[i][j] = v opens the room with number v.

    Initially, all the rooms start locked (except for room 0). 

    You can walk back and forth between rooms freely.

    Return true if and only if you can enter every room.

    Example 1:

    Input: [[1],[2],[3],[]]
    Output: true
    Explanation:  
    We start in room 0, and pick up key 1.
    We then go to room 1, and pick up key 2.
    We then go to room 2, and pick up key 3.
    We then go to room 3.  Since we were able to go to every room, we return true.
    Example 2:

    Input: [[1,3],[3,0,1],[2],[0]]
    Output: false
    Explanation: We can't enter the room with number 2.    
    
    """
    
    def keys_and_rooms(rooms):
        
        #create a set to track all keys
        visited = set()
        visited.add(0)
        stack = [0]
        
        while stack:
            #get the keys for the given room
            keys = rooms[stack.pop()]
            
            #iterate through keys
            for key in keys:
                #if key not in set, add it to stack and set
                if key not in visited:
                    visited.add(key)
                    stack.append(key)
                    
        return len(visited) == len(rooms)
        
                
        
        
        
    

obj = Problems()    
grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]

print(obj.num_of_islands(grid))