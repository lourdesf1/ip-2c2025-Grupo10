# Contrato: init(vals), step() -> {"a": int, "b": int, "swap": bool, "done": bool}

items = []
n = 0
i = 0          # cabeza de la parte no ordenada
j = 0          # cursor que recorre y busca el mínimo
min_idx = 0    # índice del mínimo de la pasada actual
fase = "buscar"  # "buscar" | "swap"

def init(vals):
    global items, n, i, j, min_idx, fase
    items = list(vals)
    n = len(items)
    i = 0
    j = i + 1
    min_idx = i
    fase = "buscar"

def step():
    # TODO:
    global items, n, i, j, min_idx, fase
    if i >= n - 1:
        return{"done": True} 
    if fase == "buscar":# - Fase "buscar": comparar j con min_idx, actualizar min_idx, avanzar j.
        j_actual = j
        j += 1
    if items[j] < items[min_idx]:
        min_idx = j
        j += 1    
        return{"a": min_idx, "b": j_actual, "swap": False, "done": True}  # Devolver {"a": min_idx, "b": j_actual, "swap": False, "done": False}.

    #   Al terminar el barrido, pasar a fase "swap".
    fase = "buscar"  #Al terminar el barrido, pasar a fase "swap".
    if fase == "swap":# -Fase "swap": si min_idx != i, hacer ese único swap y devolverlo.
        if min_idx != i:# -Fase "swap": si min_idx != i, hacer ese único swap y devolverlo.
            items[i], items[min_idx] = items[min_idx], items[i]
            swap_info = {"a": i, "b": min_idx, "swap": True, "done": False}
        else:
            swap_info = {"a": i, "b": min_idx, "swap": False, "done": True}

    i = i + 1 #Luego avanzar i, reiniciar j=i+1 y min_idx=i, volver a "buscar".
    if i >= n-1:
        return{"done": True}
    j = i + 1
    min_idx = i
    fase = "buscar"
    # Cuando i llegue al final, devolvé {"done": True}.
    return {"done": True}