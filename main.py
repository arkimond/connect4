from tablero import Tablero
from agente import Agente

def jugar_partida_humano_agente(agente):
    tablero = Tablero()
    agente_actual = agente if random.choice([True, False]) else "humano"

    while not tablero.tablero_lleno():
        tablero.mostrar()
        print(f"Turno de {agente_actual}")

        if agente_actual == "humano":
            accion = int(input("Elige una columna (0-6): "))
            while not tablero.es_movimiento_valido(accion):
                accion = int(input("Columna no válida. Elige otra (0-6): "))
            jugador = 2
        else:
            accion = agente.elegir_accion(tablero)
            jugador = 1

        tablero.realizar_movimiento(accion, jugador)

        if tablero.hay_ganador(jugador):
            tablero.mostrar()
            print(f"¡El ganador es {agente_actual}!")
            break

        agente_actual = "humano" if agente_actual == agente else agente

    if tablero.tablero_lleno():
        tablero.mostrar()
        print("¡Empate!")

if __name__ == "__main__":
    agente = Agente(1)  # Cargar el agente entrenado aquí
    while True:
        jugar_partida_humano_agente(agente)
        seguir_jugando = input("¿Quieres jugar otra partida? (s/n): ")
        if seguir_jugando.lower() != "s":
            break

