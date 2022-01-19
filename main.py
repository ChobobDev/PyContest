from flask import Flask,render_template,request
from functions import scrape as sc
app = Flask(__name__)

@app.route('/result/language=<language>&so')
def so_site(language):
    return language+"so"


@app.route('/result/language=<language>')
def all_site(language):
    return language

@app.route("/result",methods=['GET','POST'])
def result():
    if request.method == 'POST':
        job_name = request.form['job_name']
        selected_site=request.form.getlist('Site')
    return render_template('result.html',jobs=jobs)


@app.route("/",methods=['GET','POST'])
def home():
    
    return render_template('index.html')

if __name__ == "__main__":
    app.run()
