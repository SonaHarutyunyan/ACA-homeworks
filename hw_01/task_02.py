#Function takes obj and creates dictionary with method names as keys and result of calling this methods as values

def obj_to_dictionary(obj):
    d = {}
    for func in dir(type(obj)):
        if callable(getattr(type(obj), func)) and not func.startswith("__"):
            d[func] = getattr(obj, func)()
    return d
       
    
    
class Shark:
    def __init__(self, name):
        self.name = name
        
    def swim(self):
        return 1

    def be_awesome(self):
        return 2
        
        
a = Shark('Sona')
print(obj_to_dictionary(a))
