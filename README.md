# Presupuesto de publicidad: ¿qué algoritmo elegir?

Problema: una empresa tiene 10 mil dólares y tres campañas (video en redes, email marketing y feria local). Cada campaña se contrata completa o no se contrata, y se busca el mayor retorno sin pasarse del presupuesto. Es la mochila 0/1.

## Informe de decisión

**Greedy (Clase 13).** En mi Parte B, greedy ordena por densidad y escoge primero el video en redes (30/6 = 5.0, la más alta). Gasta 6 de los 10 y ya no le alcanza para otra campaña, así que termina con 30. Lo que falla es la propiedad de elección voraz: escoger lo mejor en cada paso no asegura el mejor resultado total, porque cada campaña va completa o no va. La combinación de email marketing y feria local da 40 y greedy nunca la prueba.

**Divide y Vencerás (Clase 14).** Este problema no se puede partir en dos mitades y resolver cada una por separado, porque todas las campañas se pagan del mismo presupuesto. Lo que gasto en una mitad cambia lo que me queda para la otra. Entonces no se cumple la condición de que los subproblemas sean independientes, que es lo que necesita divide y vencerás.

**Programación Dinámica (Clase 15).** En mi tabla, el estado es dp[i][p]: el mejor retorno usando las primeras i campañas con un presupuesto de p. Los subproblemas se superponen porque una misma casilla, por ejemplo dp[i-1][p], se vuelve a usar en varios cálculos; la tabla la guarda y no la calcula de nuevo. En cada casilla decido entre no contratar la campaña i (dp[i-1][p]) o contratarla (su retorno + dp[i-1][p-costo]), y me quedo con la mayor.

**Backtracking (Clase 16).** Lo resolvería probando todos los subconjuntos de campañas, que son 2^n. Con 3 campañas son 8 combinaciones, fácil. Con 30 serían más de mil millones (1.073.741.824), y ahí ya no es viable porque crece exponencialmente. Por eso aquí conviene la programación dinámica.

## Cómo ejecutarlo

    py presupuesto.py