from flask import Flask,render_template
import stackoverflow as so
app = Flask(__name__)

@app.route("/")
def hello():
    so.get_job_url(["pyton","java","javascript"])
    return render_template('index.html')

if __name__ == "__main__":
    app.run()