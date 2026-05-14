"""
Aquí Irán todos los endpoints de la aplicación para conectarlo con el frontend
"""
# Importamos librerías

from flask import Flask, jsonify, request, render_template
from player import MusicPlayer

music = [
    {"id": 1, "nombre": "Beauty And A Beat", "artista": "Justin Bieber ft. Nicki Minaj", "duracion": "3:48"},
    {"id": 2, "nombre": "Swim", "artista": "BTS", "duracion": "2:39"},
    {"id": 3, "nombre": "Drop Dead", "artista": "Olivia Rodrigo", "duracion": "3:44"},
    {"id": 4, "nombre": "The Fate of Ophelia", "artista": "Taylor Swift", "duracion": "3:55"},
    {"id": 5, "nombre": "Dracula", "artista": "Tame Impala & JENNIE", "duracion": "3:25"},
    {"id": 6, "nombre": "Choosin' Texas", "artista": "Ella Langley", "duracion": "3:52"},
    {"id": 7, "nombre": "I Just Might", "artista": "Bruno Mars", "duracion": "3:32"},
    {"id": 8, "nombre": "Stateside", "artista": "PinkPantheress & Zara Larsson", "duracion": "3:04"},
    {"id": 9, "nombre": "DTMF", "artista": "Bad Bunny", "duracion": "3:57"},
    {"id": 10, "nombre": "Man I Need", "artista": "Olivia Dean", "duracion": "3:04"},
    {"id": 11, "nombre": "Ordinary", "artista": "Alex Warren", "duracion": "3:06"},
    {"id": 12, "nombre": "Daisies", "artista": "Justin Bieber", "duracion": "2:56"},
    {"id": 13, "nombre": "Golden", "artista": "HUNTR/X", "duracion": "3:14"},
    {"id": 14, "nombre": "Where Is My Husband!", "artista": "RAYE", "duracion": "3:17"},
    {"id": 15, "nombre": "Lush Life", "artista": "Zara Larsson", "duracion": "3:20"},
    {"id": 16, "nombre": "Back To Friends", "artista": "sombr", "duracion": "3:19"},
    {"id": 17, "nombre": "End Of Beginning", "artista": "Djo", "duracion": "2:39"},
    {"id": 18, "nombre": "Risk It All", "artista": "Bruno Mars", "duracion": "3:24"},
    {"id": 19, "nombre": "Aperture", "artista": "Harry Styles", "duracion": "3:15"},
    {"id": 20, "nombre": "Billie Jean", "artista": "Michael Jackson", "duracion": "4:54"}
]