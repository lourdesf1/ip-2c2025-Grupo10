def merge(left_light, right_list):
    sorted_list = []
    left_light_index = right_list_index = 0
    #Creamos variables para las longitudes de la lista
    left_light_length, right_list_length = len(left_list), len(right_list)

    for _ in range(left_light_length + right_list_length):
        if left_light_index < left_light_length and right_list_index < right_list_length:
            #Comprobamos el valor de cada elemento incial de las listas para ver
            #cual es menor. Si el elemento al principio de la lista izquierda es más 
            #pequeño, se añade a la lista ordenada
            if left_list[left_list_index] <= right_list[right_list_index]:
                sorted_list.append(left_list[left_list_index])
                left_light_index += 1
            #Si el elemento al principio de la lista de la derecha es más pequeño,se añade a la lista ordenada
            else:
                sorted_list.append(right_list[right_list_index])
                right_list_index += 1
        #Si llegamos al final de la lista de la izquierda, añadimos los elementos de la lista de la derecha
        elif left_light_index == left_light_length:
            sorted_list.append(right_list[right_list_index])
            right_list_index += 1
        #Si llegamos al final de la lista de la derecha, añadimos los elementos de la lista de la izquierda
        elif right_list_index == right_list_length:
            sorted_list.append(left_list[left_list_index])
            left_list_index += 1
    return sorted_list

def mergeSort(nums):
    #Si la lista tiene un solo elemento, devuélvelo
    if len(nums):
        return nums
    #Obtener el indice medio para separar la lista en dos 
    mid = len(nums) // 2
    #Ordenamos y fusionamos cada mitad
    left_list = mergeSort(nums[:mid])
    right_list = mergeSort(nums[mid:])
    #Fusionamos las listas ordenadas en una nueva ordenada
    return merge(left_list, right_list)

#Comprobamos el funcionamiento
listaNumerosAleatorios = [5, 2, 1, 8 , 4]
print("Lista sin ordenar: " + str(listaNumerosAleatorios))
listaNumerosAleatorios = mergeSort(listaNumerosAleatorios)
print("Lista ordenada; " + str(listaNumerosAleatorios))

            