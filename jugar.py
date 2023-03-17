from tablero import Tablero
from agente import Agente
import random

def jugar_humano_vs_ia(agente_ia):
    tablero = Tablero()
    turno_humano = 1
    turno_ia = -1
    tablero.turno_actual = turno_humano if random.choice([True, False]) else turno_ia

    while not tablero.tablero_lleno():
        tablero.mostrar_tablero()

        if tablero.turno_actual == turno_humano:
            accion = int(input("Introduce la columna (0-6) en la que deseas colocar tu ficha: "))
            if tablero.es_movimiento_valido(accion):
                tablero.realizar_movimiento(accion, tablero.turno_actual)
                if tablero.hay_ganador(tablero.turno_actual):
                    print("¡Has ganado!")
                    break
                tablero.turno_actual = turno_ia
        else:
            accion = agente_ia.elegir_accion(tablero)
            tablero.realizar_movimiento(accion, tablero.turno_actual)
            if tablero.hay_ganador(tablero.turno_actual):
                print("La IA ha ganado.")
                break
            tablero.turno_actual = turno_humano

    if not tablero.hay_ganador(tablero.turno_actual):
        print("Empate.")

if __name__ == "__main__":
    agente_entrenado = Agente(2)  # Crea una nueva instancia del agente con el turno 2 (IA)
    agente_entrenado.cargar_tabla_q("tabla_q_agente1.json")  # Carga la tabla Q guardada
    jugar_humano_vs_ia(agente_entrenado)
