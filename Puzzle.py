import copy
from Utility import *

Moves = {"U" : 0, "L" : 1, "R" : 2, "D" : 3}
Slot = {1 : [0,0], 2 : [0,1], 3 : [0,2], 4 : [0,3], 5 : [1,0], 6 : [1,1], 7 : [1,2], 8 : [1,3], 9 : [2,0], 10 : [2,1], 11 : [2,2], 12 : [2,3], 13 : [3,0], 14 : [3,1], 15 : [3,2], 16 : [3,3]}

class Puzzle:
    def __init__(self, puzzle,indexKosong,moves, depth):
        self.puzzle = copy.deepcopy(puzzle)
        self.indexKosong = [indexKosong[0],indexKosong[1]]
        self.moves = copy.deepcopy(moves)
        # self.loopMove = copy.deepcopy(loopMove)
        self.possibleMoves = []
        self.depth = depth
        self.lastMove = ""
        self.stage = 1

    #HEURISTIK YANG TIDAK JADI DIGUNAKAN
    def checkStage(self):
        if(self.stage >= 1 and self.puzzle[0][0] == 1 and self.puzzle[0][1] == 2):
            self.stage = 2
        if(self.stage >= 2 and self.puzzle[0][2] == 3 and self.puzzle[0][3] == 4):
            self.stage = 3
        if(self.stage >= 3 and self.puzzle[1][0] == 5 and self.puzzle[1][1] == 6):
            self.stage = 4
        if(self.stage >= 4 and self.puzzle[1][2] == 7 and self.puzzle[1][3] == 8):
            self.stage = 5
        if(self.stage >= 5 and self.puzzle[2][0] == 9 and self.puzzle[3][0] == 13):
            self.stage = 6
        if(self.stage >= 6 and self.puzzle[2][1] == 10 and self.puzzle[2][2] == 11 and self.puzzle[2][3] == 12):
            self.stage = 7

    #MEMINDAHKAN SPACE KOSONG PADA PUZZLE
    def moveSpace(self, move):
        if(move == "U"):
            self.puzzle[self.indexKosong[0]][self.indexKosong[1]] = self.puzzle[self.indexKosong[0]-1][self.indexKosong[1]]
            self.puzzle[self.indexKosong[0]-1][self.indexKosong[1]] = 16
            self.indexKosong[0] -= 1
            # self.loopMove.append("U")
            self.moves.append("U")
            self.lastMove = "D"
            # self.clearLoop("U")
        elif(move == "L"):
            self.puzzle[self.indexKosong[0]][self.indexKosong[1]] = self.puzzle[self.indexKosong[0]][self.indexKosong[1]-1]
            self.puzzle[self.indexKosong[0]][self.indexKosong[1]-1] = 16
            self.indexKosong[1] -= 1
            # self.loopMove.append("L")
            self.moves.append("L")
            self.lastMove = "R"
            # self.clearLoop("L")
        elif(move == "R"):
            self.puzzle[self.indexKosong[0]][self.indexKosong[1]] = self.puzzle[self.indexKosong[0]][self.indexKosong[1]+1]
            self.puzzle[self.indexKosong[0]][self.indexKosong[1]+1] = 16
            self.indexKosong[1] += 1
            # self.loopMove.append("R")
            self.moves.append("R")
            self.lastMove = "L"
            # self.clearLoop("R")
        elif(move == "D"):
            self.puzzle[self.indexKosong[0]][self.indexKosong[1]] = self.puzzle[self.indexKosong[0]+1][self.indexKosong[1]]
            self.puzzle[self.indexKosong[0]+1][self.indexKosong[1]] = 16
            self.indexKosong[0] += 1
            # self.loopMove.append("D")
            self.moves.append("D")
            self.lastMove = "U"
            # self.clearLoop("D")

        self.depth += 1
    
    #MENUNJUKAN SEQUENCE PUZZLE HINGGA PENYELESAIAN
    def moveAndPrint(self):
        for i in range(len(self.moves)):
            self.moveSpace(self.moves[i])
            print("Move ke-",i+1,": ",self.moves[i])
            printPuzzle(self.puzzle)
            print()

    #MENGECEK SELURUH POSSIBLE MOVE
    def generatePossibleMove(self):
        possibleMove = []
        up = False
        down = False
        left = False
        right = False
        if(self.indexKosong[0] != 0):
            up = True
        if(self.indexKosong[1] != 0):
            left = True
        if(self.indexKosong[0] != 3):
            down = True
        if(self.indexKosong[1] != 3):
            right = True
        if(up):
            self.possibleMoves.append("U")
        if(left):
            self.possibleMoves.append("L")
        if(right):
            self.possibleMoves.append("R")
        if(down):
            self.possibleMoves.append("D")
        if(self.lastMove in self.possibleMoves):
            self.possibleMoves.remove(self.lastMove)

    def clearPossibleMoves(self):
        self.possibleMoves = []
    
    #MENGECEK JIKA PUZZLE SUDAH SELESAI
    def isFinalState(self):
        for i in range(4):
            for j in range(4):
                if(self.puzzle[i][j] != i*4+j+1):
                    return False
        return True

    #MENCARI NILAI DARI K
    def KValue(self):
        if((self.indexKosong[0]+self.indexKosong[1])% 2 == 0):
            return 0
        else:
            return 1
    
    #MENGECEK KURANG(i)
    def checkKurang(self, val):
        checking = False
        counter = 0
        for i in range(4):
            for j in range(4):
                if(self.puzzle[i][j] == val):
                    checking = True
                elif(checking):
                    if(self.puzzle[i][j]<val):
                        counter += 1
        return counter

    #MENGECEK JIKA SUATU PUZZLE REACHABLE
    def checkReachable(self,arrKurang):
        k = self.KValue()
        reachable = 0
        for i in range(1,17): #MENGECEK FUNGSI KURANG(i) DARI 2 HINGGA 15 KARENA 1 SUDAH PASTI 0 NILAINYA
            kurang = self.checkKurang(i)
            arrKurang.append(kurang)
            reachable += kurang
        arrKurang.append(reachable+k)
        # print("K = ", k, "reachable = ", reachable)
        return (reachable+k)%2 == 0
    
    #MERESET LOOPMOVE
    def clearLoop(self,move):
        if(len(self.loopMove) < 4 and move in self.loopMove):
            self.loopMove = []
        elif(len(self.loopMove) == 4 and move != self.loopMove[0]):
            self.loopMove = []
        elif(len(self.loopMove) == 5):
            self.loopMove = []
    
    def printInfo(self):
        print("Puzzle: ")
        printPuzzle(self.puzzle)
        print("Possible Move: ", self.possibleMoves)
        # print("Loop Move: ", self.loopMove)
        print("Index Kosong: ", self.indexKosong)
        # print("Moves: ", self.moves)
        print("Last move: ", self.lastMove)
        print()

    def getNumIndex(self,num):
        for i in range(4):
            for j in range(4):
                if(self.puzzle[i][j] == num):
                    return [i,j]

    def isNear(indexNum,indexKosong):
        if(indexNum[0] == indexKosong[0]+1 or indexNum[0] == indexKosong[0]-1 or indexNum[1] == indexKosong[1]+1 or indexNum[1] == indexKosong[1]-1):
            return True
        return False
    
    def isInPosition(index,num):
        return index[0] + index[1]+1 != num


    #MENGHASILKAN COST DARI MOVE
    def getMoveCost(self):

        

        # CARA PPT
        cost = 0
        for i in range(4):
            for j in range(4):
                if self.puzzle[i][j] != i*4+j+1 and self.puzzle[i][j] != 16:
                    cost += 1
        return cost + self.depth

        # MANHATTAN DISTANCE
        # cost = 0
        # for i in range(1,16):
        #     index = self.getNumIndex(i)
        #     cost += abs(index[0] - Slot[i][0]) + abs(index[1] - Slot[i][1])
        # return cost + self.depth

    #MENCOBA BERGERAK KE SEGALA ARAH DAN JIKA PUZZLE BELUM PERNAH BERADA PADA SATE TERTENTU, MAKA AKAN DIHITUNG COSTNYA DAN DIPERHITUNGKAN KE QUEUE
    def generateChildNode(self,PrioQueue,exist):
        for i in range(len(self.possibleMoves)):
            puzzleCheck = Puzzle(self.puzzle,self.indexKosong,self.moves, self.depth)
            puzzleCheck.moveSpace(self.possibleMoves[i])
            string1D = puzzleToString(puzzleCheck.puzzle)
            if(not string1D in exist):
                cost = puzzleCheck.getMoveCost()
                PrioQueue.enqueue((cost,puzzleCheck))

                exist[string1D] = puzzleCheck.depth
    
