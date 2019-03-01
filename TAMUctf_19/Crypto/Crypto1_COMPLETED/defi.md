# -.-

Le fichier flag.txt contient plein de "di" "dit" et "dah"

## Du morse

Appres quelques recherches c'est du morse

en fait : 

* "di" et "dit" => "."
* "dah"		=> "-"

plus qu'a traduire le tout

## Script python

```Python
fichier = open("flag.txt", "r")
data = fichier.read()
fichier.close()
data = data.replace("-","")
data = data.replace("dit",".")
data = data.replace("di",".")
data = data.replace("dah","-")

retour = open("retour.txt", "w")
retour.write(data)
retour.close()

print "done"
```

Voila on obtient "retour.txt" qui contient la traduction en morse traditionel

## Du morse au texte

Grace a [ce site](http://www.unit-conversion.info/texttools/morse-code/) j'ai
pu traduire du morse en texte

## Putain c'est de l'hexa

En fait apres 1h de recherche j'ai enfin compris que c'est de l'hexadecimal.
il faut le traduire et hop le flag

*gigem{C1icK_cl1CK-y0u_h4v3_m4I1}*
