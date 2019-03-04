# STEM CTF: Cyber Challenge 2019

*ven, 22 fév. 2019, 19:00 GMT — sam, 23 fév. 2019, 19:00 GMT*

Team rating points : **1,349**

## In Plain Text (50)

Une fois avoir extrait les fichiers téléchargés, on peut observer un executable binary

### Exploration simple

En l'ouvrant avec cat on s'aperçoit que quelque mot sont visible

J'ai donc essayé

```bash
$ strings challenge
```

On peut observer la phrase "Could you just tell me the flag real quick ?"

En dessous le flag

**MCA{y3ah___sur3___here___y0u___g0}**

## Nomination (100)

le fichier telecharge est une image.

Une premiere partie du code est en haut à gauche **MCA{g1jVx4a**

La deuxieme partie devient visible avec un filtre monochrome ce qui donne le flag suivant :

**MCA{g1jVx4a2zcpoZx2q}**
