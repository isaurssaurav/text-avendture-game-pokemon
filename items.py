# Base class for all items
class Item():
    # __init__ is the contructor method
    def __init__(self, name, description, value):
        self.name = name   # attribute of the Item class and any subclasses
        self.description = description # attribute of the Item class and any subclasses
        self.value = value # attribute of the Item class and any subclasses
    
    # __str__ method is used to print the object
    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\n".format(self.name, self.description, self.value)


class Gold(Item):

    def __init__(self, amt): 
        self.amt = amt
        super().__init__(name="Gold",
                         description="A round coin",
                         value=self.amt)

class PokeBall(Item):
    def __init__(self,amt):
        self.amt = amt
        super().__init__(name="PokeBall",description="Red and white ball to catch pokemon", value= self.amt)
