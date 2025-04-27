from pyspark import SparkContext, SparkConf

def dijkstra(sc, file_path, source):
    lines = sc.textFile(file_path).repartition(16)  # ✅ Repartition for speed

    # Handle messy header
    header = lines.first()
    header_parts = header.strip().split()
    if len(header_parts) >= 2:
        num_nodes, num_edges = int(header_parts[0]), int(header_parts[1])
    else:
        raise ValueError("Header line must contain at least two numbers: num_nodes and num_edges")

    # Parse edges (skip header line)
    edges = lines.zipWithIndex().filter(lambda x: x[1] > 0).map(lambda x: x[0])
    edges = edges.map(lambda line: line.strip().split()) \
                 .filter(lambda parts: len(parts) == 3) \
                 .map(lambda parts: (int(parts[0]), (int(parts[1]), int(parts[2]))))

    # Build adjacency list
    adjacency_list = edges.groupByKey().mapValues(list).cache()

    # Initialize distances
    distances = sc.parallelize([(node, float('inf')) for node in range(num_nodes)]).cache()
    distances = distances.map(lambda x: (x[0], 0) if x[0] == source else x)

    unvisited = distances

    while True:
        current = unvisited.reduce(lambda a, b: a if a[1] < b[1] else b)

        if current[1] == float('inf'):
            break  # No more reachable nodes

        current_node, current_dist = current

        neighbors = adjacency_list.lookup(current_node)
        if not neighbors:
            neighbors = []
        else:
            neighbors = neighbors[0]

        updates = sc.parallelize(neighbors).map(lambda x: (x[0], current_dist + x[1]))

        distances = distances.leftOuterJoin(updates).map(lambda x: (x[0], min(x[1][0], x[1][1]) if x[1][1] is not None else x[1][0]))

        # Remove current node from unvisited
        unvisited = distances.filter(lambda x: x[0] != current_node)

    return distances.collect()

def main():
    conf = SparkConf().setAppName("DijkstraShortestPath").setMaster("local[*]")
    sc = SparkContext(conf=conf)

    file_path = "weighted_graph.txt"  # your input file
    source_node = 0  # start from node 0

    result = dijkstra(sc, file_path, source_node)

    print(f"Shortest distances from node {source_node}:")
    for node, distance in sorted(result):
        if distance == float('inf'):
            print(f"Node {node}: INF")
        else:
            print(f"Node {node}: {distance}")

    sc.stop()

if __name__ == "__main__":
    main()

