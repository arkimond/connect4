import random
from tablero import Tablero
from agente import Agente

def jugar_partida(agente1, agente2):
    tablero = Tablero()
    agente_actual = agente1 if random.choice([True, False]) else agente2

    while not tablero.tablero_lleno():
        accion = agente_actual.elegir_accion(tablero)
        tablero.realizar_movimiento(accion, agente_actual.turno)

        if tablero.hay_ganador(agente_actual.turno):
            return agente_actual.turno

        agente_actual = agente1 if agente_actual == agente2 else agente2

    return 0

def entrenar_agentes(agente1, agente2, num_partidas):
    ganadas = 0
    perdidas = 0
    empates = 0

    for i in range(num_partidas):
        resultado = jugar_partida(agente1, agente2)

        if resultado == 1:
            ganadas += 1
        elif resultado == -1:
            perdidas += 1
        else:
            empates += 1

        if (i + 1) % 1000 == 0:
            print(f"Partida {i + 1} de {num_partidas}")

    with open("resultados_entrenamiento.txt", "w") as f:
        f.write(f"Ganadas: {ganadas}\n")
        f.write(f"Perdidas: {perdidas}\n")
        f.write(f"Empates: {empates}\n")

    agente1.guardar_tabla_q("tabla_q_agente1.json")

    print(f"\nResultados del entrenamiento (Agente 1 vs Agente 2):")
    print(f"Ganadas: {ganadas}")
    print(f"Perdidas: {perdidas}")
    print(f"Empates: {empates}")

if __name__ == "__main__":
    agente1 = Agente(1)
    agente2 = Agente(2)

    num_partidas = 1000000
    entrenar_agentes(agente1, agente2, num_partidas)
