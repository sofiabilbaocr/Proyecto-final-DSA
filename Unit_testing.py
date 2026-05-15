"""
Unit Testing con 10 escenarios
"""

import unittest
from player import MusicPlayer

import unittest

class TestMusicPlayer(unittest.TestCase):

    def setUp(self):
        self.player = MusicPlayer()

    # 1. El reproductor inicia vacío
    def test_start_empty(self):
        self.assertIsNone(self.player.current_song)

    # 2. Agregar una canción aumenta el stack de "Siguientes"
    def test_add_song(self):
        self.player.add_song("Song 1")
        self.assertEqual(self.player.peek_next(), "Song 1")

    # 3. Al darle 'Next', la canción se vuelve la actual
    def test_play_next_basic(self):
        self.player.add_song("Song 1")
        self.player.play_next()
        self.assertEqual(self.player.current_song, "Song 1")

    # 4. 'Next' cuando no hay canciones devuelve el mensaje de error
    def test_next_empty(self):
        res = self.player.play_next()
        self.assertEqual(res, 'No hay canciones siguientes.')

    # 5. 'Prev' cuando no hay canciones devuelve el mensaje de error
    def test_prev_empty(self):
        res = self.player.play_prev()
        self.assertEqual(res, 'No hay canciones anteriores.')

    # 6. Al pasar de canción, la anterior se guarda en el stack izquierdo
    def test_history_flow(self):
        self.player.add_song("Song 1")
        self.player.add_song("Song 2")
        self.player.play_next() 
        self.player.play_next() 
        self.assertEqual(self.player.peek_prev(), "Song 2")

    # 7. Regresar a la canción anterior funciona correctamente
    def test_return_to_previous(self):
        self.player.add_song("A")
        self.player.add_song("B")
        self.player.play_next() 
        self.player.play_next() 
        self.player.play_prev() 
        self.assertEqual(self.player.current_song, "B")

    # 8. El stack tiene un límite (Overflow)
    def test_stack_full(self):
        for i in range(20):
            self.player.add_song(f"S{i}")
        # El puntero top_next debe estar en 0 (ya no puede bajar más)
        self.assertEqual(self.player.stack.top_next, 0)

    # 9. Ver que el arreglo se limpie (No deja basura al hacer pop)
    def test_clean_memory(self):
        self.player.add_song("Limpieza")
        self.player.play_next()
        # El espacio 19 (donde estaba la canción) debe ser None ahora
        self.assertIsNone(self.player.stack.elements[19])

    # 10. Peek no altera el estado del reproductor
    def test_peek_no_changes(self):
        self.player.add_song("Stay")
        self.player.peek_next()
        # Después de un peek, la canción debe seguir en el stack, no en el reproductor
        self.assertIsNone(self.player.current_song)
        self.assertEqual(self.player.peek_next(), "Stay")

if __name__ == "__main__":
    unittest.main()