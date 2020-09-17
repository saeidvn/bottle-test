from bottle import Bottle, run

app = Bottle()

@app.get("/")
def hello():
    return "<h1>hello world</h1>"

@app.get("/movies")
def movies():
    return "<h1>a lot of movies</h1>"


run(app)

