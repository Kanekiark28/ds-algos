"""
Adjacency Matrix Representation of Graph

"""

class Graphs:
    
    
    def __init__(self,num_of_vertex):
        #create a VxV adj_matrix
        self.adj_matrix = [[-1]*num_of_vertex for x in range(num_of_vertex)]
        self.num_of_vertex = num_of_vertex
        #dictionary of vertices
        self.vertices = {}
        self.verticeslist = [0]*num_of_vertex
        
    def set_vertex(self,vtx,id):
        if 0<=vtx<self.num_of_vertex:
            #graph.set_vertex(0,'a')
            self.vertices[id] = vtx
            self.verticeslist[vtx] = id
            
    def set_edge(self,frm,to,cost=0):
        #set edge from 'node' to 'node' with cost=0
        frm = self.vertices[frm]
        to = self.vertices[to]
        self.adj_matrix[frm][to] = cost
        #di-graph
        self.adj_matrix[to][frm] = cost
        
    def get_vertex(self):
        return self.verticeslist
    
    def get_edges(self):
        edges = []
        #loop through adj_matrix
        for i in range(self.num_of_vertex):
            for j in range(self.num_of_vertex):
                #if edge exists
                if self.adj_matrix[i][j] != -1:
                    #append nodes->nodes (edge) as a tuple
                    edges.append((self.verticeslist[i],self.verticeslist[j],self.adj_matrix[i][j]))
        return edges
        
    def get_matrix(self):
        return self.adj_matrix
    
#Testing
graph = Graphs(6)
graph.set_vertex(0,'a')
graph.set_vertex(1,'b')
graph.set_vertex(2,'c')
graph.set_vertex(3,'d')
graph.set_vertex(4,'e')
graph.set_vertex(5,'f')
graph.set_edge('a','e',20)
graph.set_edge('a','c',50)
graph.set_edge('c','b',80)
graph.set_edge('b','e',40)
graph.set_edge('e','d',90)
graph.set_edge('f','e',50)
print("Vertices of Graph")
print(graph.get_vertex())
print("Edges of Graph")
print(graph.get_edges())
print("Adjacency Matrix of Graph")
print(graph.adj_matrix)
print(graph.verticeslist)