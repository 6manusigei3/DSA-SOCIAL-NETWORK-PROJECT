from flask import Flask, render_template, request
from system.friend_manager import FriendManager

app = Flask(__name__)
fm = FriendManager()

@app.route("/", methods=["GET", "POST"])
def index():
    message = ""

    if request.method == "POST":
        action = request.form.get("action")
        user = request.form.get("user")
        friend = request.form.get("friend")

        if action == "add":
            fm.add_friend(user, friend)
            message = "Connection added!"

        elif action == "remove":
            fm.remove_friend(user, friend)
            message = "Connection removed!"

    graph = fm.graph.graph  # access underlying graph

    return render_template("index.html", graph=graph, message=message)

if __name__ == "__main__":
    app.run(debug=True)
