import os
import random
import sys
import time

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from system.recommendation_engine import recommend_friends


def generate_graph(user_count=1000, avg_friends=10):
    graph = {}
    users = [f"user{i}" for i in range(user_count)]

    for user in users:
        graph[user] = []

    for user in users:
        friends = random.sample(users, k=min(avg_friends, user_count - 1))
        if user in friends:
            friends.remove(user)
        graph[user] = friends

    for user, friends in graph.items():
        for friend in friends:
            if user not in graph[friend]:
                graph[friend].append(user)

    return graph


def benchmark():
    graph = generate_graph(user_count=2000, avg_friends=12)
    target = "user0"

    start = time.perf_counter()
    recs = recommend_friends(graph, target, top_k=5)
    duration = time.perf_counter() - start

    print(f"Top recommendations for {target}: {recs}")
    print(f"Recommendation runtime: {duration:.6f} seconds")


if __name__ == "__main__":
    benchmark()
