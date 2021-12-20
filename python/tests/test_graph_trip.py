from code_challenges.graph_business_trip.graph_business_trip import Graph,Edge,Vertex,Queue,graph_business_trip

import pytest

def test_business_trip_True(city):
    actual = graph_business_trip(city[0], [city[2], city[4], city[6]])
    expected = "True,$115"
    assert actual == expected

def test__business_trip_True2(city):
    actual = graph_business_trip(city[0], [city[3], city[1]])
    expected = "True,$82"
    assert actual == expected

def test_graph_business_False(city):
    actual = graph_business_trip(city[0], [city[5], city[2], city[6]])
    expected = "False,$0"
    assert actual == expected


@pytest.fixture
def city():
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

    return graph,pandora,arendelle,metroville,monstroplolis,narnia,naboo
