# --- Estado Global ---
items: list[int] = []
n: int = 0
# Pila para almacenar los índices de los subarreglos a ordenar (low, high)
# Se inicializa con el rango completo [0, n-1]
stack: list[tuple[int, int]] = []
# Punteros internos para el micro-paso de la partición (particionado de Lomuto)
low: int = -1
high: int = -1
pivot_index: int = -1  # Índice del pivote (items[high] para Lomuto)
i: int = -1  # Puntero para la posición donde debería ir el pivote (índice del elemento más pequeño visto hasta ahora)
j: int = -1  # Puntero para iterar a través del subarreglo [low, high-1]
partición_terminada: bool = True # Indica si hay que empezar una nueva partición (True) o estamos dentro de una (False)

# --- Implementación de Funciones Requeridas ---
def init(vals: list[int]) -> None:
    global items, n, stack, low, high, pivot_index, i, j, partición_terminada
    items = list(vals)  # Guardar copia
    n = len(items)
    # Inicializar estado para Quick Sort iterativo (usando pila)
    stack = []
    if n > 0:
        stack.append((0, n - 1))  # Añadir el rango inicial completo
    # Inicializar punteros de partición (valores de 'reset' para indicar que no hay partición activa)
    low = -1
    high = -1
    pivot_index = -1
    i = -1
    j = -1
    partición_terminada = True

def _swap(a: int, b: int) -> None:
    global items
    items[a], items[b] = items[b], items[a]

def step() -> dict:
    global items, n, stack, low, high, pivot_index, i, j, partición_terminada
    # 1. Comprobar si el algoritmo ha terminado
    if not stack and partición_terminada:
        return {"done": True}
    # 2. Empezar una nueva partición si la anterior ha terminado
    if partición_terminada:
        if not stack:
            return {"done": True} # Doble chequeo, por si acaso
        # Desapilar el próximo subarreglo a ordenar (low, high)
        low, high = stack.pop()
        # Si el subarreglo tiene 0 o 1 elemento, se considera ordenado, y simplemente se pasa al siguiente.
        if low >= high:
            return step() # Llamada recursiva para procesar el siguiente subarreglo
        # Inicializar el estado para la partición (Particionado de Lomuto: Pivote = items[high])
        pivot_index = high
        i = low - 1  # 'i' comienza un paso antes del subarreglo
        j = low      # 'j' comienza en el primer elemento del subarreglo
        partición_terminada = False # Estamos dentro de un proceso de partición
        # Devuelve el primer paso de la partición: marcar el pivote
        return {"a": low, "b": pivot_index, "swap": False, "done": False}
    # 3. Micro-paso dentro de la Partición (Iterar j)
    # Lógica: Mover 'j' de low hasta high-1 y comparar con el pivote.
    if j < pivot_index: # Mientras 'j' no haya alcanzado el pivote (high)        
        a = j
        b = pivot_index # El pivote siempre es high
        if items[j] <= items[pivot_index]:
            # El elemento actual (items[j]) es menor o igual al pivote.
            # Debe ir a la izquierda de donde acabará el pivote.
            i += 1           
            # Intercambiar items[i] e items[j]
            _swap(i, j)           
            # Preparar el resultado
            result = {"a": i, "b": j, "swap": True, "done": False}
        else:
            # El elemento actual (items[j]) es mayor que el pivote.
            # Se queda donde está, 'i' no se mueve. No hay swap.
            result = {"a": i if i >= low else low, "b": j, "swap": False, "done": False}
            # Se usa 'i' (o 'low') como referencia 'a' para la visualización, aunque no se use en la lógica de Lomuto.       
        j += 1 # Mover 'j' al siguiente elemento
        return result
    # 4. Finalizar la Partición: Colocar el Pivote en su posición final
    # 'j' ha llegado a 'pivot_index' (high). La iteración de Lomuto ha terminado.
    if j == pivot_index:
        # Colocar el pivote (items[high]) en su posición final (i+1)
        pivot_pos = i + 1
        a = pivot_pos
        b = pivot_index
        _swap(pivot_pos, pivot_index)       
        # Marcar la partición como terminada para el siguiente ciclo
        partición_terminada = True        
        # Guardar los subarreglos para la próxima iteración del Quick Sort
        # Subarreglo izquierdo
        if low < pivot_pos - 1:
            stack.append((low, pivot_pos - 1))
        # Subarreglo derecho
        if pivot_pos + 1 < high:
            stack.append((pivot_pos + 1, high))
        # El índice de retorno 'a' y 'b' es la posición del pivote y su origen (high).
        # El intercambio SÍ se realiza aquí.
        return {"a": a, "b": b, "swap": True, "done": False}
    # Si se llega aquí, algo salió mal o la lista estaba vacía inicialmente.
    return {"done": True}