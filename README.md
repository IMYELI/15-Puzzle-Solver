# 15-Puzzle-Solver
## Penjelasan Singkat
Program 15-Puzzle-Solver menggunakan algoritma Branch and Bound yang menggunakan misplaced tiles sebagai heuristic nya sesuai spek tugas besar. Namun juga disediakan heuristic Manhattan Distance pada line 194 di file Puzzle.py. Heuristic dapat diganti dengan menjadikan heuristic sebelumnya sebagai comment dan hilangkan simbol comment pada heuristic yang ingin digunakan. Program pertama akan mengecek apakah suatu puzzle bisa diselesaikan sebelum melakukan pencarian.

## Requirement
- Python (disarankan versi 3.9 keatas)
- modul tkinter

## Cara menjalankan program
### Alternatif 1
1. Pilih ingin menggunakan CLI(PuzzleSolver.py) atau GUI(PuzzleSolverGUI.py) 
2. Jalankan dengan command "python {nama file}"

### Alternatif 2
1. Klik 2x file .bat di folder BIN sesuai yang ingin digunakan(CLI atau GUI)

## Cara menggunakan program
### CLI
1. Masukan file puzzle ke folder test
2. Jalankan program
3. Program akan meminta input.
4. Masukkan nama file puzzle
Masukan file juga dapat di generate secara otomatis dengan mengganti command parsePuzzle() pada line 31 dengan generatePuzzle() lalu line 29 dan 30 dijadikan comment

### GUI
- Import file
1. Pilih menu import/export di kiri atas program
2. Tekan import puzzle
3. Pilih file dari filedialog
4. Tekan tombol solve

- Mengacak puzzle sendiri
1. Acak puzzle dengan tombol up down left right
2. Tekan tombol solve

- Export puzzle yang telah diacak
1. Pilih menu import/export di kiri atas program
2. Tekan save puzzle
3. Tentukan tempat dan nama save file di filedialog

- Mengulang hasil acakan puzzle
1. Pilih menu import/export di kiri atas program
2. Tekan reset puzzle
