items = []
n = 0
gap = 0
i = 0
j = 0

def init(vals: list[int]) -> None:
    global items, n, gap, i, j
    items = list(vals)
    n = len(items)
    gap = n // 2
    i = gap
    j = i

def step() -> dict:
    global items, n, gap, i, j
    if gap == 0:
        return{"done": True}
    #MIENTRAS QUEDEN GAPS POR PROCESAR.
    if i < n:
        #SI J RECORRE EL SUBARRAY I-GAP HACIA ATRÁS EN PASOS DE GAP.
        if j >= gap:
            a = j
            b = j - gap
            #DEVOLVEMOS UN MICRO-PASO (UNA COMPARACIÓN Y POSIBLE SWAP).
            if items[a] < items[b]:
                #HACEMOS EL SWAP REAL.
                items[a], items[b] = items[b], items[a]
                #RETROCEDEMOS J PARA SEGUIR COMPARANDO EN EL PRÓXIMO STEP()
                j -= gap
                return{"a": a, "b": b, "swap": True, "done": False}
            else:
                #NO SWAP -> TERMINAMOS EL INNER-LOOP PARA ESTE I.
                j = -1
                return{"a": a, "b": b, "swap": False, "done": False}
        #TERMINADO J-LOOP -> AVANZAR I
        i += 1
        j = i #PREPARAR PARA LA SIGUIENTE INSERCIÓN
        return{"a": 0, "b": 0, "swap": False, "done": False}
    #TERMINADO I-LOOP -> REDUCIR GAP
    gap //= 2
    if gap > 0:
        i = gap
        j = i
        return{"a": 0, "b": 0, "swap": False}
    #SIN GAPS -> TERMINADO
    return{"done": True}