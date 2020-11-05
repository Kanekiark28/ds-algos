"""
Adjacency List representation of Graphs
"""

class Vertex:
    
    def __init__(self,data) -> None:
        self.vertex = data
        self.next = None
        
class Graph:
    
    def __init__(self,vertices) -> None:
        self.vertices = vertices
        self.graph = [None]*self.vertices
        
    def add_edge(self,frm,to):
        vertex = Vertex(to)
        vertex.next = self.graph[frm]
        self.graph[frm] = vertex
        
        vertex = Vertex(frm)
        vertex.next = self.graph[to]
        self.graph[to] = vertex
        
    def print_graph(self):
        for i in range(self.vertices):
            print(f"Adjacency list of vertex {i}\n head",end="")
            temp = self.graph[i]
            while temp:
                print(f" -> {temp.vertex}",end="")
                temp = temp.next
            print("\n")
            
#test
graph = Graph(5)
graph.add_edge(0,1)
graph.add_edge(0,4)
graph.add_edge(1,2)
graph.add_edge(1,3)
graph.add_edge(1,4)
graph.add_edge(2,3)
graph.add_edge(3,4)

graph.print_graph()
        
        
        