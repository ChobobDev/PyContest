import requests,asyncio
from bs4 import BeautifulSoup
from functions import stackoverflow as so ,weworkremotely as wwr,remoteok as ro


def requestWithUgerAgent(url):
    headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Whale/3.12.129.46 Safari/537.360'}
    soup = BeautifulSoup(requests.get(url, headers=headers).text, "html.parser")
    return soup

def scrape_all(job_name):
    
    so_job = asyncio.run(so.get_jobs(job_name)) 
    wwr_job = asyncio.run(wwr.get_jobs(job_name))
    ro_job = asyncio.run(ro.get_jobs(job_name))
    jobs=so_job+wwr_job+ro_job
    return jobs
