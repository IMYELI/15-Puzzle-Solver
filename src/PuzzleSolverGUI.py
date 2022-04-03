import tkinter as tk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
import copy
import PuzzleSolver as PS
import Puzzle as P
import time
from Utility import *

puzzle = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,' ']
puzzleCheck = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
indexKosong = [3,3]
kurang = ['','','','','','','','','','','','','','','','', '']
moves = []
generated = ''
waktu = 0
totalMoves = 0

# IMPORT FILE
def openFile():
    filetypes = [
        ('Text files', '*.txt')
    ]
    global indexKosong, puzzle
    try:
        filename =  fd.askopenfilename(title='Open a file',filetypes=filetypes)
        
        with open(filename,"r") as f:
            datas = f.readlines()
            count = 0
            for line in datas:
                num = line.split()
                for i in num:
                    if(int(i) == 16):
                        puzzle[count] = 16
                        indexKosong = [count//4,count%4]
                    else:
                        puzzle[count] = int(i)
                    count += 1
            updatePuzzle()
        
    except:
        showinfo('Error', 'Invalid puzzle')

#UPDATE PUZZLE PADA GUI
def updatePuzzle():
    global puzzle,puzzleCheck
    puzzleCheck = copy.deepcopy(puzzle)
    puzzle[indexKosong[0]*4 + indexKosong[1]] = ' '
    l1.config(text=puzzle[0])
    l2.config(text=puzzle[1])
    l3.config(text=puzzle[2])
    l4.config(text=puzzle[3])
    l5.config(text=puzzle[4])
    l6.config(text=puzzle[5])
    l7.config(text=puzzle[6])
    l8.config(text=puzzle[7])
    l9.config(text=puzzle[8])
    l10.config(text=puzzle[9])
    l11.config(text=puzzle[10])
    l12.config(text=puzzle[11])
    l13.config(text=puzzle[12])
    l14.config(text=puzzle[13])
    l15.config(text=puzzle[14])
    l16.config(text=puzzle[15])

#UPDATE LABEL KURANG
def updateKurang():
    global kurang
    lKurang1.config(text="Kurang(1): " + str(kurang[0]))
    lKurang2.config(text="Kurang(2): "+ str(kurang[1]))
    lKurang3.config(text="Kurang(3): "+ str(kurang[2]))
    lKurang4.config(text="Kurang(4): "+ str(kurang[3]))
    lKurang5.config(text="Kurang(5): "+ str(kurang[4]))
    lKurang6.config(text="Kurang(6): "+ str(kurang[5]))
    lKurang7.config(text="Kurang(7): "+ str(kurang[6]))
    lKurang8.config(text="Kurang(8): "+ str(kurang[7]))
    lKurang9.config(text="Kurang(9): "+ str(kurang[8]))
    lKurang10.config(text="Kurang(10): "+ str(kurang[9]))
    lKurang11.config(text="Kurang(11): "+ str(kurang[10]))
    lKurang12.config(text="Kurang(12): "+ str(kurang[11]))
    lKurang13.config(text="Kurang(13): "+ str(kurang[12]))
    lKurang14.config(text="Kurang(14): "+ str(kurang[13]))
    lKurang15.config(text="Kurang(15): "+ str(kurang[14]))
    lKurang16.config(text="Kurang(16): "+ str(kurang[15]))
    lkurangx.config(text="Kurang(i) + X: "+ str(kurang[16]))


# COMMAND PERGERAKAN
def moveUp():
    global puzzle,indexKosong
    if(indexKosong[0] == 0):
        showinfo('Error', 'Move out of bound')
    else:
        puzzle[indexKosong[0]*4 + indexKosong[1]] = puzzle[indexKosong[0]*4 + indexKosong[1] - 4]
        puzzle[indexKosong[0]*4 + indexKosong[1] - 4] = 16
        indexKosong[0] -= 1
    updatePuzzle()

def moveDown():
    global puzzle,indexKosong
    if(indexKosong[0] == 3):
        showinfo('Error', 'Move out of bound')
    else:
        puzzle[indexKosong[0]*4 + indexKosong[1]] = puzzle[indexKosong[0]*4 + indexKosong[1] + 4]
        puzzle[indexKosong[0]*4 + indexKosong[1] + 4] = 16
        indexKosong[0] += 1
    updatePuzzle()

def moveLeft():
    global puzzle,indexKosong
    if(indexKosong[1] == 0):
        showinfo('Error', 'Move out of bound')
    else:
        puzzle[indexKosong[0]*4 + indexKosong[1]] = puzzle[indexKosong[0]*4 + indexKosong[1] - 1]
        puzzle[indexKosong[0]*4 + indexKosong[1] - 1] = 16
        indexKosong[1] -= 1
    updatePuzzle()

def moveRight():
    global puzzle,indexKosong
    if(indexKosong[1] == 3):
        showinfo('Error', 'Move out of bound')
    else:
        puzzle[indexKosong[0]*4 + indexKosong[1]] = puzzle[indexKosong[0]*4 + indexKosong[1] + 1]
        puzzle[indexKosong[0]*4 + indexKosong[1] + 1] = 16
        indexKosong[1] += 1
    updatePuzzle()


# SOLVE PUZZLE DENGAN BRANCH AND BOUND
def solvePuzzle():
    global puzzleCheck,indexKosong, moves, kurang, generated, waktu, totalMoves
    objPuzzle = P.Puzzle(puzzleCheck,indexKosong,[],0)
    objPuzzle.puzzle = make2DPuzzle(objPuzzle.puzzle)
    kurang = []
    start = time.time()
    if(objPuzzle.checkReachable(kurang)):
        updateKurang()
        objPuzzle, generated = PS.BranchAndBound(objPuzzle)
        end = time.time()
        waktu = end-start
        moves = objPuzzle.moves
        lGeneratedNode.config(text="Generated Node: "+ str(generated))
        totalMoves = len(moves)
        lTotalMoves.config(text="Total Moves: "+ str(totalMoves))
        lTime.config(text="Time: "+ str(waktu))
        autoSolve()
    else:
        updateKurang()
        generated = 0
        waktu = 0
        totalMoves = 0
        lGeneratedNode.config(text="Generated Node: "+ str(generated))
        lTime.config(text="Time: "+ str(waktu))
        lTotalMoves.config(text="Total Moves: "+ str(totalMoves))
        showinfo('Check Result', 'Puzzle is not solvable')
    
#BERGERAK OTOMATIS UNTUK MENYELESAIKAN PUZZLE
def autoSolve():
    global moves
    for i in moves:
        if(i == "U"):
            moveUp()
        elif(i=="D"):
            moveDown()
        elif(i=="L"):
            moveLeft()
        elif(i=="R"):
            moveRight()
        frame.update()
        time.sleep(0.5)

def saveFile():
    global puzzleCheck
    f = fd.asksaveasfile(initialfile = 'Untitled.txt', defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documents","*.txt")])
    for i in range(16):
        f.write(str(puzzleCheck[i])+" ")
        if(i%4==3):
            f.write("\n")

def resetPuzzle():
    global puzzle, indexKosong
    puzzle = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
    indexKosong = [3,3]
    updatePuzzle()

frame = tk.Tk()


menu = tk.Menu(frame)
frame.config(menu=menu)
fileMenu = tk.Menu(menu, tearoff = 0)
menu.add_cascade(label='Import/Export Puzzle', menu=fileMenu)
fileMenu.add_command(label='Reset Puzzle', command=resetPuzzle)
fileMenu.add_command(label='Save Puzzle', command=saveFile)
fileMenu.add_command(label='Load Puzzle', command=openFile)

lPuzzle = tk.Label(frame, text='Puzzle:')

l1 = tk.Label(frame, text=puzzle[0], font="Helvetica 16 bold", width=5)
l2 = tk.Label(frame, text=puzzle[1], font="Helvetica 16 bold", width=5)
l3 = tk.Label(frame, text=puzzle[2], font="Helvetica 16 bold", width=5)
l4 = tk.Label(frame, text=puzzle[3], font="Helvetica 16 bold", width=5)
l5 = tk.Label(frame, text=puzzle[4], font="Helvetica 16 bold", width=5)
l6 = tk.Label(frame, text=puzzle[5], font="Helvetica 16 bold", width=5)
l7 = tk.Label(frame, text=puzzle[6], font="Helvetica 16 bold", width=5)
l8 = tk.Label(frame, text=puzzle[7], font="Helvetica 16 bold", width=5)
l9 = tk.Label(frame, text=puzzle[8], font="Helvetica 16 bold", width=5)
l10 = tk.Label(frame, text=puzzle[9], font="Helvetica 16 bold", width=5)
l11 = tk.Label(frame, text=puzzle[10], font="Helvetica 16 bold", width=5)
l12 = tk.Label(frame, text=puzzle[11], font="Helvetica 16 bold", width=5)
l13 = tk.Label(frame, text=puzzle[12], font="Helvetica 16 bold", width=5)
l14 = tk.Label(frame, text=puzzle[13], font="Helvetica 16 bold", width=5)
l15 = tk.Label(frame, text=puzzle[14], font="Helvetica 16 bold", width=5)
l16 = tk.Label(frame, text=puzzle[15], font="Helvetica 16 bold", width=5)

lKurang = tk.Label(frame, text="Kurang(i):")
lKurang.grid(row=0, column=7)
lKurang1 = tk.Label(frame, text="Kurang(1): " + kurang[0])
lKurang1.grid(row=1, column=7)
lKurang2 = tk.Label(frame, text="Kurang(2): " + kurang[1])
lKurang2.grid(row=2, column=7)
lKurang3 = tk.Label(frame, text="Kurang(3): " + kurang[2])
lKurang3.grid(row=3, column=7)
lKurang4 = tk.Label(frame, text="Kurang(4): " + kurang[3])
lKurang4.grid(row=4, column=7)
lKurang5 = tk.Label(frame, text="Kurang(5): " + kurang[4])
lKurang5.grid(row=5, column=7)
lKurang6 = tk.Label(frame, text="Kurang(6): " + kurang[5])
lKurang6.grid(row=6, column=7)
lKurang7 = tk.Label(frame, text="Kurang(7): " + kurang[6])
lKurang7.grid(row=7, column=7)
lKurang8 = tk.Label(frame, text="Kurang(8): " + kurang[7])
lKurang8.grid(row=8, column=7)
lKurang9 = tk.Label(frame, text="Kurang(9): " + kurang[8])
lKurang9.grid(row=1, column=8)
lKurang10 = tk.Label(frame, text="Kurang(10): " + kurang[9])
lKurang10.grid(row=2, column=8)
lKurang11 = tk.Label(frame, text="Kurang(11): " + kurang[10])
lKurang11.grid(row=3, column=8)
lKurang12 = tk.Label(frame, text="Kurang(12): " + kurang[11])
lKurang12.grid(row=4, column=8)
lKurang13 = tk.Label(frame, text="Kurang(13): " + kurang[12])
lKurang13.grid(row=5, column=8)
lKurang14 = tk.Label(frame, text="Kurang(14): " + kurang[13])
lKurang14.grid(row=6, column=8)
lKurang15 = tk.Label(frame, text="Kurang(15): " + kurang[14])
lKurang15.grid(row=7, column=8)
lKurang16 = tk.Label(frame, text="Kurang(16): " + kurang[15])
lKurang16.grid(row=8, column=8)
lkurangx = tk.Label(frame, text="Kurang(i) + X: " + kurang[16])
lkurangx.grid(row=9, column=7,columnspan=2)


lPuzzle.grid(row=0, column=0, columnspan=4)

lGeneratedNode = tk.Label(frame, text="Generated Node: " + generated)
lGeneratedNode.grid(row=10, column=7, columnspan=2)

lTime = tk.Label(frame, text="Time: " + str(waktu))
lTime.grid(row=11, column=7, columnspan=2)

lTotalMoves = tk.Label(frame, text="Total Moves: " + str(totalMoves))
lTotalMoves.grid(row=12, column=7, columnspan=2)

l1.grid(row=1, column=3)
l2.grid(row=1, column=4)
l3.grid(row=1, column=5)
l4.grid(row=1, column=6)
l5.grid(row=2, column=3)
l6.grid(row=2, column=4)
l7.grid(row=2, column=5)
l8.grid(row=2, column=6)
l9.grid(row=3, column=3)
l10.grid(row=3, column=4)
l11.grid(row=3, column=5)
l12.grid(row=3, column=6)
l13.grid(row=4, column=3)
l14.grid(row=4, column=4)
l15.grid(row=4, column=5)
l16.grid(row=4, column=6)

bUp = tk.Button(frame, text='Up', command=moveUp, width=10)
bDown = tk.Button(frame, text='Down', command=moveDown, width=10)
bLeft = tk.Button(frame, text='Left', command=moveLeft, width=10)
bRight = tk.Button(frame, text='Right', command=moveRight, width=10)

bUp.grid(row = 6, column = 4, columnspan=2)
bLeft.grid(row = 7, column = 4)
bRight.grid(row = 7, column = 5)
bDown.grid(row = 8, column = 4, columnspan=2)

bSolve = tk.Button(frame, text='Solve', command=solvePuzzle, width=20)
bSolve.grid(row = 9, column = 3, columnspan=4)

frame.mainloop()