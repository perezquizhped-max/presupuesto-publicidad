def mejor_inversion(campanas, presupuesto):
    """Mochila 0/1 con programación dinámica.
    campanas: lista de tuplas (nombre, costo, retorno)
    Devuelve (retorno_maximo, lista_de_campanas_elegidas)
    """
    n = len(campanas)

    # dp[i][p] = retorno máximo usando las primeras i campañas con presupuesto p
    dp = [[0] * (presupuesto + 1) for _ in range(n + 1)]

    # Construcción de la tabla: cada casilla decide incluir o excluir la campaña i
    for i in range(1, n + 1):
        nombre, costo, retorno = campanas[i - 1]
        for p in range(presupuesto + 1):
            if costo <= p:
                # Opción 1: no contratarla -> dp[i-1][p]
                # Opción 2: contratarla -> retorno + lo mejor con el presupuesto que sobra
                dp[i][p] = max(dp[i - 1][p], retorno + dp[i - 1][p - costo])
            else:
                # No alcanza el presupuesto, no se puede contratar
                dp[i][p] = dp[i - 1][p]

    # Reconstrucción: recorremos la tabla hacia atrás
    elegidas = []
    p = presupuesto
    for i in range(n, 0, -1):
        # Si el valor cambió respecto a la fila anterior, la campaña i sí se contrató
        if dp[i][p] != dp[i - 1][p]:
            nombre, costo, retorno = campanas[i - 1]
            elegidas.append(nombre)
            p -= costo  # restamos su costo del presupuesto que queda

    elegidas.reverse()  # las encontramos al revés, las ordenamos
    return dp[n][presupuesto], elegidas


def inversion_greedy(campanas, presupuesto):
    """Greedy: ordena por densidad (retorno/costo) y contrata mientras alcance."""
    ordenadas = sorted(campanas, key=lambda c: c[2] / c[1], reverse=True)
    total = 0
    elegidas = []
    restante = presupuesto
    for nombre, costo, retorno in ordenadas:
        if costo <= restante:      # si todavía alcanza, la contratamos
            elegidas.append(nombre)
            total += retorno
            restante -= costo
    return total, elegidas


if __name__ == "__main__":
    campanas = [
        ("video en redes", 6, 30),    # (nombre, costo, retorno) en miles de dólares
        ("email marketing", 5, 20),
        ("feria local", 5, 20),
    ]
    presupuesto = 10

    retorno_pd, elegidas_pd = mejor_inversion(campanas, presupuesto)
    retorno_gr, elegidas_gr = inversion_greedy(campanas, presupuesto)

    print("Comparación de métodos (miles de dólares)")
    print("-" * 45)
    print("Programación dinámica")
    print(f"  Retorno máximo: {retorno_pd}")
    print(f"  Campañas elegidas: {', '.join(elegidas_pd)}")
    print("Greedy (por densidad retorno/costo)")
    print(f"  Retorno obtenido: {retorno_gr}")
    print(f"  Campañas elegidas: {', '.join(elegidas_gr)}")
    print("-" * 45)
    print(f"Diferencia a favor de programación dinámica: {retorno_pd - retorno_gr}")