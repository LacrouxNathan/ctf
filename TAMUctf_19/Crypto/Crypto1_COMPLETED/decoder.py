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
