def recommend_friends(graph, user):
    visited = set()
    queue = []
    recommendations = set()

    # Step 1: Get direct friends
    direct_friends = set(graph.get_friends(user))

    # Step 2: Add them to queue
    for friend in direct_friends:
        queue.append(friend)

    visited.add(user)

    # Step 3: BFS traversal
    while queue:
        current = queue.pop(0)

        if current not in visited:
            visited.add(current)

            # Look at friends of this friend
            for friend_of_friend in graph.get_friends(current):

                # Recommend if:
                # - not the user
                # - not already a friend
                if friend_of_friend != user and friend_of_friend not in direct_friends:
                    recommendations.add(friend_of_friend)

    return list(recommendations)
