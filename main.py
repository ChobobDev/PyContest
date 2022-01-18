import time
from flask import Flask,render_template,request
import stackoverflow as so
import weworkremotely as wwr
import remoteok as ro
app = Flask(__name__)

@app.route("/result",methods=['GET','POST'])
def result():
    if request.method == 'POST':
        job_name = request.form['job_name']
        selected_site=request.form.getlist('Site')
    jobs=[]
    start_time = time.time()
    for site in selected_site:
        if site=="so":
            jobs.extend(so.get_jobs([job_name]))
        if site=="wwr":
            jobs.extend(wwr.get_jobs([job_name]))
        if site=="ro":
            jobs.extend(ro.get_jobs([job_name]))
    n=1
    for job in jobs:
        if "number" not in job:
            job["number"]=n
        n+=1
    print("--- %s seconds ---" % (time.time() - start_time))
    return render_template('result.html',jobs=jobs)


@app.route("/",methods=['GET','POST'])
def home():
    
    return render_template('index.html')

if __name__ == "__main__":
    
    app.run()
