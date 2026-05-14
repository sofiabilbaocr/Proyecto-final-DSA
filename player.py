
'''
Lógica del reproductor de música
'''
 
from double_stack import DoubleStack
 
 
class MusicPlayer:
    def __init__(self):
        self.stack = DoubleStack(20)
        self.current_song = None        #es la canción que está sonando
 
    def __repr__(self) -> str:
        return (
            f'Now playing: {self.current_song}\n'
            f'{self.stack}'
        )
    
    def add_song(self, song: str) -> None:
        #arega una canción al stack de siguientes
        self.stack.push_next(song)