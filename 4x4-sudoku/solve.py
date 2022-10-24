from array import array
from sudoku import Sudoku
from pwn import *

io = connect("ctf.uiactf.no", 5005)

# Puzzles solved so far
count = 0

# Solve 20 puzzles
while (count < 20):
    count = count + 1

    # Wait for the start of the next puzzle
    rec = io.recvuntil(b'[')
    
    # Read every line of the puzzle,
    # every line looks something like this: [0,0,4,2]
    line1 = io.recvline(False).decode()
    line2 = io.recvline(False).decode()
    line3 = io.recvline(False).decode()
    line4 = io.recvline(False).decode()

    # Python way of parsing array strings into int arrays,
    # when the developer doesn't know Python
    b1 = [int(i) for i in line1.replace('[', '').replace(']', '').split(',')]
    b2 = [int(i) for i in line2.replace('[', '').replace(']', '').split(',')]
    b3 = [int(i) for i in line3.replace('[', '').replace(']', '').split(',')]
    b4 = [int(i) for i in line4.replace('[', '').replace(']', '').split(',')]
    b = [b1, b2, b3, b4]
    print(b)

    puzzle = Sudoku(2, 2, board=b)
    #print(puzzle)
    solution = str(puzzle.solve().board).replace(',', '').replace('[', '').replace(']', '').replace(' ', '')

    # Send solution
    print("Løsning: " + solution)
    io.sendline(solution.encode())

# Finished solving all 20 puzzles
print(io.recvuntil(b"Flag: ").decode())
print(io.recvline().decode())
