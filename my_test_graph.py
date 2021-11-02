from graph import Graph

G = Graph('ABCD')

G.add_edge('A', 'B')
G.add_edge('A', 'C')
G.add_edge('B', 'C')
G.add_edge('C', 'D')
G.add_edge('C', 'C')
# print("Graph G :", G)

# A B C D
print("Vertices:", G.vertices())
# (A, B), (A, C), (B, C), (C, D)
print("Edeges:", G.edges())
print("Vertex C exists?", G.vertex_exists('C'))
print("Vertex F exists?", G.vertex_exists('F'))
print("Get vertex C:", G.get_vertex('C'))
# deg(C) = 3
print("Degree of C:", G.degree('C'))
print("G is empty?", G.is_empty())
print("G is null?", G.is_null())
print("G is singleton or trivial?", G.is_singleton(), G.is_trivial())
print("G is simple?", G.is_simple())
print("G is complete?", G.is_complete_Kn())
print("G has loop?", G.has_loop() )
print("G has parallel?", G.has_parallel())
# A : 2, B : 2, C : 3, D : 1
print("Degree centrality of G:", G.degree_centrality())
#should be 1/3
print("Network density: %.2f" % G.network_density())
