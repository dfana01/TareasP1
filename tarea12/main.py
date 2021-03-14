pre_calculated_results = dict()


def fibonacci(n):
    """
    :complexity
         :space: O(n), porque usamos un diccionario que almacenaras todas las llamadas del numero que hacemos
         :time: O(n), fibonnaci recursivo normal cuenta con una complejidad de O(n^2) dado que recorre todo los arboles,
         pero en este caso la complejidad baja por la memoizacion donde usamos un diccionario el cual permite que el recorrido
         sea n pues solo genera un numero una vez y despues solo lo saca del diccionario donde la complejidad es O(1)
    """
    if n <= 1:
        return n

    if n in pre_calculated_results:
        return pre_calculated_results[n]

    pre_calculated_results[n] = fibonacci(n - 1) + fibonacci(n - 2)

    return pre_calculated_results[n]
