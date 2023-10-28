import random
from datetime import date
from driver import Driver
from race import Race
from validationANDother import start_input_validator, string_input_validator, age_input_validator, \
    validate_driver_by_name, current_points_input_validator, find_user_by_name, show_drivers_to_update, update_driver, \
    sort_driver, standing_table, position_sorter, race_date_validator, get_race_location,race_details_updator, \
    load_drivers_from_file, race_table, validate_date, date_sorter

def menu():
    print('''          \x1B[1;3;35m~Type ADD for adding driver details  
          ~Type DDD for deleting 
          ~Type UDD for updating driver details 
          ~Type VCT for viewing the rally cross standings table 
          ~Type VRL for viewing race table sorted according to the date 
          ~Type STF to save the current data to a text file 
          ~Type RFF to load data from the saved text file 
          ~Type ESC to exit the program\x1B[0m
          ''')

def start():
    #load drivers
    #load_drivers_from_file()
    show_drivers_to_update(Driver.allDrivers) #Display drivers name to user
    menu()
    while True:
        user_input = start_input_validator()
        if user_input == "ADD":
            ADD()
        elif user_input == "DDD":
            DDD()
        elif user_input == "UDD":
            UDD()
        elif user_input == "VCT":
            VCT()
        elif user_input == "SRR":
            SRR()
        elif user_input == "VRL":
            VRL()
        elif user_input == "STF":
            STF()
        elif user_input == "RFF":
            RFF()
        elif user_input == "ESC":
            break
        else:
            print("Invalid option")



def ADD(): #1
    name = string_input_validator("name")
    user_exist = validate_driver_by_name(Driver.allDrivers, name)
    if user_exist:
        print(f"Driver already exists by the name: {name} !")
        ADD()
    else:
        age = age_input_validator()
        team = string_input_validator("team")
        car = string_input_validator("car")
        current_points = current_points_input_validator()
        new_user = Driver(name, age, team, car, current_points)
        print(f"Driver {name.strip()} successfully added to team {team} !")
    start()

def DDD(): #2
    if len(Driver.allDrivers) > 0: #should include at least one data to delete users
        show_drivers_to_update(Driver.allDrivers)
        name_to_delete = string_input_validator("delete")
        driver = find_user_by_name(Driver.allDrivers, name_to_delete)
        if driver is not None:
            print(f"Successfully removed driver '{driver.name}' from the system .")
            Driver.allDrivers.remove(driver)
        else:
            print(f"No driver found by name '{name_to_delete}' !")
            DDD()
    else:
        print("\n Sorry there are no drivers in the system")
    start()

def UDD(): #3
    if len(Driver.allDrivers) > 0: #should include at least one data to update users
        show_drivers_to_update(Driver.allDrivers)
        name_to_update = string_input_validator("update")
        driver = find_user_by_name(Driver.allDrivers, name_to_update)
        if driver is not None:
            update_driver(driver)
        else:
            print(f"There is no driver found by name '{name_to_update}' ! ")
            UDD()
    else:
        print("\n Sorry there are no drivers in the system")
    start()

def VCT(): #4
    if len(Driver.allDrivers) > 0:  # should include at least one data to create table
        sort_driver(Driver.allDrivers)
        standing_table()
    else:
        print("\n Sorry there are no drivers in the system")
    start()

def SRR(): #5
    race_location = get_race_location()
    if len(Driver.allDrivers) > 3: # should include at least 4 drivers to srr
        race_date = race_date_validator()
        race_date_exists = validate_date(race_date)
        if race_date_exists:
            print(f"The date already added ")
            SRR()
        print('''   ---| Welcome to Random Race |---
             ~Points~
        1st Place - 10 points
        2nd Place - 7 points
        3rd Place - 5 points
    ---|------------------------|---''')

        value = len(Driver.allDrivers)
        global  winners, first, second, third
        position = []
        winners = []
        first = []
        second = []
        third = []
        current_points_list = []
        for i in range(1, value+1):
            position.append(i)
            random.shuffle(position)
        position_count = 1
        position_sorter(position)
        for each_position in position:
            current_points_list.append(Driver.allDrivers[each_position-1].current_points)
            if each_position == 1:
                first = Driver.allDrivers[each_position-1]
                pts = int(first.current_points)
                pts = pts + 10
                first.current_points = pts
            if each_position == 2:
                second = Driver.allDrivers[each_position-1]
                pts = int(second.current_points)
                pts = pts + 7
                second.current_points = pts
            if each_position == 3:
                third = Driver.allDrivers[each_position-1]
                pts = int(third.current_points)
                pts = pts + 5
                third.current_points = pts
            position_count += 1
        print(current_points_list)
        race_details_updator(position, race_date, race_location,current_points_list)
    else:
        print("\n SORRY ! At least there are 4 drivers should be added.")
    start()

def VRL(): #6
    for each_race in Race.allRaces:
        date_sorter(Race.allRaces)
        race_table(each_race)
    start()

def STF(): #7
    with open('driver.txt', 'w') as f:
        for driver in Driver.allDrivers:
            f_string=f"{driver.name},{driver.age},{driver.team},{driver.car},{driver.current_points}"
            f.write(f_string)
            f.write('\n')


    with open('race.txt', 'w') as f:
        for race in Race.allRaces:
            f.write(race.date)
            f.write('\n')
            f.write(race.location)
            f.write('\n')
            f.write(str(race.participants))
            f.write('\n')
            f.write(str(race.positions))
            f.write('\n')
            f.write(str(race.points))
            f.write('\n')
            f.write("")
            f.write('\n')


def RFF(): #8

    load_drivers_from_file()

    start()


#-----------------------------------------------------------------

print("--- Welcome to World rally cross championship ---")
print()
print()

start()


