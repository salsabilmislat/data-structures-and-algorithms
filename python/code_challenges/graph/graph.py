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





if __name__=="__main__":
    graph=Graph()
    val1=graph.add_node("A")
    val2=graph.add_node("B")
    val3=graph.add_node("C")
    graph.add_edge(val1,val2,50)
    graph.add_edge(val1,val3,1)
    graph.add_edge(val2,val3,1)


    # for i in graph.breadth_first(val1):
    #     print (i)

