from flask import Flask,render_template,request
import stackoverflow as so
import weworkremotely as wwr
import remoteok as ro
app = Flask(__name__)

@app.route("/result",methods=['GET','POST'])
def result():
    if request.method == 'POST':
        selected_site=request.form.getlist('Site')
        print(selected_site)
    jobs=[]
    for site in selected_site:
        print(site)
        if site=="so":
            jobs.extend(so.get_jobs(["Python"]))
        if site=="wwr":
            jobs.extend(wwr.get_jobs(["Python"]))
        if site=="ro":
            jobs.extend(ro.get_jobs(["Python"]))
    n=1
    for job in jobs:
        if "number" not in job:
            job["number"]=n
        n+=1
    print(jobs)
    print(so.get_jobs(["Python"]))
    return render_template('result.html',jobs=jobs)


@app.route("/",methods=['GET','POST'])
def home():
    
    return render_template('index.html')

if __name__ == "__main__":
    
    app.run()
