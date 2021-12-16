from code_challenges.graph.graph import Graph,Edge,Vertex,Queue
import pytest

def test_add_node():

  graph = Graph()

  expected = "test"

  actual = graph.add_node('test').value

  assert actual == expected

def test_size_empty():

    graph = Graph()

    expected = 0

    actual = graph.size()

    assert actual == expected


def test_size():

    graph = Graph()

    graph.add_node('spam')

    expected = 1

    actual = graph.size()

    assert actual == expected


def test_add_edge_interloper_start():

    graph = Graph()

    start = Vertex('start')

    end = graph.add_node('end')

    with pytest.raises(KeyError):
        graph.add_edge(start, end)


def test_add_edge_interloper_end():

    graph = Graph()

    end = Vertex('end')

    start = graph.add_node('start')

    with pytest.raises(KeyError):

        graph.add_edge(start, end)

def test_get_nodes():

    graph = Graph()

    banana = graph.add_node('banana')

    apple = graph.add_node('apple')

    loner = Vertex('loner')

    expected = 2

    actual = len(graph.get_nodes())

    assert actual == expected


def test_get_neighbors():

    graph = Graph()

    banana = graph.add_node('banana')

    apple = graph.add_node('apple')

    graph.add_edge(apple, banana, 44)

    neighbors = graph.get_neighbors(apple)

    assert len(neighbors) == 1

    neighbor_edge = neighbors[0]

    assert neighbor_edge.vertex.value == 'banana'

    assert neighbor_edge.weight == 44

# def test_graph():
#   graph = Graph()
#   v1 = graph.add_node('A')
#   v2 = graph.add_node('B')
#   v3 = graph.add_node('C')
#   v4 = graph.add_node('D')
#   v5 = graph.add_node('E')
#   graph.add_edge(v1,v2,1)
#   graph.add_edge(v1,v3,2)
#   graph.add_edge(v2,v4,4)
#   graph.add_edge(v3,v4,8)
#   graph.add_edge(v3,v5,3)
#   graph.add_edge(v4,v5,5)
#   assert graph.size() == 5
#     #   assert graph.get_nodes() == dict_keys(['A', 'B', 'C', 'D', 'E'])
#   assert graph.get_neighbors(v1) == [('B', 1), ('C', 2)]
#   assert graph.get_neighbors(v2) == [('D', 4)]
#   assert graph.get_neighbors(v3) == [('D', 8), ('E', 3)]
#   assert graph.get_neighbors(v4) == [('E', 5)]
#   assert graph.get_neighbors(v5) == []
#   assert graph.print_graph() == {'A': [('B', 1), ('C', 2)], 'B': [('D', 4)], 'C': [('D', 8), ('E', 3)], 'D': [('E', 5)], 'E': []}
