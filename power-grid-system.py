import csv

class House:
    def __init__(self, number, power):
        self.house_no = number
        self.power_required = power
        self.assigned_propagator_no = -1
        
    def assign_propagator(self, number):
        self.assigned_propagator_no = number
    
    def __str__(self):
        return f"house_no: {self.house_no} power_required: {self.power_required}"
    
class Propagator:
    def __init__(self, number, max_power):
        self.propagator_no = number
        self.maximum_power = max_power
        self.power_remaining = max_power
        self.houses_connected = list()
        
    def __str__(self):
        return f"no : {self.propagator_no} max_power: {self.maximum_power} power_remaining: {self.power_remaining}"
    
    def connected_houses_info(self):
        for inner_list in self.houses_connected:
            house_no=inner_list[0]
            power_required=inner_list[1]
            house=House(house_no, power_required)
            print(house)
    
    # check if the house is connected part of the list or not.           
    def is_house_present(self, house_no:int):
        if house_no in self.houses_connected:
            return self.houses_connected.index(house_no)
        else:
            return -1
        #pass
    
    # Add the house in the list.
    # Before adding check if the house is already connected
    def add_house(self, house:House):
        if self.is_house_present(house.house_no) != -1 :
            #print('House', house.house_no, 'is already connected to a propagator!')
            return False
        else:
            if self.power_remaining < house.power_required:
                #print ('house', house.house_no, 'cannot be added as the power remaining is insufficient!')
                return False
            else:
                self.power_remaining=self.power_remaining - house.power_required
                temp = [house.house_no, house.power_required, self.propagator_no]
                self.houses_connected.append(temp)
                return True
        #pass
    
    # Remove the house from the list, before removing need to check
    # if the house is in the assigned propoagtor list. 
    def remove_house(self, house_no:int):
        for i in range(len(self.houses_connected)):
            for inner_list in self.houses_connected:
                if house_no in inner_list:
                    house_no=inner_list[0]
                    power_required=inner_list[1]
                    temp = self.houses_connected.index(inner_list)
                    self.power_remaining=self.power_remaining + power_required
                    self.houses_connected.pop(temp)
                    return True
            else:
                return False
        #pass
                
                        
class PowerGrid:
    def __init__(self):
        self.propagators = dict()
    # Adding the propagtor into in the dictionary. 
    # Check if the propagator is not part of the dictioary already
    # It will not posess any value in the beginning. 
    def add_propagator(self, propagator:Propagator):
        if propagator in self.propagators:
            print("propagator", propagator.propagator_no, "already exists")
            return False
        else:
            self.propagators[propagator.propagator_no] = propagator
        #pass
            
    # Removing the propagtor into in the dictionary. 
    # Check if the propagator is part of the dictioary or not    
    def remove_propagator(self, propagator_no):
        if propagator_no not in self.propagators:
            print("Propagator", propagator_no, "does not exist and hence cannot be removed")
            return False
        else:
            for i in range(len(self.propagators[propagator_no].houses_connected)):
                for item in self.propagators[propagator_no].houses_connected:
                    house_no=item[0]
                    self.propagators[propagator_no].remove_house(house_no)
            self.propagators.pop(propagator_no)
            print("Propagator", propagator_no, "is successfully removed")
            return True
        #pass
    
    def add_house(self, house:House, propagator_no:int):
        if propagator_no in self.propagators:
            return self.propagators[propagator_no].add_house(house)
        else:
            return False
        
    def remove_house(self, house_no:int, propagator_no:int):
        if propagator_no in self.propagators:
            return self.propagators[propagator_no].remove_house(house_no)
        else:
            return False

def create_power_grid():
    power_grid = PowerGrid()
    
    with open('app.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            
            entity_type = row['Type']
            
            if entity_type == "propagator":
                propagator = Propagator(int(row['Entity_Number']), int(row['Power']))
                power_grid.add_propagator(propagator)
            
            elif entity_type == "house":
                
                house = House(int(row['Entity_Number']), int(row['Power']))
                house.assigned_propagator_no = int(row['Assigned_Propagator'])
                
                power_grid.add_house(house, int(row['Assigned_Propagator']))
          
    return power_grid

if __name__ == "__main__":
    power_grid = create_power_grid()
    
    for _, propagator in power_grid.propagators.items():
        
        #Printing the propagator information
        print(f"Propagator No : {propagator.propagator_no}")
        print("------------Propagator Information-----------------")
        print(propagator)
        print("------------Connected Houses Information-----------------")
        propagator.connected_houses_info()
        print("\n")
        
    print("----Removing House 1014 from Propagator 1002----")
    if power_grid.remove_house(1014, 1002):
        print("House 1014 is successfully removed from Propagator 1002")
    else:
        print("House 1014 is not connected with Propagator 1002")
        
    
    print("\n----Removing House 1024 from Propagator 1003----")
    if power_grid.remove_house(1024, 1003):
        print("House 1024 is successfully removed from Propagator 1003")
    else:
        print("House 1024 is not connected with Propagator 1003")