class Contact:
    '''
    Contact class to represent a contact with a name and number.
    Attributes:
        name (str): The name of the contact.
        number (str): The phone number of the contact.
    '''
    
    def __init__(self, name, number):
        self.name = name
        self.number = number

    def __str__(self):
        return f"{self.name}: {self.number}"

class Node:
    '''
    Node class to represent a single entry in the hash table.
    Attributes:
        key (str): The key (name) of the contact.
        value (Contact): The value (Contact object) associated with the key.
        next (Node): Pointer to the next node in case of a collision.
    '''
   
    def __init__(self, key, value):
        self.key = key #Contact Name
        self.value = value #Contact Object
        self.next = None #Link to the next node

class HashTable:
    '''
    HashTable class to represent a hash table for storing contacts.
    Attributes:
        size (int): The size of the hash table.
        data (list): The underlying array to store linked lists for collision handling.
    Methods:
        hash_function(key): Converts a string key into an array index.
        insert(key, value): Inserts a new contact into the hash table.
        search(key): Searches for a contact by name.
        print_table(): Prints the structure of the hash table.
    '''
    
    def __init__(self, size):
        self.size = size 
        self.data= [None] * size #initialize

    def hashFunction(self, key):
        #Hash: sum of ASCII values mod table size
        return sum(ord(char) for char in key) % self.size

    def insert(self, key, number):
        index = self.hashFunction(key)
        newContact = Contact(key, number)
        newNode = Node(key, newContact)

        if self.data[index] is None:
            self.data[index] = newNode
        else:
            current = self.data[index]
            while current:
                if current.key == key:
                    current.value.number = number #update existing contact
                    return
                if current.next is None:
                    break
                current = current.next
            current.next = newNode #Adding to the end of the chain

    def search(self, key):
        index = self.hashFunction(key)
        current = self.data[index]

        while current:
            if current.key == key:
                return current.value
            current = current.next
        return None
    
    def printTable(self):
        for i in range(self.size):
            print(f"Index {i}:", end=" ")
            current = self.data[i]
            if not current:
                print("Empty")
            else:
                while current:
                    print(f"- {current.value}", end=" ")
                    current = current.next
                print()
# Test your hash table implementation here.  

table = HashTable(10)
table.printTable()

table.insert("John", "909-876-1234")
table.insert("Rebecca", "111-555-0002")
table.printTable()

contact = table.search("John")
print("\nSearch result:", contact)

# Collision test
table.insert("Amy", "111-222-3333")
table.insert("May", "222-333-1111")  # Will collide with Amy
table.printTable()

# Duplicate key test
table.insert("Rebecca", "999-444-9999")
table.printTable()

# Search for non-existent contact
print(table.search("Chris"))  # None


"""
DESIGN MEMO

I believe that hash tables are great for fast and relaible lookups because they use a hash function to create an index, which allows for constat time acces in most cases.
Unlinke lists, hash tables can retrieve data in O(1) time.
In this program, after some research, I decided to implement separate chaining to handle possible collitions. Basically, in the case that more than one contact are assigned the same
index, the program has already created a linked list in each index allowing for one index to store more than one contact. By doing this, thsi program is able to handle collisions without overwritting any data.
I think that a software developer could choose a hash table over a list when having fast resource access is critical and the data set is really large. From my short experience, it feels like trees are more
complex to implement and slower than hash tables, I think is really interesting how a hash table is able to provide a fast lookup with apparently "unordered" data. 
"""