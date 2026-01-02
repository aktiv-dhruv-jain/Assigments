import weakref


class Shelf() : 
    _instances = weakref.WeakSet()
    def __init__(self,name):
        self.shelfname = name
        Shelf._instances.add(self)
        
    @classmethod
    def get_all_instances(cls):
        return list(cls._instances)
        
    def hello(self):
        print("hey inside shelf")
    
shelf1 = Shelf('shelf1')
shelf2 = Shelf('shelf2')
all_shelfs = Shelf.get_all_instances()
for shelf in all_shelfs:
    print(f"Name: {shelf.shelfname}")
