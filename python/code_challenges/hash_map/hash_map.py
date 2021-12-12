class Node:

   def __init__(self,value):
       self.value=value
       self.next=None


class LinkedList:

    def __init__(self):
        self.head=None


    def append(self,value):

        node = Node(value)

        if self.head is None:
            self.head = node

        else:
            current = self.head

            while current.next != None:
                current = current.next
            current.next = node

    def __str__(self):

        result = ""

        if self.head is None:
            result += None

        else:
            current = self.head

            while(current):
                result +=str(current.value)+" -> "
                current = current.next
            result += "NULL"
            return result

class HashTable:
    """
    HashTable Class to  initialize the array size
    """
    def __init__(self, size=1024):
        self.size = size
        self.map = [None] * self.size
        # self.key=""

    def hash(self,key):
        """
        a function to get the hash value of the key in ascii code
        """
        ascii_sum=0
        for char in key:
            ascii_sum+=ord(char)
        return ascii_sum*11 % self.size

    def add(self, key, value):

        hashed_key = self.hash(key)
        if not self.map[hashed_key]:
            self.map[hashed_key] = [key,value]
            # self.key = [key,value]
            return [key,value]
        else:
            if isinstance(self.map[hashed_key], LinkedList):
                self.map[hashed_key].append([key,value])
                return [key,value]
            else:
                chain = LinkedList()
                # existing_pair = self.key
                existing_pair= self.map[hashed_key]
                new_pair =[key,value]
                self.map[hashed_key]=chain
                chain.append((existing_pair))
                chain.append(new_pair)
                return new_pair
        # if type(  self.map[hashed_key])== list:
        #      self.map[hashed_key]= self.map[hashed_key][1]

    def get(self, key):
        hashed_key=self.hash(key)
        if  self.map[hashed_key]==None:
              print("Not Found")
              return None
        else:
            if type(  self.map[hashed_key])== list:
                print(self.map[hashed_key][1])
                return self.map[hashed_key][1]

            else:
                current =  self.map[hashed_key].head
            if current!=None:
                while current.next != None:
                    if current.value[0] == key:
                        print (current.value[1])
                        return (current.value[1])
                    current = current.next

    def contains(self, key):
        hashed_key=self.hash(key)
        if  self.map[hashed_key]==None:
            return False
        else:
            if type(  self.map[hashed_key])== list:
                print (True)
                return True
            else:
                current =  self.map[hashed_key].head
            if current!=None:
                while current.next != None:
                    if current.value[0] == key:
                        print (True)
                        return (True)
                    current = current.next
                print ("false")
                return False


def repeated_word(string):

    if not string  :
        return "This Is An Empty String"

    string = string.replace(".", "")
    string = string.replace(",", "")
    string = string.replace("-", "")
    string = string.lower()

    list_words = string.split()

    new_hashtable = HashTable()

    for word in list_words:

        if new_hashtable.contains(word):
            return word

        else:
            new_hashtable.add(word, word)

    return "There Is No Duplicate"

if __name__ == "__main__":

    string1 = "Once upon a time, there was a brave princess who..."
    print(f"{string1} >>> {repeated_word(string1)}\n")

    string2 = "It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way – in short, the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only..."
    print(f"{string2} >>> {repeated_word(string2)}\n")

    string3 = "It was a queer, sultry summer, the summer they electrocuted the Rosenbergs, and I didn’t know what I was doing in New York..."
    print(f"{string3} >>> {repeated_word(string3)}\n")
