import Task
import flask

app = flask.Flask(__name__)

@app.route("/")
def index():
    return "hi"

@app.route("/task")
def task():
    t = Task.Task("Test Task", "This is a test task", isAnAssignment = True)
    return t.getDetails()

if __name__ == "__main__":
    app.run(debug=True)
