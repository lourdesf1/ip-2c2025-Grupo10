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
    global items, n, i, j, min_idx, fase

    if i >= n:
        return {"done": True}

    if fase == "buscar":
        if j < n:
            # Todavía buscando el mínimo en la parte no ordenada
            curr_j = j # Guardamos el valor actual antes de incrementar j
            if items[j] < items[min_idx]:
                min_idx = j
            j += 1
            # Devolvemos el estado actual para visualización (comparación de j y min_idx)
            return {"a": min_idx, "b": curr_j, "swap": False, "done": False}
        else:
            # Se completó el barrido de búsqueda, pasar a fase "swap"
            fase = "swap"
            # La próxima llamada a step ejecutará la fase "swap"
            return step() # Llamada recursiva para ejecutar el swap inmediatamente

    elif fase == "swap":
        if min_idx != i:
            # Realizar el único swap
            items[i], items[min_idx] = items[min_idx], items[i]
            # Devolver la acción de swap para visualización
            result = {"a": i, "b": min_idx, "swap": True, "done": False}
        else:
            # No se necesita swap (el elemento ya está en su lugar)
            result = {"a": i, "b": i, "swap": False, "done": False}
        
        # Prepararse para la siguiente iteración
        i += 1
        j = i + 1
        min_idx = i
        fase = "buscar"
        return result

    # Caso por defecto, aunque no debería ser alcanzado
    return {"done": True}