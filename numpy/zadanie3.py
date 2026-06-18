import numpy as np

np.random.seed(42)

#dane: 30 dni x 4 lokalizacje
temperatury = np.random.normal(loc=22, scale=5, size=(30, 4))
temperatury = np.round(temperatury, 1)

# ===== STATYSTYKI PRZED KOREKTĄ =====

srednie_lokalizacje = np.mean(temperatury, axis=0)#średnia temperatura dla każdej lokalizacji

srednie_dni = np.mean(temperatury, axis=1)
dzien_max = np.argmax(srednie_dni)
temp_max = srednie_dni[dzien_max] #dzień z najwyższą średnią temperaturą

mask_odstajace = (temperatury < 10) | (temperatury > 35)
liczba_odstajacych = np.sum(mask_odstajace)#maski wartości odstających

srednia_globalna_przed = np.mean(temperatury)
std_globalne_przed = np.std(temperatury)#statystyki globalne przed korektą

print("STATYSTYKI PRZED KOREKTĄ")
print("Średnie temperatury w lokalizacjach:",
      np.round(srednie_lokalizacje, 1).tolist())
print(f"Dzień z najwyższą średnią temperaturą: {dzien_max + 1} "
      f"({temp_max:.1f}°C)")
print(f"Liczba wartości odstających: {liczba_odstajacych}")

# ===== KOREKTA DANYCH =====

temperatury_korekta = temperatury.copy()

for i in range(temperatury.shape[1]):
    mediana = np.median(temperatury[:, i])
    temperatury_korekta[mask_odstajace[:, i], i] = mediana

srednia_globalna_po = np.mean(temperatury_korekta)
std_globalne_po = np.std(temperatury_korekta)#statystyki globalne po korekcie

print("\nSTATYSTYKI PO KOREKCIE")
print(f"Średnia globalna: {srednia_globalna_przed:.2f}°C -> {srednia_globalna_po:.2f}°C")
print(f"Odchylenie standardowe: {std_globalne_przed:.2f}°C -> {std_globalne_po:.2f}°C")