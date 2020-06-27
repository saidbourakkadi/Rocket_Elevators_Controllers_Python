print("hello word")
class Cage:
    def __init__(self,id, levelActual, direction):
        self.id = id
        self.battery = 1         
        self.column = 1
        self.statusDoor = "closed"
        self.position_door_x = 0 # close: 0 / open : 150
        self.timing_door = 3000 
        self.timing_floor = 20000
        self.listUp = []        
        self.listUpOrder = [] 
        self.listDown = []   
        self.listDownOrder = [] 
        self.direction = direction 
        self.levelActual = levelActual 
        self.sensor_status_cage = "Clear"  
        self.close_button = "inactif" 
        self.open_button = "inactif"

        
    def display_status_cage(self):
        print('status_cage: '+ str(self.id) + ' , level Actual: '+ str(self.levelActual) + ' , direction: '+ str(self.direction))
    def call_level(self,levelCall):
        print('level call: '+str(levelCall))
        if self.levelActual > levelCall:
            print("level actual is biggest then the level call so we down")
        elif self.levelActual < levelCall:
            print("level actual is lower then the level call so we up")
        else:  print("level actual is the same then the call")
    def insert_in_to_listUp():
        pass
    def insert_in_to_listDown():
        pass


# instance my object cag1 with this://def __init__(self,id, levelActual, direction)://
cage1 = Cage(1, 1, "idle")
cage2 = Cage(2, 5, "idle")

# display  status cage:id
cage1.display_status_cage()
cage2.display_status_cage()

# function call
def call():
    id = int(input('Enter cage number ? : '))
    call_destination = int(input('Enter your destination ? : '))
    if id == 1:
        cage1.call_level(call_destination)
    elif id == 2:
        cage2.call_level(call_destination)
    else: print('We have not this cage yet')
    
    


call()
# display call inside
# cage_choice = input('Enter the number of cage you choice ? : ')
# floor_destination_inside = int(input('Enter the floor destination ? : '))
# cage1.call_level(floor_destination_inside)    
  