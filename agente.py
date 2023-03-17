import random
import json

class Agente:
    def __init__(self, turno, alfa=0.5, gamma=0.9, epsilon=0.1, epsilon_decay=0.999):
        self.turno = turno
        self.alfa = alfa
        self.gamma = gamma
        self.epsilon = epsilon
        self.epsilon_decay = epsilon_decay
        self.tabla_q = {}

    def obtener_estado(self, tablero):
        return tuple(tuple(fila) for fila in tablero.tablero)

    def obtener_acciones_validas(self, tablero):
        acciones_validas = []
        for columna in range(tablero.columnas):
            if tablero.es_movimiento_valido(columna):
                acciones_validas.append(columna)
        return acciones_validas

    def elegir_accion(self, tablero):
        if random.uniform(0, 1) < self.epsilon:
            return random.choice(self.obtener_acciones_validas(tablero))

        estado = self.obtener_estado(tablero)
        acciones_validas = self.obtener_acciones_validas(tablero)
        max_q = float("-inf")
        mejor_accion = None

        for accion in acciones_validas:
            q = self.tabla_q.get((estado, accion), 0)
            if q > max_q:
                max_q = q
                mejor_accion = accion

        return mejor_accion

    def actualizar_q(self, estado, accion, recompensa, siguiente_estado):
        q_actual = self.tabla_q.get((estado, accion), 0)
        max_q_siguiente = max([self.tabla_q.get((siguiente_estado, a), 0) for a in range(7)])

        self.tabla_q[(estado, accion)] = q_actual + self.alfa * (
            recompensa + self.gamma * max_q_siguiente - q_actual
        )

    def guardar_tabla_q(self, archivo):
        with open(archivo, "w") as f:
            json.dump(self.tabla_q, f)

    def cargar_tabla_q(self, archivo):
        with open(archivo, "r") as f:
            self.tabla_q = json.load(f)