
## Author: Salem <Salem@SALEM-OFFICE>

import numpy as np
import matplotlib.pyplot as plt


file_name = "HprdNetwork.txt"
distance_matrix = []
degree_distribution = []

#Read graph from file and store it into adjacency matrix
def get_graph():
    graph_file = np.loadtxt(file_name, dtype= float, delimiter=' ',usecols=range(2))
    vertex_number = int(max(np.max(graph_file[:,0]),np.max(graph_file[:,1])))
    adjacency_matrix = np.zeros((vertex_number,vertex_number))
    for i in range(len(graph_file)):
        x = int(graph_file[i][0])
        y = int(graph_file[i][1])
        adjacency_matrix[x-1][y-1] = 1
        adjacency_matrix[y-1][x-1] = 1

    return adjacency_matrix


#Applying breadth first search for finding the shortest path of a specific node to all nodes

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

def get_degree(graph):
    n = len(graph)
    degree = np.zeros(n)
    for i in range(n):
        degree[i] = np.count_nonzero(graph[i])
    return degree

def get_clustering_coefficient(graph, vertex):
    length = 0
    coefficient = 0
    adjacency_vertex = graph[vertex]
    vertex_index = np.nonzero(adjacency_vertex)[0]
    if len(vertex_index) == 0:
        return 0
    else:
        for i in range(len(vertex_index)):
            for j in range(i+1, len(vertex_index)):
                if graph[vertex_index[i]][vertex_index[j]] > 0:
                    length +=1
        try:
            coefficient = 2*length/(len(vertex_index)*(len(vertex_index)-1))
        except ZeroDivisionError:
            print("Zero Division Error occurred")
    return coefficient


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    file = open(file_name+'result.txt','a')
    file.write(file_name + "\n")
    graph = get_graph()
    n = len(get_graph())
    degree_of_each_node = get_degree(graph)
    file.write("Degree of nodes:\n")
    for i in range(len(degree_of_each_node)):
        line = str(i+1) + " ----> " + str(int(degree_of_each_node[i])) + "\n"
        file.write(line)
    average_degree = np.sum(degree_of_each_node)/len(degree_of_each_node)
    file.write("The average degree of graph is :" + str(average_degree) + "\n")
    file.write("Alamin")
    distance_matrix = np.zeros((n, n))
    for i in range(n):
        print(i)
        get_distance = bfs_algorithm(graph, i + 1)
        for j in range(len(get_distance)):
            x = get_distance[j][0]
            y = get_distance[j][1]
            d = get_distance[j][2]
            distance_matrix[x - 1][y - 1] = d
            distance_matrix[y - 1][x - 1] = d

    path_length = 0
    for i in range(n):
        path_length += np.sum(distance_matrix[i])

    path_length = path_length/(n*(n-1))
    line = "The average path length :" + str(path_length) + "\n"
    file.write(line)

    file.write("Eccentricity of each node: \n")
    for i in range(n):
        line = str(i+1) + " ----> " + str((distance_matrix[i])) + "\n"
        file.write(line)
    file.write("The radius of the graph is: ")
    min_ = 9999
    for i in range(n):
        min_ = min(min_,np.min([j for j in distance_matrix[i] if j != 0]))

    file.write(str(int(min_)) + "\n")

    file.write("The diameter of the graph is :")
    max_ = -1
    for i in range(n):
        max_ = max(max_,np.max(distance_matrix[i]))
    file.write(str(int(max_)) + "\n")

    file.write("Degree distribution: \n")
    line = ""
    max_degree = np.max(degree_of_each_node)
    for i in range(int(max_degree)+1):
        line += str(i) + " "
    line = line + "\n"
    file.write(line)
    line = line_1=""
    for i in range(1,int(max_degree)+1):
        count = list(degree_of_each_node).count(i)
        for j in range(len(degree_of_each_node)):
            if degree_of_each_node[j] == i:
                degree_distribution.append(count/n)
        line += str(count) + " "
        line_1 +=str(count/n) + " "
    line = line + "\n"
    line_1 += "\n"
    file.write(line)
    file.write(line_1)
    print(degree_distribution)

    file.write("Cluster Coefficient of each node:\n")
    graph_clustering_cofficient = 0
    for i in range(n):
        clustering_coefficient = get_clustering_coefficient(graph,i)
        graph_clustering_cofficient += clustering_coefficient
        line = str(int(i+1)) + " ----> " + str(clustering_coefficient) + "\n"
        file.write(line)

    line = "The Clustering Coefficient of the graph is: " + str(graph_clustering_cofficient/n) + "\n"
    file.write(line)

    graph_vertice = []
    for i in range(n):
        graph_vertice.append(i+1)
    w = 10
    h = 10
    d = 70
    plt.figure(figsize=(w, h), dpi=d)
    plot_1 = plt.figure(1)
    plot_2 = plt.figure(2)
    #plt.scatter(graph_vertice,degree_of_each_node)
    plt.xlabel("Number of vertex")
    plt.ylabel("Degree of vertex")
    #plt.savefig(file_name + "plot_1.png")
    plt.loglog(graph_vertice,degree_distribution)
    plt.savefig(file_name+"plot_2.png")





