from pwn import *
import re

io = connect("ctf.uiactf.no", 5002)

print(io.recvline().decode())

while (True):
    exp = io.recvline(False).decode()
    
    if (exp.find('=') > -1):
        exp = exp.replace('=', '').replace('?', '')
        if (re.match("[0-9\+\-\*\/].*", exp) != None):
            print(exp)
            answer = eval(exp)
            print(answer)
            io.sendline(f"{answer}")
        else:
            print("Contains illegal chars! exp: " + exp)
    else:
        io.interactive()
