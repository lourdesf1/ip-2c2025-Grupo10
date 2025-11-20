# Template genérico — SKELETON
# Contrato: init(vals), step() -> {"a": int, "b": int, "swap": bool, "done": bool}

items = []
n = 0
i = 0# Agregá acá tus punteros/estado, p.ej.: i = 0; j = 0; fase = "x"; stack = []
j = 0
fase = "x"
stack = []

def init(vals):
    global items, n
    items = list(vals)
    n = len(items)
    # TODO: inicializar punteros/estado
    i = 0
    j = 0

def step():
    # TODO: implementar UN micro-paso de tu algoritmo y devolver el dict.
    global items, n, i, j
    if i >= n-1:
        return{"done": True}
    # Recordá:
    a = j
    b = j + 1 
    swap = "False"
    # - a, b dentro de [0, n-1]
    # - si swap=True, primero hacé el intercambio en 'items'
    if items[a] > items[b]:
        items[a], items[b] = items[b], items[a]
        swap = "True"

    j += 1
    if j >= n - 1 - i:
        j = 0
        i += 1
        return{"a": a, "b": b, "swap": swap, "done": False}
    # - cuando termines, devolvé {"done": True}
    return {"done": True}
