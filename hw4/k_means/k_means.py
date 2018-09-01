import os
import pyspark
from pyspark import SparkConf, SparkContext
conf = SparkConf()
sc = SparkContext(conf=conf)
import numpy as np

def load_points(file_1, file_2):
    points = sc.textFile(file_1).map(
        lambda line: np.array([float(x) for x in line.split(' ')])).cache()
    centroids = sc.textFile(file_2).map(
        lambda line: np.array([float(x) for x in line.split(' ')])).collect()
    return points, centroids

def euclidean_distance(point_1, point_2):
    d_ = 0
    for index in range(len(point_1)):
        d_ = d_ + (point_1[index] - point_2[index]) ** 2
    return d_ ** 0.5

def pyspark_kmeans(data_file, centroids_file, Max_iter=20):

    def is_equal(centroids_1, centroids_2):
        if len(centroids_1) != len(centroids_2):
            return False
        for c in centroids_1:
            if c not in centroids_2:
                return False
        return True

    points, centroids = load_points(data_file, centroids_file)
    centroids = [l.tolist() for l in centroids]
    for i in range(Max_iter):
        if i % 10 == 9:
            print('Iteration ', i+1)
        points_classified = points.map(lambda d: (reclassify(d, centroids), [np.array(d), 1]))
        class_sum = points_classified.reduceByKey(lambda x, y: (x[0] + y[0], x[1] + y[1]))
        new_centroids = class_sum.map(lambda x: x[1][0] / x[1][1]).collect()
        new_centroids = [l.tolist() for l in new_centroids]
        if is_equal(centroids, new_centroids):
            break
        else:
            centroids = new_centroids
    with open('output.txt', 'w') as f:
        for _list in centroids:
            for _string in _list:
                f.write(str(_string) + ', ')
            f.write('\n')
    return

def reclassify(point, centroids):
    d = float('Inf')
    smallest_index = -1
    for index in range(len(centroids)):
        d_single = euclidean_distance(point, centroids[index])
        if d_single < d:
            d = d_single
            smallest_index = index
    return smallest_index


if __name__ == '__main__':
    pyspark_kmeans('data.txt', 'centroids.txt', Max_iter=100)