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

    def __init__(self, name="unknown"):
        ### solution:start
        self.name = name
        ### solution:end
