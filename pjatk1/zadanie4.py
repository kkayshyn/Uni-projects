with open("dane.txt", "r", encoding="utf-8") as f:
    slowa = [linia.strip() for linia in f] # Wczytanie słów z pliku

slownik = {} # Tworzenie słownika

for s in slowa:
    dl = len(s)
    slownik.setdefault(dl, []).append(s)

for lista in slownik.values():
    lista.sort() # Sortowanie słów w każdej grupie

with open("wynik.txt", "w", encoding="utf-8") as f:
    for dlugosc in sorted(slownik.keys()):
        grupa = ", ".join(slownik[dlugosc])
        f.write(f"Długość {dlugosc}: {grupa}\n") # Zapis do pliku wynikowego