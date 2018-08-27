class bellman_ford_prob(object):
    
    def __init__(self, file_name):
        self.graph = None
        self.build_graph(file_name)

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

    def get_path_weight(self, lines):
        result = []
        path_weight = lines.split(',')
        for i in range(0, len(path_weight), 2):
            result.append((str(path_weight[i][1:]), float(path_weight[i + 1][:-1])))
        return result

    def bellman_ford(self, source):
        result = {}
        for k in self.graph.keys():
            result[k] = [float('Inf'), k, '/']
        result[source][0] = 0.0
        for count in range(len(self.graph)):
            for k in self.graph.keys():
                for i in self.graph[k]:
                    if result[i[0]][0] > result[k][0] + i[1]:
                        result[i[0]][0] = result[k][0] + i[1]
                        result[i[0]][2] = k
        for k in self.graph.keys():
            for i in self.graph[k]:
                if result[i[0]][0] > result[k][0] + i[1]:
                    return True, result
        return False, result

    def get_negative_circles(self, result):
        visited = []
        for starting_points in result.keys():
            if starting_points in visited:
                continue
            path = [starting_points]
            visited.append(starting_points)
            current_points = starting_points
            while result[current_points][2] != '/':
                current_points = result[current_points][2]
                path.append(current_points)
                visited.append(current_points)
                if current_points in path[:-1]:
                    first_index = path.index(current_points)
                    return path[first_index:]

    def find_negative_cicles(self):
        neg_circle, result = self.bellman_ford('0')
        if neg_circle:
            path = self.get_negative_circles(result)
            return '->'.join(path[::-1])
        else:
            return "No negative circle"

if __name__ == '__main__':
    bf = bellman_ford_prob('graph1.txt')
    print(bf.find_negative_cicles())
    #should be like '1->2->3->4->1'
