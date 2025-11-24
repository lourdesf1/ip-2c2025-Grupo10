# Contrato: init(vals), step() -> {"a": int, "b": int, "swap": bool, "done": bool}

items = []
n = 0
i = 0
j = 0

def init(vals):
    global items, n, i, j
    items = list(vals)
    n = len(items)
    i = 0
    j = 0

def step():
    # TODO:
    global items, n, i, j
    if i >= n - 1:
        return{"done": True}
    # Elegir índices a y b a comparar en este micro-paso (según tu Bubble).
    a = j
    b = j + 1 #Adyacente del indice, elemento de al lado.
    # Si corresponde, hacer el intercambio real en items[a], items[b] y marcar swap=True.
    if i < n-1:
        if items[a] > items[b]: #Sin ciclos for porque funciona "paso a paso"
            items[a], items[b] = items[b], items[a] #Intercambio de menor a mayor.
            swap = True
        else:
            swap = False

    j += 1 #Aumento el indice

    if j >= n - i - 1: #Si hay que reiniciar el indice
        j = 0
        i += 1
    # Devolver {"a": a, "b": b, "swap": swap, "done": False}.
    return{"a": a, "b": b, "swap": swap, "done": False}
    # Cuando no queden pasos, devolvé {"done": True}.
    if i >= n-1:
        return {"done": True}

