from tqdm import tqdm
from multiprocessing import Process,Manager
from functions import request_soup as rs

manager = Manager()
job_list = manager.list()

def extract_jobs(soup):
  for job in tqdm(soup):
    title = job.find('h3', {'itemprop':'name'}).text
    company = job.find('h2', {'itemprop':'title'}).text
    link = "https://remoteok.io" + job.find('a', {'class':'preventLink'})['href']
    job = {
      'site': "RemoteOk",
      'company':company,
      'location':"N/A",
      'title': title,
      'link':f"https://weworkremotely.com{link}",
    }
    job_list.append(job)


def get_jobs(jobs):
  for job in jobs:
    try:
      job_url= f'https://remoteok.com/remote-{job}-jobs'
      soup=rs.requestWithUgerAgent(job_url).find_all('tr', {'class':'job'})
      rop1 = Process(target=extract_jobs, args=(soup,))
      rop1.start()
      rop1.join()
      temp_list=job_list
      job_list=[]
      return temp_list
    except:
      return []

