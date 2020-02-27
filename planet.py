class planet(object):
    def __init__(self, name, mass, temp, radius, distance):
        self.name = name
        self.mass = mass
        self.temp = temp
        self.radius = radius
        self.distance = distance

    def __str__(self):
        return f"Name: {self.name}, Mass: {self.mass}, Temp: {self.temp}, Radius: {self.radius}, Distance: {self.distance}"

    
    
