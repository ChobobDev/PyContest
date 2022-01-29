import asyncio
from flask import Flask,render_template,request,redirect
from functions import utils as ut

app = Flask(__name__)

sitesButtons ={"all":"all","so":"/so","wwr":"./wwr","ro":"./ro","sowwr":"./so&wwr","soro":"./so&ro","wwrro":"./wwr&ro"}

@app.route('/result/language=<language>/wwr&so')
def so_wwr_redirect(language):
    return redirect(f"/result/language={language}/so&wwr")

@app.route('/result/language=<language>/ro&so')
def so_ro_redirect(language):
    return redirect(f"/result/language={language}/so&ro")

@app.route('/result/language=<language>/ro&wwr')
def wwr_ro_redirect(language):
    return redirect(f"/result/language={language}/wwr&ro")

@app.route('/result/language=<language>/wwr&ro')
def wwr_ro_site(language):
    prev_time=ut.check_time(language)
    print(prev_time)
    if(prev_time>6):
        jobs=ut.scrape_all(language)
        if len(jobs) !=0:
            return render_template('result.html',jobs=jobs,langlogo=f"/static/img/{language.lower()}-logo.png",language=language)
        else:
            return(redirect("/"))
    else:
        json_job=ut.load_json(language)
        jobs=ut.wwr_dict(json_job)+ut.ro_dict(json_job)
        return render_template('result.html',jobs=jobs,langlogo=f"/static/img/{language.lower()}-logo.png",language=language)
    

@app.route('/result/language=<language>/so&ro')
def so_ro_site(language):
    prev_time=ut.check_time(language)
    print(prev_time)
    if(prev_time>6):
        jobs=ut.scrape_all(language)
        if len(jobs) !=0:
            return render_template('result.html',jobs=jobs,langlogo=f"/static/img/{language.lower()}-logo.png",language=language)
        else:
            return(redirect("/"))
    else:
        json_job=ut.load_json(language)
        jobs=ut.so_dict(json_job)+ut.ro_dict(json_job)
        return render_template('result.html',jobs=jobs,langlogo=f"/static/img/{language.lower()}-logo.png",language=language)
    

@app.route('/result/language=<language>/so&wwr')
def so_wwr_site(language):
    prev_time=ut.check_time(language)
    print(prev_time)
    if(prev_time>6):
        jobs=ut.scrape_all(language)
        if len(jobs) !=0:
            jobs=ut.so_dict(jobs)+ut.wwr_dict(jobs)
            return render_template('result.html',jobs=jobs,langlogo=f"/static/img/{language.lower()}-logo.png",language=language)
        else:
            return(redirect("/"))
    else:
        json_job=ut.load_json(language)
        jobs=ut.so_dict(json_job)+ut.wwr_dict(json_job)
        return render_template('result.html',jobs=jobs,langlogo=f"/static/img/{language.lower()}-logo.png",language=language)
    

@app.route('/result/language=<language>/wwr')
def wwr_site(language):
    prev_time=ut.check_time(language)
    print(prev_time)
    if(prev_time>6):
        jobs=ut.scrape_all(language)
        if len(jobs) !=0:
            jobs=ut.wwr_dict(jobs)
            return render_template('result.html',jobs=jobs,langlogo=f"/static/img/{language.lower()}-logo.png",language=language)
        else:
            return(redirect("/"))
    else:
        jobs=ut.wwr_dict(ut.load_json(language))
        return render_template('result.html',jobs=jobs,langlogo=f"/static/img/{language.lower()}-logo.png",language=language)
    
@app.route('/result/language=<language>/ro')
def ro_site(language):
    prev_time=ut.check_time(language)
    print(prev_time)
    if(prev_time>6):
        jobs=ut.scrape_all(language)
        if len(jobs) !=0:
            jobs=ut.ro_dict(jobs)
            return render_template('result.html',jobs=jobs,langlogo=f"/static/img/{language.lower()}-logo.png",language=language)
        else:
            return(redirect("/"))
    else:
        jobs=ut.ro_dict(ut.load_json(language))
        return render_template('result.html',jobs=jobs,langlogo=f"/static/img/{language.lower()}-logo.png",language=language)
    

@app.route('/result/language=<language>/so')
def so_site(language):
    prev_time=ut.check_time(language)
    print(prev_time)
    if(prev_time>6):
        jobs=ut.scrape_all(language)
        if len(jobs) !=0:
            jobs=ut.so_dict(jobs)
            return render_template('result.html',jobs=jobs,langlogo=f"/static/img/{language.lower()}-logo.png",language=language)
        else:
            return(redirect("/"))
    else:
        jobs=ut.so_dict(ut.load_json(language))
        return render_template('result.html',jobs=jobs,langlogo=f"/static/img/{language.lower()}-logo.png",language=language)
    

@app.route('/result/language=<language>/',methods=['GET','POST'])
def all_site(language):
    prev_time=ut.check_time(language)
    print(prev_time)
    if(prev_time>6):
        jobs=ut.scrape_all(language)
        if len(jobs) !=0:
            return render_template('result.html',jobs=jobs,langlogo=f"/static/img/{language.lower()}-logo.png",language=language,lastupdate=0)
        else:
            return(redirect("/"))
    else:
        return render_template('result.html',jobs=ut.load_json(language),langlogo=f"/static/img/{language.lower()}-logo.png",language=language,lastupdate=prev_time)
    

@app.route("/",methods=['GET','POST'])
def home():
    if request.method == 'POST':
        job_name = request.form['job_name'].lower()
        selected_site=request.form.get('site')
        url=ut.return_url(selected_site,job_name)
        return(redirect(url))

    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug="on")
