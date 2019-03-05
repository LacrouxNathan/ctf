#HowDyApp

C'est juste un apk

## SmartPhone side

L'application est juste un cliker, quand on clique sur l'icone le chiffre augmente

## apktool side

Grace à apktool on peut "dePacketer" le .apk afin d'observer tous les xml
les .java reste compilé donc quasi illisible

**On peut observer dans les resources du jeux le flag présent dans "/res/values/strings.xml"**
Il est encode en base 64 donc il suffit de le decoder

Ce qui nous donne **gigem{infinite_gigems}**


