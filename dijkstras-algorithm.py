graph = {}

graph["start"] = {}
graph["start"]["a"] = 6
graph["start"]["b"] = 2

graph["a"] = {}
graph["a"]["finish"] = 1
graph["b"] = {}
graph["b"]["a"] = 3
graph["b"]["finish"] = 5
graph["finish"] = {}

print(graph)

infinity = float('inf')

costs = {}
costs["a"] = 6
costs["b"] = 2
costs["finish"] = infinity

parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["finish"] = None

print(costs)
print(parents)

processed = []


def find_lowerst_cost_node(costs):
    lowest_cost = float('inf')
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node


print(find_lowerst_cost_node(costs))

print('----')
node = find_lowerst_cost_node(costs)
while node is not None:
    print(f"{node} current node")
    cost = costs[node]
    neighbors = graph[node]
    print(f"{neighbors} - current node neighbors")
    for n in neighbors.keys():
        print(f"{n} - node and cost - {cost}")
        new_cost = cost + neighbors[n]
        if costs[n] > new_cost:
            costs[n] = new_cost
            parents[n] = node
            print(f"best cost - {new_cost}")

    processed.append(node)
    print(f"{processed} update processed array")
    print('costs', costs)
    print('parents', parents)
    node = find_lowerst_cost_node(costs)

