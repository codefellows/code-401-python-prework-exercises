class Mammal:
    ### solution:start
    has_hair = True
    ### solution:end


class Cat(Mammal):
    pass


class Sphynx(Cat):
    ### solution:start
    has_hair = False
    ### solution:end


class Dog(Mammal):

    ### solution:start
    def __init__(self, name="unknown"):
        self.name = name
    
    ### solution:end
