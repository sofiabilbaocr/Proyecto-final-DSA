'''
Implementación del double stack
2 stacks que comparten un array de tamaño fijo que crece en lados opuestos
'''


class DoubleStack:
    def __init__(self, size: int):
        self.elements = [None] * size
        self.size = size
        self.top_prev = -1          # Stack izquierdo: canciones anteriores
        self.top_next = size        # Stack derecho: canciones siguientes
