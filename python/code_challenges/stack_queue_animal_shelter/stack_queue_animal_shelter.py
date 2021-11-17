class Node:

    def __init__(self,value):
       self.value=value
       self.next=None


class Queue:

    def __init__(self):

        self.front=None
        self.rear=None

    def __str__(self):
        current = self.front
        items = []
        while current:
            items.append(str(current.value))
            current = current.next
        return " ".join(items)

    def enqueue(self, value):

        node=Node(value)

        if not self.rear:
            self.front=node
            self.rear=node

        else:
            self.rear.next=node
            self.rear=node

    def dequeue(self):

        if not self.front:

          raise Exception ('This Queue is Empty')


        temp=self.front
        self.front=self.front.next
        temp.next=None
        return temp.value


    def peek(self):

        if self.isEmpty():

            return ('This Queue is Empty')

        else:
            return self.front.value



    def isEmpty(self):
        if self.front:
            return False

        return True




class AnimalShelter:

    def __init__(self):

        self.dog=Queue()
        self.cat=Queue()

    def enqueue(self, animal):

        if animal.animaltype =='cat':
            self.cat.enqueue(animal.nickname)
            return animal.nickname
        elif animal.animaltype =='dog':
            self.dog.enqueue(animal.nickname)
            return animal.nickname
        else:

            return 'This is not cat or dog'

    def dequeue(self, pref):

        if pref == 'cat':

            if self.cat.isEmpty():
                raise Exception("empty")
            else:
                return self.cat.dequeue()

        elif pref == 'dog':

            if self.dog.isEmpty():
                raise Exception("empty")
            else:
                return self.dog.dequeue()

        else:

            return None

class Cat:

    def __init__(self,nickname):
        self.nickname=nickname
        self.animaltype='cat'

class Dog:

    def __init__(self,nickname):
        self.nickname= nickname
        self.animaltype='dog'



if __name__ == '__main__':

    animal_shelter = AnimalShelter()
    dog_one = Dog("MILO")
    dog_two = Dog("MAX")
    dog_three = Dog("KOBE")
    animal_shelter.enqueue(dog_one)
    animal_shelter.enqueue(dog_two)
    animal_shelter.enqueue(dog_three)
    animal_shelter.dequeue("dog")
    print(animal_shelter.dog)




