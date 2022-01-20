import asyncio
from distutils.log import debug
from flask import Flask,render_template,request,redirect
from functions import utils as ut

app = Flask(__name__)

@app.route('/result/language=<language>&wwr&so')
def so_wwr_redirect(language):
    return redirect(f"/result/language={language}&so&wwr")

@app.route('/result/language=<language>&ro&so')
def so_ro_redirect(language):
    return redirect(f"/result/language={language}&so&ro")

@app.route('/result/language=<language>&ro&wwr')
def wwr_ro_redirect(language):
    return redirect(f"/result/language={language}&wwr&ro")

@app.route('/result/language=<language>&wwr&ro')
def wwr_ro_site(language):
    return render_template('result.html',jobs=ut.scrape_wwr_ro(language))

@app.route('/result/language=<language>&so&ro')
def so_ro_site(language):
    return render_template('result.html',jobs=ut.scrape_so_ro(language))

@app.route('/result/language=<language>&so&wwr')
def so_wwr_site(language):
    return render_template('result.html',jobs=ut.scrape_so_wwr(language))

@app.route('/result/language=<language>&wwr')
def wwr_site(language):
    return render_template('result.html',jobs=ut.scrape_wwr(language))

@app.route('/result/language=<language>&ro')
def ro_site(language):
    return render_template('result.html',jobs=ut.scrape_ro(language))

@app.route('/result/language=<language>&so')
def so_site(language):
    return render_template('result.html',jobs=ut.scrape_so(language))

@app.route('/result/language=<language>',methods=['GET','POST'])
def all_site(language):
    return render_template('result.html',jobs=ut.scrape_all(language))

@app.route("/",methods=['GET','POST'])
def home():
    
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug="on")
