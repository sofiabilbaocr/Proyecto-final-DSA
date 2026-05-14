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

    def __repr__(self) -> str:
        return (
            f'Previous stack: {self.elements[:self.top_prev + 1]} | '
            f'TOP_PREV: {self.top_prev}\n'
            f'Next stack:     {self.elements[self.top_next:]} | '
            f'TOP_NEXT: {self.top_next}'
        )
