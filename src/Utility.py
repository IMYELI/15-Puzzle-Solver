import random as rd

#IMPORT PUZZLE DARI FILE TXT
def parsePuzzle(filename):
    puzzle = []
    with open(filename) as f:
        for line in f:
            puzzle.append([int(x) for x in line.split()])
    
    for i in range(4):
        for j in range(4):
            if puzzle[i][j] == 16:
                indexKosong = [i,j]
                break
    return puzzle,indexKosong

#DIGUNAKAN UNTUK MENGENERATE PUZZLE
def generatePuzzle():
    puzzle = []
    i = 0
    while(i!=16):
        rand = rd.randint(1,16) 
        while(rand in puzzle):  #cek apakah sudah ada di puzzle
            rand = rd.randint(1,16)
        puzzle.append(rand)
        i += 1
    matPuzzle = []
    k = 0
    indexKosong = 0
    for i in range(4): #membuat puzzle
        matPuzzle.append([])
        for j in range(4): 
            if puzzle[j+k] == 16: #mencari space kosong
                indexKosong = [int(k/4),j] #menyimpan index kosong
            matPuzzle[i].append(puzzle[j+k])
            # print(matPuzzle, i, j)
        k += 4
    return matPuzzle, indexKosong

#PRINT STATE PUZZLE
def printPuzzle(puzzle):
    for i in range(4):
        for j in range(4):
            if(puzzle[i][j] == 16):
                print('space'.ljust(5), end=' ')
            else:
                print(str(puzzle[i][j]).ljust(5), end=" ")
        print()

#MENGUBAH PUZZLE MENJADI STRING
def puzzleToString(puzzle):
    string = ""
    for i in range(4):
        for j in range(4):
            string += str(puzzle[i][j])
    return string

#MENGUBAH 2D PUZZLE MENJADI 1D PUZZLE
def make1DPuzzle(Puzzle):
    puzzle = [0 for i in range(16)]
    for i in range(4):
        for j in range(4):
            puzzle[i*4+j] = Puzzle[i][j]
    return puzzle

#MEMBUAT 1D PUZZLE MENJADI 2D PUZZLE
def make2DPuzzle(Puzzle):
    puzzle = [[0 for i in range(4)] for j in range(4)]
    for i in range(4):
        for j in range(4):
            puzzle[i][j] = Puzzle[i*4+j]
    return puzzle
