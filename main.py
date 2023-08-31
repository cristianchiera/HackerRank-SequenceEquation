def permutationEquation(p):
    # Write your code here
    n = len(p)
    y_values = []

    for x in range(1, n + 1):
        # Buscar el indice de x en p
        index_x = p.index(x) + 1
        
        # Encontrar el indice de p(index_x) en p y sumar 1 para obtener y
        index_y = p.index(index_x) + 1
        
        y_values.append(index_y)

    return y_values
