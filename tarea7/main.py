def has_cycle(head):
    """
    :overview
        Necesitamos poder identificar si una lista tiene un ciclo.
    :complexity
        - Time Complexity: O(n) en el peor de los casos tendremos que recorrer todo el arreglo para lograr identificar
        si tiene un ciclo.
        - Space Complexity: O(1) solo usamos dos variables por lo tanto es constante.
    :data structure Linked List
    :link https://www.hackerrank.com/challenges/detect-whether-a-linked-list-contains-a-cycle/problem
    """
    node1 = head
    node2 = head.next
    while node2 is not None and node2.next is not None:
        if node1 == node2:
            return 1
        node1 = node1.next
        node2 = node2.next.next
    return 0


def poisonous_plants(p):
    """
    :overview
        Necesitamos poder identificar la plantas que morirán dependiendo el nivel de pesticida que usamos.
    :complexity
        - Time Complexity: O(n) tenemos que recorrer todo el arreglo para saber si todas las plantas que moriran o
        sobreviviran.
        - Space Complexity: O(n) tenemos una pila la cual agregamos las plantas dependiendo si esta se mas débil o
        no esta puede llegar a ser O(n) en el peor de los casos.
    :data structure Stack
    :link https://www.hackerrank.com/challenges/poisonous-plants
    """
    stack = []
    max_day = 0
    for plant in p:
        day = 0
        while stack and stack[-1][0] >= plant:
            day = max(day, stack.pop()[1])

        if stack:
            day += 1
        else:
            day = 0

        max_day = max(max_day, day)
        stack.append([plant, day])

    return max_day


def minimum_bribes(q):
    """
    :overview
        Se trata de verificar el orden de una fila el cual esta preestablecido pero las personas tiene la opción de
        saltarse dos personas si esta dos lo permiten el problema es que otras personas se estan saltando mas de los
        dos que tiene permitido y debemos de detectar esos casos.
    :complexity
        - Time Complexity: O(n) tenemos que recorrer todo el arreglo para saber si el mismo esta ordenado bajo las
        condiciones que establecimos
        - Space Complexity: O(1) como solo usamos una variable para contar la cantidad de movimientos que hicieron
        las personas su complejidad es constante.
    :data structure Array
    :link https://www.hackerrank.com/challenges/new-year-chaos
    """
    swap = 0
    for i in range(len(q)-1, 0, -1):
        if q[i] != i+1:
            if q[i-1] == i+1:
                swap += 1
                q[i-1], q[i] = q[i], q[i-1]
            elif q[i-2] == i+1:
                swap += 2
                q[i-2], q[i-1], q[i] = q[i-1], q[i], q[i-2]
            else:
                return "Too chaotic"
    return swap
