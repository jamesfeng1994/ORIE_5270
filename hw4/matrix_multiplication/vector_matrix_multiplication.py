import os
from pyspark import SparkConf, SparkContext
conf = SparkConf()
sc = SparkContext(conf=conf)

def pyspark_matrix(m, v):

    matrix = sc.textFile(m).map(lambda x: x.split(',')[1:]).map(lambda value: [float(x) for x in value]).cache()
    vector = sc.textFile(v).map(lambda x: x.split(',')).map(lambda value: [float(x) for x in value]).cache()

    matrix_flat = matrix.zipWithIndex().map(lambda line:
                                            (line[1], [(line[0][i], i) for i in range(len(line[0]))])).flatMap(
        lambda line: [(i[1], (line[0], i[0])) for i in line[1]])
    vector_flat = vector.flatMap(lambda line: [(i, line[i]) for i in range(len(line))])
    flat_join = matrix_flat.join(vector_flat).map(lambda line:
                                                  (line[1][0][0], line[1][0][1] * line[1][1])).reduceByKey(
        lambda a, b: a + b).map(lambda line: line[1])
    calc_res = flat_join.collect()

    file = open("output.txt", "w")
    for num in calc_res:
        file.write(str(num) + ', ')
        file.write('\n')
    file.close()
    sc.stop()
    return

if __name__ == '__main__':
    pyspark_matrix('A.txt', 'B.txt')