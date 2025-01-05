import numpy 
frame=numpy.array([
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0]
])

paded_frame = numpy.pad (frame, 1, mode='constant') # le code pour les bordures donnée par le prof

print(paded_frame)


def compute_number_neighbors(paded_frame, index_line, index_column,):
    new_paded_frame=paded_frame.copy() 
    
    neighbors= [
     [0, -1],
     [1, -1],
     [1, 0],
     [1, 1],
     [0, 1],
     [-1, 1],
     [-1, 0],
    [-1, -1],   
] 
    box_neighbor= 0
    for neighbor in neighbors:
        neighbors_index_line = index_line + neighbor[0]
        neighbors_index_column = index_column + neighbor[1]
        if paded_frame[neighbors_index_line, neighbors_index_column] == 1:
            box_neighbor+= 1

    return box_neighbor

