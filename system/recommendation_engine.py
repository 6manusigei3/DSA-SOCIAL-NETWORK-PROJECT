def recommend_friends(graph, user):
    if user not in graph:
        return []

    # Direct friends
    direct_friends = set(graph[user])

    recommendations = set()

    # Friends of friends
    for friend in direct_friends:
        for fof in graph.get(friend, []):
            if fof != user and fof not in direct_friends:
                recommendations.add(fof)

    return list(recommendations)