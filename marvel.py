class Marvel(object):
    def __init__(self, name, movie):
        self.name=name
        self.movie=movie
    

    def printAll(self):
        print("Hi there, Welcome to Marvel Directory")


mj = Marvel("MJ", "Spider Man : Homecoming, Far from Home, No way Home")
peter= Marvel("Peter Parker a.k.a Spider Man", "Spider Man : Homecoming, Far from Home, No way Home")
stark = Marvel("Tony Stark a.k.a Iron Man", "Iron Man, Avengers:End Game, Captain America")

print("Hi there, Welcome to Marvel Directory")
print("*")
print(mj.name)
print(mj.movie)
print("*")
print(peter.name)
print(peter.movie)
print("*")
print(stark.name)
print(stark.movie)
print("*")
