class Node():

    def __init__(self, key:int, val: int):
        self.key = key
        self.value = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.tracker = {}

        self.head = Node(-1, -1)
        self.last = Node(1001, -1)
        self.head.next = self.last
        self.last.prev = self.head

    def get(self, key: int) -> int:
        if key in self.tracker:
            self.tracker[key].next.prev = self.tracker[key].prev
            self.tracker[key].prev.next = self.tracker[key].next

            self.tracker[key].next = self.last
            self.tracker[key].prev = self.last.prev

            self.last.prev.next = self.tracker[key]
            self.last.prev = self.tracker[key]
            
            return self.tracker[key].value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key not in self.tracker:
            if len(self.tracker) >= self.capacity:
                self.tracker.pop(self.head.next.key)
                self.head.next = self.head.next.next
                self.head.next.prev = self.head
            
            new_node = Node(key, value)
            new_node.next = self.last
            new_node.prev = self.last.prev
            self.last.prev = new_node
            new_node.prev.next = new_node
            self.tracker[key] = new_node
        
        else:
            self.tracker[key].value = value

            self.tracker[key].next.prev = self.tracker[key].prev
            self.tracker[key].prev.next = self.tracker[key].next

            self.tracker[key].next = self.last
            self.tracker[key].prev = self.last.prev

            self.last.prev.next = self.tracker[key]
            self.last.prev = self.tracker[key]

        print(self.head.next)