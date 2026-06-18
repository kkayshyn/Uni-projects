zdanie = input("Podaj zdanie: ") # Funkcja prosząca użytkownika o zdanie

zdanie = zdanie.lower() # Zamiana całego tekstu na małe litery, żeby 'A' i 'a' były traktowane tak samo

samogloski = ['a', 'e', 'i', 'o', 'u', 'y'] # Lista samogłosek, które chcemy zliczać

licznik = {} # Słownik na wyniki, np. {'a': 3, 'e': 1, ...}

for znak in zdanie: # Pętla przechodząca po każdym znaku w zdaniu
    # Jeśli znak jest samogłoską – zliczamy
    if znak in samogloski:
        if znak not in licznik:
            licznik[znak] = 1
        else:
            licznik[znak] += 1


for samogloska, ile in licznik.items():
    print(f"{samogloska}: {ile}") # Wyświetlenie wyników tylko dla samogłosek, które faktycznie wystąpiły