import abc

class AutoStorage: #1
    __counter = 0
    
    
    def __init__(self):
        cls = self.__class__
        prefix = cls.__name__
        index = cls.__counter
        self.storage_name = '_{}#{}'.format(prefix, index)
        cls.__counter += 1
        
    def __get__(self, instance, owner):
        if instance is None:
            return self
        else:
            return getattr(instance, self.storage_name)
        
    def __set__(self, instance, value):
        setattr(instance, self.storage_name, value) #2
        

class Validated(abc.ABC, AutoStorage): #3
    def __set__(self, instance, value):
        value = self.validate(instance, value) #4
        super().__set__(instance, value) #5
        
    @abc.abstractmethod
    def validate(self, instance, value): #6
        """return validated value or raise ValueError"""
        

class Quantity(Validated): #7
    """a number greater than zero"""
    def validate(self, instance, value):
        if value <= 0:
            raise ValueError('value must be > 0')
        return value
    

class NonBlank(Validated):
    """a string with at least one ono-space character"""
    def validate(self, instance, value):
        value = value.strip()
        if len(value) == 0:
            raise ValueError('value cannot be empty or blank')
        return value #8
    
def entity(cls): #1
    for key, attr in cls.__dict__.items(): #2
        if isinstance(attr, Validated): #4
            type_name = type(attr).__name__
            attr.strorage_name = '_{}#{}'.format(type_name, key) #4
    return cls #5

    
class LineItem:
    description = NonBlank()
    weight = Quantity()
    price = Quantity()
    
    def __init__(self, description, weight, price):
        self.description = description
        self.weight = weight
        self.price = price
        
    def subtotal(self):
        return self.weight * self.price