items = []
n = 0

# Estado del algoritmo
start = 0
end = 0
i = 0
direction = "forward"   # "forward" o "backward"
active = True           # si todavía hay algo para ordenar


def init(vals):
    global items, n, start, end, i, direction, active
    items = list(vals)
    n = len(items)

    start = 0
    end = n - 1
    i = start
    direction = "forward"
    active = True

def step():
    global items, n, start, end, i, direction, active
    # ----------------------------------
    # FIN DEL ALGORITMO
    # ----------------------------------
    if not active or n <= 1:
        active = False
        return {"a": 0, "b": 0, "swap": False, "done": True}

    # ======================================================
    # BARRIDO HACIA ADELANTE (left → right)
    # ======================================================
    if direction == "forward":

        # Si todavía estamos comparando i ↔ i+1
        if i < end:
            a = i
            b = i + 1

            if items[a] > items[b]:
                # swap
                items[a], items[b] = items[b], items[a]
                out = {"a": a, "b": b, "swap": True, "done": False}
            else:
                out = {"a": a, "b": b, "swap": False, "done": False}

            i += 1
            return out

        # Fin del barrido forward
        end -= 1
        direction = "backward"
        i = end    # empezamos a comparar hacia atrás
        return {"a": i, "b": i - 1 if i > start else start, "swap": False, "done": False}

    # ======================================================
    # BARRIDO HACIA ATRÁS (right → left)
    # ======================================================
    else:  # direction == "backward"

        if i > start:
            a = i - 1
            b = i

            if items[a] > items[b]:
                items[a], items[b] = items[b], items[a]
                out = {"a": a, "b": b, "swap": True, "done": False}
            else:
                out = {"a": a, "b": b, "swap": False, "done": False}

            i -= 1
            return out

        # Fin del barrido backward
        start += 1

        # Si ya se cruzaron los límites → terminado
        if start >= end:
            active = False
            return {"a": 0, "b": 0, "swap": False, "done": True}

        direction = "forward"
        i = start
        return {"a": i, "b": i + 1 if i < end else end, "swap": False, "done": False}
