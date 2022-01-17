from flask import Flask,render_template
import stackoverflow as so
import weworkremotely as wwr
import remoteok as ro
app = Flask(__name__)

@app.route("/")
def hello():
    jobs=so.get_jobs(["python"])+wwr.get_jobs(["python"])+ro.get_jobs(["python"])
    return render_template('index.html',jobs=jobs)

if __name__ == "__main__":
    
    app.run()
