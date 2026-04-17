# -----------------------------------
# I. SELECTION SORT (Greedy)
# -----------------------------------
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    print("Selection Sort:", arr)

# call function
selection_sort([64, 25, 12, 22, 11])


# -----------------------------------
# II. MINIMUM SPANNING TREE (Simple Greedy - Prim style)
# -----------------------------------
def mst_simple():
    graph = [
        [0, 2, 0, 6],
        [2, 0, 3, 8],
        [0, 3, 0, 0],
        [6, 8, 0, 0]
    ]

    selected = [False] * 4
    selected[0] = True

    print("\nMST (Simple):")
    for _ in range(3):
        min_edge = 999
        x = y = 0

        for i in range(4):
            if selected[i]:
                for j in range(4):
                    if not selected[j] and graph[i][j]:
                        if graph[i][j] < min_edge:
                            min_edge = graph[i][j]
                            x, y = i, j

        print(x, "-", y, ":", min_edge)
        selected[y] = True

# call function
mst_simple()


# -----------------------------------
# III. SINGLE SOURCE SHORTEST PATH (Dijkstra)
# -----------------------------------
def shortest_path():
    graph = [
        [0, 4, 1, 0],
        [4, 0, 2, 5],
        [1, 2, 0, 8],
        [0, 5, 8, 0]
    ]

    dist = [999] * 4
    visited = [False] * 4
    dist[0] = 0

    for _ in range(4):
        min_dist = 999
        u = -1

        for i in range(4):
            if not visited[i] and dist[i] < min_dist:
                min_dist = dist[i]
                u = i

        visited[u] = True

        for v in range(4):
            if graph[u][v] and not visited[v]:
                if dist[u] + graph[u][v] < dist[v]:
                    dist[v] = dist[u] + graph[u][v]

    print("\nShortest Path:", dist)

# call function
shortest_path()


# -----------------------------------
# IV. JOB SCHEDULING (Greedy)
# -----------------------------------
def job_scheduling():
    jobs = [
        ("J1", 2, 100),
        ("J2", 1, 50),
        ("J3", 2, 10),
        ("J4", 1, 20)
    ]

    jobs.sort(key=lambda x: x[2], reverse=True)

    slots = [None] * 2

    for job in jobs:
        for i in range(job[1] - 1, -1, -1):
            if slots[i] is None:
                slots[i] = job[0]
                break

    print("\nJob Scheduling:", slots)

# call function
job_scheduling()


# -----------------------------------
# V. PRIM'S MST
# -----------------------------------
def prim_mst():
    graph = [
        [0, 2, 0, 6],
        [2, 0, 3, 8],
        [0, 3, 0, 0],
        [6, 8, 0, 0]
    ]

    selected = [False]*4
    selected[0] = True

    print("\nPrim MST:")
    for _ in range(3):
        min_edge = 999
        x = y = 0

        for i in range(4):
            if selected[i]:
                for j in range(4):
                    if not selected[j] and graph[i][j]:
                        if graph[i][j] < min_edge:
                            min_edge = graph[i][j]
                            x, y = i, j

        print(x, "-", y, ":", min_edge)
        selected[y] = True

# call function
prim_mst()


# -----------------------------------
# VI. KRUSKAL'S MST
# -----------------------------------
def kruskal_mst():
    edges = [
        (2, 0, 1),
        (3, 1, 2),
        (6, 0, 3),
        (8, 1, 3)
    ]

    edges.sort()
    parent = [0, 1, 2, 3]

    def find(x):
        while parent[x] != x:
            x = parent[x]
        return x

    print("\nKruskal MST:")
    for w, u, v in edges:
        pu = find(u)
        pv = find(v)
        if pu != pv:
            print(u, "-", v, ":", w)
            parent[pu] = pv

# call function
kruskal_mst()


# -----------------------------------
# VII. DIJKSTRA (again for clarity)
# -----------------------------------
def dijkstra():
    graph = [
        [0, 4, 1, 0],
        [4, 0, 2, 5],
        [1, 2, 0, 8],
        [0, 5, 8, 0]
    ]

    dist = [999] * 4
    visited = [False] * 4
    dist[0] = 0

    for _ in range(4):
        min_dist = 999
        u = -1

        for i in range(4):
            if not visited[i] and dist[i] < min_dist:
                u = i
                min_dist = dist[i]

        visited[u] = True

        for v in range(4):
            if graph[u][v] and not visited[v]:
                if dist[u] + graph[u][v] < dist[v]:
                    dist[v] = dist[u] + graph[u][v]

    print("\nDijkstra:", dist)

# call function
dijkstra()