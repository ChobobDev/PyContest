import asyncio
from flask import Flask,render_template,request,redirect,send_file,abort
from functions import utils as ut
from threading import Thread

app = Flask('app')



@app.route('/result/language=<language>/wwr&so')
def so_wwr_redirect(language):
    return redirect(f"/result/language={language}/so&wwr")

@app.route('/result/language=<language>/ro&so')
def so_ro_redirect(language):
    return redirect(f"/result/language={language}/so&ro")

@app.route('/result/language=<language>/ro&wwr')
def wwr_ro_redirect(language):
    return redirect(f"/result/language={language}/wwr&ro")

@app.route('/notfound=<language>')
def job_not_found(language):
    return render_template('notfound.html',language=language)

@app.errorhandler(404)
def page_not_found(e):
   
    return render_template('404.html'), 404

@app.route('/profile=<name>')
def profile(name):
    special_list=["arthur","nico","lynn","mizzu","chinshuu","woori","dgm"]
    if name in special_list:
        return render_template('special_profile.html',name=name)
    else:
        abort(404)

@app.route('/result/language=<language>/wwr&ro',methods=['GET','POST'])
def wwr_ro_site(language):
    prev_time=ut.check_time(language)
    print(prev_time)
    if(prev_time>6):
        parsed_jobs=ut.scrape_all(language)
        jobs=ut.wwr_dict(parsed_jobs)+ut.ro_dict(parsed_jobs)
        if len(jobs) !=0:
            if request.method == 'POST':
                if request.form.get('export') == 'export':
                    ut.export(jobs,language,"wwrro")
                    return send_file(f"{language}-jobs-wwrro.csv")
                elif request.form.get('update') == 'update':
                    ut.scrape_all(language)
                    return(redirect(f'/result/language={language}/wwr&ro'))
                elif request.form.get('header-search')=='header-search':
                    job_name = request.form['searchJobHeader'].lower()
                    selected_site=request.form.get('site')
                    url=ut.return_url(selected_site,job_name)
                    return(redirect(url))
            return render_template('result.html',jobs=jobs,langlogo=f"/static/img/{language.lower()}-logo.png",language=language,lastupdate=0)
        else:
            return(redirect(f"/notfound={language}"))
    else:
        json_job=ut.load_json(language)
        jobs=ut.wwr_dict(json_job)+ut.ro_dict(json_job)
        if request.method == 'POST':
            if request.form.get('export') == 'export':
                ut.export(jobs,language,"wwrro")
                return send_file(f"{language}-jobs-wwrro.csv")
            elif request.form.get('update') == 'update':
                ut.scrape_all(language)
                return(redirect(f'/result/language={language}/wwr&ro'))
            elif request.form.get('header-search')=='header-search':
                job_name = request.form['searchJobHeader'].lower()
                selected_site=request.form.get('site')
                url=ut.return_url(selected_site,job_name)
                return(redirect(url))
        return render_template('result.html',jobs=jobs,langlogo=f"/static/img/{language.lower()}-logo.png",language=language,lastupdate=prev_time)
    

@app.route('/result/language=<language>/so&ro',methods=['GET','POST'])
def so_ro_site(language):
    prev_time=ut.check_time(language)
    print(prev_time)
    if(prev_time>6):
        parsed_jobs=ut.scrape_all(language)
        jobs=ut.so_dict(parsed_jobs)+ut.ro_dict(parsed_jobs)
        if len(jobs) !=0:
            if request.method == 'POST':
                if request.form.get('export') == 'export':
                    ut.export(jobs,language,"soro")
                    return send_file(f"{language}-jobs-soro.csv")
                elif request.form.get('update') == 'update':
                    ut.scrape_all(language)
                    return(redirect(f'/result/language={language}/so&ro'))
                elif request.form.get('header-search')=='header-search':
                    job_name = request.form['searchJobHeader'].lower()
                    selected_site=request.form.get('site')
                    url=ut.return_url(selected_site,job_name)
                    return(redirect(url))
            return render_template('result.html',jobs=jobs,langlogo=f"/static/img/{language.lower()}-logo.png",language=language,lastupdate=0)
        else:
            return(redirect(f"/notfound={language}"))
    else:
        json_job=ut.load_json(language)
        jobs=ut.so_dict(json_job)+ut.ro_dict(json_job)
        if request.method == 'POST':
            if request.form.get('export') == 'export':
                ut.export(jobs,language,"soro")
                return send_file(f"{language}-jobs-soro.csv")
            elif request.form.get('update') == 'update':
                ut.scrape_all(language)
                return(redirect(f'/result/language={language}/so&ro'))
            elif request.form.get('header-search')=='header-search':
                job_name = request.form['searchJobHeader'].lower()
                selected_site=request.form.get('site')
                url=ut.return_url(selected_site,job_name)
                return(redirect(url))
        return render_template('result.html',jobs=jobs,langlogo=f"/static/img/{language.lower()}-logo.png",language=language,lastupdate=prev_time)
    

@app.route('/result/language=<language>/so&wwr',methods=['GET','POST'])
def so_wwr_site(language):
    prev_time=ut.check_time(language)
    print(prev_time)
    if(prev_time>6):
        parsed_jobs=ut.scrape_all(language)
        jobs=ut.so_dict(parsed_jobs)+ut.wwr_dict(parsed_jobs)
        if len(jobs) !=0:
            if request.method == 'POST':
                if request.form.get('export') == 'export':
                    ut.export(jobs,language,"sowwr")
                    return send_file(f"{language}-jobs-sowwr.csv")
                elif request.form.get('update') == 'update':
                    ut.scrape_all(language)
                    return(redirect(f'/result/language={language}/so&wwr'))
                elif request.form.get('header-search')=='header-search':
                    job_name = request.form['searchJobHeader'].lower()
                    selected_site=request.form.get('site')
                    url=ut.return_url(selected_site,job_name)
                    return(redirect(url))
            return render_template('result.html',jobs=jobs,langlogo=f"/static/img/{language.lower()}-logo.png",language=language,lastupdate=0)
        else:
            return(redirect(f"/notfound={language}"))
    else:
        json_job=ut.load_json(language)
        jobs=ut.so_dict(json_job)+ut.wwr_dict(json_job)
        if request.method == 'POST':
            if request.form.get('export') == 'export':
                ut.export(jobs,language,"sowwr")
                return send_file(f"{language}-jobs-sowwr.csv")
            elif request.form.get('update') == 'update':
                ut.scrape_all(language)
                return(redirect(f'/result/language={language}/so&wwr'))
            elif request.form.get('header-search')=='header-search':
                job_name = request.form['searchJobHeader'].lower()
                selected_site=request.form.get('site')
                url=ut.return_url(selected_site,job_name)
                return(redirect(url))
        return render_template('result.html',jobs=jobs,langlogo=f"/static/img/{language.lower()}-logo.png",language=language,lastupdate=prev_time)
    

@app.route('/result/language=<language>/wwr',methods=['GET','POST'])
def wwr_site(language):
    prev_time=ut.check_time(language)
    print(prev_time)
    if(prev_time>6):
        parsed_jobs=ut.scrape_all(language)
        jobs=ut.wwr_dict(parsed_jobs)
        if len(jobs) !=0:
            if request.method == 'POST':
                if request.form.get('export') == 'export':
                    ut.export(jobs,language,"wwr")
                    return send_file(f"{language}-jobs-wwr.csv")
                elif request.form.get('update') == 'update':
                    ut.scrape_all(language)
                    return(redirect(f'/result/language={language}/wwr'))
                elif request.form.get('header-search')=='header-search':
                    job_name = request.form['searchJobHeader'].lower()
                    selected_site=request.form.get('site')
                    url=ut.return_url(selected_site,job_name)
                    return(redirect(url))
            return render_template('result.html',jobs=jobs,langlogo=f"/static/img/{language.lower()}-logo.png",language=language,lastupdate=0)
        else:
            return(redirect(f"/notfound={language}"))
    else:
        jobs=ut.wwr_dict(ut.load_json(language))
        if request.method == 'POST':
            if request.form.get('export') == 'export':
                ut.export(jobs,language,"wwr")
                return send_file(f"{language}-jobs-wwr.csv")
            elif request.form.get('update') == 'update':
                ut.scrape_all(language)
                return(redirect(f'/result/language={language}/wwr'))
            elif request.form.get('header-search')=='header-search':
                job_name = request.form['searchJobHeader'].lower()
                selected_site=request.form.get('site')
                url=ut.return_url(selected_site,job_name)
                return(redirect(url))
        return render_template('result.html',jobs=jobs,langlogo=f"/static/img/{language.lower()}-logo.png",language=language,lastupdate=prev_time)
    
@app.route('/result/language=<language>/ro',methods=['GET','POST'])
def ro_site(language):
    prev_time=ut.check_time(language)
    print(prev_time)
    if(prev_time>6):
        parsed_jobs=ut.scrape_all(language)
        jobs=ut.ro_dict(parsed_jobs)
        if len(jobs) !=0:
            if request.method == 'POST':
                if request.form.get('export') == 'export':
                    ut.export(jobs,language,"ro")
                    return send_file(f"{language}-jobs-ro.csv")
                elif request.form.get('update') == 'update':
                    ut.scrape_all(language)
                    return(redirect(f'/result/language={language}/ro'))
                elif request.form.get('header-search')=='header-search':
                    job_name = request.form['searchJobHeader'].lower()
                    selected_site=request.form.get('site')
                    url=ut.return_url(selected_site,job_name)
                    return(redirect(url))
            return render_template('result.html',jobs=jobs,langlogo=f"/static/img/{language.lower()}-logo.png",language=language,lastupdate=0)
        else:
            return(redirect(f"/notfound={language}"))
    else:
        jobs=ut.ro_dict(ut.load_json(language))
        if request.method == 'POST':
            if request.form.get('export') == 'export':
                ut.export(jobs,language,"ro")
                return send_file(f"{language}-jobs-ro.csv")
            elif request.form.get('update') == 'update':
                ut.scrape_all(language)
                return(redirect(f'/result/language={language}/ro'))
            elif request.form.get('header-search')=='header-search':
                job_name = request.form['searchJobHeader'].lower()
                selected_site=request.form.get('site')
                url=ut.return_url(selected_site,job_name)
                return(redirect(url))
        return render_template('result.html',jobs=jobs,langlogo=f"/static/img/{language.lower()}-logo.png",language=language,lastupdate=prev_time)
    

@app.route('/result/language=<language>/so',methods=['GET','POST'])
def so_site(language):
    prev_time=ut.check_time(language)
    print(prev_time)
    if(prev_time>6):
        jobs=ut.scrape_all(language)
        if len(jobs) !=0:
            jobs=ut.so_dict(jobs)
            if request.method == 'POST':
                if request.form.get('export') == 'export':
                    ut.export(jobs,language,"so")
                    return send_file(f"{language}-jobs-so.csv")
                elif request.form.get('update') == 'update':
                    ut.scrape_all(language)
                    return(redirect(f'/result/language={language}/so'))
                elif request.form.get('header-search')=='header-search':
                    job_name = request.form['searchJobHeader'].lower()
                    selected_site=request.form.get('site')
                    url=ut.return_url(selected_site,job_name)
                    return(redirect(url))
            return render_template('result.html',jobs=jobs,langlogo=f"/static/img/{language.lower()}-logo.png",language=language,lastupdate=0)
        else:
            return(redirect(f"/notfound={language}"))
    else:
        jobs=ut.so_dict(ut.load_json(language))
        if request.method == 'POST':
            if request.form.get('export') == 'export':
                ut.export(jobs,language,"so")
                return send_file(f"{language}-jobs-so.csv")
            elif request.form.get('update') == 'update':
                ut.scrape_all(language)
                return(redirect(f'/result/language={language}/so'))
            elif request.form.get('header-search')=='header-search':
                job_name = request.form['searchJobHeader'].lower()
                selected_site=request.form.get('site')
                url=ut.return_url(selected_site,job_name)
                return(redirect(url))
        return render_template('result.html',jobs=jobs,langlogo=f"/static/img/{language.lower()}-logo.png",language=language,lastupdate=prev_time)
    

@app.route('/result/language=<language>/',methods=['GET','POST'])
def all_site(language):
    prev_time=ut.check_time(language)
    print(prev_time)
    if(prev_time>6):
        jobs=ut.scrape_all(language)
        if len(jobs) !=0:
            if request.method == 'POST':
                if request.form.get('export') == 'export':
                    ut.export(jobs,language,"all")
                    return send_file(f"{language}-jobs-all.csv")
                elif request.form.get('update') == 'update':
                    ut.scrape_all(language)
                    return(redirect(f'/result/language={language}/'))
                elif request.form.get('header-search')=='header-search':
                    job_name = request.form['searchJobHeader'].lower()
                    selected_site=request.form.get('site')
                    url=ut.return_url(selected_site,job_name)
                    return(redirect(url))
            return render_template('result.html',jobs=jobs,langlogo=f"/static/img/{language.lower()}-logo.png",language=language,lastupdate=0)
        else:
            return(redirect(f"/notfound={language}"))
    else:
        jobs=ut.load_json(language)
        if request.method == 'POST':
            if request.form.get('export') == 'export':
                ut.export(jobs,language,"all")
                return send_file(f"{language}-jobs-all.csv")
            elif request.form.get('update') == 'update':
                ut.scrape_all(language)
                return(redirect(f'/result/language={language}/'))
            elif request.form.get('header-search')=='header-search':
                job_name = request.form['searchJobHeader'].lower()
                selected_site=request.form.get('site')
                url=ut.return_url(selected_site,job_name)
                return(redirect(url))

        return render_template('result.html',jobs=jobs,langlogo=f"/static/img/{language.lower()}-logo.png",language=language,lastupdate=prev_time)
    
    


@app.route("/",methods=['GET','POST'])
def home():
    if request.method == 'POST':
        job_name = request.form['job_name'].lower()
        selected_site=request.form.get('site')
        url=ut.return_url(selected_site,job_name)
        return(redirect(url))
        

    return render_template('index.html')

app.run(host='0.0.0.0',port=8080,debug="true")
# Thread(target=app.run,args=("0.0.0.0",8080,"true")).start()
