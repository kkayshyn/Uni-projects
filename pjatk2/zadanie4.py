import numpy as np

def normalizacja_minmax(dane):
    xmin = np.min(dane, axis=0)
    xmax = np.max(dane, axis=0)
    return (dane - xmin) / (xmax - xmin)

def standaryzacja_zscore(dane):
    mean = np.mean(dane, axis=0)
    std = np.std(dane, axis=0)
    return (dane - mean) / std

np.random.seed(0)

#dane: 100 pomiarów x 3 cechy
dane = np.random.rand(100, 3)
dane[:, 0] = dane[:, 0] * 50 + 50   #masa [kg]
dane[:, 1] = dane[:, 1] * 15 + 15   #temperatura [°C]
dane[:, 2] = dane[:, 2] * 50 + 980  #ciśnienie [hPa]

dane_norm = normalizacja_minmax(dane)
dane_std = standaryzacja_zscore(dane)#zastosowanie normalizacji i standaryzacji

def statystyki(nazwa, dane):
    print(f"\n{nazwa}")
    print("Średnia:", np.mean(dane, axis=0))
    print("Min:    ", np.min(dane, axis=0))
    print("Max:    ", np.max(dane, axis=0))
    print("Std:    ", np.std(dane, axis=0))#funkcja do wyświetlania statystyk
    
statystyki("Dane oryginalne", dane)
statystyki("Dane po normalizacji (min-max)", dane_norm)
statystyki("Dane po standaryzacji (z-score)", dane_std)