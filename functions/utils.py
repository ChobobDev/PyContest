import requests
from bs4 import BeautifulSoup
from functions import stackoverflow as so ,weworkremotely as wwr,remoteok as ro


def requestWithUgerAgent(url):
    headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Whale/3.12.129.46 Safari/537.360'}
    soup = BeautifulSoup(requests.get(url, headers=headers).text, "html.parser")
    return soup

async def scrape_all(job_name):
    jobs=[]
    print("HERE - SO")
    so_job = asyncio.create_task(so.get_jobs(job_name)) 
    await so_job
    jobs.extend(so_job.result())
    print("HERE - WWR")
    wwr_job = asyncio.create_task(wwr.get_jobs(job_name))
    await wwr_job
    jobs.extend(wwr_job.result())
    print("HERE - RO")
    ro_job = asyncio.create_task(ro.get_jobs(job_name))
    await ro_job
    jobs.extend(ro_job.result())
