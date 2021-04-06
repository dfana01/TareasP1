"""
Tarea 13
• Crear un programa que dada una expresión aritmética como entrada, pueda retornar la representación en notación
polaca (Polish Notation), notación polaca inversa (Reverse Polish Notation) ó notación de infijo.
• Se pueden usar paréntesis y/o corchetes para determinar el orden de las operaciones aritméticas.
• Las operaciones aritméticas permitidas son */+-
• Incluir unit test
• Utilizar árboles y sus recorridos
"""


def is_operator(s):
    if s in ["*", "/", "+", "-"]:
        return True
    else:
        return False


def is_number(s):
    return False


def tokenize(s):
    operands = []
    stack = []
    for i in s:
        print(i)


def main():
    print(tokenize("(3 + 4)"))
    print(tokenize("6 * (3 + 4)"))
