from array import array
from sudoku import Sudoku
from pwn import *

io = connect("ctf.uiactf.no", 5006)

# Puzzles solved so far
count = 0

# Solve 50 puzzles
while (count < 50):
    count = count + 1

    # Wait for the start of the next puzzle
    rec = io.recvuntil(b'[')
    
    # Read every line of the puzzle,
    # every line looks something like this: [0,0,4,2]
    line1 = io.recvline(False).decode()
    line2 = io.recvline(False).decode()
    line3 = io.recvline(False).decode()
    line4 = io.recvline(False).decode()
    line5 = io.recvline(False).decode()
    line6 = io.recvline(False).decode()
    line7 = io.recvline(False).decode()
    line8 = io.recvline(False).decode()
    line9 = io.recvline(False).decode()

    # Python way of parsing array strings into int arrays,
    # when the developer doesn't know Python
    b1 = [int(i) for i in line1.replace('[', '').replace(']', '').split(',')]
    b2 = [int(i) for i in line2.replace('[', '').replace(']', '').split(',')]
    b3 = [int(i) for i in line3.replace('[', '').replace(']', '').split(',')]
    b4 = [int(i) for i in line4.replace('[', '').replace(']', '').split(',')]
    b5 = [int(i) for i in line5.replace('[', '').replace(']', '').split(',')]
    b6 = [int(i) for i in line6.replace('[', '').replace(']', '').split(',')]
    b7 = [int(i) for i in line7.replace('[', '').replace(']', '').split(',')]
    b8 = [int(i) for i in line8.replace('[', '').replace(']', '').split(',')]
    b9 = [int(i) for i in line9.replace('[', '').replace(']', '').split(',')]
    b = [b1, b2, b3, b4, b5, b6, b7, b8, b9]
    print(b)

    puzzle = Sudoku(3, 3, board=b)
    print(puzzle)

    solution = str(puzzle.solve().board).replace(',', '').replace('[', '').replace(']', '').replace(' ', '')

    # Send solution
    print("Løsning: " + solution)
    io.sendline(solution.encode())

# Finished solving all 50 puzzles
print(io.recvuntil(b"Flag: ").decode())
print(io.recvline().decode())
