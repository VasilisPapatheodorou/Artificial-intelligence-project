from random import shuffle
from cubeMoves import CubeMoves
class Cube(CubeMoves):
    
    # List of the first letter of each color used in constructor for the creation of the cube
    color = ["W", "R", "B", "O", "G", "Y"]
    k = 0
    
    # Cube constructor 
    def __init__(self):
        self.cube = [] # List that will hold the cube info
        
        # Creates a 3 x 3 x 6 cube combines color letter with position number "W1, W2, W3" etc
        for c in Cube.color:
            self.cube.append([[c + Cube.counter() for i in range(3)]for j in range(3)])
    
    # Sets the position number for the cube list
    @classmethod
    def counter(cls):
        cls.setK(cls.k + 1)
        return str(cls.k)
    
    # Resets the number to 0 if cube side is done
    @classmethod
    def setK(cls, K):
        if cls.k == 9:
            cls.k = 0
            K = 1
        cls.k = K
        
    # Setter for the cube state
    def setCube(self, cubeState):
        self.cube = cubeState
    
    # Returns the information of the cube in a list
    def getCubeList(self):
        
        return self.cube
    
    # Prints Cube with 0 being Up, 1 Front, 2 Left, 3 Back, 4 Right, 5 Down
    def printCube(self):
        
        for i in self.cube[0]:
            print(i)
            
        for z in range(3):
            if z == 0:
                pass
            else:
                print("")
            
            for j in range(1,5):
                    print(self.cube[j][z], end = ' ')
        
        print("")
        for v in self.cube[5]:
            print(v)
            
       
       
            
