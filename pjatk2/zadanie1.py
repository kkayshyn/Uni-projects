import numpy as np

def znajdz_wartosci(tablica, prog):
    maska = tablica > prog #tworzenie maski elementów większych od progu
    
    liczba = np.sum(maska) #liczba elementów
    
    srednia = tablica[maska].mean() if liczba > 0 else 0 #utworzenie średniej (zabezpieczenie na wypadek braku elementów)
    
    pozycje = list(zip(*np.where(maska))) #pozycje jako lista krotek (wiersz, kolumna)
    
    return liczba, srednia, pozycje

tablica = np.arange(1, 101).reshape(10, 10)

liczba, srednia, pozycje = znajdz_wartosci(tablica, 75)

print(f"Liczba elementów > 75: {liczba}")
print(f"Średnia wartość: {srednia:.2f}")
print(f"Pierwsze 5 pozycji: {pozycje[:5]}")