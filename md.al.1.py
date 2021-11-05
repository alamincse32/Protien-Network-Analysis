## Author: Salem <Salem@SALEM-OFFICE>

import numpy as np
import matplotlib.pyplot as plt

file_name = "karate.txt"
distance_matrix = []
degree_distribution = []


# Read graph from file and store it into adjacency matrix
def get_graph():
    graph_file = np.loadtxt(file_name, dtype=float, delimiter=' ', usecols=range(2))
    vertex_number = int(max(np.max(graph_file[:, 0]), np.max(graph_file[:, 1])))
    adjacency_matrix = np.zeros((vertex_number, vertex_number))
    for i in range(len(graph_file)):
        x = int(graph_file[i][0])
        y = int(graph_file[i][1])
        adjacency_matrix[x - 1][y - 1] = 1
        adjacency_matrix[y - 1][x - 1] = 1

    return adjacency_matrix


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
            for j in range(i + 1, len(vertex_index)):
                if graph[vertex_index[i]][vertex_index[j]] > 0:
                    length += 1
        try:
            coefficient = 2 * length / (len(vertex_index) * (len(vertex_index) - 1))
        except ZeroDivisionError:
            print("Zero Division Error occurred")
    return coefficient


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    file = open(file_name + 'result.txt', 'a')
    file.write(file_name + "\n")
    graph = get_graph()
    n = len(get_graph())
    degree_of_each_node = get_degree(graph)
    file.write("Degree of nodes:\n")
    for i in range(len(degree_of_each_node)):
        line = str(i + 1) + " ----> " + str(int(degree_of_each_node[i])) + "\n"
        file.write(line)
    average_degree = np.sum(degree_of_each_node) / len(degree_of_each_node)

    file.write("Degree distribution: \n")
    line = ""
    max_degree = np.max(degree_of_each_node)
    for i in range(int(max_degree) + 1):
        line += str(i) + " "
    line = line + "\n"
    file.write(line)
    line = line_1 = ""
    for i in range(1, int(max_degree) + 1):
        count = list(degree_of_each_node).count(i)
        for j in range(len(degree_of_each_node)):
            if degree_of_each_node[j] == i:
                degree_distribution.append(count / n)
        line += str(count) + " "
        line_1 += str(count / n) + " "
    line = line + "\n"
    line_1 += "\n"
    file.write(line)
    file.write(line_1)

    file.write("Cluster Coefficient of each node:\n")
    graph_clustering_cofficient = 0
    for i in range(n):
        clustering_coefficient = get_clustering_coefficient(graph, i)
        graph_clustering_cofficient += clustering_coefficient
        line = str(int(i + 1)) + " ----> " + str(clustering_coefficient) + "\n"
        file.write(line)

    line = "The Clustering Coefficient of the graph is: " + str(graph_clustering_cofficient / n) + "\n"
    file.write(line)
    file.close()
    graph_vertice = []
    for i in range(n):
        graph_vertice.append(i + 1)
    w = 10
    h = 10
    d = 70
    plt.figure(figsize=(w, h), dpi=d)
    plot_1 = plt.figure(1)
    plot_2 = plt.figure(2)
    plt.scatter(graph_vertice,degree_of_each_node)
    plt.xlabel("Number of vertex")
    plt.ylabel("Degree of vertex")
    plt.savefig(file_name + "plot_1.png")
    #plt.loglog(graph_vertice, degree_distribution)
    #plt.savefig(file_name + "plot_2.png")
