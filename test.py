import numpy as np

file_name = "graph.txt"
distance_matrix = []
def get_graph():
    graph_file = np.loadtxt(file_name, dtype= int, delimiter=' ')
    vertex_number = max(np.max(graph_file[:,0]),np.max(graph_file[:,1]))
    adjacency_matrix = np.zeros((vertex_number,vertex_number))
    for i in range(len(graph_file)):
        x = graph_file[i][0]
        y = graph_file[i][1]
        adjacency_matrix[x-1][y-1] = 1
        adjacency_matrix[y-1][x-1] = 1

    return adjacency_matrix


def bfs_algorithm(graph,vertex):
    distance = []
    length = 0
    flage_queue=[]
    neighbour_nodes = []
    for i in range(len(graph)):
        flage_queue.append(False)
    neighbour_nodes.append(vertex)
    flage_queue[vertex-1] = True

    while len(neighbour_nodes) > 0:
        u = neighbour_nodes.pop(0)
        length +=1
        adjacency_matrix = graph[u-1]
        for i in range(len(adjacency_matrix)):
            if adjacency_matrix[i] > 0 and flage_queue[i] == False:
                flage_queue[i] = True
                neighbour_nodes.append(i+1)
                distance.append([vertex,i+1,length])

    return distance







if __name__ == '__main__':

    graph = get_graph()
    n = len(graph)
    distance_matrix = np.zeros((n,n))
    for i in range(n):
        get_distance = bfs_algorithm(graph,i+1)
        for j in range(len(get_distance)):
            x = get_distance[j][0]
            y = get_distance[j][1]
            d = get_distance[j][2]
            distance_matrix[x-1][y-1] = d
            distance_matrix[y-1][x-1] = d



    print(distance_matrix)