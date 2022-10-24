from pwn import *

io = connect("ctf.uiactf.no", 5001)

print(io.recvline().decode())

while (True):
    exp = io.recvline(False).decode()
    print(exp)
    if (exp.find('+') > -1):
        parts = exp.split('=')
        parts = parts[0].split('+')
        answer = f"{int(parts[0]) + int(parts[1])}"
        print(answer)
        io.sendline(answer.encode())
    else:
        io.interactive()
