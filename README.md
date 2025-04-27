# dijkstra-spark

Implementation of Dijkstra’s shortest path algorithm using Apache Spark RDDs for distributed graph processing. Developed as part of a cloud computing project.

---

# Dijkstra's Algorithm Using Apache Spark

## Overview
This project implements **Dijkstra’s shortest path algorithm** using **Apache Spark RDDs** for distributed graph processing. It was developed as part of a cloud computing assignment focused on distributed systems and big data frameworks.

The goal is to compute the shortest distance from a **source node** to **all other nodes** in a large graph using parallel data processing techniques.

## Features
- Computes shortest distances from a source node to all other nodes.
- Marks unreachable nodes as `"INF"`.
- Utilizes **Spark RDD transformations** (`map`, `reduce`, `filter`, etc.).
- Designed to handle **large graphs** with **10,000 nodes** and **100,000 edges**.

## Technologies Used
- **Apache Spark 3.4.4**
- **Python 3.10**
- **MacOS (Apple M3 Chip, 8-core CPU, 8GB RAM)**
- **Visual Studio Code**

## Project Structure
| File | Description |
| :--- | :--- |
| `dijkstra_spark.py` | Main Python script implementing Dijkstra’s algorithm with Spark RDDs. |
| `weighted_graph.txt` | Input graph file containing edges and weights. |
| `README.md` | Documentation and project instructions. |

## How to Run

1. **Install Dependencies:**
   ```bash
   pip install pyspark
   ```

2. **Set Required Environment Variables:**
   ```bash
   export PYTHONHASHSEED=0
   ```

3. **Run the Program:**
   ```bash
   python3 dijkstra_spark.py
   ```

⚡ *Tip:* Ensure you are in the correct virtual environment if using one (like `spark_env`).

## Input Format
The input graph must be provided in **edge list format**:

```
num_nodes num_edges
u1 v1 weight1
u2 v2 weight2
...
```

**Example:**
```
5 6
0 1 7
0 2 3
1 3 9
2 4 4
3 4 6
1 4 2
```

Where:
- Each line describes a **directed edge** from node `u` to node `v` with a given `weight`.

## Output Format
The output displays the shortest distance from the source node to every other node.

**Example Output:**
```
Shortest distances from node 0:
Node 0: 0
Node 1: 7
Node 2: 3
Node 3: 10
Node 4: 7
```

- If a node is unreachable from the source, its distance is reported as `"INF"`.

## Notes
- Recommended number of RDD partitions: **16 partitions** (for best performance on an 8-core CPU).
- Execution time may be slower when running large graphs locally due to limited RAM and CPU parallelism.
- Installing `psutil` (optional) can improve Spark shuffle operation performance:
  ```bash
  pip install psutil
  ```

---



