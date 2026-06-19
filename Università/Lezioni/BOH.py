import matplotlib.pyplot as plt
import numpy as np

parole = [
    "algoritmo",       # 9 lettere
    "re",              # 2 lettere
    "matrice",         # 7 lettere
    "esame",           # 5 lettere
    "nanotecnologia",  # 14 lettere
    "api",             # 3 lettere
    "python",          # 6 lettere
    "sci",             # 3 lettere
    "fotografia",      # 10 lettere
    "voto"             # 4 lettere
]

for i in range(len(parole)):
    for j in range(len(parole)-1):
        if len(parole[j])>len(parole[j+1]):
            parole[j], parole[j+1]=parole[j+1], parole[j]

print(parole)