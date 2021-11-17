from code_challenges.stack_queue_animal_shelter.stack_queue_animal_shelter import AnimalShelter,Cat,Dog,Node,Queue

import pytest



def test_enqueue_dog():
    """
    Testing enqueue method for a queue
    """

    animal=AnimalShelter()
    Alex=Dog("Alex")

    expected = "Alex"
    actual =animal.enqueue(Alex)

    assert expected == actual


def test_enqueue_cat():
    """
    Testing enqueue method for a queue
    """
    animal=AnimalShelter()
    Lucy=Cat("Lucy")

    actual =animal.enqueue(Lucy)
    expected = "Lucy"
    assert expected == actual


def test_dequeue_cat():
    """
    Testing dequeue method for a queue
    """
    animal=AnimalShelter()
    Lucy=Cat("Lucy")

    animal.enqueue(Lucy)

    expected = "Lucy"
    actual = animal.dequeue("cat")

    assert expected == actual



def test_dequeue_dog():
    """
    Testing dequeue method for a queue
    """
    animal=AnimalShelter()
    Billy=Dog("Billy")

    animal.enqueue(Billy)

    expected = "Billy"
    actual = animal.dequeue("dog")

    assert expected == actual


def test_dequeue_other_animals():
    """
    Testing dequeue method for a queue
    """
    animal=AnimalShelter()

    Billy=Dog("Billy")
    animal.enqueue(Billy)

    Lucy=Cat("Lucy")
    animal.enqueue(Lucy)

    expected = None
    actual = animal.dequeue("wolf")

    assert expected == actual


def test_dequeue_empty_cat():
    """
    Testing dequeue method for a queue
    """
    with pytest.raises(Exception):
        animal=AnimalShelter()
        Lucy=Cat("Lucy")

        animal.dequeue("cat")


def test_dequeue_empty_dog():
    """
    Testing dequeue method for a queue
    """
    with pytest.raises(Exception):
        animal=AnimalShelter()
        Billy=Dog("Billy")

        animal.dequeue("dog")




# def test_enqueue_dequeue_dog():

#     shelter=AnimalShelter()
#     dog_1=Dog('Alx')
#     dog_2=Dog('Boby')
#     dog_3=Dog('Max')
#     shelter.enqueue(dog_1)
#     shelter.enqueue(dog_2)
#     shelter.enqueue(dog_3)
#     assert shelter.dog == "Alx Boby Max"
#     shelter.dequeue('dog')
#     assert shelter.dog == "Boby Max"


# def test_enqueue_dequeue_cat():

#     shelter=AnimalShelter()
#     cat_1=Cat('MeMe')
#     cat_2=Cat('Roby')
#     cat_3=Cat('Keke')
#     shelter.enqueue(cat_1)
#     shelter.enqueue(cat_2)
#     shelter.enqueue(cat_3)
#     assert shelter.cat == 'MeMe Roby Keke'
#     shelter.dequeue('cat')
#     assert shelter.cat =='Roby Keke'
