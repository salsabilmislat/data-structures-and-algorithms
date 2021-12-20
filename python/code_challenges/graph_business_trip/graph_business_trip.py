from collections import deque

class Queue():


  def __init__(self):

    self.dq = deque()

  def enqueue(self,value):

    self.dq.appendleft(value)

  def dequeue(self):

    return self.dq.pop()

  def __len__ (self):


    return len(self.dq)

class Vertex:

    def __init__(self,value):
        self.value=value

    def __str__(self):

        return str(self.value)

class Edge:

    def __init__(self,vertex,weight):

        self.vertex = vertex
        self.weight = weight

class Graph:

    def __init__(self) -> None:
        self._adj_list={}

    def add_node(self,value):

        node=Vertex(value)
        self._adj_list[node]=[]

        return node

    def add_edge(self,start_vertex,end_vertex,weight =0):

        if start_vertex not in self._adj_list:

            raise KeyError('Start vertex not found in the graph')

        if end_vertex not in self._adj_list:

            raise KeyError('end vertex not found in the graph')
        edge=Edge(end_vertex,weight)
        self._adj_list[start_vertex].append(edge)

    def get_neighbors(self,vertex):
        # return self._adj_list.get(vertex,[])
        return self._adj_list[vertex]

    def get_nodes(self):

        return self._adj_list.keys()

    def size(self):

        return len(self._adj_list)

def graph_business_trip(graph, arr_city):

    trip = False
    trip_two = False
    cost = 0

    for city_name in range(len(arr_city) - 1):
        edges = graph._adj_list[arr_city[city_name]]
        trip_two = False

        for edge in edges:
            if arr_city[city_name + 1] == edge.vertex:
                cost += edge.weight
                trip = True
                trip_two = True

    trip = trip and trip_two
    if not trip:
        cost = 0
        trip = False
        return f"{trip},${cost}"

    return f"{trip},${cost}"

if __name__ == "__main__":
    graph = Graph()

    pandora = graph.add_node('Pandora')
    arendelle = graph.add_node('Arendelle')
    metroville = graph.add_node('Metroville')
    monstroplolis = graph.add_node('Monstroplolis')
    narnia = graph.add_node('Narnia')
    naboo = graph.add_node('Naboo')

    graph.add_edge(pandora, arendelle, 150)
    graph.add_edge(pandora, metroville, 82)

    graph.add_edge(arendelle, pandora, 150)
    graph.add_edge(arendelle, metroville, 99)
    graph.add_edge(arendelle, monstroplolis, 42)

    graph.add_edge(metroville, pandora, 82)
    graph.add_edge(metroville, arendelle, 99)
    graph.add_edge(metroville, monstroplolis, 105)
    graph.add_edge(metroville, naboo, 26)
    graph.add_edge(metroville, narnia, 37)

    graph.add_edge(monstroplolis, arendelle, 42)
    graph.add_edge(monstroplolis, metroville, 105)
    graph.add_edge(monstroplolis, naboo, 73)

    graph.add_edge(naboo, monstroplolis, 73)
    graph.add_edge(naboo, metroville, 26)
    graph.add_edge(naboo, narnia, 250)

    graph.add_edge(narnia, metroville, 37)
    graph.add_edge(narnia, naboo, 250)

    print(graph_business_trip(graph,[arendelle, monstroplolis, naboo]))
    
