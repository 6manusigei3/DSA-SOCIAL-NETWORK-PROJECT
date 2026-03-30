from collections import deque
import heapq


def recommend_friends(graph, user, top_k=10):
    if user not in graph:
        return []

    direct_friends = set(graph[user])
    scores = {}
    visited = {user}
    queue = deque([(user, 0)])

    while queue:
        current, depth = queue.popleft()
        if depth >= 2:
            continue

        for neighbor in graph.get(current, []):
            if neighbor == user:
                continue

            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, depth + 1))

            if depth == 1 and neighbor not in direct_friends:
                scores[neighbor] = scores.get(neighbor, 0) + 1

    if not scores:
        return []

    top_recs = heapq.nlargest(top_k, scores.items(), key=lambda item: (item[1], item[0]))
    return [name for name, _ in top_recs]
