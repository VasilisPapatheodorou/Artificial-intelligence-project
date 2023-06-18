import copy
from cube import *

class AStar:
    
    pathList = [] # List of the path to goal
    openList = [] # List of all the generated children
    closedList = [] # List of visitted nodes
    gen = 0 # Generation of children  
    
    #def ths H
    
    def findF(goalCube, mixCube):
        h = 0
        # flags are used to only add the right amount to h for each case 
        # If corners are in right position add 0 to h
        for i in range(2, 5, 2):
            for j in range(0, 3, 2):
                for z in range(0, 3, 2):
                    if goalCube.getCubeList()[i][j][z] == mixCube.getCubeList()[i][j][z]:
                        h += 0
                    else:
                        flag = True
                        # If corners after 1 of the 12 moves are goal state add 1 to h
                        for n in range(12):
                            tempMixCube = copy.deepcopy(mixCube)
                            tempMixCube.giveMoveFunc(n)
                            if goalCube.getCubeList()[i][j][z] == tempMixCube.getCubeList()[i][j][z]:
                                h += 1
                                flag = False
                                break
                        # If corners needs 2 moves to be goal state add 2 to h
                        if flag:
                            h += 2
        # Edges one if edges are in goal state add 0 to h
        for i in range(0, 6, 5):
            for j in range(0, 3, 2):
                if goalCube.getCubeList()[i][j][1] == mixCube.getCubeList()[i][j][1]:
                    h += 0
                else: 
                    # Edges one if edges after 1 of the 12 moves are goal state add 1 to h 
                    flag = True
                    flag2 = False
                    for n in range(12):
                        tempMixCube = copy.deepcopy(mixCube)
                        tempMixCube.giveMoveFunc(n)
                        if goalCube.getCubeList()[i][j][1] == tempMixCube.getCubeList()[i][j][1]:
                            h += 1
                            flag = False
                            break
                    if flag:
                        # Edges one if edges after 2 moves are goal state add 2 to h 
                        for n in range(12):
                            tempMixCube = copy.deepcopy(mixCube)
                            tempMixCube.giveMoveFunc(n)
                            for z in range(12):
                                tempMixCube = copy.deepcopy(tempMixCube)
                                tempMixCube.giveMoveFunc(z)
                                
                                if goalCube.getCubeList()[i][j][1] == tempMixCube.getCubeList()[i][j][1]:
                                    h += 2
                                    flag = False
                                    flag2 = True
                                    break
                            if flag2:
                                break
                    #Edges one if edges need 3 moves to be in goal state add 3 to h 
                    if flag:
                        h += 3
        # Edges two if edges are in goal state add 0 to h
        for i in range(0, 6):
            if i == 1 or i == 3:
                    continue
            for j in range(0, 3, 2):
                if goalCube.getCubeList()[i][1][j] == mixCube.getCubeList()[i][1][j]:
                    h += 0
                else: 
                    # Edges two if edges are in goal state add 1 to h
                    flag = True
                    flag2 = False
                    for n in range(12):
                        tempMixCube = copy.deepcopy(mixCube)
                        tempMixCube.giveMoveFunc(n)
                        
                        if goalCube.getCubeList()[i][1][j] == tempMixCube.getCubeList()[i][1][j]:
                            h += 1
                            flag = False
                            break
                    if flag:
                        # Edges two if edges after 2 moves are goal state add 2 to h
                        for n in range(12):
                            tempMixCube = copy.deepcopy(mixCube)
                            tempMixCube.giveMoveFunc(n)
                            for z in range(12):
                                tempMixCube = copy.deepcopy(tempMixCube)
                                tempMixCube.giveMoveFunc(z)
                                if goalCube.getCubeList()[i][1][j] == tempMixCube.getCubeList()[i][1][j]:
                                    h += 2
                                    flag = False
                                    flag2 = True
                                    break
                            if flag2:
                                break
                    # Edges two if edges need 3 moves to be in goal state add 3 to h
                    if flag:
                        h += 3
        f = (AStar.gen // 12) + h
        return f
    
    # Return True if number of side to solve are solved 
    def sideOfCubeToSolve(goalCube, mixCube, side):

        for i in range(6):
            if(mixCube.getCubeList()[i] == goalCube.getCubeList()[i]):
                side -= 1
        if(side <= 0):
            return True
        else:
            return False
    
    def aStar(goalCube, mixCube, side):
        # Adds first parent node
        AStar.openList.append((AStar.findF(goalCube, mixCube), -1, mixCube))
        while(len(AStar.openList) != 0):
            
            # Use sideOfCubeToSolve to see if number of sides given to solve are solved  
            if(AStar.sideOfCubeToSolve(goalCube, mixCube, side)):
                # Finds path list via backtracking 
                # Comparing the last state in the list to every state in closed list
                AStar.pathList.append(AStar.closedList[-1])
                for k in reversed(range(len(AStar.closedList))):
                    tempCube = copy.deepcopy(AStar.closedList[k][2]) # Deepcopy mixCube to find the path via backtracking
                    tempCube.giveMoveFunc(AStar.pathList[-1][1]) 
                    # 
                    if(tempCube.getCubeList() ==  AStar.pathList[-1][2].getCubeList()):
                        AStar.pathList.append(AStar.closedList[k])
                AStar.pathList.reverse()
                print("The path to the goal state is:", [i[1] for i in AStar.pathList ])
                mixCube.printCube()
            
                break
            
            # Stores and removes from openList the node with the min F
            minF = min(AStar.openList ,key=lambda x:x[0])
            AStar.openList.pop(AStar.openList.index(minF))

            # Stores parent to closed list after openning all his children
            AStar.closedList.append(minF)
            
            # If the parent is the first node dont make a move
            if(minF[1] == -1):
                pass
            else:
            # Copies the state of the parent cube to the mixCube 
                mixCube.copyCubeState(minF[2].getCubeList())
            # Calculate generation of children to determinate g eg. g = 1 = gen = 12 // 12
            AStar.gen += 12
            
            # Creates parent's children
            for n in range(12):
                tempCube = copy.deepcopy(mixCube) # Deepcopy mixCube to make each move (children) without changing the original mixCube
                tempCube.giveMoveFunc(n) # Use move n
                
                flag = True # Flag to check if child is in closed list
                           
                for i in range(len(AStar.closedList)):
                    # Check if a node is in closed list with a bigger f if it is replace it with the lower f
                    if (tempCube.getCubeList() == AStar.closedList[i][2].getCubeList() and AStar.findF(goalCube, tempCube) < AStar.closedList[i][0]):
                        AStar.closedList.pop(i)
                        AStar.closedList.append(((AStar.findF(goalCube, tempCube), n, tempCube)))
                        
                    elif(tempCube.getCubeList() == AStar.closedList[i][2].getCubeList()):
                        flag = False # Do not add child to openlist because it is in closed

                for j in range(len(AStar.openList)):
                    # Check if a node is in open list with bigger f if it is replace it with the lower f
                    if (tempCube.getCubeList() == AStar.openList[j][2].getCubeList() and AStar.findF(goalCube, tempCube) < AStar.openList[j][0]):
                        AStar.openList.pop(j)
                        AStar.openList.append(((AStar.findF(goalCube, tempCube), n, tempCube)))
                    elif(tempCube.getCubeList() == AStar.openList[j][2].getCubeList()):
                        flag = False # Do not add child to openlist because it is already in the open list
                
                if(flag):
                    # Add child to open list if its not in closed list
                    AStar.openList.append(((AStar.findF(goalCube, tempCube), n, tempCube)))
                
            
            