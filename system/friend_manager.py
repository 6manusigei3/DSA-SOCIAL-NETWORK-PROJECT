from database.db_connection import connect_db
from structures.queue import Queue


class FriendManager:
    def __init__(self):
        self.network = {}      # Graph (Adjacency List)
        self.requests = Queue()  # Queue for friend requests

    # ✅ CREATE USER (FIXED FOR DUPLICATES)
    def create_user(self, username):
        db = connect_db()
        cursor = db.cursor()

        try:
            cursor.execute(
                "INSERT INTO users (username) VALUES (%s)", (username,))
            db.commit()
            print(f"User {username} created successfully")
        except Exception:
            print(f"User {username} already exists")

        # Also initialize in graph if not present
        if username not in self.network:
            self.network[username] = []

        cursor.close()
        db.close()

    # ✅ ADD FRIEND (GRAPH CONNECTION)
    def add_friend(self, user1, user2):
        if user1 not in self.network:
            self.network[user1] = []
        if user2 not in self.network:
            self.network[user2] = []

        self.network[user1].append(user2)
        self.network[user2].append(user1)

    # ✅ SEND FRIEND REQUEST (QUEUE)
    def send_request(self, sender, receiver):
        print(f"{sender} sent a request to {receiver}")
        self.requests.enqueue((sender, receiver))

    # ✅ ACCEPT FRIEND REQUEST (QUEUE → GRAPH)
    def accept_request(self):
        request = self.requests.dequeue()

        if request:
            sender, receiver = request
            print(f"{receiver} accepted request from {sender}")
            self.add_friend(sender, receiver)
        else:
            print("No pending requests")

    # ✅ DISPLAY NETWORK
    def display(self):
        for user in self.network:
            print(f"{user} -> {self.network[user]}")