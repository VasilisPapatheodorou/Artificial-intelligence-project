from random import randint
class CubeMoves:
    
    # static method cube rotation to the right
    @staticmethod
    def clockwiseRotation(input_): 
        for i in range(2):
            temp = input_[0][i]
            input_[0][i] = input_[2-i][0]
            input_[2 - i][0] = input_[2][2 - i]
            input_[2][2 - i] = input_[i][2]
            input_[i][2] = temp

    # static method cube rotation to the left
    @staticmethod   
    def antiClockwiseRotation(input_): 
        for i in range(2):
            temp = input_[0][i]
            input_[0][i] = input_[i][2]
            input_[i][2] = input_[2][2 - i]
            input_[2][2 - i] = input_[2 - i][0]
            input_[2 - i][0] = temp   
    
    # all 12 cube moves exept the middle moves
    def moveUpClockwise(self):
        self.clockwiseRotation(self.cube[0])
        for i in range(3):
            temp = self.cube[1][0][i]
            self.cube[1][0][i] = self.cube[2][0][i]
            self.cube[2][0][i] = self.cube[3][0][i]
            self.cube[3][0][i] = self.cube[4][0][i]
            self.cube[4][0][i] = temp
    
    def moveUpAntiClockwise(self):
        self.antiClockwiseRotation(self.cube[0])
        
        for i in range(3):
            temp = self.cube[1][0][i]
            self.cube[1][0][i] = self.cube[4][0][i]
            self.cube[4][0][i] = self.cube[3][0][i]
            self.cube[3][0][i] = self.cube[2][0][i]
            self.cube[2][0][i] = temp
    
    def moveFrontClockwise(self):
        self.clockwiseRotation(self.cube[2])
        
        temp = [self.cube[5][0][0], self.cube[5][0][1], self.cube[5][0][2]]
        for i in range(3):
            self.cube[5][0][2 - i] = self.cube[3][i][0]
            self.cube[3][i][0] = self.cube[0][2][i]
            self.cube[0][2][i] = self.cube[1][2 - i][2]
            
        for j in range(3):
            self.cube[1][j][2] = temp[j]           
    
    def moveFrontAntiClockwise(self):
        self.antiClockwiseRotation(self.cube[2])
        
        temp = [self.cube[3][0][0], self.cube[3][1][0], self.cube[3][2][0]]
        for i in range(3):
            self.cube[3][2 - i][0] = self.cube[5][0][i]
            self.cube[5][0][i] = self.cube[1][i][2]
            self.cube[1][i][2] = self.cube[0][2][2 - i]
            
        for j in range(3):
            self.cube[0][2][j] = temp[j]     
        
    def moveLeftClockwise(self):
        self.clockwiseRotation(self.cube[1])
        
        temp = [self.cube[0][0][0], self.cube[0][1][0], self.cube[0][2][0]]
        for i in range(3):
            self.cube[0][2 - i][0] = self.cube[4][i][2]
            self.cube[4][i][2] = self.cube[5][2 - i][0]
            
        for j in range(3):
            
            self.cube[5][j][0] = self.cube[2][j][0]
            self.cube[2][j][0] = temp[j] 
    
    def moveLeftAntiClockwise(self):
        self.antiClockwiseRotation(self.cube[1])
        
        temp = [self.cube[5][0][0], self.cube[5][1][0], self.cube[5][2][0]]
        for i in range(3):
            self.cube[5][2 - i][0] = self.cube[4][i][2]
            self.cube[4][i][2] = self.cube[0][2 - i][0]
            
        for j in range(3):
            self.cube[0][j][0] = self.cube[2][j][0]
            self.cube[2][j][0] = temp[j] 
    
    def moveDownClockwise(self):
        self.clockwiseRotation(self.cube[5])
        
        for i in range(3):
            temp = self.cube[1][2][i]
            self.cube[1][2][i] = self.cube[4][2][i]
            self.cube[4][2][i] = self.cube[3][2][i]
            self.cube[3][2][i] = self.cube[2][2][i]
            self.cube[2][2][i] = temp
    
    def moveDownAntiClockwise(self):
        self.antiClockwiseRotation(self.cube[5])
        
        for i in range(3):
            temp = self.cube[1][2][i]
            self.cube[1][2][i] = self.cube[2][2][i]
            self.cube[2][2][i] = self.cube[3][2][i]
            self.cube[3][2][i] = self.cube[4][2][i]
            self.cube[4][2][i] = temp
    
    def moveBackClockwise(self):
        self.clockwiseRotation(self.cube[4])
        
        temp = [self.cube[3][0][2], self.cube[3][1][2], self.cube[3][2][2]]
        for i in range(3):
            self.cube[3][2 - i][2] = self.cube[5][2][i]
            self.cube[5][2][i] = self.cube[1][i][0]
            self.cube[1][i][0] = self.cube[0][0][2 - i]
            
        for j in range(3):
            self.cube[0][0][j] = temp[j] 
    
    def moveBackAntiClockwise(self):
        self.antiClockwiseRotation(self.cube[4])
        
        temp = [self.cube[5][2][0], self.cube[5][2][1], self.cube[5][2][2]]
        for i in range(3):
            self.cube[5][2][2 - i] = self.cube[3][i][2]
            self.cube[3][i][2] = self.cube[0][0][i]
            self.cube[0][0][i] = self.cube[1][2 - i][0]
            
        for j in range(3):
            self.cube[1][j][0] = temp[j]           
    
    def moveRightClockwise(self):
        self.clockwiseRotation(self.cube[3])
        
        temp = [self.cube[4][0][0], self.cube[4][1][0], self.cube[4][2][0]]
        for i in range(3):
            self.cube[4][2 - i][0] = self.cube[0][i][2]
            self.cube[0][i][2] = self.cube[2][i][2]
            self.cube[2][i][2] = self.cube[5][i][2]
            
        for j in range(3):
            self.cube[5][2 - j][2] = temp[j] 
    
    def moveRightAntiClockwise(self):
        self.antiClockwiseRotation(self.cube[3])
        
        temp = [self.cube[0][0][2], self.cube[0][1][2], self.cube[0][2][2]]
        for i in range(3):
            self.cube[0][2 - i][2] = self.cube[4][i][0]
            self.cube[4][i][0] = self.cube[5][2 - i][2]

        for j in range(3):
            self.cube[5][j][2] = self.cube[2][j][2]
            self.cube[2][j][2] = temp[j]
    
    # calls move entered (0 - 11) uses self so its unique for each Cube obj
    def giveMoveFunc(self, locOfMove):
        
        lOfMoves = [self.moveRightClockwise, self.moveRightAntiClockwise,
                    self.moveLeftClockwise, self.moveLeftAntiClockwise,
                    self.moveFrontClockwise, self.moveFrontAntiClockwise,
                    self.moveUpClockwise, self.moveUpAntiClockwise,
                    self.moveBackClockwise, self.moveBackAntiClockwise,
                    self.moveDownClockwise, self.moveDownAntiClockwise]
        
        lOfMoves[locOfMove]()
    
    # copies cube state to use for the parent
    def copyCubeState(self, state):
        
        self.setCube(state)
    
    # Mix cube as many times as you enter default is 15 by using giveMoveFunc and randint  
    def mixCube(self, randomMoves = 15):
        
        for i in range(randomMoves):
            x = randint(0 , 11)
            self.giveMoveFunc(x)