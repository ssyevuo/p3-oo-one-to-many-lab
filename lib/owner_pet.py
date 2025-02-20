class Pet:
    # class variable PET_TYPES
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []
    def __init__(self, name, pet_type, owner = None):
        self.name = name
        self.pet_type = pet_type 
        self._owner = owner
        if pet_type not in Pet.PET_TYPES:
            raise Exception("Invalid pet type")
        Pet.all.append(self)

    @property
    def owner(self):
        return self._owner
    
    @owner.setter
    def owner(self, value):
        if not isinstance(value, Owner):
            raise TypeError("Owner must be an instance of Owner class")
        self._owner = value

class Owner:
    def __init__(self, name):
        self.name = name 

    # returns a list of all pets owned by this owner
    def pets(self):
        return [pet for pet in Pet.all if pet.owner == self]
    
    #ensures that the pet is of type pet and adds the owner to the pet and raises an exception
    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise TypeError("Pet must be an instance of Pet class")
        pet.owner = self

    # returns a sorted list of pets by their name
    def get_sorted_pets(self):
        return sorted(self.pets(), key=lambda x: x.name)