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

def compute_next_frame(paded_frame, index_line, index_column):
    paded_frame
    new_paded_frame= numpy.array([
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0]
])
    
    
    for index_line in range (1, paded_frame -1):
        for index_column in range (1, paded_frame -1):
         total_of_neighbors=compute_number_neighbors(paded_frame, index_line, index_column)
         
         if paded_frame [index_line,index_column]==1
         if total_of_neighbors < 2 or total_of_neighbors > 3:
          new_paded_frame [index_line,index_column]=0
    else:
        if  total_of_neighbors ==3 :
         new_paded_frame [index_column,index_line]=1
        return new_paded_frame
       
       
