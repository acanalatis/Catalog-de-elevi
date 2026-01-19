elevi = ["Ana", "Bogdan", "Carmen", "Darius", "Elena"]
note  = [9, 7, 10, 4, 8]

elev_nou = "Felix"
nota_elev_nou = 6
elev_de_sters = "Darius"

interogari_nume = ["Ana", "Mara", "Elena", "stop"]

absente = [1, 0, 2, 3, 0]
print ("              REZOLVARE:")
print("\n -> AFISARE SI PRELUCRARE")
#Partea A, A1
print("\nA1. Elevi cu note:")
for i in range(len(elevi)):
    print (f"{elevi[i]} are nota {note[i]}")

#Partea A, A2
nota_minima = min(note)
nota_maxima = max(note)
elev_min = [elevi[i] for i in range(len(note)) if note[i] == nota_minima]
elev_max = [elevi[i] for i in range(len(note)) if note[i] == nota_maxima]


print(f"\nA2. Nota minima: {nota_minima}, obținuta de: {', '.join(elev_min)}")
print(f"    Nota maxima: {nota_maxima}, obtinuta de: {', '.join(elev_max)}")

#Partea A, A3
media = 1
for nota in note:
    if nota > 0:
        media = (sum(note) // len(note))
print (f" \nA3. Media clasei este: {media}")

#Partea A, A4
print(f"\nA4. Elevi promovati: ")
for i in range(len(elevi)):
    if note[i] > 5:
        print(elevi[i])
        
#Partea B, B5
print ("\n -> ACTUALIZARI")

for i in range(len(note)):
    if note[i] < 10: #nota maxima 10
        nota_actualizata = note[i] + 1
    print(f" Nota după un punct:", note[i],'->', nota_actualizata)

#Partea B, B6
elevi.append(elev_nou)
note.append(nota_elev_nou)
print("\nB6. Lista actualizata: ")
print(" -> Elevi:", elevi)
print(" -> Note :", note)


#Partea B, B7
if elev_de_sters in elevi:
    index = elevi.index(elev_de_sters)
    elevi.pop(index)
    note.pop(index)
    print("\nB7. Lista actualizata: ")
print(" -> Elevi:", elevi)
print(" -> Note :", note)

#Partea B, B8
print(" \nB8. Elevi cu note:")
for i in range(len(elevi)):
    print (f"{elevi[i]} are nota {note[i]}")

#Partea C, C9
print ("\n-> CAUTARI SI STATISTICI")
print ("\nC9.")

index = 0
while index < len(interogari_nume):
    nume = interogari_nume[index]
    if nume == "stop":
        break
    if nume in elevi:
        pozitie = elevi.index(nume)
        print(note[pozitie])
    else:
        print(f"{nume} nu există în catalog")
    index += 1
    
#Partea C, C10
promovati = 0 
respinsi = 0 
for n in note:
    if n < 5:
        respinsi += 1
    if n >= 5:
        promovati += 1
print ("\nC10.", promovati, "elevi au nota cel putin 5")
print ("    ", respinsi, "elevi au nota sub 5")

#Partea C, C11
lista_minim5= []
for nota in note:
    if nota >= 5:
        lista_minim5.append(nota)
print("\nC11.", "Lista elevilor cu note >= 5 este: ", lista_minim5)
medie_noua = 1 
for i in lista_minim5:
    medie_noua = sum(note) // len(note)
print("     Media clasei este: ", medie_noua)














    
    
    
    
    
    
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
