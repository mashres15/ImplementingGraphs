from graph import Graph

def graph_from_edgelist(E, directed=False):
    g = Graph(directed)
    V = set()
    for e in E:
        V.add(e[0])
        V.add(e[1])
    verts = {}  # map from vertex label to Vertex instance
    for v in V:
        verts[v] = g.insert_vertex(v)
    for e in E:
        src = e[0]
        dest = e[1]
        element = e[2] if len(e) > 2 else None
        g.insert_edge(verts[src],verts[dest],element)
    return g
def figure_undirected():
    E = (                                                                                 
        ('A', 'B', 1), ('A', 'C', 2), ('A', 'D', 3),                                        
        ('A', 'E', 4), ('B', 'C', 5), ('D', 'C', 6),                                        
        ('E', 'C', 7),                                                                    
        )                                                                                   
    return graph_from_edgelist(E,False)
def figure_directed():                                                                  
    E = (                                                                                 
        ('A', 'B', 1), ('A', 'C', 2), ('A', 'D', 3),                                        
        ('E', 'A', 4), ('C', 'B', 5), ('C', 'D', 6),                                        
        ('C', 'E', 7),                                                                      
        )                                                                                   
    return graph_from_edgelist(E,True) 
    
#--------------------------Testing---------------------------------------------------
if __name__ == "__main__":
    
    
    
    undirected = figure_undirected()
    directed = figure_directed()
    
    for i in undirected.vertices():
        a = i.element()
        if a == 'D':
            delete_u_vertex = i
    
    for j in undirected.edges():
        b = j.element()
        if b == 5:
            delete_u_edge = j
           
    for  k in directed.vertices():
        c = k.element()
        if c == 'D':
            delete_d_vertex = k
        
    for l in directed.edges():
        d = l.element()
        if d == 5:
            delete_d_edge = l
    
    
    #--------------undirected graph------------------------------
    
    
    print()    
    print('******************************************************************************')
    print("==============================UNDIRECTED GRAPH================================")
    print('******************************************************************************')
    print()
   
    # ------------------------Printing the original graph--------------------------
   
    print("Printing the original graph:")
    print("-----------------------------")
    undirected.print_graph()
    print ()
    
    # ------------------------BFS Traversal--------------------------
    
    print()
    print("BFS traversal:")
    print("-----------------------------")
    
    for vertex, edge in undirected.bfs_traversal().items():
        print (vertex.element(),end =': {')
        print(str(edge),end=',')
        print ('}')
    print ()
    
    
    #--------------------------------------Remove Vertex------------------------------------------------
    try:
        print()
        print("After Removing Vertex",undirected.remove_vertex(delete_u_vertex),":")
        print("-----------------------------")
    except Exception as err:
        print (err)     
    print ()
    undirected.print_graph()
    print()
    
    
    # -------------------------------------------Removing edge----------------------------------
    try:
        print()
        print("After Removing edge", undirected.remove_edge(delete_u_edge),":")
        print("-----------------------------")
    except Exception as err:
        print (err)
    print()
    undirected.print_graph()
    print()   
    
    
   
    #----------------------------directed graph-------------------------------------------
    
    print()    
    print('******************************************************************************')
    print("==============================DIRECTED GRAPH==================================")
    print('******************************************************************************')
    print()
    
    #----------------------------printing original directed graph------------------------
    
    print("Printing the intial graph")
    print("-------------------------")
    directed.print_graph()
    print()
  
    # ---------------------------------BFS traversal-----------------------------------
    
    print()
    print("BFS traversal:")
    print("-------------------------")
    for vertex, edge in directed.bfs_traversal().items():
        print (vertex.element(),end =': {')
        print(str(edge),end=',')
        print ('}')
    print ()
    
     # ------------------------------------Removing Vertex-------------------------------------------
    try:
        print()
        print("After Removing Vertex", directed.remove_vertex(delete_d_vertex),":")
        print("-------------------------")
    except Exception as err:
        print(err)
    print()
    directed.print_graph()
    print ()
    
    #------------------------------- Removing edge (B,C,5)----------------------------------------------
    try:
        print()
        print("After Removing edge",directed.remove_edge(delete_d_edge),":" )
        print("-------------------------")
    except Exception as err:
        print(err)
    print()
    directed.print_graph()
    print()

    print("-------------------------------------THE END-----------------------------------------")