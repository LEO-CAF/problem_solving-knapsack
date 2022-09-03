import csv

# variabili - input

dati_peso=[]
dati_guadagno=[]
massimo_peso=600 # input
minimo_guadagno=200 # input
combinazioni=['123','124','125','126','134','135','136','145','146','156','234','235','236','245','246','256','345','346','356','456']
selezione_peso=[]
selezione_guadagno=[]
miglior_guadagno=0
miglior_combinazione=0

# lettura .csv

with open("input.csv") as f:
    dati=csv.DictReader(f,delimiter=";")
    for riga in dati:
        dati_guadagno.append(int(riga["guadagno"]))
        dati_peso.append(int(riga["peso"]))

# main

for i in combinazioni:
    if dati_peso[int(i[0])-1]+dati_peso[int(i[1])-1]+dati_peso[int(i[2])-1]<massimo_peso:
        selezione_peso.append(i)

for i in selezione_peso:
    if dati_guadagno[int(i[0])-1]+dati_guadagno[int(i[1])-1]+dati_guadagno[int(i[2])-1]>minimo_guadagno:
        selezione_guadagno.append(i)

for i in selezione_guadagno:
    if dati_guadagno[int(i[0])-1]+dati_guadagno[int(i[1])-1]+dati_guadagno[int(i[2])-1]>miglior_guadagno:
        miglior_combinazione=int(i)
        miglior_guadagno=miglior=dati_guadagno[int(i[0])-1]+dati_guadagno[int(i[1])-1]+dati_guadagno[int(i[2])-1]

# output

print("Miglior Combinazione:",miglior_combinazione)
print("Miglior Guadagno:",miglior_guadagno)
