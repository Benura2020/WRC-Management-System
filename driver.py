class Driver:
    allDrivers = []


    def __init__(self, name: str, age: int, team: str, car:str, current_points: int):
        self.name = name
        self.age = age
        self.team = team
        self.car = car
        self.current_points = current_points
        Driver.allDrivers.append(self)


    def __repr__(self):
        return f"Driver ['{self.name}', '{self.age}', '{self.team}', '{self.car}', '{self.current_points}']"




