from flask import Flask, render_template, redirect

app = Flask(__name__)
app.secret_key = "coolkey"

@app.route("/<username>")
@app.route("/@<username>")
def route1(username):
    PlaceID = 8737602449
    Arguments = f"?launchData=%7B%22giftTarget%22%3A%22{username}%22%7D&placeId={PlaceID}"
    URL = f"https://www.roblox.com/games/start{Arguments}"
    return render_template("redirect.html", USERNAME=username, URL=URL)

if __name__ == "__main__":
    app.run(debug=True)
