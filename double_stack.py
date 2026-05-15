'''
Implementación del double stack
2 stacks que comparten un array de tamaño fijo que crece en lados opuestos
'''


class DoubleStack:
    def __init__(self, size: int):
        self.elements = [None] * size
        self.size = size
        self.top_prev = -1          #stack izquierdo: canciones anteriores
        self.top_next = size        #stack derecho: canciones siguientes

    def __repr__(self) -> str:
        return (
            f'Previous stack: {self.elements[:self.top_prev + 1]} | '
            f'TOP_PREV: {self.top_prev}\n'
            f'Next stack:     {self.elements[self.top_next:]} | '
            f'TOP_NEXT: {self.top_next}'
        )


    #stack izquierdo: canciones anteriores
 
    def push_prev(self, song: str) -> None:
        # Si los dos tops se tocan, el array está lleno
        if self.top_prev + 1 == self.top_next:
            print('Stack Overflow: no hay espacio disponible.')
            return None
        self.top_prev += 1
        self.elements[self.top_prev] = song
 
    def pop_prev(self) -> str:
        #top_prev en -1 es que no hay canciones anteriores
        if self.top_prev == -1:
            return 'Stack Underflow: no hay canciones anteriores.'
        song = self.elements[self.top_prev]
        self.elements[self.top_prev] = None
        self.top_prev -= 1
        return song
 
    def peek_prev(self) -> str:
        #solo mira la mas arriba no saca la canción del stack
        if self.top_prev == -1:
            return 'Stack Underflow: no hay canciones anteriores.'
        return self.elements[self.top_prev]
 

    #stack derecho: canciones siguientes
 
    def push_next(self, song: str) -> None:
        # Si los dos tops se tocan, el array está lleno
        if self.top_prev + 1 == self.top_next:
            print('Stack Overflow: ya no se pueden añadir más cancioens')
            return None
        self.top_next -= 1
        self.elements[self.top_next] = song
 
    def pop_next(self) -> str:
        # top_next en self.size significa que no hay canciones siguientes
        if self.top_next == self.size:
            return 'Stack Underflow: no hay canciones siguientes.'
        song = self.elements[self.top_next]
        self.elements[self.top_next] = None
        self.top_next += 1
        return song
 
    def peek_next(self) -> str:
        #mira la mas arriba, no saca la canción del stack
        if self.top_next == self.size:
            return 'Stack Underflow: no hay canciones siguientes.'
        return self.elements[self.top_next]