import requests,asyncio
from bs4 import BeautifulSoup
from flask import redirect
from functions import stackoverflow as so ,weworkremotely as wwr,remoteok as ro


def requestWithUgerAgent(url):
    headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Whale/3.12.129.46 Safari/537.360'}
    soup = BeautifulSoup(requests.get(url, headers=headers).text, "html.parser")
    return soup

def scrape_all(job_name):
    return asyncio.run(so.get_jobs(job_name))+asyncio.run(wwr.get_jobs(job_name))+asyncio.run(ro.get_jobs(job_name))

def scrape_so(job_name):
    return asyncio.run(so.get_jobs(job_name)) 

def scrape_wwr(job_name):
    return asyncio.run(wwr.get_jobs(job_name)) 

def scrape_ro(job_name):
    return asyncio.run(ro.get_jobs(job_name))

def scrape_so_wwr(job_name):
    return asyncio.run(so.get_jobs(job_name))+asyncio.run(wwr.get_jobs(job_name))

def scrape_so_ro(job_name):
    return asyncio.run(so.get_jobs(job_name))+asyncio.run(ro.get_jobs(job_name))

def scrape_wwr_ro(job_name):
    return asyncio.run(wwr.get_jobs(job_name))+asyncio.run(ro.get_jobs(job_name))

def return_url(selected_site,job_name):
    if selected_site=="all":
        return (f"/result/language={job_name}")
    elif selected_site=="so":
        return (f"/result/language={job_name}&so")
    elif selected_site=="wwr":
        return (f"/result/language={job_name}&wwr")
    elif selected_site=="ro":
        return (f"/result/language={job_name}&ro")
    elif selected_site=="sowwr":
        return (f"/result/language={job_name}&so&wwr")
    elif selected_site=="soro":
        return (f"/result/language={job_name}&so&ro")
    elif selected_site=="wwrro":
        return (f"/result/language={job_name}&wwr&ro")