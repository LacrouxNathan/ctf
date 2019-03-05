# Snake Over Cheese

Le fichier fournis est une fichier python 2.7 : 

```bash
$ file reversing2.pyc
```
Strings ne donne rien de particulier, il faut donc le décompiler

## Uncompyle 2

Un voit que le script demmande une chaine de charactere et si elle est egale
a celle rentre, le flag apparait.

Il suffit de rentrer le tableau de valeur et faire ce que fait le prog
On trouve le message secret "SuperSecretKey"

```python
XidT = [83,117,112,101,114,83,101,99,114,101,116,75,101,121]
for i in XidT:
	ku += chr(i)
print XidT
```

On rentre le code dans le prog et le flag apparait

**flag{decompile}**
