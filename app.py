"""
Aquí Irán todos los endpoints de la aplicación para conectarlo con el frontend
"""
# Importamos librerías

from flask import Flask, jsonify, request, render_template
from player import MusicPlayer

music = [ #Diccionario hardcodeado con las canciones
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
app = Flask(__name__)

# Instancia global del reproductor
player = MusicPlayer()


@app.route('/')
def index():
    return render_template('index.html') #Esto hace que cuando se corra busque en una carpeta templates (Tiene que ser así por defecto) y adentro de ella corra el index.html

@app.route('/status', methods=['GET'])
def get_status():
    # Se agreaga top_prev y top_next para que el JS sepa qué pintar
    return jsonify({
        "current_song": player.current_song,
        "prev_stack": [s for s in player.stack.elements[:player.stack.top_prev + 1] if s is not None],
        "next_stack": [s for s in player.stack.elements[player.stack.top_next:] if s is not None][::-1],
        "raw_array": player.stack.elements,
        "top1_index": player.stack.top_prev,  
        "top2_index": player.stack.top_next  
    })

@app.route('/add', methods=['POST']) #Recibe la petición de añadir una canción al array y lo hace o no
def add_song():
    data = request.json
    song_name = data.get('song')
    if song_name:
        player.add_song(song_name)
        return jsonify({"message": "Canción añadida", "status": "success"})
    return jsonify({"message": "Error", "status": "fail"}), 400

@app.route('/next', methods=['POST']) #Pasa una canción de un lado del array al otro lado
def next_song():
    res = player.play_next()
    return jsonify({"result": res})

@app.route('/prev', methods=['POST']) #Pasa una canción reproducida a reproducirse. botón de canción anterior
def prev_song():
    res = player.play_prev()
    return jsonify({"result": res})

@app.route('/api/library', methods=['GET']) #Para leer las canciones que tenemos (Por si se necesita)
def get_library():
    return jsonify(music)

@app.route('/clear', methods=['POST']) #Para Vaciar el array
def clear_stack():
    player.stack.__init__(20) 
    player.current_song = None
    
    return jsonify({
        "ok": True,
        "message": "Stack vaciado correctamente"
    })

if __name__ == '__main__':
    app.run(debug=True)