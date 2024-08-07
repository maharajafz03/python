


class Bike:
    Name = None
    Bike = None
    Age = None
    Model= None

    def __init__(self,Name,Bike,Age,Model):
         self.Name = Name
         self.Bike = Bike
         self.Age = Age
         self.Model = Model



add = Bike("maha","s1000rr",98, 2018)

# add.Age = 98
# add.Model = 2018

# print(add)
print(add.Name, add.Bike, add.Age, add.Model)