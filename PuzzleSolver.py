import copy
from Utility import *
import Puzzle as Pz
import PrioQueue as PQ
import time

#IMPLEMENTASI ALGORITMA BRANCH AND BOUND
def BranchAndBound(puzzle):
    Pq = PQ.PrioQueue()
    exist = {puzzleToString(puzzle.puzzle) : puzzle.depth}
    
    while(not puzzle.isFinalState()):
        puzzle.generatePossibleMove()
        puzzle.generateChildNode(Pq,exist)
        puzzle = Pq.dequeue()[1]
    return puzzle, len(exist)

#PRINT PENGECEKAN PUZZLE SOLVABLE ATAU TIDAK DENGAN RUMUS Kurang(i) + X
def printKurang(arr):
    print("Kurang(i):")
    total = 0
    for i in range(len(arr)-1):
        print("Kurang("+ str(i+1) +") =", arr[i])
        total += arr[i]
    print("Total Kurang(i) + X = ", arr[len(arr)-1])
    print()

if(__name__ == "__main__"):
    name = input("Masukkan nama file(tanpa ekstensi): ")
    name = "test\\" + name + ".txt"
    matPuzzle, indexKosong = parsePuzzle(name)
    moveSeq = []
    arrKurang = []
    Puzzle = Pz.Puzzle(matPuzzle,indexKosong,moveSeq, 0)
    PuzzleCheck = Pz.Puzzle(Puzzle.puzzle,Puzzle.indexKosong,Puzzle.moves, Puzzle.depth)
    PuzzleCheck.generatePossibleMove()
    PuzzleCheck.printInfo()

    if(Puzzle.checkReachable(arrKurang)):
        printKurang(arrKurang)
        start = time.time()
        solvedPuzzle,generatedNode = BranchAndBound(PuzzleCheck)
        end = time.time()
        print("Waktu pencarian: ", end-start)
        print("Node yang di generate: ", generatedNode)
        Puzzle.moves = copy.deepcopy(solvedPuzzle.moves)
        Puzzle.moveAndPrint()
    else:
        print("Puzzle Unsolvable")