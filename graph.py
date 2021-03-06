class Vertex:
    def __init__(self, label):
        """
        Initializes the vertex with label and it is not visited by default.
        """
        self.label = label
        self.visited = False
    def __repr__(self):
        """
        Represents Vertex if printed
        """
        return f"{self.label}{'*' if self.visited else ''}"

class Graph:
    def __init__(self, list_labels=[]):
        """
        Initializes the graph as a dictionary with with vertex name (label) as a key and array of neighbouring verteces as a value.
        """
        self.graph = dict((Vertex(l), []) for l in set(list_labels))

    def vertices(self):
        '''
        Returns all the vertices of the graph
        '''
        return list(self.graph.keys())

    def edges(self):
        """
        Return lists with no duplicate edges for a undirected Graph;
        Still works with parallel edges
        """
        ret = list()
        for v1 in self.vertices():
            for v2 in self.graph[v1]:
                if not (v2, v1) in ret:
                    ret.append((v1, v2))
        return ret

    def vertex_exists(self, label):
        '''
        Returns boolean whether the given vertex with label label exists or not
        '''
        labels = []
        for v in self.graph.keys():
            labels.append(v.label)
        return label in labels

    def get_vertex(self, label):
        '''
        Returns the vertex object with the given label
        Returns None if does not exists
        '''
        for v in self.graph.keys():
            if v.label == label:
                return v
        return None

    def add_vertex(self, label):
        '''
        Adds new vertex to the graph with the given label
        '''
        if not self.vertex_exists(label):
            self.graph[Vertex(label)] = []
            return True
        return False

    def add_edge(self, labelA, labelB):
        '''
        Adds new edge between labelA and labelB
        '''
        A, B = self.get_vertex(labelA), self.get_vertex(labelB)
        if A and B:
            self.graph[A].append(B)
            if labelA != labelB:
                self.graph[B].append(A)

    def degree(self, label):
        '''
        Prints the degree of the vertex
        '''
        V = self.get_vertex(label)
        loops = self.graph[V].count(V)
        print("Label: ", label)
        print("\tLoops :", loops)
        print("\tlen(self.graph) :", len(self.graph[V]))
        return len(self.graph[V]) + loops # each loop counts twice

    def is_empty(self):
        if self.graph.keys():
            return sum(self.degree(v.label) for v in self.graph.keys()) == 0
        return True

    def is_null(self):
        return len(self.graph.keys()) == 0

    def is_singleton(self):
        return len(self.graph.keys()) == 1 and self.is_empty()

    def is_trivial(self):
        return self.is_singleton()

    def is_simple(self):
        return not (self.has_loop() or self.has_parallel())

    def is_complete_Kn(self):
        vertices = self.vertices()
        lenv = len(vertices)-1
        if self.is_simple() and not self.is_null():
            for v in vertices:
                if self.degree(v.label) != lenv:
                    return False
            return True
        return False

    def is_loop(self, label):
        vertex = self.get_vertex(label)
        return vertex in self.graph[vertex]

    def has_loop(self):
        for v in self.vertices():
            print("\t{} is loop? {}".format(v.label, self.is_loop(v.label)))
            if self.is_loop(v.label):
                return True
        return False

    def is_parallel(self, labelA, labelB):
        A, B = self.get_vertex(labelA), self.get_vertex(labelB)
        return True if self.graph[A].count(B) > 1 or \
            self.graph[B].count(A) > 1 else False

    def has_parallel(self):
        for vertex, adj_vertices in self.graph.items():
            for v in adj_vertices:
                print("\t{} is parallel? {}".format(v, self.is_parallel(vertex.label, v.label)))
                if self.is_parallel(vertex.label, v.label):
                    return True
        return False

    def degree_centrality(self, label=''):
        """
        If presented with a label, calculate centrality for the
        correspondent vertex; otherwise returns a dictionary
        with vertices as keys with values of degree_centrality
        """
        if label:
            return self.degree(label)
        else:
            return dict((v, self.degree(v.label))
                for v in self.graph.keys())

    def network_density(self):
        n = len(self.vertices())
        return len(self.edges())/(n*(n-1)) if n > 1 else 0
