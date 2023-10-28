from driver import Driver
from race import Race
import datetime
import random

#user can only get year 2022 date for simulate random race
def race_date_validator():
    try:
        year = int(input("Enter the year as '2022' : "))
        while year != datetime.date.today().year:
            print("Invalid input.")
    except ValueError:
        year = int(input("Enter the year as '2022' : "))
    try:
        month = int(input("Enter the month in numbers (1-12) : "))
        while month > 12 or month < 0:
            print("Invalid input.")
    except ValueError:
        month = int(input("Enter the month in numbers (1-12): "))
    try:
        date = int(input("Enter the date  in number (1- 31) : "))
        while date > 31 or date < 0:
            print("Invalid!")
    except ValueError:
        date = int(input("Enter the date in number (1- 31) : "))
    return f"{year}/{month}/{date}"

#can't input null values and ignore lowercase and uppercase while getting user input
def start_input_validator():
    global user_input
    valid = False
    while not valid:
        user_input = input("Enter the option : ").upper()
        if len(user_input.strip()) > 0:
            valid = True
            return user_input.strip()
        else:
            print("Please enter a valid input!")


def string_input_validator(types):  #name,car,team cannot be null values . It can be a number
    global string_input
    done = False
    while not done:
        try:
            if types == "name":
                string_input = input("Please enter your name : ")
            elif types == "car":
                string_input = input("Please enter your car : ")
            elif types == "team":
                string_input = input("Please enter your team : ")
            elif types == "delete":
                string_input = input("Please enter name to delete : ")
            elif types == "update":
                string_input = input("Please enter name to update : ")

            if len(string_input.strip()) > 0:
                done = True
                return string_input
            else:
                print("Invalid input please try again!")
        except ValueError:
            print("String required")



def age_input_validator(): #Age cannot be zero or neagtive value. And should be in 18-80 range
    global age_input
    done = False
    while not done:
        try:
            age_input = input("Please enter your age : ")
            if len(age_input.strip()) > 0:
                converted = int(age_input)
                if converted > 0:
                    if converted in range(18, 81):
                        done = True
                        return age_input
                    else:
                        print("Age should be in the 18 - 80 range")
                else:
                    print("Age should be a positive integer")
            else:
                print("Invalid input please try again !")
        except:
            print("Integer required")



def current_points_input_validator(): #current points should a positive value. And also can be Zero for some drivers.
    global current_points_input
    done = False
    while not done:
        try:
            current_points_input = input("Please enter your current points : ")
            if len(current_points_input.strip()) >= 0:
                converted = int(current_points_input)
                if converted >= 0:
                    done = True
                    return current_points_input
                else:
                    print("Current points should be a positive Integer !")
            else:
                print("Invalid input please try again !")
        except ValueError:
            print("Integer required.(If you haven't please enter 0)")

def number_input_validator():
    global number_input
    done = False
    while not done:
        try:
            number_input = input("Please enter the option number to update  : ")
            if len(number_input.strip()) >= 0:
                converted = int(number_input)
                if converted >= 0:
                    done = True
                    return number_input
                else:
                    print("Enter a given number correctly !")
            else:
                print("Invalid input please try again !")
        except ValueError:
            print("Please enter a given integer")



def validate_driver_by_name(drivers, newName: str): #name cannot be repeat
    for driver in drivers:
        if driver.name.upper() == newName.upper():
            return True
    return False

def find_user_by_name(drivers, newName : str): # find driver name to update or delete
    for driver in drivers:
        if driver.name.upper() == newName.upper():
            return driver
    return None

def show_drivers_to_update(drivers): #user can see drivers names when launching
    for driver in drivers:
        print(driver)
    print()

def update_driver(driver):
    done = False
    while not done:
        print('''Which one you want to update ? Please enter the number .
                1.Name
                2.Age
                3.Team
                4.Car
                5.Current points
                99.exit ''')
        option = number_input_validator()
        if option == "1":
            name = string_input_validator("name")
            driver.name = name
        elif option == "2":
            age = age_input_validator()
            driver.age = age
        elif option == "3":
            team = string_input_validator("team")
            driver.team = team
        elif option == "4":
            car = string_input_validator("car")
            driver.car = car
        elif option == "5":
            current_point = current_points_input_validator()
            driver.current_point = current_point
        elif option == "99":
            done = True
        else:
            print("Invalid selection")

def sort_driver(drivers): #sort drivers by points
    global point_list, name_list, age_list, team_list, car_list
    point_list = []
    name_list = []
    age_list = []
    team_list = []
    car_list = []
    for driver in drivers:
        point_list.append(driver.current_points)
        name_list.append(driver.name)
        age_list.append(driver.age)
        team_list.append(driver.team)
        car_list.append(driver.car)
        for i in range(0, len(point_list)):
            for j in range(i+1, len(point_list)):
                if int(point_list[i]) <= int(point_list[j]):
                    point_list[i], point_list[j] = point_list[j], point_list[i]
                    name_list[i], name_list[j] = name_list[j], name_list[i]
                    age_list[i], age_list[j] = age_list[j], age_list[i]
                    team_list[i], team_list[j] = team_list[j], team_list[i]
                    car_list[i], car_list[j] = car_list[j], car_list[i]


def standing_table(): #for VCT
    print(" +------------+----------+------------+-----------+-------+ ")
    print(" :    Name    :  Points  :    Team    :    Car    :  Age  : ")
    print(" +------------+----------+------------+-----------+-------+ ")
    for name, point, team, car, age in zip(name_list, point_list, team_list, car_list, age_list):
        print(" |",name,(9-len(name))*" ","|",point,(7-len(str(point)))*" ","|",team,(9-len(team))*" ","|",car,(8-len(car))*" ","|",age,(4-len(str(age)))*" ","|")
    print(" +------------+----------+------------+-----------+-------+ ")
    print()
    print()


def race_table(race): #for VRL
    print("Date : " + race.date)
    print("Location : " + race.location)
    print(" +----------------+---------------+------------+ ")
    print(" :    Position    :   Name        :    Points  :")
    print(" +----------------+---------------+------------+ ")
    for position, name, points in zip(race.positions, race.participants, race.points):
        print(" |", position, (13 - len(str(position))) * " ", "|", name, (12 - len(str(name))) * " ", "|", points,
              (9 - len(str(points))) * " ", "|")
    print(" +----------------+---------------+------------+ ")
    print()
    print()


def position_sorter(position): #to sort driver names according to points
    x = position
    competitors = Driver.allDrivers
    n = len(x)
    for i in range(n):
        for j in range(0, n - i - 1):
            if x[j] > x[j + 1]:
                x[j], x[j + 1] = x[j + 1], x[j]
                competitors[j], competitors[j + 1] = competitors[j + 1], competitors[j]
    for pos in x:
        print(f"Place {pos} - {competitors[pos-1]}")


def get_race_location(): #system can select random location from the location list
    locations = ["Nyirad", "Holjes", "Montalegre", "Barcelona", "Riga", "Norway"]
    race_location = random.choice(locations)
    return race_location


def race_details_updator(position, race_date, race_location,points_list):
    x = position
    y = points_list
    competitors = driver_names_extractor()
    n = len(x)
    for i in range(n):
        for j in range(0, n - i - 1):
            if x[j] > x[j + 1]:
                x[j], x[j + 1] = x[j + 1], x[j]
                competitors[j], competitors[j + 1] = competitors[j + 1], competitors[j]
                y[j], y[j + 1] = y[j + 1], y[j]
    race = Race(race_date, race_location)
    race.participants = competitors
    race.positions = x
    race.points = y

def driver_names_extractor():
    names_list = []
    for driver in Driver.allDrivers:
        names_list.append(driver.name)
    return names_list

def load_drivers_from_file():
    with open("driver.txt") as file_in:
        for line in file_in:
            refs = line.split(",")
            Driver(refs[0], int(refs[1]), refs[2], refs[3], int(refs[1]))

def validate_date(date): #to check the race date
    for race in Race.allRaces:
        if race.date == date:
            return True
    return False

def date_sorter(all):
    x = []
    y = Race.allRaces
    for value in all:
        x.append(value.date)
    n = len(x)
    for i in range(n):
        refs_1 = x[i].split("/")
        year_1 = refs_1[0]
        month_1 = refs_1[1]
        day_1 = refs_1[2]
        for j in range(0, n - i - 1):
            refs_2 = x[j].split("/")
            year_2 = refs_2[0]
            month_2 = refs_2[1]
            day_2 = refs_2[2]
            if year_1 != year_2:
                if int(year_2) > int(year_1):
                    y[j], y[j + 1] = y[j + 1], y[j]
            elif month_1 != month_2:
                if int(month_2) > int(month_1):
                    y[j], y[j + 1] = y[j + 1], y[j]
            elif day_1 != day_2:
                if int(day_2) > int(day_1):
                    y[j], y[j + 1] = y[j + 1], y[j]
    print(y)