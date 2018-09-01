import heapq

class dijkstra_prob(object):
    
    def __init__(self, file_name):
        self.graph = None
        self.build_graph(file_name)
        
    def get_path_weight(self, lines):
        result = []
        path_weight = lines.split(',')
        for i in range(0, len(path_weight), 2):
            result.append((str(path_weight[i][1:]), float(path_weight[i + 1][:-1])))
        return result

    def build_graph(self, file_name):
        text_file = open(file_name, "r")
        raw_list = text_file.read().split('\n')
        graph = {}
        for i in range(0, len(raw_list), 2):
            key_value = str(raw_list[i])
            if i + 1 < len(raw_list) and raw_list[i + 1] != '':
                graph[key_value] = self.get_path_weight(raw_list[i + 1])
            else:
                graph[key_value] = []
        self.graph = graph
 

    def dijkstra(self, source):
        result = {}
        for k in self.graph.keys():
            result[k] = [float('Inf'), k, '/']
        result[source][0] = 0.0
        visited = []
        min_heap = []
        source_path = self.graph[source]
        heapq.heappush(min_heap, result[source])
        while len(min_heap) != 0:
            current_point = heapq.heappop(min_heap)
            current_point_path = self.graph[current_point[1]]
            if current_point[1] not in visited:
                for i in current_point_path:
                    if result[i[0]][0] > current_point[0] + i[1]:
                        result[i[0]][0] = current_point[0] + i[1]
                        result[i[0]][2] = current_point[1]
                        heapq.heappush(min_heap, result[i[0]])
                visited.append(current_point[1])
        return result

    def get_distance_path(self, source, destination, result):
        distance = result[destination][0]
        if distance == float('Inf'):
            return float('Inf'), ['/']
        else:
            path = []
            path.append(destination)
            while source not in path:
                path.append(result[path[-1]][2])
            path = path[::-1]
            return (distance, '->'.join(path))

    def find_shortest_path(self, source, destination):
        d_result = self.dijkstra(source)
        return self.get_distance_path(source, destination, d_result)


if __name__ == '__main__':
    dj = dijkstra_prob('graph2.txt')
    print(dj.find_shortest_path('2','0'))
