class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_user(self, user)
        if user not in self.adj_list:
            self.adj_list[user] = []

    def add_edge(self, user1, user2):
        if user1 not in self.adj_list:
            self.add_user(user1)
        if user2 not in self.adj_list:
            self.add_user(user2)

        self.adj_list[user1].append(user2)
        self.adj_list[user2].append(user1)

    def get_friends(self, user):
        return self.adj_list.get(user, [])

    def display(self):
        for user in self.adj_list:
            print(user, "->", self.adj_list[user])
