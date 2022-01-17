from flask import Flask,render_template
import stackoverflow as so
import weworkremotely as wwr
import remoteok as ro
app = Flask(__name__)

@app.route("/")
def hello():

    return render_template('index.html')

if __name__ == "__main__":
    jobs=so.get_jobs(["python"])+wwr.get_jobs(["python"])+ro.get_jobs(["python"])
    print(jobs)
    app.run()
