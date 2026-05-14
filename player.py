
'''
Lógica del reproductor de música
'''
 
from double_stack import DoubleStack
 
 
class MusicPlayer:
    def __init__(self):
        self.stack = DoubleStack(20)  #tamaño del stack o sea maximo de canciones del reproductor
        self.current_song = None        #es la canción que está sonando
 
    def __repr__(self) -> str:
        return (
            f'Now playing: {self.current_song}\n'
            f'{self.stack}'
        )
    
    def add_song(self, song: str) -> None:
        #arega una canción al stack de siguientes
        self.stack.push_next(song)


    def play_next(self) -> str:
        #verifica que haya una canción siguiente
        if self.stack.top_next == self.stack.size:
            return 'No hay canciones siguientes.'
        
    #l canción actual pasa al stack de anteriores
        if self.current_song is not None:
            self.stack.push_prev(self.current_song)