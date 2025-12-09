from flask import Flask, render_template

from api.API import API
app=Flask(__name__)
api=API()
@app.route("/", methods=["GET"])
def index():
    animes = api.get_animepage(1)
    images = api.images(animes[0])
    return render_template("index.html", animes=animes, images=images)




if __name__ == "__main__":
    app.run(debug=True)
