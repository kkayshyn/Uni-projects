import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
# Wczytanie zepsutego obrazu
obraz_zepsuty = Image.open('santa_zepsuty.jpg')
obraz_array = np.array(obraz_zepsuty)
print("ANALIZA ZEPSUTEGO OBRAZKA")
print(f"Kształt tablicy: {obraz_array.shape}")
print(f"\nŚrednie wartości kanałów:")
print(f" Kanał 0 (R): {obraz_array[:,:,0].mean():.2f}")
print(f" Kanał 1 (G): {obraz_array[:,:,1].mean():.2f}")
print(f" Kanał 2 (B): {obraz_array[:,:,2].mean():.2f}")

obraz_naprawiony = obraz_array.copy()
srednie = [
    obraz_array[:, :, 0].mean(),  #R
    obraz_array[:, :, 1].mean(),  #G
    obraz_array[:, :, 2].mean()   #B
] #wykrycie zepsutego kanału

kanal_zepsuty = np.argmax(srednie)
print(f"\nZepsuty kanał: {kanal_zepsuty} (0=R, 1=G, 2=B)")

kanaly_poprawne = [i for i in range(3) if i != kanal_zepsuty]
wartosc_docelowa = np.mean([srednie[i] for i in kanaly_poprawne]) #wartość referencyjna

wspolczynnik = wartosc_docelowa / srednie[kanal_zepsuty]
print(f"Współczynnik skalowania: {wspolczynnik:.3f}")#naprawa kanału

obraz_naprawiony[:, :, kanal_zepsuty] = np.clip(
    obraz_array[:, :, kanal_zepsuty] * wspolczynnik,
    0, 255
).astype(np.uint8)

# Wyświetlenie wyników
fig, axes = plt.subplots(1, 2, figsize=(12, 5))
axes[0].imshow(obraz_array)
axes[0].set_title('Zepsuty obraz')
axes[0].axis('off')
axes[1].imshow(obraz_naprawiony)
axes[1].set_title('Naprawiony obraz')
axes[1].axis('off')
plt.tight_layout()
plt.show()