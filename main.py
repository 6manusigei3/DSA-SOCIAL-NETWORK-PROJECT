from system.friend_manager import FriendManager
from system.recommendation_engine import recommend_friends

fm = FriendManager()

print("Creating users...")
fm.create_user("Alice")
fm.create_user("Bob")
fm.create_user("Carol")
fm.create_user("David")

print("\nSending friend requests...")
fm.send_request("Alice", "Bob")
fm.send_request("Bob", "Carol")
fm.send_request("Carol", "David")

print("\nAccepting requests...")
fm.accept_request()
fm.accept_request()
fm.accept_request()

print("\nNetwork:")
fm.display()

print("\nRecommendations for Alice:")
print(recommend_friends(fm.network, "Alice"))

print("\nUndo last action:")
fm.undo()
fm.display()