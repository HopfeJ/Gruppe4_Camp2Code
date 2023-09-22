import numpy as np

# Beispiel-NumPy-Array
arr = np.array([[-1, 1], [-2, 2], [3, -3], [4, -4]])

# Extrahieren Sie die Wertepaare, bei denen der erste Wert negativ ist
filtered_arr = arr[arr[:, 0] < 0]

# Drucken Sie das Ergebnis
print(filtered_arr)
