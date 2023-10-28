class Race:
    allRaces = []

    def __init__(self, race_date, race_location: str):
        self.date = race_date
        self.location = race_location
        self.participants = []
        self.positions = []
        self.points = []

        Race.allRaces.append(self)

    def __repr__(self):
        return f"({self.date},{self.location})"
