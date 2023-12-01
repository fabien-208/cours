#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
programme qui génére un ficher audio au  format wav.
"""


wav_spec = [
      ("FileTypeBlocID", 4),# Constante « RIFF »  (0x52,0x49,0x46,0x46)
      ("FileSize", 4),      # Taille du fichier moins 8 octets
      ("FileFormatID", 4),  # Format = « WAVE »  (0x57,0x41,0x56,0x45)
      ("FormatBlocID", 4),  # Identifiant « fmt␣ »  (0x66,0x6D, 0x74,0x20)
      ("BlocSize", 4),      # Nombre d'octets du bloc - 16  (0x10)
      ("AudioFormat", 2),   # Format du stockage dans le fichier (1: PCM, ...)
      ("NbrCanaux", 2),     # Nombre de canaux (de 1 à 6, cf. ci-dessous)
      ("Frequence", 4),     # Fréquence d'échantillonnage (en hertz) [Valeurs standardisées : 11 025, 22 050, 44 100 et éventuellement 48 000 et 96 000]
      ("BytePerSec", 4),    # Nombre d'octets à lire par seconde (c.-à-d., Frequence * BytePerBloc).
      ("BytePerBloc", 2),   # Nombre d'octets par bloc d'échantillonnage (c.-à-d., tous canaux confondus : NbrCanaux * BitsPerSample/8).
      ("BitsPerSample", 2), # Nombre de bits utilisés pour le codage de chaque échantillon (8, 16, 24)
      ("DataBlocID", 4),    # Constante « data »  (0x64,0x61,0x74,0x61)
      ("DataSize", 4),      # Nombre d'octets des données (c.-à-d. "Data[]", c.-à-d. taille_du_fichier - t
         ]

def ouvrir_fichier_wav(fichier):
    """
    permet d'extraire le contenu d'un fichier wav
    """
    
    with open(fichier) as data:
        data = fichier.read()
    return data


def analyse_data_wav(data: bytes)->None:
    """
    prermet d'extraire les spécifités d'un fichier wav
    """
    pointeur = 0
    taille = len(wav_spec)
    for indice in range(taille):
        (nom, longeur)= wav_spec(indice)
        valeur = ""
        for nb_octet in range(longeur):
            valeur+=data(pointeur)
            pointeur +=1
        print(nom, longeur, "->", valeur)
