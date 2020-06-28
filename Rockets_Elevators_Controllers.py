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
        self.destination=[]
        self.listUp = []        
        self.listUpOrder = [] 
        self.listDown = []   
        self.listDownOrder = []
        self.listPoubelle = []
        self.direction = direction 
        self.levelActual = levelActual 
        self.sensor_status_cage = "Clear"  
        self.close_button = "inactif" 
        self.open_button = "inactif"

        
    def display_status_cage(self):
        print('status_cage: '+ str(self.id) + ' , level Actual: '+ str(self.levelActual) + ' , direction: '+ str(self.direction))
    def call_level(self,levelCall):
        
        print('level call: '+str(levelCall))
        if levelCall == -1 or levelCall == 0:
            self.listPoubelle.append(levelCall)
            
        elif self.levelActual > levelCall and (levelCall != 0):
            if levelCall in self.listDown:
                print('this number is already Actif')
            else: 
                self.listDown.append(levelCall)
                self.listDown.sort(reverse=True)
            
            #print("level actual is biggest then the level call so we down on "+str(step)+' steps')
        elif self.levelActual < levelCall and (levelCall != 0):
            if levelCall in self.listUp:
                print('this number is already Actif')
            else: 
                self.listUp.append(levelCall)
                self.listUp.sort(reverse=False)
            #print("level actual is lower then the level call so we up on "+str(step)+' steps')
        else:
            print("level actual is the same then the call so we open the door for you you arrived")
            print("The door is Open")
            print("The door is closed")
        print('listUp: '+ str(self.listUp))
        print('listDown: '+ str(self.listDown))

        
    def move_up(self):
        self.direction = 'up'
        for list in self.listUp:
            print("level actual is: "+ str(self.levelActual))
            print("the direction in this cage is : " + self.direction)
            print("we go in the floor: " + str(list))
            while self.levelActual < list : 
                self.levelActual +=1
                print("level actual is: "+ str(self.levelActual))
            self.open_close_door()
        del self.listUp[:]        
        print("the listUp is empty now :"+ str(self.listUp))
        #print("the direction in this cage is : " + self.direction)
            
    def move_down(self):
        self.direction = 'down'
        for list in self.listDown:
            print("level actual is: "+ str(self.levelActual))
            print("the direction in this cage is : " + self.direction)
            print("we go in the floor: " + str(list))
            while self.levelActual > list : 
                self.levelActual -=1
                print("level actual is: "+ str(self.levelActual))
            self.open_close_door()
        del self.listDown[:]               
        self.direction = "idle"
        print("the listDown is empty now :"+ str(self.listDown))
        print("the direction in this cage is : " + self.direction)
            
         
    def open_close_door(self):
        print("we are arrived")
        self.position_door_x = 150
        print("The door is Open")
        self.position_door_x = 0
        print("The door is closed")



# instance my object cag1 with this://def __init__(self,id, levelActual, direction)://
cage1 = Cage(1, 5, "up")
cage2 = Cage(2, 5, "up")

# display  status cage:id
cage1.display_status_cage()
cage2.display_status_cage()

# variables
id = 0

# choice your cage
while id != 1 and id !=2:
    id = int(input('Enter cage number [1,2] ? : '))
    print("you are in the cage number: "+str(id))

# function call inside 
# the first call is decided for the first direction cage
dest = 1
if id == 1:
    while dest != 0 and dest > 0 and dest <= 10:
        destination = int(input('Enter your destination [1 to 10] ? if you finished enter 0: '))
        cage1.call_level(destination)
        dest = destination
    cage1.move_up()
    cage1.move_down()
    

if id == 2:
    while dest != 0 and dest >0 and dest <= 10:
        dest = int(input('Enter your destination [1 to 10] ? if you finished enter 0: '))
        cage2.call_level(dest)
    cage2.move_up()
    cage2.move_down()
    
   



    



  