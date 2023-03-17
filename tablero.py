class Tablero:
    def __init__(self, filas=6, columnas=7):
        self.filas = filas
        self.columnas = columnas
        self.tablero = [[0 for _ in range(columnas)] for _ in range(filas)]
        self.turno_actual = 1  # 1 para el humano y -1 para la IA

    def cambiar_turno(self):
        self.turno_actual = -self.turno_actual

    def realizar_movimiento(self, columna, jugador):
        for fila in range(self.filas - 1, -1, -1):
            if self.tablero[fila][columna] == 0:
                self.tablero[fila][columna] = jugador
                return True
        return False

    def es_movimiento_valido(self, columna):
        return self.tablero[0][columna] == 0

    def hay_ganador(self, jugador):
        for fila in range(self.filas):
            for columna in range(self.columnas):
                if self.tablero[fila][columna] == jugador:
                    if self.verificar_ganador(fila, columna, jugador):
                        return True
        return False

    def verificar_ganador(self, fila, columna, jugador):
        direcciones = [(1, 0), (0, 1), (1, 1), (-1, 1)]
        for dx, dy in direcciones:
            contador = 0
            for i in range(4):
                x, y = fila + i * dx, columna + i * dy
                if (
                    0 <= x < self.filas
                    and 0 <= y < self.columnas
                    and self.tablero[x][y] == jugador
                ):
                    contador += 1
            if contador == 4:
                return True
        return False

    def tablero_lleno(self):
        for columna in range(self.columnas):
            if self.es_movimiento_valido(columna):
                return False
        return True

    def reiniciar(self):
        for fila in range(self.filas):
            for columna in range(self.columnas):
                self.tablero[fila][columna] = 0

    def mostrar_tablero(self):
        for fila in self.tablero:
            print(" | ".join(map(str, fila)))
            print("-" * (4 * len(fila) - 1))