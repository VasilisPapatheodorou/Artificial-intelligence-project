from cube import Cube
from aStar import AStar

cubeToSolve = Cube()
goalCube = Cube()
print("-1: Exit")
print("0: For random shuffle")
print("1: For custom move")

while True:
    switchNum = int(input("Give option: "))

    if switchNum == -1:
        break
    elif switchNum == 0:
        nForShuffle = int(input("Give number of moves to use in the shuffling of the cube: "))
        cubeToSolve.mixCube(nForShuffle)
        nOfSide = int(input("Give number of sides to solve: "))
        AStar.aStar(goalCube, cubeToSolve, nOfSide)
        break
    elif switchNum == 1:
        nForCustom = int(input("Give -1: to start A* 0: R 1: R' 2: L 3: L' 4: F 5: F' 6: U 7 :U' 8: B 9: B' 10: D 11: D' : "))
        while nForCustom != -1:
            cubeToSolve.giveMoveFunc(nForCustom)
            nForCustom = int(input("Give -1: to start A* 0: R 1: R' 2: L 3: L' 4: F 5: F' 6: U 7 :U' 8: B 9: B' 10: D 11: D' : "))
        nOfSide = int(input("Give number of sides to solve: "))
        AStar.aStar(goalCube, cubeToSolve, nOfSide)
        break
    else:
        print("Wrong input")